---
title: "Commissioning SINAMICS G120/G115D/G110M drives"
package: StdrG120CommenUS
topics: 251
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Commissioning SINAMICS G120/G115D/G110M drives

This section contains information on the following topics:

- [Adding drives](#adding-drives)
- [Running through the wizard](Running%20through%20the%20wizard.md#running-through-the-wizard)
- [SINAMICS G120 drive functions](#sinamics-g120-drive-functions)
- [Parameterizing standard drives](#parameterizing-standard-drives)

## Adding drives

This section contains information on the following topics:

- [Adding drives offline](#adding-drives-offline)
- [Configuring G115D drives](#configuring-g115d-drives)
- [Explanation of SIMOGEAR order number](#explanation-of-simogear-order-number)
- [Adding a drive online](#adding-a-drive-online)

### Adding drives offline

#### Requirement

You have created a project.

#### Adding a new device

You can insert new devices in the portal view or in the project view

To insert devices in the project view, proceed as follows:

1. Double-click "Add new device".

   The dialog box with the same name opens.
2. Click "Drives" to display the available drives.
3. Select the drive from the list.
4. Select the firmware version installed on your drive.
5. Enter a name and click "OK".

If you leave the "Device view" option activated, the device view opens automatically.

**Adding a device in the network view**

Alternatively, you can insert a device in the network view.

1. Open the network view.
2. Drag and drop the device from the hardware catalog to the network view.

#### Adding a power unit

If you have inserted a drive, you must add a power unit for the SINAMICS G120 converter. The power units have already been created with the G120C and G115D.

For G115D, the power unit is not added in this conventional way. It is as mentioned in the topic "[Configuring G115D drives](#configuring-g115d-drives)".

To insert a power unit, proceed as follows:

1. Open the device view of the drive.
2. Select "Drives & starters > SINAMICS drives > SINAMICS G120 > Power units" in the hardware catalog.
3. Select the power unit.
4. Drag and drop the power unit to the drive unit in the device view.

   Or

   Copy the power unit from the Hardware Manager and paste it into the device view (Ctrl + C and Ctrl + V).

#### Result

Drive and power unit have been inserted. Now continue with the configuration or parameter assignment.

#### Alternative adding in the network view

Alternatively, you can insert a drive from the hardware catalog using drag and drop in the network view. To insert the power unit, switch to the device view.

### Configuring G115D drives

#### Configuring G115D drives

While adding G115D devices, the devices are listed for PN, AS-i, and I/O variants. An empty device with the selected variant is plugged in.

On adding a G115D drive an option to configure a Wall mount or a Motor mount is shown in the "Properties"->"Module Selection" tab.

![Configuring G115D drives](images/134863495691_DV_resource.Stream@PNG-en-US.png)

#### Configuring Wall mount

1. Select "Wall mount" radio button.
2. Select the article number from the list.
3. After selection, click "Go to commissioning", this will navigate to the commissioning editor for quick configuration using the wizard.

> **Note**
>
> This can be updated if the device is uploaded once or based on the selection of Motor mount type as well.

#### Configuring Motor mount

1. Select "Motor mount" radio button.

   ![Configuring Motor mount](images/158971348107_DV_resource.Stream@PNG-en-US.png)
2. Enter or select from the drop down, a Motor mount order number. For more information on the order number, refer to "[Explanation of SIMOGEAR order number](#explanation-of-simogear-order-number)".
3. Click on the ‘Accept’ button to finalize and choose the Motor mount order number. This will add the suitable device in the project.
4. Once accepted, a brief description of the selected Motor mount device is displayed.
5. Click "Go to commissioning", this will navigate to the commissioning editor for quick configuration using the wizard.

### Explanation of SIMOGEAR order number

The order number structure of SIMOGEAR is very important in the selection of a right G115D drive of a corresponding power (kW) rating. The Explanation of SIMOGEAR order number is shown in the below image.

![Figure](images/166113158795_DV_resource.Stream@PNG-en-US.png)

### Adding a drive online

#### Finding and adding a device via "Accessible devices"

There is an online connection to the drive and you want to upload the drive directly to the project.

#### Using accessible devices

To find the drive in the network, proceed as follows:

1. Click "Accessible devices".

   The dialog box with the same name opens.
2. Select the PG/PC interface type, e.g. "S7USB".
3. Select the PG/PC interface, e.g. "USB".
4. Click "Start search" to search for the accessible devices via the selected interface.

   The found devices are displayed under "Accessible devices in the target subnet".
5. Click "Display" to display the device under "Online access > <interface> > Accessible devices updated".
6. Select the device and perform "Online > Upload device as new station (hardware and software)".

#### Using online access

As an alternative to "Accessible devices", the TIA Portal provides the "Online access" function. All the interfaces on your PG/PC are listed here.

To find a device, proceed as follows:

1. Click the "Online access" folder in the project navigator.

   The available online access points are displayed.
2. Click the interface that you want to use, e.g. USB [S7 USB].
3. Click the "Update accessible devices" entry.

   The devices that can be accessed via this interface are displayed.
4. Select the device and perform "Online > Upload device as new station (hardware and software)".

#### Result

The drive is uploaded to the project and displayed. Then parameterize the drive.

> **Note**
>
> G115D drives when uploaded, the user can reconfigure the device from "Properties" -> "Module selection" page.

## SINAMICS G120 drive functions

This section contains information on the following topics:

- [General functions](#general-functions)
- [Technology](#technology)
- [Safety functions](#safety-functions)

### General functions

This section contains information on the following topics:

- [Assigning interfaces](#assigning-interfaces)
- [Converter control](#converter-control)
- [Command sources](#command-sources)
- [Setpoint sources](#setpoint-sources)
- [Setpoint processing](#setpoint-processing)
- [Motor control](#motor-control)
- [Protective functions](#protective-functions)
- [Application-specific functions](#application-specific-functions)
- [Specific G120P functions](#specific-g120p-functions)

#### Assigning interfaces

This section contains information on the following topics:

- [SINAMICS G120 interface assignments - CU240B-2](#sinamics-g120-interface-assignments---cu240b-2)
- [Interface assignments -CU240E -2](#interface-assignments--cu240e--2)
- [Interface assignments - G120P](#interface-assignments---g120p)
- [Interface assignments - G120D CU250D](#interface-assignments---g120d-cu250d)
- [Interface assignments - G120D CU240D](#interface-assignments---g120d-cu240d)
- [Interface assignments - G120 CU250S](#interface-assignments---g120-cu250s)
- [Interface assignments - G110M](#interface-assignments---g110m)
- [Interface assignments - G115D](#interface-assignments---g115d)

##### SINAMICS G120 interface assignments - CU240B-2

###### Default setting 7: "Fieldbus with data set switchover"

Factory setting for converters with PROFIBUS interface

![Default setting 7: "Fieldbus with data set switchover"](images/114233779723_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730 | AO 0: p0771[0] | DI 0: r0722.0, …, DI 3: r0722.3 |
| Speed setpoint (main setpoint): p1070[0] = 2050[1]  Jog 1 speed setpoint: p1058, factory setting: 150 rpm  Jog 2 speed setpoint: p1059, factory setting: -150 rpm |  |  |
| Designation in the BOP-2: FB cdS |  |  |

###### Default setting 9: "Standard I/O with MOP"

![Default setting 9: "Standard I/O with MOP"](images/114233788939_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730 | AO 0: p0771[0] | DI 0: r0722.0, …, DI 3: r0722.3 |
| Motorized potentiometer setpoint after ramp-function generator: r1050  Speed setpoint (main setpoint): p1070[0] = 1050 |  |  |
| Designation in the BOP-2: Std MoP |  |  |

###### Default setting 12: "Standard I/O with analog setpoint"

Factory setting for converters with USS interface

![Default setting 12: "Standard I/O with analog setpoint"](images/114243764747_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730 | AO 0: p0771[0] | DI 0: r0722.0, …, DI 2: r0722.2 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: Std ASP |  |  |  |

###### Default setting 17: "2-wire (forw/backw1)"

![Default setting 17: "2-wire (forw/backw1)"](images/114243773963_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730 | AO 0: p0771[0] | DI 0: r0722.2, …, DI 2: r0722.2 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: 2-wIrE 1 |  |  |  |

###### Default setting 18: "2-wire (forw/backw2)"

![Default setting 18: "2-wire (forw/backw2)"](images/114243773963_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730 | AO 0: p0771[0] | DI 0: r0722.2, …, DI 2: r0722.2 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in theBOP-2: 2-wIrE 1 |  |  |  |

###### Default setting 19: "3-wire (enable/forw/backw)"

![Default setting 19: "3-wire (enable/forw/backw)"](images/114244085771_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730 | AO 0: p0771[0] | DI 0: r0722.0, …, DI 3: r0722.3 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: 3-wIrE 2 |  |  |  |

###### Default setting 20: "3-wire (enable/on/reverse)"

![Default setting 20: "3-wire (enable/on/reverse)"](images/114244299787_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730 | AO 0: p0771[0] | DI 0: r0722.0, …, DI 3: r0722.3 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: 3-wIrE 2 |  |  |  |

###### Default setting 21: "USS fieldbus"

![Default setting 21: "USS fieldbus"](images/126440498699_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730 | AO 0: p0771[0] | DI 2: r0722.2 |
| Speed setpoint (main setpoint): p1070[0] = 2050[1] |  |  |
| Designation in the BOP-2: FB USS |  |  |

---

**See also**

[Default settings of the setpoints / command sources](Running%20through%20the%20wizard.md#default-settings-of-the-setpoints-command-sources-1)
  
[Two-wire control, method 1](#two-wire-control-method-1)
  
[Two-wire control, method 2](#two-wire-control-method-2)
  
[Two-wire control, method 3](#two-wire-control-method-3)
  
[Three-wire control, method 1](#three-wire-control-method-1)
  
[Three-wire control, method 2](#three-wire-control-method-2)

##### Interface assignments -CU240E -2

###### Default setting 1: "Conveyor technology with 2 fixed frequencies"

![Default setting 1: "Conveyor technology with 2 fixed frequencies"](images/124644817163_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 5: r0722.5 |
| Fixed speed setpoint 3: p1003, fixed speed setpoint 4: p1004, fixed speed setpoint active: r1024  Speed setpoint (main setpoint): p1070[0] = 1024  DI 4 and DI 5 = high: The converter adds both fixed speed setpoints |  |  |
| Designation in the BOP-2: coN 2 SP |  |  |

###### Default setting 2: "Conveyor systems with Basic Safety"

![Default setting 2: "Conveyor systems with Basic Safety"](images/114232771083_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 5: r0722.5 |
| Fixed speed setpoint 1: p1001, fixed speed setpoint 2: p1002, fixed speed setpoint active: r1024  Speed setpoint (main setpoint): p1070[0] = 1024  DI 0 and DI 1 = high: The converter adds both fixed speed setpoints. |  |  |
| Designation in the BOP-2: coN SAFE |  |  |

###### Default setting 3: "Conveyor systems with 4 fixed frequencies"

![Default setting 3: "Conveyor systems with 4 fixed frequencies"](images/114232775691_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 5: r0722.5 |
| Fixed speed setpoint 1: p1001, … fixed speed setpoint 4: p1004, fixed speed setpoint active: r1024  Speed setpoint (main setpoint): p1070[0] = 1024  Several of the DI 0, DI 1, DI 4, and DI 5 = high: the converter adds the corresponding fixed speed setpoints. |  |  |
| Designation in the BOP-2: coN 4 SP |  |  |

###### Default setting 4: "Conveyor system with fieldbus"

![Default setting 4: "Conveyor system with fieldbus"](images/114232857099_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] |
| Speed setpoint (main setpoint): p1070[0] = 2050[1] |  |
| Designation in the BOP-2: coN Fb |  |

###### Default setting 5: "Conveyor systems with fieldbus and Basic Safety"

![Default setting 5: "Conveyor systems with fieldbus and Basic Safety"](images/114232861707_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 4: r0722.4, DI 5: r0722.5 |
| Speed setpoint (main setpoint): p1070[0] = 2050[1] |  |  |
| Designation in the BOP-2: coN Fb S |  |  |

###### Default setting 6: "Fieldbus with Extended Safety"

Only with Control Units CU240E‑2 F, CU240E‑2 DP‑F, and CU240E‑2 PN‑F.

![Default setting 6: "Fieldbus with Extended Safety"](images/114232866315_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 5: r0722.5 |
| Speed setpoint (main setpoint): p1070[0] = 2050[1] |  |  |
| Designation in the BOP-2: Fb SAFE |  |  |

###### Default setting 7: "Fieldbus with data set switchover"

Factory setting for converters with PROFIBUS or PROFINET interface

![Default setting 7: "Fieldbus with data set switchover"](images/126440951819_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 3: r0722.3 |
| Speed setpoint (main setpoint): p1070[0] = 2050[1]  Jog 1 speed setpoint: p1058, factory setting: 150 rpm  Jog 2 speed setpoint: p1059, factory setting: -150 rpm |  |  |
| Designation in the BOP-2: FB cdS |  |  |

###### Default setting 8: "MOP with Basic Safety"

![Default setting 8: "MOP with Basic Safety"](images/114233784331_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 5: r0722.5 |
| Motorized potentiometer setpoint after ramp-function generator: r1050  Speed setpoint (main setpoint): p1070[0] = 1050 |  |  |
| Designation in the BOP-2: MoP SAFE |  |  |

###### Default setting 9: "Standard I/O with MOP"

![Default setting 9: "Standard I/O with MOP"](images/126442351883_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 3: r0722.3 |
| Motorized potentiometer setpoint after ramp-function generator: r1050  Speed setpoint (main setpoint): p1070[0] = 1050 |  |  |
| Designation in the BOP-2: Std MoP |  |  |

###### Default setting 12: "Standard I/O with analog setpoint"

![Default setting 12: "Standard I/O with analog setpoint"](images/126442748939_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 2: r0722.2 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: Std ASP |  |  |  |

###### Default setting 13: "Standard I/O with analog setpoint and safety"

![Default setting 13: "Standard I/O with analog setpoint and safety"](images/126442869003_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 5: r0722.5 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: ASPS |  |  |  |

###### Default setting 14: "Process industry with fieldbus"

PROFIdrive telegram 20

![Default setting 14: "Process industry with fieldbus"](images/126450041867_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| MOP = motorized potentiometer |  |  |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 5: r0722.5 |
| Motorized potentiometer setpoint after ramp-function generator: r1050  Speed setpoint (main setpoint): p1070[0] = 2050[1], p1070[1] = 1050  Switch controller via PZD01, bit 15: p0810 = r2090.15 |  |  |
| Designation in the BOP-2: Proc Fb |  |  |

###### Default setting 15: "Process industry"

![Default setting 15: "Process industry"](images/126450929931_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.5, …, DI 4: r0722.5 | AI 0: r0755[0] |
| Motorized potentiometer setpoint after ramp-function generator: r1050  Speed setpoint (main setpoint): p1070[0] = 755[0], p1070[1] = 1050 |  |  |  |
| Designation in the BOP-2: Proc |  |  |  |

###### Default setting 17: "2-wire (forw/backw1)"

![Default setting 17: "2-wire (forw/backw1)"](images/126451536395_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.2, …, DI 2: r0722.2 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: 2-wIrE 1 |  |  |  |

###### Default setting 18: "2-wire (forw/backw2)"

![Default setting 18: "2-wire (forw/backw2)"](images/126451536395_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.2, …, DI 2: r0722.2 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in theBOP-2:2-wIrE 2 |  |  |  |

###### Default setting 19: "3-wire (enable/forw/backw)"

![Default setting 19: "3-wire (enable/forw/backw)"](images/126452066059_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 4: r0722.4 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: 3-wIrE 1 |  |  |  |

###### Default setting 20: "3-wire (enable/on/reverse)"

![Default setting 20: "3-wire (enable/on/reverse)"](images/126453453323_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 4: r0722.4 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: 3-wIrE 2 |  |  |  |

###### Default setting 21: "USS fieldbus"

![Default setting 21: "USS fieldbus"](images/126455762187_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 2: r0722.2 |
| Speed setpoint (main setpoint): p1070[0] = 2050[1] |  |  |
| Designation in the BOP-2: FB USS |  |  |

##### Interface assignments - G120P

###### Default setting 7: "Fieldbus with data set switchover"

Factory setting for converters with PROFIBUS or PROFINET interface

![Default setting 7: "Fieldbus with data set switchover"](images/126456720395_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 3: r0722.3 |
| Speed setpoint (main setpoint): p1070[0] = 2050[1]  Jog 1 speed setpoint: p1058, factory setting: 150 rpm  Jog 2 speed setpoint: p1059, factory setting: -150 rpm |  |  |
| Designation in the BOP-2: FB cdS |  |  |

###### Default setting 9: "Standard I/O with MOP"

![Default setting 9: "Standard I/O with MOP"](images/126457091851_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 3: r0722.3 |
| Motorized potentiometer setpoint after ramp-function generator: r1050  Speed setpoint (main setpoint): p1070[0] = 1050 |  |  |
| Designation in the BOP-2: Std MoP |  |  |

###### Default setting 12: "Standard I/O with analog setpoint"

Factory setting for converters with USS, Modbus, BACnet, MS/TP or P1 interface

![Default setting 12: "Standard I/O with analog setpoint"](images/126496496267_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 2: r0722.2 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: Std ASP |  |  |  |

###### Default setting 14: "Process industry with fieldbus"

![Default setting 14: "Process industry with fieldbus"](images/126496560523_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 5: r0722.5 |
| Motorized potentiometer setpoint after ramp-function generator: r1050  Speed setpoint (main setpoint): p1070[0] = 2050[1], p1070[1] = 1050  Switch controller via PZD01, bit 15: p0810 = r2090.15 |  |  |
| Designation in the BOP-2: Proc Fb |  |  |

###### Default setting 15: "Process industry"

![Default setting 15: "Process industry"](images/126496676235_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 5: r0722.5 | AI 0: r0755[0] |
| Motorized potentiometer setpoint after ramp-function generator: r1050  Speed setpoint (main setpoint): p1070[0] = 755[0], p1070[1] = 1050 |  |  |  |
| Designation in the BOP-2: Proc |  |  |  |

###### Default setting 17: "2-wire (forw/backw1)"

![Default setting 17: "2-wire (forw/backw1)"](images/126496855691_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 2: r0722.2 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: 2-wIrE 1 |  |  |  |

###### Default setting 18: "2-wire (forw/backw2)"

![Default setting 18: "2-wire (forw/backw2)"](images/126496855691_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 2: r0722.2 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in theBOP-2:2-wIrE 2 |  |  |  |

###### Default setting 19: "3-wire (enable/forw/backw)"

![Default setting 19: "3-wire (enable/forw/backw)"](images/126496983947_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 4: r0722.4 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: 3-wIrE 1 |  |  |  |

###### Default setting 20: "3-wire (enable/on/reverse)"

![Default setting 20: "3-wire (enable/on/reverse)"](images/126497852811_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 4: r0722.4 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: 3-wIrE 2 |  |  |  |

###### Default setting 21: "USS fieldbus"

![Default setting 21: "USS fieldbus"](images/126501865611_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 2: r0722.2 |  |
| Speed setpoint (main setpoint): p1070[0] = 2050[1] |  |  |  |
| Designation in the BOP-2: FB USS |  |  |  |

##### Interface assignments - G120D CU250D

###### Default setting 26: "EPOS without fieldbus"

Factory setting

![Default setting 26: "EPOS without fieldbus"](images/126509816331_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 | DI 0: r0722.0, …, DI 5: r0722.5 |

###### Default setting 27: "EPOS with fieldbus"

![Default setting 27: "EPOS with fieldbus"](images/126510046987_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 |  |

##### Interface assignments - G120D CU240D

###### Default setting 1: "Conveyor system with 2 fixed frequencies"

![Default setting 1: "Conveyor system with 2 fixed frequencies"](images/126511029387_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 | DI 0: r0722.0, …, DI 5: r0722.5 |
| Fixed speed setpoint 3: p1003, fixed speed setpoint 4: p1004, fixed speed setpoint active: r1024  Speed setpoint (main setpoint): p1070[0] = 1024  DI 4 and DI 5 = high: the inverter adds the two fixed speed setpoints |  |

###### Default setting 2: "Conveyor system with Basic Safety"

![Default setting 2: "Conveyor system with Basic Safety"](images/126511951243_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 | DI 0: r0722.0, …, DI 5: r0722.5 |
| Fixed speed setpoint 1: p1001, fixed speed setpoint 2: p1002, fixed speed setpoint active: r1024  Speed setpoint (main setpoint): p1070[0] = 1024  DI 0 and DI 1 = high: the inverter adds the two fixed speed setpoints. |  |

###### Default setting 3: "Conveyor system with 4 fixed frequencies"

![Default setting 3: "Conveyor system with 4 fixed frequencies"](images/126512412299_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 | DI 0: r0722.0, …, DI 5: r0722.5 |
| Fixed speed setpoint 1: p1001, … fixed speed setpoint 4: p1004, fixed speed setpoint active: r1024  Speed setpoint (main setpoint): p1070[0] = 1024  Several of the DI 0, DI 1, DI 4, and DI 5 = high: the inverter adds the corresponding fixed speed setpoints. |  |

###### Default setting 4: "Conveyor system with fieldbus"

![Default setting 4: "Conveyor system with fieldbus"](images/126513423755_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 |  |
| Speed setpoint (main setpoint): p1070[0] = 2050[1] |  |

###### Default setting 5: "Conveyor system with fieldbus and Basic Safety"

![Default setting 5: "Conveyor system with fieldbus and Basic Safety"](images/126513654411_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 | DI 4: r0722.4, DI 5: r0722.5 |
| Speed setpoint (main setpoint): p1070[0] = 2050[1] |  |

###### Default setting 6: "Fieldbus with Extended Safety"

![Default setting 6: "Fieldbus with Extended Safety"](images/126513912715_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 | DI 0: r0722.0, …, DI 5: r0722.5 |
| Speed setpoint (main setpoint): p1070[0] = 2050[1] |  |

###### Default setting 7: "Fieldbus with data set switchover"

![Default setting 7: "Fieldbus with data set switchover"](images/126514565515_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 | DI 0: r0722.0, …, DI 3: r0722.3 |
| Speed setpoint (main setpoint): p1070[0] = 2050[1]  Jog 1 speed setpoint: p1058, factory setting: 150 rpm  Jog 2 speed setpoint: p1059, factory setting: -150 rpm |  |

###### Default setting 8: "MOP with Basic Safety"

![Default setting 8: "MOP with Basic Safety"](images/126514783115_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 | DI 0: r0722.0, …, DI 5: r0722.5 |
| Motorized potentiometer, setpoint after the ramp-function generator r1050  Speed setpoint (main setpoint): p1070[0] = 1050 |  |

###### Default setting 9: "Standard I/O with MOP"

![Default setting 9: "Standard I/O with MOP"](images/126515073035_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 | DI 0: r0722.0, …, DI 3: r0722.3 |
| Motorized potentiometer, setpoint after the ramp-function generator r1050  Speed setpoint (main setpoint): p1070[0] = 1050 |  |

###### Default setting 12: "Standard I/O with analog setpoint"

![Default setting 12: "Standard I/O with analog setpoint"](images/126515201035_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | DI 0: r0722.0, …, DI 2: r0722.2 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |

###### Default setting 13: "Standard I/O with analog setpoint and safety"

![Default setting 13: "Standard I/O with analog setpoint and safety"](images/126515341835_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | DI 0: r0722.0, …, DI 5: r0722.5 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |

###### Default setting 14: "Process industry with fieldbus"

![Default setting 14: "Process industry with fieldbus"](images/126515482635_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 | DI 0: r0722.0, …, DI 5: r0722.5 |
| Motorized potentiometer, setpoint after the ramp-function generator r1050  Speed setpoint (main setpoint): p1070[0] = 2050[1], p1070[1] = 1050  Switch controller via PZD01, bit 15: p0810 = r2090.15 |  |

###### Default setting 24: "Distributed conveyor systems with fieldbus"

![Default setting 24: "Distributed conveyor systems with fieldbus"](images/126515610635_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 | DI 0: r0722.0, …, DI 5: r0722.5 |
| p2081[0] = r0722.0, …, p2081[5] = r0722.5  p0730 = r2094.0, p0731 = r2094.1  Speed setpoint (main setpoint): p1070[0] = 2050[1] |  |

###### Default setting 25: "Distributed conveyor systems with fieldbus, safety"

![Default setting 25: "Distributed conveyor systems with fieldbus, safety"](images/126515751435_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 | DI 0: r0722.0, …, DI 5: r0722.5 |
| p2081[0] = r0722.0, …, p2081[3] = r0722.3  p0730 = r2094.0, p0731 = r2094.1  Speed setpoint (main setpoint): p1070[0] = 2050[1] |  |

##### Interface assignments - G120 CU250S

###### Default setting 1: "Conveyor technology with 2 fixed frequencies"

![Default setting 1: "Conveyor technology with 2 fixed frequencies"](images/124644817163_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 5: r0722.5 |
| Fixed speed setpoint 3: p1003, fixed speed setpoint 4: p1004, fixed speed setpoint active: r1024  Speed setpoint (main setpoint): p1070[0] = 1024  DI 4 and DI 5 = high: The inverter adds both fixed speed setpoints |  |  |
| Designation in the BOP-2: coN 2 SP |  |  |

###### Default setting 2: "Conveyor systems with Basic Safety"

![Default setting 2: "Conveyor systems with Basic Safety"](images/114232771083_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 5: r0722.5 |
| Fixed speed setpoint 1: p1001, fixed speed setpoint 2: p1002, fixed speed setpoint active: r1024  Speed setpoint (main setpoint): p1070[0] = 1024  DI 0 and DI 1 = high: The inverter adds both fixed speed setpoints. |  |  |
| Designation in the BOP-2: coN SAFE |  |  |

###### Default setting 3: "Conveyor systems with 4 fixed frequencies"

![Default setting 3: "Conveyor systems with 4 fixed frequencies"](images/114232775691_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 5: r0722.5 |
| Fixed speed setpoint 1: p1001, … fixed speed setpoint 4: p1004, fixed speed setpoint active: r1024  Speed setpoint (main setpoint): p1070[0] = 1024  Several of the DI 0, DI 1, DI 4, and DI 5 = high: the inverter adds the corresponding fixed speed setpoints. |  |  |
| Designation in the BOP-2: coN 4 SP |  |  |

###### Default setting 4: "Conveyor system with fieldbus"

![Default setting 4: "Conveyor system with fieldbus"](images/114232857099_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] |
| Speed setpoint (main setpoint): p1070[0] = 2050[1] |  |
| Designation in the BOP-2: coN Fb |  |

###### Default setting 5: "Conveyor systems with fieldbus and Basic Safety"

![Default setting 5: "Conveyor systems with fieldbus and Basic Safety"](images/114232861707_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 4: r0722.4, DI 5: r0722.5 |
| Speed setpoint (main setpoint): p1070[0] = 2050[1] |  |  |
| Designation in the BOP-2: coN Fb S |  |  |

###### Default setting 7: "Fieldbus with data set switchover"

![Default setting 7: "Fieldbus with data set switchover"](images/126440946699_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 3: r0722.3 |
| Speed setpoint (main setpoint): p1070[0] = 2050[1]  Jog 1 speed setpoint: p1058, factory setting: 150 rpm  Jog 2 speed setpoint: p1059, factory setting: -150 rpm |  |  |
| Designation in the BOP-2: FB cdS |  |  |

###### Default setting 8: "MOP with Basic Safety"

![Default setting 8: "MOP with Basic Safety"](images/114233784331_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| MOP = motorized potentiometer |  |  |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 5: r0722.5 |
| Motorized potentiometer setpoint after ramp-function generator: r1050  Speed setpoint (main setpoint): p1070[0] = 1050 |  |  |
| Designation in the BOP-2: MoP SAFE |  |  |

###### Default setting 9: "Standard I/O with MOP"

![Default setting 9: "Standard I/O with MOP"](images/114322726155_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| MOP = motorized potentiometer |  |  |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 3: r0722.3 |
| Motorized potentiometer setpoint after ramp-function generator: r1050  Speed setpoint (main setpoint): p1070[0] = 1050 |  |  |
| Designation in the BOP-2: Std MoP |  |  |

###### Default setting 12: "Standard I/O with analog setpoint"

![Default setting 12: "Standard I/O with analog setpoint"](images/124644822539_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 2: r0722.2 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: Std ASP |  |  |  |

###### Default setting 13: "Standard I/O with analog setpoint and safety"

![Default setting 13: "Standard I/O with analog setpoint and safety"](images/126442863883_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 5: r0722.5 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: ASPS |  |  |  |

###### Default setting 14: "Process industry with fieldbus"

![Default setting 14: "Process industry with fieldbus"](images/126450036747_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| MOP = motorized potentiometer |  |  |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 5: r0722.5 |
| Motorized potentiometer setpoint after ramp-function generator: r1050  Speed setpoint (main setpoint): p1070[0] = 2050[1], p1070[1] = 1050  Switch controller via PZD01, bit 15: p0810 = r2090.15 |  |  |
| Designation in the BOP-2: Proc Fb |  |  |

###### Default setting 15: "Process industry"

![Default setting 15: "Process industry"](images/126450476811_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| MOP = motorized potentiometer |  |  |  |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.5, …, DI 4: r0722.5 | AI 0: r0755[0] |
| Motorized potentiometer setpoint after ramp-function generator: r1050  Speed setpoint (main setpoint): p1070[0] = 755[0], p1070[1] = 1050 |  |  |  |
| Designation in the BOP-2: Proc |  |  |  |

###### Default setting 17: "2-wire (forw/backw1)"

![Default setting 17: "2-wire (forw/backw1)"](images/126451531275_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.2, …, DI 2: r0722.2 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: 2-wIrE 1 |  |  |  |

###### Default setting 18: "2-wire (forw/backw2)"

![Default setting 18: "2-wire (forw/backw2)"](images/126451531275_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 2: r0722.2 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: 2-wIrE 2 |  |  |  |

###### Default setting 19: "3-wire (enable/forw/backw)"

![Default setting 19: "3-wire (enable/forw/backw)"](images/126452060939_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 4: r0722.4 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: 3-wIrE 1 |  |  |  |

###### Default setting 20: "3-wire (enable/on/reverse)"

![Default setting 20: "3-wire (enable/on/reverse)"](images/126453115403_DV_resource.Stream@PNG-en-US.png)

|  |  |  |  |
| --- | --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 0: r0722.0, …, DI 4: r0722.4 | AI 0: r0755[0] |
| Speed setpoint (main setpoint): p1070[0] = 755[0] |  |  |  |
| Designation in the BOP-2: 3-wIrE 2 |  |  |  |

###### Default setting 21: "USS fieldbus"

![Default setting 21: "USS fieldbus"](images/126455757067_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 2: r0722.2 |
| Speed setpoint (main setpoint): p1070[0] = 2050[1] |  |  |
| Designation in the BOP-2: FB USS |  |  |

###### Default setting 22: "CAN fieldbus"

![Default setting 22: "CAN fieldbus"](images/126541010059_DV_resource.Stream@PNG-en-US.png)

|  |  |  |
| --- | --- | --- |
| DO 0: p0730, DO 1: p0731 | AO 0: p0771[0], AO 1: p0771[1] | DI 2: r0722.2 |
| Speed setpoint (main setpoint): p1070[0] = 2050[1] |  |  |
| Designation in the BOP-2: FB CAN |  |  |

##### Interface assignments - G110M

###### Default settings for the CU240M

The default settings that are available for the CU240M Control Modules are shown in the figures below. Default settings 7 is the default setting for the CU240M DP and CU240M PN Control Modules, default settings 21 is the default settings for the CU240M USS Control Module and default settings 30 is the default settings for the CU240M ASi Control Modules.

![Default settings 7 - Switch over between fieldbus and jogging using DI 3 (default DP/PN)](images/126544799883_DV_resource.Stream@PNG-en-US.png)

Default settings 7 - Switch over between fieldbus and jogging using DI 3 (default DP/PN)

![Default settings 9 - Motorized potentiometer (MOP)](images/126545030283_DV_resource.Stream@PNG-en-US.png)

Default settings 9 - Motorized potentiometer (MOP)

![Default settings 12 - Two-wire control with method 1](images/126545068683_DV_resource.Stream@PNG-en-US.png)

Default settings 12 - Two-wire control with method 1

![Default settings 17 - Two-wire control with method 2](images/126545119883_DV_resource.Stream@PNG-en-US.png)

Default settings 17 - Two-wire control with method 2

![Default settings 18 Two-wire control with method 3](images/126545286283_DV_resource.Stream@PNG-en-US.png)

Default settings 18 Two-wire control with method 3

![Default settings 19 Three-wire control with method 1](images/126545503883_DV_resource.Stream@PNG-en-US.png)

Default settings 19 Three-wire control with method 1

![Default settings 20 Three-wire control with method 2](images/126558534539_DV_resource.Stream@PNG-en-US.png)

Default settings 20 Three-wire control with method 2

![Default settings 21 Fieldbus USS](images/126545759883_DV_resource.Stream@PNG-en-US.png)

Default settings 21 Fieldbus USS

![Default settings 28 Conveyor with 2 fixed setpoints](images/126546105483_DV_resource.Stream@PNG-en-US.png)

Default settings 28 Conveyor with 2 fixed setpoints

![Default settings 29 Conveyer with potentiometer and fixed setpoint (default USS)](images/126546182283_DV_resource.Stream@PNG-en-US.png)

Default settings 29 Conveyer with potentiometer and fixed setpoint (default USS)

![Default settings 30 ASi Single device with fixed setpoints (Default ASi)](images/126546297483_DV_resource.Stream@PNG-en-US.png)

Default settings 30 ASi Single device with fixed setpoints (Default ASi)

![Default settings 31 ASi Dual device with fixed setpoints](images/126547065483_DV_resource.Stream@PNG-en-US.png)

Default settings 31 ASi Dual device with fixed setpoints

![Default settings 32 ASi Single device with analog setpoint](images/126547193483_DV_resource.Stream@PNG-en-US.png)

Default settings 32 ASi Single device with analog setpoint

![Default settings 33 4DI decentral conveyor with fieldbus](images/126551788683_DV_resource.Stream@PNG-en-US.png)

Default settings 33 4DI decentral conveyor with fieldbus

![Default settings 34 ASi Dual device with setpoint](images/126558329483_DV_resource.Stream@PNG-en-US.png)

Default settings 34 ASi Dual device with setpoint

##### Interface assignments - G115D

###### Default settings for the G115D

The default settings that are available for the G115D Control Modules are shown in the figures below. Default settings 65 is the default setting for the G115D I/O Control Module , default settings 67 is the default settings for the G115D PN Control Module and default settings 30 is the default settings for the G115D AS-i Control Modules.

![Default 9](images/114372849675_DV_resource.Stream@PNG-en-US.png)

Default 9

![default 30 ASi Single device with fixed setpoints](images/114372977675_DV_resource.Stream@PNG-en-US.png)

default 30 ASi Single device with fixed setpoints

![default 31 ASi Dual device with fixed setpoints](images/114372990475_DV_resource.Stream@PNG-en-US.png)

default 31 ASi Dual device with fixed setpoints

![default34 ASi Dual device with setpoint](images/114373041675_DV_resource.Stream@PNG-en-US.png)

default34 ASi Dual device with setpoint

![default 60](images/125971709067_DV_resource.Stream@PNG-en-US.png)

default 60

![default 61 Two-wire control with method 2](images/125974243467_DV_resource.Stream@PNG-en-US.png)

default 61 Two-wire control with method 2

![default 62 Two-wire control with method 3](images/125979184011_DV_resource.Stream@PNG-en-US.png)

default 62 Two-wire control with method 3

![default 63 Three-wire control with method 1](images/125980361611_DV_resource.Stream@PNG-en-US.png)

default 63 Three-wire control with method 1

![default 64 Three-wire control with method 2](images/125980886411_DV_resource.Stream@PNG-en-US.png)

default 64 Three-wire control with method 2

![default 65 Conveyer with potentiometer and fixed setpoint](images/125981270411_DV_resource.Stream@PNG-en-US.png)

default 65 Conveyer with potentiometer and fixed setpoint

![default 66 ASi Single device with analog setpoint](images/125981884811_DV_resource.Stream@PNG-en-US.png)

default 66 ASi Single device with analog setpoint

![default 67 4DI decentral conveyor with fieldbus](images/125993545611_DV_resource.Stream@PNG-en-US.png)

default 67 4DI decentral conveyor with fieldbus

#### Converter control

This section contains information on the following topics:

- [Switching the motor on and off](#switching-the-motor-on-and-off)
- [Converter control using digital inputs](#converter-control-using-digital-inputs)
- [Two-wire control, method 1](#two-wire-control-method-1)
- [Two-wire control, method 2](#two-wire-control-method-2)
- [Two-wire control, method 3](#two-wire-control-method-3)
- [Three-wire control, method 1](#three-wire-control-method-1)
- [Three-wire control, method 2](#three-wire-control-method-2)
- [Running the motor in jog mode (JOG function)](#running-the-motor-in-jog-mode-jog-function)

##### Switching the motor on and off

###### Description

|  |  |  |
| --- | --- | --- |
| After switching on the supply voltage, the converter normally goes into the "Ready to start" state. In this state, the converter waits for the command to switch-on the motor:  - The converter switches on the motor with the ON command. The converter changes to the "Operation" state. - After the OFF1 command, the converter brakes the motor with the ramp-down time of the ramp-function generator. The converter switches off the motor once standstill has been reached. The converter is again "ready to start". |  | ![Description](images/103437845643_DV_resource.Stream@PNG-en-US.png) |

###### Converter states and commands for switching the motor on and off

In addition to the OFF1 command, there are other commands that are used to switch off the motor:

- OFF2 - the converter immediately switches off the motor without first braking it.
- OFF3 - this command means "quick stop". After an OFF3 command, the converter brakes the motor with the OFF3 ramp-down time. After reaching standstill, the converter switches off the motor.  
  The command is frequently used for exceptional operating situations where it is necessary to brake the motor especially quickly, e.g. when it involves collision protection.

The following diagram shows the internal sequence control of the converter when switching the motor on and off.

![State overview of the converter](images/103437841035_DV_resource.Stream@PNG-en-US.png)

State overview of the converter

Explanation of the converter states

| State | Explanation |
| --- | --- |
| Switching on inhibited | In this state, the converter does not respond to the ON command. The converter goes into this state under the following conditions:  - The ON command was active when switching on the converter. Exception: When the automatic start function is active, the ON command must be active after switching on the power supply. - The OFF2 or OFF3 command is selected. |
| Ready for switching on | This state is required to switch on the motor. |
| Ready | The converter waits for the operating enable.  If the converter is controlled via a fieldbus, then you must set the operating enable in a control word bit. If the converter is exclusively controlled via its digital inputs, then the operating enable signal is automatically set in the factory settings. |
| Operation | The motor is switched on. |
| Normal stop | The motor was switched off with an OFF1 command and brakes with the ramp-down time of the ramp-function generator. |
| Quick stop | The motor was switched off with an OFF3 command and brakes with the OFF3 ramp-down time. |

##### Converter control using digital inputs

The converter has a different methods for controlling the motor using two or three commands.

If you are controlling the converter via digital inputs, define how the motor is switched on and off and how it is changed over from clockwise to counter-clockwise rotation in the wizard with parameter p0015 (drive unit macro) at "Defaults of the setpoint/command sources".

Five different methods are available for controlling the motor. Three of the five methods just require two control commands (two-wire control). The other two methods require three control commands (three-wire control).

**Overview**

| Symbol | Meaning |
| --- | --- |
| **Behavior of the motor** |  |
| ![Figure](images/109214062859_DV_resource.Stream@PNG-en-US.png) | **Two-wire control, method 1**   ON/OFF1:  Switches the motor on or off    Reversing:  Reverses the motor direction of rotation |
| ![Figure](images/109255289739_DV_resource.Stream@PNG-en-US.png) | **Two-wire control, method 2 and  two-wire control, method 3**   ON/OFF1 clockwise rotation:  Switches the motor on or off, clockwise rotation    ON/OFF1 counter-clockwise rotation:  Switches the motor on or off, counter-clockwise rotation |
| ![Figure](images/109255673483_DV_resource.Stream@PNG-en-US.png) | **Three-wire control, method 1**   Enable/OFF1:  Enables the motor to be switched on or switched off    ON clockwise rotation:  Switches on the motor, clockwise rotation    ON counter-clockwise rotation:  Switches on the motor, counter-clockwise rotation |
| ![Figure](images/109255864971_DV_resource.Stream@PNG-en-US.png) | **Three-wire control, method 2**   Enable/OFF1:  Enables the motor to be switched on or switched off    ON:  Switches on the motor    Reversing:  Reverses the motor direction of rotation |

---

**See also**

[Two-wire control, method 1](#two-wire-control-method-1)
  
[Two-wire control, method 2](#two-wire-control-method-2)
  
[Two-wire control, method 3](#two-wire-control-method-3)
  
[Three-wire control, method 1](#three-wire-control-method-1)
  
[Three-wire control, method 2](#three-wire-control-method-2)

##### Two-wire control, method 1

![Two-wire control, method 1](images/114039497867_DV_resource.Stream@PNG-en-US.png)

Two-wire control, method 1

Command "ON/OFF1" switches the motor on and off. The "Reversing" command inverts the motor direction of rotation.

Function table

| ON/OFF1 | Reversing | Function |
| --- | --- | --- |
| 0 | 0 | OFF1: The motor stops. |
| 0 | 1 | OFF1: The motor stops. |
| 1 | 0 | ON: Clockwise rotation of motor. |
| 1 | 1 | ON: Counter-clockwise rotation of motor. |

Select two-wire control, method 1

| Parameter | Description |
| --- | --- |
| p0015 = 12 | **Macro drive unit**   You must carry out quick commissioning in order to set parameter p0015.  Assigning digital inputs DI to the commands:  DI 0: ON/OFF1  DI 1: Reversing |

Changing the assignment of the digital inputs

| Parameter | Description |
| --- | --- |
| p0840[0 … n] = 722.x | **BI: ON/OFF1** (ON/OFF1)  Example: p0840 = 722.3 ⇒ DI 3: ON/OFF1 |
| p1113[0 … n] = 722.x | **BI: Setpoint inversion** (reversing) |

---

**See also**

[Converter control using digital inputs](#converter-control-using-digital-inputs)
  
[SINAMICS G120 interface assignments - CU240B-2](#sinamics-g120-interface-assignments---cu240b-2)

##### Two-wire control, method 2

![Two-wire control, method 2](images/114040248075_DV_resource.Stream@PNG-en-US.png)

Two-wire control, method 2

Commands "ON/OFF1 clockwise rotation" and "ON/OFF1 counter-clockwise rotation" switch on the motor - and simultaneously select a direction of rotation. The converter only accepts a new command when the motor is at a standstill.

Function table

| ON/OFF1 clockwise rotation | ON/OFF1 counter-clockwise rotation | Function |
| --- | --- | --- |
| 0 | 0 | OFF1: The motor stops. |
| 1 | 0 | ON: Clockwise rotation of motor. |
| 0 | 1 | ON: Counter-clockwise rotation of motor. |
| 1 | 1 | ON: The motor direction of rotation is based on the signal that takes on the status "1" first. |

Select two-wire control, method 2

| Parameter | Description |
| --- | --- |
| p0015 = 17 | **Macro drive unit**   You must carry out quick commissioning in order to set parameter p0015.  Assigning digital inputs DI to the commands:  DI 0: ON/OFF1 clockwise rotation  DI 1: ON/OFF1 counter-clockwise rotation |

Changing the assignment of the digital inputs

| Parameter | Description |
| --- | --- |
| p3330[0 … n] = 722.x | **BI: 2/3 wire control command 1** (ON/OFF1 clockwise rotation) |
| p3331[0 … n] = 722.x | **BI: 2/3 wire control command 2** (ON/OFF1 counter-clockwise rotation)  Example: p3331 = 722.0 ⇒ DI 0: ON/OFF1 counter-clockwise rotation |

---

**See also**

[Converter control using digital inputs](#converter-control-using-digital-inputs)
  
[SINAMICS G120 interface assignments - CU240B-2](#sinamics-g120-interface-assignments---cu240b-2)

##### Two-wire control, method 3

![Two-wire control, method 3](images/114043276683_DV_resource.Stream@PNG-en-US.png)

Two-wire control, method 3

Commands "ON/OFF1 clockwise rotation" and "ON/OFF1 counter-clockwise rotation" switch on the motor - and simultaneously select a direction of rotation. The converter accepts a new command at any time, independent of the motor speed.

Function table

| ON/OFF1 clockwise rotation | ON/OFF1 counter-clockwise rotation | Function |
| --- | --- | --- |
| 0 | 0 | OFF1: The motor stops. |
| 1 | 0 | ON: Clockwise rotation of motor. |
| 0 | 1 | ON: Counter-clockwise rotation of motor. |
| 1 | 1 | OFF1: The motor stops. |

Select two-wire control, method 3

| Parameter | Description |
| --- | --- |
| p0015 = 18 | **Macro drive unit**   You must carry out quick commissioning in order to set parameter p0015.  Assigning digital inputs DI to the commands:  DI 0: ON/OFF1 clockwise rotation  DI 1: ON/OFF1 counter-clockwise rotation |

Changing the assignment of the digital inputs

| Parameter | Description |
| --- | --- |
| p3330[0 … n] = 722.x | **BI: 2/3 wire control command 1** (ON/OFF1 clockwise rotation) |
| p3331[0 … n] = 722.x | **BI: 2/3 wire control command 2** (ON/OFF1 counter-clockwise rotation)  Example: p3331 = 722.0 ⇒ DI 0: ON/OFF1 counter-clockwise rotation |

##### Three-wire control, method 1

![Three-wire control, method 1](images/114043989643_DV_resource.Stream@PNG-en-US.png)

Three-wire control, method 1

The "Enable" command is a precondition for switching on the motor. Commands "ON clockwise rotation" and "ON counter-clockwise rotation" switch on the motor - and simultaneously select a direction of rotation. Removing the enable switches the motor off (OFF1).

Function table

| Enable/OFF1 | ON clockwise rotation | ON counter-clockwise rotation | Function |
| --- | --- | --- | --- |
| 0 | 0 or 1 | 0 or 1 | OFF1: The motor stops. |
| 1 | 0→1 | 0 | ON: Clockwise rotation of motor. |
| 1 | 0 | 0→1 | ON: Counter-clockwise rotation of motor. |
| 1 | 1 | 1 | OFF1: The motor stops. |

Select three-wire control, method 1

| Parameter | Description |
| --- | --- |
| p0015 = 19 | **Macro drive unit**   You must carry out quick commissioning in order to set parameter p0015.  Assigning digital inputs DI to the commands:  DI 0: Enable / OFF1  DI 1: ON clockwise rotation  DI 2: ON counter-clockwise rotation |

Changing the assignment of the digital inputs

| Parameter | Description |
| --- | --- |
| p3330[0 … n] = 722.x | **BI: 2/3 wire control command 1** (enable/OFF1) |
| p3331[0 … n] = 722.x | **BI: 2/3 wire control command 2** (ON clockwise rotation) |
| p3332[0 … n] = 722.x | **BI: 2/3 wire control command 3** (ON counter-clockwise rotation)  Example: p3332 = 722.0 ⇒ DI 0: ON counter-clockwise rotation |

---

**See also**

[Converter control using digital inputs](#converter-control-using-digital-inputs)
  
[SINAMICS G120 interface assignments - CU240B-2](#sinamics-g120-interface-assignments---cu240b-2)

##### Three-wire control, method 2

![Three-wire control, method 2](images/114045597195_DV_resource.Stream@PNG-en-US.png)

Three-wire control, method 2

The "Enable" command is a precondition for switching on the motor. The "ON" command switches the motor on. The "Reversing" command inverts the motor direction of rotation. Removing the enable switches the motor off (OFF1).

Function table

| Enable/OFF1 | ON | Reversing | Function |
| --- | --- | --- | --- |
| 0 | 0 or 1 | 0 or 1 | OFF1: The motor stops. |
| 1 | 0→1 | 0 | ON: Clockwise rotation of motor. |
| 1 | 0→1 | 1 | ON: Counter-clockwise rotation of motor. |

Select three-wire control, method 2

| Parameter | Description |
| --- | --- |
| p0015 = 20 | **Macro drive unit**   You must carry out quick commissioning in order to set parameter p0015.  Assigning digital inputs DI to the commands:  DI 0: Enable / OFF1  DI 1: ON  DI 2: Reversing |

Changing the assignment of the digital inputs

| Parameter | Description |
| --- | --- |
| p3330[0 … n] = 722.x | **BI: 2/3 wire control command 1** (enable/OFF1) |
| p3331[0 … n] = 722.x | **BI: 2/3 wire control command 2** (ON)  Example: p3331 = 722.0 ⇒ DI 0: ON command |
| p3332[0 … n] = 722.x | **BI: 2/3 wire control command 3** (reversing) |

---

**See also**

[Converter control using digital inputs](#converter-control-using-digital-inputs)
  
[SINAMICS G120 interface assignments - CU240B-2](#sinamics-g120-interface-assignments---cu240b-2)

##### Running the motor in jog mode (JOG function)

The "Jog" function is typically used to temporarily move a machine part using local control commands, e.g. a transport conveyor belt.

![Figure](images/114047473931_DV_resource.Stream@PNG-en-US.png)

Commands "Jog 1" or "Jog: 2" switch the motor on and off.

The commands are only active when the converter is in the "Ready for switching on" state.

![Behavior of the motor when "jogging"](images/103438462603_DV_resource.Stream@PNG-en-US.png)

Behavior of the motor when "jogging"

After switching on, the motor accelerates to the setpoint, jog 1 or setpoint, jog 2. The two different setpoints can, for example, be assigned to motor clockwise and counter-clockwise rotation.

When jogging, the same ramp-function generator is active as for the ON/OFF1 command.

###### Settings for jog

| Parameter | Description |  |
| --- | --- | --- |
| p1058 | **Jog 1 speed setpoint** (factory setting 150 rpm) |  |
| p1059 | **Jog 2 speed setpoint** (factory setting -150 rpm) |  |
| p1082 | **Maximum speed** (factory setting 1500 rpm) |  |
| p1110 | **Disable negative direction** |  |
| =0: Negative direction of rotation is enabled | =1: Negative direction of rotation is disabled |  |
| p1111 | **Disable positive direction** |  |
| =0: Positive direction of rotation is enabled | =1: Positive direction of rotation is disabled |  |
| p1113 | **Setpoint inversion** |  |
| =0: Setpoint is not inverted | =1: Setpoint is inverted |  |
| p1120 | **Ramp-function generator ramp-up time** (factory setting 10 s) |  |
| p1121 | **Ramp-function generator ramp-down time** (factory setting 10 s) |  |
| p1055 = 722.0 | **Jog bit 0:** Select jog 1 via digital input 0 |  |
| p1056 = 722.1 | **Jog bit 1:** Select jog 2 via digital input 1 |  |

#### Command sources

This section contains information on the following topics:

- [Command sources](#command-sources-1)

##### Command sources

###### Overview of the command sources

The command source is the interface via which the converter receives its control commands. The following interfaces are available:

- Terminals, e.g. digital inputs
- Fieldbus (PROFIdrive)

###### Changing the command source

The command source is selected in the basic commissioning in the drive wizard.

If you must subsequently change the command source, set parameter p700.

---

**See also**

[Switching over the converter control (command data set)](Configuring%20SINAMICS%20G120-G115D-G110M%20drives.md#switching-over-the-converter-control-command-data-set)

#### Setpoint sources

This section contains information on the following topics:

- [Overview of the setpoint sources](#overview-of-the-setpoint-sources)
- [Analog input as setpoint source](#analog-input-as-setpoint-source)
- [Specifying the setpoint via the fieldbus](#specifying-the-setpoint-via-the-fieldbus)
- [Motorized potentiometer as setpoint source](#motorized-potentiometer-as-setpoint-source)
- [Fixed speed as setpoint source](#fixed-speed-as-setpoint-source)
- [Pulse input as source of setpoint value](#pulse-input-as-source-of-setpoint-value)

##### Overview of the setpoint sources

![Figure](images/109300151819_DV_resource.Stream@PNG-en-US.png)

The converter receives its main setpoint from the setpoint source. The main setpoint generally specifies the motor speed.

![Setpoint sources for the converter](images/109300228363_DV_resource.Stream@PNG-en-US.png)

Setpoint sources for the converter

You have the following options when selecting the source of the main setpoint:

- Converter fieldbus interface
- Analog input of the converter
- Motorized potentiometer emulated in the converter
- Fixed setpoints stored in the converter
- Probe: The converter converts a sequence of pulse signals at the digital input into an analog value.

You have the same selection options when selecting the source of the supplementary setpoint.

Under the following conditions, the converter switches from the main setpoint to other setpoints:

- When the technology controller is active, its output specifies the motor speed.
- When jogging is active.
- When controlling from an operator panel or Startdrive.

##### Analog input as setpoint source

###### Procedure

If you have selected a pre-assignment without a function of the analog input, then you must interconnect the parameter of the main setpoint with an analog input.

![Example: Analog input 0 as setpoint source](images/113717689611_DV_resource.Stream@PNG-en-US.png)

Example: Analog input 0 as setpoint source

In the quick commissioning, you define the preassignment for the converter interfaces. Depending on what has been preassigned, after quick commissioning, the analog input can be interconnected with the main setpoint.

###### Example

Setting with analog input 0 as setpoint source:

| Parameter | Description |
| --- | --- |
| p1070 = 755[0] | Interconnects main setpoint with analog input 0 |
| p1075 = 755[0] | Interconnects supplementary setpoint with analog input 0 |

###### Parameter

| Parameter | Description | Setting |
| --- | --- | --- |
| r0755[0...1] | CO: CU analog inputs, actual value in percent | Displays the actual referenced input value of the analog inputs  [0] = analog input 0  [1] = analog input 1 |
| p1070[0…n] | CI: Main setpoint | Signal source for the main setpoint  The factory setting depends on the converter.  Converter with PROFIBUS or PROFINET interface: [0] 2050[1]  Converter without PROFIBUS or PROFINET interface: [0] 755[0] |
| p1071[0…n] | CI: Main setpoint scaling | Signal source for scaling the main setpoint  Factory setting: 1 |
| r1073 | CO: Main setpoint active | Displays the active main setpoint |
| p1075[0…n] | CI: Supplementary setpoint | Signal source for the supplementary setpoint  Factory setting: 0 |
| p1076[0…n] | CI: Supplementary setpoint scaling | Signal source for scaling the supplementary setpoint  Factory setting: 0 |

##### Specifying the setpoint via the fieldbus

###### Function description

![Fieldbus as setpoint source](images/113720697867_DV_resource.Stream@PNG-en-US.png)

Fieldbus as setpoint source

In the quick commissioning, you define the preassignment for the converter interfaces. Depending on what has been preassigned, after quick commissioning, the receive word PZD02 can be interconnected with the main setpoint.

###### Example

Setting with receive word PZD02 as setpoint source:

| Parameter | Description |
| --- | --- |
| p1070 = 2050[1] | Interconnects the main setpoint with the receive word PZD02 from the fieldbus. |
| p1075 = 2050[1] | Interconnects the supplementary setpoint with receive word PZD02 from the fieldbus. |

###### Parameter

| Parameter | Description | Setting |
| --- | --- | --- |
| p1070[0…n] | CI: Main setpoint | Signal source for the main setpoint  The factory setting depends on the Control Unit.  With PROFIBUS or PROFINET interface: [0] 2050[1]  Without PROFIBUS or PROFINET interface: [0] 755[0] |
| p1071[0…n] | CI: Main setpoint scaling | Signal source for scaling the main setpoint  Factory setting: 1 |
| r1073 | CO: Main setpoint active | Displays the active main setpoint |
| p1075[0…n] | CI: Supplementary setpoint | Signal source for the supplementary setpoint  Factory setting: 0 |
| p1076[0…n] | CI: Supplementary setpoint scaling | Signal source for scaling the supplementary setpoint  Factory setting: 0 |
| r2050[0…11] | CO: PROFIdrive PZD receive word | Connector output to interconnect the PZD received from the fieldbus controller in the word format.  [1] Most standard telegrams receive the speed setpoint as receive word PZD02. |

###### Further information

For further information refer to the function diagrams 2468, 9360 and 3030 of the List Manual.

##### Motorized potentiometer as setpoint source

###### Function description

The "Motorized potentiometer" function emulates an electromechanical potentiometer. The output value of the motorized potentiometer can be set with the "higher" and "lower" control signals.

![Motorized potentiometer as setpoint source](images/113721990923_DV_resource.Stream@PNG-en-US.png)

Motorized potentiometer as setpoint source

![Function chart of motorized potentiometer](images/109489714955_DV_resource.Stream@PNG-en-US.png)

Function chart of motorized potentiometer

###### Example

Setting with the motorized potentiometer as setpoint source:

| Parameter | Description |
| --- | --- |
| p1070 = 1050 | Interconnects the main setpoint with the motorized potentiometer output. |

###### Parameter

Basic setup of motorized potentiometer

| Parameter | Description | Setting |
| --- | --- | --- |
| p1035[0…n] | BI: Motorized potentiometer setpoint higher | Signal source to continuously increase the setpoint  The factory setting depends on the converter.  converters with PROFIBUS or PROFINET interface:  [0] 2090.13  [1] 0  converters without PROFIBUS or PROFINET interface: 0 |
| p1036[0…n] | BI: Motorized potentiometer setpoint lower | Signal source to continuously decrease the setpoint  The factory setting depends on the converter.  converters with PROFIBUS or PROFINET interface:  [0] 2090.14  [1] 0  converters without PROFIBUS or PROFINET interface: 0 |
| p1040[0…n] | Motorized potentiometer start value [rpm] | Start value that is effective when the motor is switched on.  Factory setting: 0 rpm |
| p1047 | MOP ramp-up time [s] | MOP ramp-up time  Factory setting: 10 s |
| p1048 | MOP ramp-down time [s] | MOP ramp-down time:  Factory setting: 10 s |
| r1050 | Motorized potentiometer, setpoint after the ramp-function generator | Motorized potentiometer, setpoint after the ramp-function generator |
| p1070[0…n] | CI: Main setpoint | Signal source for the main setpoint  The factory setting depends on the Control Unit.  With PROFIBUS or PROFINET interface: [0] 2050[1]  Without PROFIBUS or PROFINET interface: [0] 755[0] |
| p1071[0…n] | CI: Main setpoint scaling | Signal source for scaling the main setpoint  Factory setting: 1 |
| r1073 | CO: Main setpoint active | Displays the active main setpoint |
| p1075[0…n] | CI: Supplementary setpoint | Signal source for the supplementary setpoint  Factory setting: 0 |
| p1076[0…n] | CI: Supplementary setpoint scaling | Signal source for scaling the supplementary setpoint  Factory setting: 0 |

Extended setup of motorized potentiometer

| Parameter | Description | Setting |
| --- | --- | --- |
| p1030[0…n] | Motorized potentiometer configuration | Configuration for the motorized potentiometer  Factory setting: 00110 bin  .00  Storage active = 0: After the motor has been switched on, the setpoint = p1040 = 1: After the motor has switched off, the converter saves the setpoint. After the motor has switched on, the setpoint = the stored value  .01  Automatic mode, ramp-function generator active (1-signal via BI: p1041) = 0: Ramp-up/ramp-down time = 0 = 1: With ramp-function generator  In manual mode (p1041 = 0), the ramp-function generator is always active.  .02  Initial rounding active 1: With initial rounding. Using the initial rounding function it is possible to enter very small setpoint changes  .03  Storage in NVRAM active 1: If bit 00 = 1, the setpoint is retained during a power failure  .04  Ramp-function generator always active 1: The converter also calculates the ramp-function generator when the motor is switched off |
| p1037[0…n] | Motorized potentiometer maximum speed [rpm] | The converter limits the motorized potentiometer output to p1037.  Factory setting: 0 rpm  After quick commissioning, the converter sets the parameter to the appropriate value. |
| p1038[0…n] | Motorized potentiometer minimum speed [rpm] | The converter limits the motorized potentiometer output to p1038.  Factory setting: 0 rpm  After quick commissioning, the converter sets the parameter to the appropriate value. |
| p1043[0…n] | BI: Motorized potentiometer, accept setting value | Signal source for accepting the setting value. The motorized potentiometer accepts the setting value p1044 on signal change p1043 = 0 → 1.  Factory setting: 0 |
| p1044[0…n] | CI: Motorized potentiometer, setting value | Signal source for the setting value  Factory setting: 0 |

###### Further information

For more information about the motorized potentiometer, refer to function diagram 3020 in the List Manual.

##### Fixed speed as setpoint source

###### Function description

![Fixed speeds as setpoint source](images/113772184331_DV_resource.Stream@PNG-en-US.png)

Fixed speeds as setpoint source

The converter makes a distinction between two methods when selecting the fixed speed setpoints:

**Directly selecting a fixed speed setpoint**

You set 4 different fixed speed setpoints. Up to 16 different setpoints are obtained by adding one or several of the four fixed speed setpoints.

![Direct selection of the fixed speed setpoint](images/109490159627_DV_resource.Stream@PNG-en-US.png)

Direct selection of the fixed speed setpoint

**Selecting the fixed speed setpoint, binary**

You set 16 different fixed speed setpoints. You precisely select one of these 16 fixed speed setpoints by combining four selection bits.

![Binary selection of the fixed speed setpoint](images/109490543627_DV_resource.Stream@PNG-en-US.png)

Binary selection of the fixed speed setpoint

###### Example

After it has been switched on, a conveyor belt only runs with two different velocities. The motor should now operate with the following corresponding speeds:

- The signal at digital input 0 switches the motor on and accelerates it up to 300 rpm.
- The signal at digital input 1 accelerates the motor up to 2000 rpm.
- With signals at both digital inputs, the motor accelerates up to 2300 rpm.

Settings for the application example

| Parameter | Description |
| --- | --- |
| p1001 = 300.000 | **Fixed speed setpoint 1** [rpm] |
| p1002 = 2000.000 | **Fixed speed setpoint 2** [rpm] |
| p0840 = 722.0 | **ON/OFF1:** Switches on the motor with digital input 0 |
| p1070 = 1024 | **Main setpoint:** Interconnects the main setpoint with fixed speed setpoint. |
| p1020 = 722.0 | **Fixed speed setpoint selection bit 0:** Interconnects fixed speed setpoint 1 with digital input 0 (DI 0). |
| p1021 = 722.1 | **Fixed speed setpoint selection bit 1:** Interconnects fixed speed setpoint 2 with digital input 1 (DI 1). |
| p1016 = 1 | **Fixed speed setpoint mode:** Directly selects fixed speed setpoints. |

Resulting fixed speed setpoints for the application example

| Fixed speed setpoint selected via | Resulting setpoint |
| --- | --- |
| DI 0 = 0 | Motor stops |
| DI 0 = 1 and DI 1 = 0 | 300 rpm |
| DI 0 = 1 and DI 1 = 1 | 2300 rpm |

###### Parameter

| Parameter | Description | Setting |
| --- | --- | --- |
| p1001[0...n] | Fixed speed setpoint 1 [rpm] | Fixed speed setpoint 1  Factory setting: 0 rpm |
| p1002[0...n] | Fixed speed setpoint 2 [rpm] | Fixed speed setpoint 2  Factory setting: 0 rpm |
| ... | ... | ... |
| p1015[0...n] | Fixed speed setpoint 15 [rpm] | Fixed speed setpoint 15  Factory setting: 0 rpm |
| p1016 | Fixed speed setpoint mode | Fixed speed setpoint mode  Factory setting: 1  1: Direct  2: Binary |
| p1020[0...n] | Fixed speed setpoint selection, bit 0 | Fixed speed setpoint selection, bit 0  Factory setting: 0 |
| p1021[0...n] | Fixed speed setpoint selection, bit 1 | Fixed speed setpoint selection, bit 1  Factory setting: 0 |
| p1022[0...n] | Fixed speed setpoint selection, bit 2 | Fixed speed setpoint selection, bit 2  Factory setting: 0 |
| p1023[0...n] | Fixed speed setpoint selection, bit 3 | Fixed speed setpoint selection, bit 3  Factory setting: 0 |
| r1024 | Fixed speed setpoint active | Fixed speed setpoint active |
| r1025.0 | Fixed speed setpoint status | Fixed speed setpoint status  1 signal: Fixed speed setpoint is selected |

###### Further information

Additional information about binary selection can be found in function diagram 3010 in the List Manual.

Additional information about direct selection can be found in function diagram 3011 in the List Manual.

##### Pulse input as source of setpoint value

###### Interconnecting the digital input as setpoint source

Using the "probe" function ("pulse train"), the converter converts a pulse signal at one of the digital inputs DI 24 … DI 27 to an analog signal. The converter evaluates a signal with a max. frequency of 32 kHz.

![Pulse signal of the digital input as setpoint source](images/109490583051_DV_resource.Stream@PNG-en-US.png)

Pulse signal of the digital input as setpoint source

The "probe" function ("pulse train") creates an analog value from a pulse train at a digital input of the converter.

![Converting the pulse signal at the digital input to an analog value](images/109491133451_DV_resource.Stream@PNG-en-US.png)

Converting the pulse signal at the digital input to an analog value

| Parameter | Description |
| --- | --- |
| p1070 = 586 | **Main setpoint** (factory setting depending on the Control Unit) Interconnect the result of the speed calculation with the main setpoint. |
| p1075 = 586 | **Supplementary setpoint** (factory setting 0) Interconnect the result of the speed calculation with the supplementary setpoint. |

When you use this function, you cannot use any of the digital inputs to monitor the speed.   
[Monitoring the speed via digital input](#monitoring-the-speed-via-digital-input)

###### Setting the probe

| Parameter | Description |
| --- | --- |
| p0490 | **Probe** <sup> 1)</sup>  **invert** (factory setting 0000bin) The 3rd bit of the parameter value inverts the input signal of digital input 3 for the probe. |
| p0580 | **Probe** <sup> 1)</sup>  **input terminal** (factory setting 0) Interconnect the probe input with a digital input. |
| p0581 | **Probe** <sup> 1)</sup>  **edge**(factory setting 0) Edge to evaluate the probe signal for the actual measuring speed value 0: 0/1 edge 1: 1/0 edge |
| p0582 | **Probe** <sup> 1)</sup>  **Pulses per revolution** (factory setting 1) Number of pulses per revolution. |
| p0583 | **Probe** <sup> 1)</sup>  **Maximum measurement time** (factory setting 10 s) Maximum measurement time for the probe. If there is no new pulse before the maximum measuring time elapses, the converter sets the actual speed value in r0586 to zero. The time is restarted with the next pulse. |
| p0585 | **Probe** <sup> 1)</sup>  **Gear ratio** (factory setting 1) The converter multiplies the measured speed by the gear ratio before displaying it in r0586. |
| r0586 | **Probe** <sup> 1)</sup>  **Actual speed value**  Result of the speed calculation. |

#### Setpoint processing

This section contains information on the following topics:

- [Overview of setpoint processing](#overview-of-setpoint-processing)
- [Invert setpoint](#invert-setpoint)
- [Inhibit direction of rotation](#inhibit-direction-of-rotation)
- [Skip frequency bands and minimum speed](#skip-frequency-bands-and-minimum-speed)
- [Maximum speed](#maximum-speed)
- [Speed limitation](#speed-limitation)
- [Ramp-function generator](#ramp-function-generator)

##### Overview of setpoint processing

###### Overview

![Overview](images/149906770059_DV_resource.Stream@PNG-en-US.png)

Setpoint processing influences the setpoint using the following functions:

- "Invert" inverts the motor direction of rotation.
- The "Inhibit direction of rotation" function prevents the motor from rotating in the incorrect direction; this function can make sense for conveyor belts, extruders, pumps and fans, for example.
- The "Skip frequency bands" prevent the motor from being continuously operated within these skip bands. This function avoids mechanical resonance effects by only permitting the motor to operate briefly at specific speeds.
- The "Speed limitation" function protects the motor and the driven load against excessively high speeds.
- The "Ramp-function generator" function prevents the setpoint from suddenly changing. As a consequence, the motor accelerates and brakes with a reduced torque.

![Setpoint processing in the converter](images/113775513483_DV_resource.Stream@PNG-en-US.png)

Setpoint processing in the converter

##### Invert setpoint

###### Function description

![Function description](images/113772621579_DV_resource.Stream@PNG-en-US.png)

The function inverts the sign of the setpoint using a binary signal.

###### Example

To invert the setpoint via an external signal, interconnect parameter p1113 with a binary signal of your choice.

Application examples showing how a setpoint is inverted

| Parameter | Description |
| --- | --- |
| p1113 = 722.1 | Digital input 1 = 0: Setpoint remains unchanged. Digital input 1 = 1: Converter inverts the setpoint. |
| p1113 = 2090.11 | Inverts the setpoint via the fieldbus (control word 1, bit 11). |

###### Parameter

| Parameter | Description | Setting |
| --- | --- | --- |
| p1113[0…n] | BI: Setpoint inversion | Signal source for inverting the setpoint  1 signal: Invert setpoint  The factory setting depends on the fieldbus interface. |

##### Inhibit direction of rotation

###### Function description

![Function description](images/109495291531_DV_resource.Stream@PNG-en-US.png)

In the factory setting of the converter, both motor directions of rotation are enabled.

Set the corresponding parameter to a value = 1 to permanently block directions of rotation.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Incorrect direction of motor rotation if the parameterization is not suitable**  If you are using an analog input as speed setpoint source, then for a setpoint = 0 V, noise voltages can be superimposed on the analog input signal. After the on command, the motor accelerates up to the minimum frequency in the direction of the random polarity of the noise voltage. A motor rotating in the wrong direction can cause significant material damage to the machine or system.  - Inhibit the motor direction of rotation that is not permissible. |  |

###### Example

Application examples showing how a setpoint is inverted

| Parameter | Description |
| --- | --- |
| p1110[0] = 1 | Negative direction of rotation is permanently inhibited. |
| p1110[0] = 722.3 | Digital input 3 = 0: Negative direction of rotation is enabled.  Digital input 3 = 1: Negative direction of rotation is inhibited. |

###### Parameter

| Parameter | Description | Setting |
| --- | --- | --- |
| p1110[0…n] | BI: Inhibit negative direction | Signal source to inhibit the negative direction  0 signal: Direction of rotation is enabled  1 signal: Direction of rotation is inhibited  Factory setting: 0 |
| p1111[0…n] | BI: Inhibit positive direction | Signal source to inhibit the positive direction  0 signal: Direction of rotation is enabled  1 signal: Direction of rotation is inhibited  Factory setting: 0 |

##### Skip frequency bands and minimum speed

###### Skip frequency bands

The converter has four skip frequency bands that prevent continuous motor operation within a specific speed range. Further information is provided in function diagram 3050 of the List Manual.

###### Minimum speed

The converter prevents continuous motor operation at speeds < minimum speed.

![Minimum speed](images/113780065547_DV_resource.Stream@PNG-en-US.png)

Speeds where the absolute value is less than the minimum speed are only possible during motor operation when accelerating or braking.

Setting the minimum speed

| Parameter | Description |
| --- | --- |
| p1080 | **Minimum speed** (factory setting: 0 rpm) |
| p1106 | **CI: Minimum speed signal source** (factory setting: 0)  Dynamic specification of the minimum speed |

##### Maximum speed

###### Function

|  |  |  |
| --- | --- | --- |
| The maximum speed limits the speed setpoint range for both directions of rotation.  The converter generates a message (fault or alarm) when the maximum speed is exceeded. |  | ![Function](images/103439309835_DV_resource.Stream@PNG-en-US.png) |

The maximum speed also acts as a reference value for several other functions, e.g. the ramp-function generator.

If you must limit the speed depending on the direction of rotation, then you can define speed limits for each direction.

Parameters for minimum and maximum speed

| Parameter | Description |
| --- | --- |
| p1082 | **Maximum speed** (factory setting: 1500 rpm) |
| p1083 | **Speed limit, positive direction of rotation** (factory setting: 210000 rpm) |
| p1086 | **Speed limit, negative direction of rotation** (factory setting: -210000 rpm) |

##### Speed limitation

The maximum speed limits the speed setpoint range for both directions of rotation.

![Figure](images/109563157003_DV_resource.Stream@PNG-en-US.png)

The converter generates a message (fault or alarm) when the maximum speed is exceeded.

If you must limit the speed depending on the direction of rotation, then you can define speed limits for each direction.

Parameters for the speed limitation

| Parameter | Description |
| --- | --- |
| p1082 | **Maximum speed** (factory setting: 1500 rpm) |
| p1083 | **Speed limit, positive direction of rotation** (factory setting: 210,000 rpm) |
| p1085 | **CI: Speed limit, positive direction of rotation** (factory setting: 1083) |
| p1086 | **Speed limit, negative direction of rotation** (factory setting: -210,000 rpm) |
| p1088 | **CI: Speed limit, negative direction of rotation** (factory setting: 1086) |

##### Ramp-function generator

This section contains information on the following topics:

- [Ramp-function generator](#ramp-function-generator-1)
- [Extended ramp-function generator](#extended-ramp-function-generator)
- [Basic ramp-function generator](#basic-ramp-function-generator)

###### Ramp-function generator

The ramp-function generator in the setpoint channel limits the rate change of the speed setpoint (acceleration). A reduced acceleration reduces the accelerating torque of the motor. In this case, the motor reduces the load on the mechanical system of the driven machine.

You can select between two different ramp-function generator types:

- Extended ramp-function generator

  The expanded ramp-function generator limits not only the acceleration but also the change in acceleration (jerk) by rounding the setpoint. In this case, the torque does not rise suddenly in the motor.
- [Basic ramp-function generator](#basic-ramp-function-generator)

  The basic ramp-function generator limits the acceleration, however not the rate the acceleration changes (jerk).

---

**See also**

[Extended ramp-function generator](#extended-ramp-function-generator)

###### Extended ramp-function generator

###### Extended ramp-function generator

The ramp-up and ramp-down times of the extended ramp-function generator can be set independently of each other. The optimum times that you select depend on your particular application in question and can range from just a few 100 ms (e.g. for belt conveyor drives) to several minutes (e.g. for centrifuges).

![Extended ramp-function generator](images/113845935115_DV_resource.Stream@PNG-en-US.png)

Initial and final rounding permit smooth, jerk-free acceleration and braking.

The ramp-up and ramp-down times of the motor are increased by the rounding times:

- Effective ramp-up time = p1120 + 0.5 × (p1130 + p1131).
- Effective ramp-down time = p1121 + 0.5 × (p1130 + p1131).

Additional parameters to set the extended ramp-function generator

| Parameter | Description |  |
| --- | --- | --- |
| p1115 | **Ramp-function generator, selection** (factory setting: 1) Select ramp-function generator 0: Basic ramp-function generator 1: Extended ramp-function generator |  |
| p1120 | **Ramp-function generator, ramp-up time** (factory setting: 10 s) Accelerating time in seconds from zero speed up to the maximum speed p1082 |  |
| p1121 | **Ramp-function generator, ramp-down time** (factory setting: 10 s) Braking time in seconds from the maximum speed down to standstill |  |
| p1130 | **Ramp-function generator, initial rounding time** (factory setting: 0 s) Initial rounding for the extended ramp-function generator. The value applies for ramp-up and ramp-down |  |
| p1131 | **Ramp-function generator, final rounding time** (factory setting: 0 s) Final rounding for the extended ramp-function generator. The value applies for ramp-up and ramp-down |  |
| p1134 | **Ramp-function generator, rounding type** (factory setting: 0) 0: Continuous smoothing 1: Discontinuous smoothing | ![Extended ramp-function generator](images/103439430923_DV_resource.Stream@PNG-en-US.png) |
| p1135 | **OFF3 ramp-down time** (factory setting: 0 s) The quick stop (OFF3) has its own ramp-down time |  |
| p1136 | **OFF3 initial rounding time** (factory setting: 0 s) Initial rounding time for OFF3 for the extended ramp-function generator. |  |
| p1137 | **OFF3 final rounding time** (factory setting: 0 s) Final rounding time for OFF3 for the extended ramp-function generator. |  |

You can find more information in function diagram 3070 and in the parameter list of the List Manual.

###### Setting the extended ramp-function generator

**Procedure**

1. Enter the highest possible speed setpoint.
2. Switch on the motor.
3. Evaluate your drive response.

   - If the motor accelerates too slowly, then reduce the ramp-up time.

     An excessively short ramp-up time means that the motor will reach its current limiting when accelerating, and will temporarily not be able to follow the speed setpoint. In this case, the drive exceeds the set time.
   - If the motor accelerates too fast, then extend the ramp-up time.
   - Increase the initial rounding if the acceleration is jerky.
   - In most applications, it is sufficient when the final rounding is set to the same value as the initial rounding.
4. Switch off the motor.
5. Evaluate your drive response.

   - If the motor decelerates too slowly, then reduce the ramp-down time.

     The minimum ramp-down time that makes sense depends on your particular application. Depending on the Power Module used, for an excessively short ramp-down time, the converter either reaches the motor current, or the DC link voltage in the converter becomes too high.
   - Extend the ramp-down time if the motor is braked too quickly or the converter goes into a fault condition when braking.
6. Repeat steps 1 … 5 until the drive behavior meets the requirements of the machine or plant.

You have set the extended ramp-function generator.

###### Basic ramp-function generator

###### Basic ramp-function generator

![Basic ramp-function generator](images/113846670603_DV_resource.Stream@PNG-en-US.png)

When compared to the extended ramp-function generator, the basic ramp-function generator has no rounding times.

Parameters to set the basic ramp-function generator

| Parameter | Description |
| --- | --- |
| p1115 = 0 | **Ramp-function generator, selection** (factory setting: 1) Select ramp-function generator 0: Basic ramp-function generator 1: Extended ramp-function generator |
| p1120 | **Ramp-function generator, ramp-up time** (factory setting: 10 s) Accelerating time in seconds from zero speed up to the maximum speed p1082 |
| p1121 | **Ramp-function generator, ramp-down time** (factory setting: 10 s) Braking time in seconds from the maximum speed down to standstill |
| p1135 | **OFF3 ramp-down time** (factory setting: 0 s) The quick stop (OFF3) has its own ramp-down time |

#### Motor control

This section contains information on the following topics:

- [Closed-loop speed control](#closed-loop-speed-control)
- [V/f control](#vf-control)

##### Closed-loop speed control

This section contains information on the following topics:

- [Properties of the vector control](#properties-of-the-vector-control)
- [Default setting as a result of the application class](#default-setting-as-a-result-of-the-application-class)
- [Checking the encoder signal](#checking-the-encoder-signal)
- [Setting and optimizing the speed controller](#setting-and-optimizing-the-speed-controller)
- [Advanced settings](#advanced-settings)
- [Torque control](#torque-control)
- [Friction characteristic](#friction-characteristic)
- [Moment of inertia estimator](#moment-of-inertia-estimator)

###### Properties of the vector control

###### Overview

The vector control comprises closed-loop current control and a higher-level closed-loop speed control.

![Simplified function diagram for vector control with speed controller](images/111215907723_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| <sup>1)</sup> | for induction motors |
| <sup>2)</sup> | Selecting the control mode |
| <sup>3)</sup> | Settings that are required |

Simplified function diagram for vector control with speed controller

Using the motor model, the converter calculates the following closed-loop control signals from the measured phase currents and the output voltage:

- Current component I<sub>q</sub>
- Current component I<sub>q</sub>
- Speed actual value for encoderless vector control

The setpoint of the current component I<sub>d</sub> (flux setpoint) is obtained from the motor data. For speeds above the rated speed, the converter reduces the flux setpoint along the field weakening characteristic.

When the speed setpoint is increased, the speed controller responds with a higher setpoint for current component I<sub>q</sub> (torque setpoint). The closed-loop control responds to a higher torque setpoint by adding a higher slip frequency to the output frequency. The higher output frequency also results in a higher motor slip, which is proportional to the accelerating torque. I<sub>q</sub> and I<sub>d</sub>controllers keep the motor flux constant using the output voltage, and adjust the matching current component I<sub>q</sub> in the motor.

The complete function diagrams 6020 ff. for vector control are provided in the List Manual.

###### Settings required for vector control

Select the vector control during to quick commissioning.

In order to achieve a satisfactory control response, as a minimum you must set the partial functions – shown with gray background in the diagram above – to match your particular application:

- **Motor and current model**: In the quick commissioning, correctly set the motor data on the rating plate corresponding to the connection type (Y/Δ), and carry out the motor data identification routine at standstill.
- **Speed limits** and **torque limits**: In the quick commissioning, set the maximum speed (p1082) and current limit (p0640) to match your particular application**.** When exiting quick commissioning, the converter calculates the torque and power limits corresponding to the current limit. The actual torque limits are obtained from the converted current and power limits and the set torque limits.
- **Speed controller**: Start the rotating measurement of the motor data identification. You must manually optimize the controller if the rotating measurement is not possible.

###### Default setting as a result of the application class

Selecting application class Dynamic Drive Control in the quick commissioning adapts the structure of the vector control, and reduces the setting options:

|  | Vector control after selecting the application class Dynamic Drive Control | Vector control without selecting an application class |
| --- | --- | --- |
| Closed-loop torque control without higher-level speed controller | Not possible | Possible |
| Droop | Not possible | Possible |
| K<sub>P</sub>- and T<sub>I</sub>adaptation | Simplified | Advanced |
| Hold or set the integral component of the speed controller | Not possible | Possible |
| Acceleration model for precontrol | Default setting | Can be activated |
| Motor data identification at standstill or with rotating measurement | Shortened, with optional transition into operation | Complete |

###### Checking the encoder signal

If you use an encoder to measure the speed, you should check the encoder signal before the encoder feedback is active.

**Procedure**

1. Set the control mode "encoderless vector control": p1300 = 20.
2. Switch-on the motor with an average speed.
3. Compare parameters r0061 (speed encoder signal in rpm) and r0021 (calculated speed in rpm) regarding the sign and absolute value.
4. If the signs do not match, invert the speed encoder signal: Set p0410 = 1.
5. If the absolute values of the two values do not match, check the setting of p0408 and the encoder wiring.

You have ensured that the scaling and polarity of the encoder signal are correct.  
❒

---

**See also**

[Properties of the vector control](#properties-of-the-vector-control)

###### Setting and optimizing the speed controller

###### Optimum behavior - post-optimization not required

Preconditions for assessing the controller response:

- The moment of inertia of the load is constant and does not depend on the speed
- The converter does not reach the set torque limits during acceleration
- You operate the motor in the range 40 % … 60 % of its rated speed

If the motor exhibits the following response, the speed control is well set and you do not have to adapt the speed controller manually:

| Symbol | Meaning |
| --- | --- |
| ![Optimum behavior - post-optimization not required](images/111293507979_DV_resource.Stream@PNG-en-US.png) | The speed setpoint (broken line) increases with the set ramp-up time and rounding.  The speed actual value follows the setpoint without any overshoot. |

###### Control optimization required

In some cases, the self optimization result is not satisfactory, or self optimization is not possible as the motor cannot freely rotate.

| Symbol | Meaning |
| --- | --- |
| ![Control optimization required](images/111294238091_DV_resource.Stream@PNG-en-US.png) | Initially, the speed actual value follows the speed setpoint with some delay, and then overshoots the speed setpoint. |
| ![Control optimization required](images/111300164491_DV_resource.Stream@PNG-en-US.png) | First, the actual speed value increases faster than the speed setpoint. Before the setpoint reaches its final value, it passes the actual value. Finally, the actual value approaches the setpoint without any significant overshoot. |

In the two cases describe above, we recommend that you manually optimize the speed control.

###### Optimizing the speed controller

**Preconditions**

- Torque precontrol is active: p1496 = 100 %.
- The load moment of inertia is constant and independent of the speed.
- The converter requires 10 % … 50 % of the rated torque to accelerate.

  When necessary, adapt the ramp-up and ramp-down times of the ramp-function generator (p1120 and p1121).
- STARTER and Startdrive have trace functions that allow the speed setpoint and actual value to be recorded.

**Procedure**

| Symbol | Meaning |
| --- | --- |
| 1. Switch on the motor. 2. Enter a speed setpoint of approximately 40 % of the rated speed. 3. Wait until the actual speed has stabilized. 4. Increase the setpoint up to a maximum of 60 % of the rated speed. 5. Monitor the associated characteristic of the setpoint and actual speed. 6. Optimize the controller by adapting the ratio of the moments of inertia of the load and motor (p0342):       | Symbol | Meaning |    | --- | --- |    | ![Optimizing the speed controller](images/111294238091_DV_resource.Stream@PNG-en-US.png)      ![Optimizing the speed controller](images/111294238091_DV_resource.Stream@PNG-en-US.png) | Initially, the speed actual value follows the speed setpoint with some delay, and then overshoots the speed setpoint. - Increase p0342 |    | ![Optimizing the speed controller](images/111300164491_DV_resource.Stream@PNG-en-US.png)      ![Optimizing the speed controller](images/111300164491_DV_resource.Stream@PNG-en-US.png) | Initially, the speed actual value increases faster than the speed setpoint. The setpoint passes the actual value before reaching its final value. Finally, the actual value approaches the setpoint without any overshoot. - Reduce p0342 | 7. Switch off the motor. 8. Set p0340 = 4. The converter again calculates the speed controller parameters. 9. Switch on the motor. 10. Over the complete speed range check as to whether the speed control operates satisfactorily with the optimized settings. |  |

You have optimized the speed controller.  
❒

When necessary, set the ramp-up and ramp-down times of the ramp-function generator (p1120 and p1121) back to the value before optimization.

###### Mastering critical applications

The drive control can become unstable for drives with a high load moment of inertia and gearbox backlash or a coupling between the motor and load that can possibly oscillate. In this case, we recommend the following settings:

- Encoderless vector control - and vector control with encoder

  - Increase p1452 (smoothing the speed actual value).
  - Increase p1472 (integral time T<sub>I</sub>): T<sub>I</sub> ≥ 4 · p1452
  - If, after these measures, the speed controller does not operate with an adequate dynamic performance, then increase p1470 (gain K<sub>P</sub>) step-by-step.
- Additional settings for vector control with encoder

  - Increase p1441 (smoothing the speed actual value): p1441 = 2 … 4 ms.

###### Advanced settings

###### K<sub>P</sub>- and T<sub>I</sub> adaptation

K<sub>p</sub> and T<sub>I</sub> adaptation suppress speed control oscillations that may occur. The "rotating measurement" of the motor data identification optimizes the speed controller. If you have performed the rotating measurement, then the K<sub>p</sub>- and T<sub>n</sub>adaptation has been set.

You can find additional information in the List Manual:

- Vector control with speed controller: Function diagram 6050
- Vector control after presetting the application class Dynamic Drive Control Function diagram 6824

###### Droop

For mechanically coupled drives, there is the risk that the drives oppose one another: Small deviations in the speed setpoint or actual value of the coupled drives can mean that the drives are operated with significantly different torques.

The droop function ensures even torque distribution between several mechanically coupled drives.

The droop function reduces the speed setpoint as a function of the torque setpoint.

![Effect of droop in the speed controller](images/111301665803_DV_resource.Stream@PNG-en-US.png)

Effect of droop in the speed controller

When droop is active, the ramp-function generators of all of the coupled drives must be set to have identical ramp-up and ramp-down times as well as rounding-off.

| Par. | Explanation |
| --- | --- |
| r1482 | **Speed controller I torque output** |
| p1488 | **Droop input source**  (factory setting: 0)  0: Droop feedback not connected 1: Droop from the torque setpoint 2: Droop from the speed control output 3: Droop from the integral output, speed controller |
| p1489 | **Droop feedback scaling**  (factory setting: 0.05)  A value of 0.05 means: At the rated motor torque, the converter reduces the speed by 5% of the rated motor speed. |
| r1490 | **Droop feedback speed reduction** |
| p1492 | **Droop feedback enable** (factory setting: 0) |

After selecting application class "Dynamic Drive Control", droop is no longer possible.

You can find additional information in the List Manual, function diagram 6030.

###### Special settings for a pulling load

For a pulling load, e.g. a hoisting gear, a permanent force is exerted on the motor, even when the motor is stationary.

For a pulling load, we recommend that you use vector control with an encoder.

If you use encoderless vector control with a pulling load, then the following settings are required:

- Set the following parameters:

  | Par. | Explanation |  |
  | --- | --- | --- |
  | p1750 | **Motor model configuration** |  |
  | Bit 07 = 1 | Use speed switchover limits that are less sensitive to external effects |  |
  | p1610 | **Static torque setpoint (encoderless)** (Factory setting: 50 %)  Set a value which is higher than the maximum load torque that occurs. |  |
- When opening the motor holding brake, enter a speed setpoint > 0.

  For speed setpoint = 0, and with the motor holding brake open, the load drops because the induction motor rotates with the slip frequency as a result of the pulling load.
- Set the ramp-up and ramp-down times ≤ 10 s in the ramp-function generator.
- If, in quick commissioning, you have selected application class Dynamic Drive Control then set p0502 = 1 (technological application: dynamic starting or reversing).

###### Torque control

Torque control is part of the vector control and normally receives its setpoint from the speed controller output. By deactivating the speed controller and directly entering the torque setpoint, the closed-loop speed control becomes closed-loop torque control. The converter then no longer controls the motor speed, but the torque that the motor generates.

![Simplified function diagram of the closed-loop torque control](images/112097206155_DV_resource.Stream@PNG-en-US.png)

Simplified function diagram of the closed-loop torque control

###### Typical applications for torque control

The torque control is used in applications where the motor speed is specified by the connected driven load. Examples of such applications include:

- Load distribution between master and follower drives:  
  The master drive is speed controlled, the follower drive is torque controlled.
- Winding machines

###### The most important settings

Prerequisites for the correct functioning of the torque control:

- You have set the motor data correctly during the quick commissioning
- You have performed a motor data identification on the cold motor

| Parameter | Description |
| --- | --- |
| p1300 | **Control mode:**  22: Torque control without speed encoder |
| p0300 … p0360 | **Motor data** is transferred from the motor type plate during quick commissioning and calculated with the motor data identification |
| p1511 | **Additional torque** |
| p1520 | **Upper torque limit** |
| p1521 | **Lower torque limit** |
| p1530 | **Motoring power limit** |
| p1531 | **Regenerative power limit** |

Additional information about this function is provided in the parameter list and in function diagrams 6030 onwards in the List Manual.

###### Friction characteristic

###### Function

In many applications, e.g. applications with geared motors or belt conveyors, the frictional torque of the load is not negligible.

The converter provides the possibility of precontrolling the torque setpoint, bypassing the speed controller. The precontrol reduces overshooting of the speed after speed changes.

![Precontrol of the speed controller with frictional torque](images/111303833739_DV_resource.Stream@PNG-en-US.png)

Precontrol of the speed controller with frictional torque

The converter calculates the current frictional torque from a friction characteristic with 10 intermediate points.

![Friction characteristic](images/111304192139_DV_resource.Stream@PNG-en-US.png)

Friction characteristic

The intermediate points of the friction characteristic are defined for positive speeds. In the negative direction of rotation, the converter uses the intermediate points with a negative sign.

###### Recording a friction characteristic

After quick commissioning, the converter sets the speeds of the intermediate points to values suitable for the rated speed of the motor. The frictional torque of all intermediate points is still equal to zero. On request, the converter records the friction characteristic: The converter accelerates the motor step by step up to the rated speed, measures the frictional torque und writes the frictional torque into the intermediate points of the friction characteristic.

**Precondition**

The motor is permitted to accelerate up to the rated speed without endangering persons or property.

**Procedure**

1. Set P3845 = 1: The converter accelerates the motor successively in both directions of rotation and averages the measurement results of the positive and negative directions.
2. Switch on the motor (ON/OFF1 = 1).
3. The converter accelerates the motor.

   During measurement, the converter signals the alarm A07961.

   When the converter has determined all the intermediate points of the friction characteristic without fault code F07963, the converter stops the motor.

You have recorded the friction characteristic.  
❒

###### Adding friction characteristic for the torque setpoint

If you enable the friction characteristic (p3842 = 1), the converter adds the output of the friction characteristic r3841 to the torque setpoint.

###### Parameter

| Parameter | Explanation |  |
| --- | --- | --- |
| p3820 …  p2839 | Intermediate points of the friction characteristic [rpm; Nm] |  |
| r3840 | **Friction characteristic status word** |  |
| .00 | 1 signal: Friction characteristic OK |  |
| .01 | 1 signal: Determination of the friction characteristic is active |  |
| .02 | 1 signal: Determination of the friction characteristic is complete |  |
| .03 | 1 signal: Determination of the friction characteristic has been aborted |  |
| .08 | 1 signal: Friction characteristic positive direction |  |
| r3841 | **Friction characteristic, output** [Nm] |  |
| p3842 | **Activate friction characteristic**   0: Friction characteristic deactivated 1: Friction characteristic activated |  |
| p3845 | **Activate friction characteristic plot** (factory setting: 0)  0: Friction characteristic plot deactivated  1: Friction characteristic plot activated, both directions  2: Friction characteristic plot activated, positive direction  3: Friction characteristic plot activated, negative direction |  |
| p3846 | **Friction characteristic plot ramp-up/ramp-down time** (factory setting: 10 s)  Ramp-up/ramp-down time for automatic plotting of the friction characteristic. |  |
| p3847 | **Friction characteristic plot warm-up period** (factory setting: 0 s)  At the start of automatic plotting, the converter accelerates the motor up to the speed = p3829 und keeps the speed constant for this time. |  |

Further information on this topic is provided in the List Manual.

###### Moment of inertia estimator

###### Background

From the load moment of inertia and the speed setpoint change, the converter calculates the accelerating torque required for the motor. Via the speed controller precontrol, the accelerating torque specifies the main percentage of the torque setpoint. The speed controller corrects inaccuracies in the precontrol (feed-forward control).

![Influence of the moment of inertia estimator on the speed control](images/111304787851_DV_resource.Stream@PNG-en-US.png)

Influence of the moment of inertia estimator on the speed control

The more precise the value of the moment of inertia in the converter, the lower the overshoot after speed changes.

![Influence of the moment of inertia on the speed](images/111306029451_DV_resource.Stream@PNG-en-US.png)

Influence of the moment of inertia on the speed

###### Function

From the actual speed, the actual motor torque and the frictional torque of the load, the converter calculates the total moment of inertia of the load and motor.

![Overview of the function of the moment of inertia estimator](images/111306239627_DV_resource.Stream@PNG-en-US.png)

Overview of the function of the moment of inertia estimator

When using the moment of inertia estimator, we recommend that you also activate the friction characteristic.

![Function](images/156526159883_DV_resource.Stream@PNG-en-US.png)
[Friction characteristic](#friction-characteristic)

**How does the converter calculate the load torque?**

![Calculating the load torque](images/111306342027_DV_resource.Stream@PNG-en-US.png)

Calculating the load torque

At low speeds, the converter calculates the load torque M<sub>L</sub> from the actual motor torque.

The calculation takes place under the following conditions:

- Speed ≥ p1226
- Acceleration setpoint < 8 1/s<sup>2</sup> (≙ speed change 480 rpm per s)
- Acceleration × moment of inertia (r1493) < 0.9 × p1560

**How does the converter calculate the moment of inertia?**

![Calculating the moment of inertia](images/111306431627_DV_resource.Stream@PNG-en-US.png)

Calculating the moment of inertia

For higher speed changes, the converter initially calculates the accelerating torque M<sub>B</sub> as difference between the motor torque M<sub>M</sub>, load torque M<sub>L</sub> and frictional torque M<sub>R</sub>:

M<sub>B</sub> = M<sub>M</sub> - M<sub>L</sub> - M<sub>R</sub>

Moment of inertia J of the motor and load is obtained from the accelerating torque M<sub>B</sub> and angular acceleration α (α = rate at which the speed changes):

J = M<sub>B</sub> / α

If all of the following conditions are met, the converter calculates the moment of inertia:

- ① The rated accelerating torque M<sub>B</sub> must satisfy the following two conditions:

  - The sign of M<sub>B</sub> is the same as the direction of the actual acceleration
  - M<sub>B</sub> > p1560 × rated motor torque (r0333)
- ② speed > p1755
- The converter has calculated the load torque in at least one direction of rotation.
- Acceleration setpoint > 8 1/s<sup>2</sup> (≙ speed change 480 rpm per s)

③ The converter calculates the load torque again after acceleration.

**Moment of inertia precontrol**

In applications where the motor predominantly operates with a constant speed, the converter can only infrequently calculate the moment of inertia using the function described above. Moment of inertia precontrol is available for situations such as these. The moment of inertia precontrol assumes that there is an approximately linear relationship between the moment of inertia and the load torque.

Example: For a horizontal conveyor, in a first approximation, the moment of inertia depends on the load.

![Moment of inertia precontrol](images/111306546827_DV_resource.Stream@PNG-en-US.png)

Moment of inertia precontrol

The relationship between load torque and torque is saved in the converter as linear characteristic.

- In a positive direction of rotation:

  Moment of inertia J = p5312 × load torque M<sub>L</sub> + p5313
- In a negative direction of rotation:

  Moment of inertia J = p5314 × load torque M<sub>L</sub> + p5315

You have the following options to determine the characteristic:

- You already know the characteristic from other measurements. In this case, you must set the parameters to known values when commissioning the system.
- The converter iteratively determines the characteristic by performing measurements while the motor is operational.

###### Activating the moment of inertia estimator

The moment of inertia estimator is deactivated in the factory setting. p1400.18 = 0, p1400.20 = 0, p1400.22 = 0.

If you performed the rotating measurement for the motor identification during quick commissioning, we recommend leaving the moment of inertia estimator deactivated.

**Preconditions**

- You have selected encoderless vector control.
- The load torque must be constant whilst the motor accelerates or brakes.

  Typical of a constant load torque are conveyor applications and centrifuges, for example.

  Fan applications, for example, are not permitted.
- The speed setpoint is free from superimposed unwanted signals.
- The motor and load are connected to each other with an interference fit.

  Drives with slip between the motor shaft and load are not permitted, e.g. as a result of loose or worn belts.

If the conditions are not met, you must not activate the moment of inertia estimator.

**Procedure**

1. Set p1400.18 = 1
2. Check: p1496 ≠ 0
3. Activate the acceleration model of the speed controller pre-control: p1400.20 = 1.

You have activated the moment of inertia estimator.  
❒

###### The most important settings

| Parameter | Explanation |  |  |
| --- | --- | --- | --- |
| r0333 | **Rated motor torque** [Nm] |  |  |
| p0341 | **Motor moment of inertia** (factory setting: 0 kgm<sup>2</sup>)  The converter sets the parameter when selecting a listed motor. The parameter is then write-protected. |  |  |
| p0342 | **Moment of inertia ratio, total to motor** (factory setting: 1)  Ratio of moment of inertia load + motor to moment of inertia of motor without load |  |  |
| p1400 | **Speed control configuration** |  |  |
| .18 | 1 signal: Moment of inertia estimator active |  |  |
| .20 | 1 signal: Acceleration model on |  |  |
| .22 | 1 signal | Moment of inertia estimator retain value when motor switched off |  |
| 0 signal | Moment of inertia estimator reset value to initial value J<sub>0</sub> when motor switched off:  J<sub>0</sub> = p0341 × p0342 + p1498  If the load torque can change when the motor is switched off, set p1400.22 = 0. |  |  |
| .24 | 1 signal | Shortened moment of inertia estimation is active.  p1400.24 = 1 reduces the duration of the moment of inertia estimation.  Disadvantage: If the accelerating torque is not constant while calculating the moment of inertia, the calculation of the moment of inertia using p1400.24 = 1 is less precise. |  |
| r1407 | **Status word, speed controller** |  |  |
| .24 | 1 signal: Moment of inertia estimator is active |  |  |
| .25 | 1 signal: Load estimator is active |  |  |
| .26 | 1 signal: Moment of inertia estimator is engaged |  |  |
| .27 | 1 signal: Shortened moment of inertia estimation is active. |  |  |
| r1493 | **Total moment of inertia, scaled**   r1493 = p0341 × p0342 × p1496 |  |  |
| p1496 | **Acceleration precontrol scaling** (factory setting: 0 %)  According to rotating measurement of the motor data identification is p1496 = 100%. |  |  |
| p1498 | **Load moment of inertia** (factory setting: 0 kgm<sup>2</sup>) |  |  |
| p1502 | **Freeze moment of inertia estimator** (factory setting: 0)  If the load torque changes when accelerating the motor, set this signal to 0. |  |  |
| 0 signal |  | Moment of inertia estimator is active |  |
| 1 signal |  | Determined moment of inertia is frozen |  |
| p1755 | **Motor model changeover speed encoderless operation**   Defines the switchover between open-loop and closed-loop controlled operation of the encoderless vector control.  When selecting the closed-loop speed control, the converter sets p1755 = 13.3% × rated speed. |  |  |

###### Advanced settings

| Parameter | Explanation |  |  |  |
| --- | --- | --- | --- | --- |
| p1226 | **Standstill detection, speed threshold** (factory setting: 20 rpm)  The moment of inertia estimator only measures the load torque for speeds ≥ p1226.  p1226 also defines from which speed the converter switches-off the motor for OFF1 and OFF3. |  |  |  |
| p1560 | **Moment of inertia estimator accelerating torque threshold value** (factory setting: 10%) |  |  |  |
| p1561 | **Moment of inertia estimator change time inertia** (factory setting: 500 ms) |  |  | The lower that p1561 or p1562 is, the shorter the moment of inertia estimator measurements.  The larger p1561 or p1562 is, the more accurate the results provided by the moment of inertia estimator. |
| p1562 | **Moment of inertia estimator change time load** (factory setting: 10 ms) |  |  |  |
| p1563 | **Moment of inertia estimator load torque positive direction of rotation** (factory setting: 0 Nm) |  |  |  |
| p1564 | **Moment of inertia estimator load torque negative direction of rotation** (factory setting: 0 Nm) |  |  |  |
| p5310 | **Moment of inertia precontrol configuration** (factory setting: 0000 bin) |  |  |  |
| .00 | 1 signal: Activates calculation of the characteristic (p5312 … p5315) |  |  |  |
| .01 | 1 signal: Activates moment of inertia precontrol |  |  |  |
|  | p5310.00 = 0, p5310.01 = 0 | Deactivating moment of inertia precontrol |  |  |
| p5310.00 = 1, p5310.01 = 0 | Adapting the moment of inertia precontrol |  |  |  |
| p5310.00 = 0, p5310.01 = 1 | Activating the moment of inertia precontrol.  The characteristic of the moment of inertia precontrol remains unchanged. |  |  |  |
| p5310.00 = 1, p5310.01 = 1 | Activating the moment of inertia precontrol. The converter adapts the characteristic in parallel. |  |  |  |
| r5311 | **Moment of inertia precontrol status word** |  |  |  |
| .00 | 1 signal: New measuring points for the characteristic of the moment of inertia precontrol are available |  |  |  |
| .01 | 1 signal: New parameters are been calculated |  |  |  |
| .02 | 1 signal: Moment of inertia precontrol active |  |  |  |
| .03 | 1 signal: The characteristic in the positive direction of rotation has been calculated and is ready |  |  |  |
| .04 | 1 signal: The characteristic in the negative direction of rotation has been calculated and is ready |  |  |  |
| .05 | 1 signal: The converter writes actual results to the parameter |  |  |  |
| p5312 | **Moment of inertia precontrol linear positive** (factory setting: 0 1/s<sup>2</sup>) |  |  | In a positive direction of rotation:  Moment of inertia = p5312 × load torque + p5313 |
| p5313 | **Moment of inertia precontrol constant positive** (factory setting: 0 kgm<sup>2</sup>) |  |  |  |
| p5314 | **Moment of inertia precontrol linear negative** (factory setting: 0 1/s<sup>2</sup>) |  |  | In a negative direction of rotation:  Moment of inertia = p5314 × load torque + p5315 |
| p5315 | **Moment of inertia precontrol constant negative** (factory setting: 0 kgm<sup>2</sup>) |  |  |  |

##### V/f control

This section contains information on the following topics:

- [Properties of V/f control](#properties-of-vf-control)
- [Characteristics of V/f control](#characteristics-of-vf-control)
- [Characteristics with Standard drive control](#characteristics-with-standard-drive-control)
- [Selecting the V/f characteristic](#selecting-the-vf-characteristic)
- [Optimising motor starting](#optimising-motor-starting)
- [Optimizing with a high break loose torque and brief overload](#optimizing-with-a-high-break-loose-torque-and-brief-overload)
- [Optimizing the motor startup for application class Standar Drive Control](#optimizing-the-motor-startup-for-application-class-standar-drive-control)

###### Properties of V/f control

V/f control sets the voltage at the motor terminals on the basis of the specified speed setpoint. The relationship between the speed setpoint and stator voltage is calculated using characteristic curves. The required output frequency is calculated on the basis of the speed setpoint and the number of pole pairs of the motor (f = n * number of pole pairs / 60, in particular: f<sub>max</sub> = p1082 * number of pole pairs / 60). The converter provides the two most important characteristics (linear and square-law). User-defined characteristic curves are also supported.

V/f control is not a high-precision method of controlling the speed of the motor. The speed setpoint and the speed of the motor shaft are always slightly different. The deviation depends on the motor load. If the connected motor is loaded with the rated torque, the motor speed is below the speed setpoint by the amount of the rated slip. If the load is driving the motor (i.e. the motor is operating as a generator), the motor speed is above the speed setpoint.

The characteristic is selected during commissioning, using p1300.

###### Overview of the V/f control

The V/f control is a closed-loop speed control with the following characteristics:

- The converter controls the output voltage using the V/f characteristic
- The output frequency is essentially calculated from the speed setpoint and the number of pole pairs of the motor
- The slip compensation corrects the output frequency depending on the load and thus increases the speed accuracy
- Not using a PI controller prevents the speed control from becoming unstable
- In applications in which greater speed accuracy is required, a closed-loop control with load-dependent voltage boost can be selected (flux current control, FCC)

![Simplified function diagram of the V/f control](images/112097653259_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| <sup>1)</sup> | In the V/f control variant, "flux current control (FCC)," the Converter controls the motor current (starting current) at low speeds |

Simplified function diagram of the V/f control

One function not shown in the simplified function diagram is the resonance damping for damping mechanical oscillations. You will find the complete function diagrams 6300 et seq. in the List Manual.

For operation of the motor with V/f control, you must set at least the subfunctions shown with a gray background in the figure to adapt them to your application:

- V/f characteristic
- Voltage boost

###### Default setting after selecting the application class Standard Drive Control

Selecting application class Standard Drive Control in the quick commissioning adapts the structure and the setting options of the V/f control as follows:

- Starting current closed-loop control: At low speeds, a controlled motor current reduces the tendency of the motor to oscillate.
- With increasing speed, transition from closed-loop starting current control into V/f control with voltage boost depending on the load.
- The slip compensation is activated.
- Soft starting is not possible.
- Fewer parameters

![Default setting of the V/f control after selecting Standard Drive Control](images/112097997579_DV_resource.Stream@PNG-en-US.png)

Default setting of the V/f control after selecting Standard Drive Control

The complete function diagrams 6850 ff. for application class Standard Drive Control are provided in the List Manual.

###### Characteristics of V/f control

The converter has different V/f characteristics.

![Characteristics of V/f control](images/112486469387_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | The voltage boost of the characteristic optimizes the speed control at low speeds |
| ② | With the flux current control (FCC), the converter compensates for the voltage drop in the stator resistor of the motor |

Characteristics of V/f control

The converter increases its output voltage to the maximum possible output voltage. The maximum possible output voltage of the converter depends on the line voltage.

When the maximum output voltage is reached, the converter only increases the output frequency. At this point, the motor enters the field weakening range: At constant torque, the slip decreases quadratically as the speed increases.

The value of the output voltage at the rated motor frequency also depends on the following variables:

- Ratio between the converter size and the motor size
- Line voltage
- Line impedance
- Actual motor torque

###### Characteristics with Standard drive control

###### Characteristics after selecting the application class Standard Drive Control

Selecting application class Standard Drive Control reduces the number of characteristics and the setting options:

- A linear and a parabolic characteristic are available.
- Selecting a technological application defines the characteristic.
- The following cannot be set - ECO mode, FCC, the programmable characteristic and a specific voltage setpoint.

![Characteristics after selecting Standard Drive Control](images/112491570443_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | The closed-loop starting current control optimizes the speed control at low speeds |
| ② | The converter compensates the voltage drop across the motor stator resistance |

Characteristics after selecting Standard Drive Control

###### Selecting the V/f characteristic

Linear and parabolic characteristics

| Requirement | Application examples | Remark | Characteristic | Parameter |
| --- | --- | --- | --- | --- |
| The required torque is independent of the speed | Conveyor belts, roller conveyors, chain conveyors, eccentric worm pumps, compressors, extruders, centrifuges, agitators, mixers | - | Linear | p0501 = 0 |
| The required torque increases with the speed | Centrifugal pumps, radial fans, axial fans | Lower losses in the motor and converter than for a linear characteristic. | Parabolic | p0501 = 1 |

Additional information on the characteristics can be found in the parameter list and in the function diagrams 6851 ff of the List Manual.

###### Optimising motor starting

After selection of the U/f characteristic, no further settings are required in most applications.

In the following circumstances, the motor cannot accelerate to its speed setpoint after it has been switched on:

- Load moment of inertia too high
- Load torque too large
- Ramp-up time p1120 too short

To improve the starting behavior of the motor, a voltage boost can be set for the U/f characteristic at low speeds.

###### Setting the voltage boost for U/f control

The inverter boosts the voltage corresponding to the starting currents p1310 … p1312.

![The resulting voltage boost using a linear characteristic as example](images/112495221387_DV_resource.Stream@PNG-en-US.png)

The resulting voltage boost using a linear characteristic as example

**Preconditions**

- Set the ramp-up time of the ramp-function generator to a value 1 s (< 1 kW) … 10 s (> 10 kW), depending on the power rating of the motor.
- Increase the starting current in steps of ≤ 5%. Excessively high values in p1310 ... p1312 can cause the motor to overheat and switch off (trip) the inverter due to overcurrent.

  If message A07409 appears, it is not permissible that you further increase the value of any of the parameters.

**Procedure**

1. Switch on the motor with a setpoint of a few revolutions per minute.
2. Check whether the motor rotates smoothly.
3. If the motor does not rotate smoothly, or even remains stationary, increase the voltage boost p1310 until the motor runs smoothly.
4. Accelerate the motor to the maximum speed with maximum load.
5. Check that the motor follows the setpoint.
6. If necessary, increase the voltage boost p1311 until the motor accelerates without problem.

In applications with a high break loose torque, you must also increase parameter p1312 in order to achieve a satisfactory motor response.

You have set the voltage boost.  
❒

| Parameter | Description |
| --- | --- |
| p1310 | **Starting current (voltage boost) permanent** (factory setting 50%)  Compensates for voltage drops caused by long motor cables and the ohmic losses in the motor. |
| p1311 | **Starting current (voltage boost) when accelerating** (factory setting 0%)  Provides additional torque when the motor accelerates. |
| p1312 | **Starting current (voltage boost) when starting** (factory setting 0%)  Provides additional torque, however, only when the motor accelerates for the first time after it has been switched on ("break loose torque"). |

You will find more information on this function in the parameter list and in function diagram 6301 in the List Manual.

###### Optimizing with a high break loose torque and brief overload

After selection of the V/f characteristic, no further settings are required in most applications.

In the following circumstances, the motor cannot accelerate to its speed setpoint after it has been switched on:

- Load moment of inertia too high
- Load torque too large
- Ramp-up time p1120 too short

To improve the starting behavior of the motor, a voltage boost can be set for the V/f characteristic at low speeds.

###### Setting the voltage boost for V/f control

The converter boosts the voltage corresponding to the starting currents p1310 … p1312.

![The resulting voltage boost using a linear characteristic as example](images/103440747531_DV_resource.Stream@PNG-en-US.png)

The resulting voltage boost using a linear characteristic as example

**Preconditions**

- Set the ramp-up time of the ramp-function generator to a value 1 s (< 1 kW) … 10 s (> 10 kW), depending on the power rating of the motor.
- Increase the starting current in steps of ≤ 5%. Excessively high values in p1310 ... p1312 can cause the motor to overheat and switch off (trip) the converter due to overcurrent.

  If message A07409 appears, it is not permissible that you further increase the value of any of the parameters.

**Procedure**

1. Switch on the motor with a setpoint of a few revolutions per minute.
2. Check whether the motor rotates smoothly.
3. If the motor does not rotate smoothly, or even remains stationary, increase the voltage boost p1310 until the motor runs smoothly.
4. Accelerate the motor to the maximum speed with maximum load.
5. Check that the motor follows the setpoint.
6. If necessary, increase the voltage boost p1311 until the motor accelerates without problem.

In applications with a high break loose torque, you must also increase parameter p1312 in order to achieve a satisfactory motor response.

You have set the voltage boost.  
❒

Parameters for the voltage boost

| Parameter | Description |
| --- | --- |
| p1310 | **Permanent voltage boost** (factory setting 50%)  Compensates voltage drops as a result of long motor cables and the ohmic losses in the motor. |
| p1311 | **Voltage boost when accelerating** (factory setting 0%)  Provides additional torque when the motor accelerates. |
| p1312 | **Voltage boost when starting** (factory setting 0%)  Provides additional torque, however, only when the motor accelerates for the first time after it has been switched on ("break loose torque"). |

You will find more information on this function in the parameter list and in function diagram 6301 in the List Manual.

###### Optimizing the motor startup for application class Standar Drive Control

After selecting application class Standard Drive Control, in most applications no additional settings need to be made.

At standstill, the converter ensures that at least the rated motor magnetizing current flows. Magnetizing current p0320 approximately corresponds to the no-load current at 50% … 80% of the rated motor speed.

In the following circumstances, the motor cannot accelerate to its speed setpoint after it has been switched on:

- Load moment of inertia too high
- Load torque too large
- Ramp-up time p1120 too short

The current can be increased at low speeds to improve the starting behavior of the motor.

###### Starting current (boost) after selecting the application class Standard Drive Control

![The resulting voltage boost using a linear characteristic as example](images/126677280395_DV_resource.Stream@PNG-en-US.png)

The resulting voltage boost using a linear characteristic as example

The converter boosts the voltage corresponding to the starting currents p1310 … p1312.

**Preconditions**

- Set the ramp-up time of the ramp-function generator to a value 1 s (< 1 kW) … 10 s (> 10 kW), depending on the power rating of the motor.
- Increase the starting current in steps of ≤ 5%. Excessively high values in p1310 ... p1312 can cause the motor to overheat and switch off (trip) the converter due to overcurrent.

  If message A07409 appears, it is not permissible that you further increase the value of any of the parameters.

**Procedure**

1. Switch on the motor with a setpoint of a few revolutions per minute.
2. Check whether the motor rotates smoothly.
3. If the motor does not rotate smoothly, or even remains stationary, increase the voltage boost p1310 until the motor runs smoothly.
4. Accelerate the motor to the maximum speed with maximum load.
5. Check that the motor follows the setpoint.
6. If necessary, increase the voltage boost p1311 until the motor accelerates without problem.

In applications with a high break loose torque, you must also increase parameter p1312 in order to achieve a satisfactory motor response.

You have set the voltage boost.  
❒

| Parameter | Description |
| --- | --- |
| p1310 | **Starting current (voltage boost) permanent** (factory setting 50%)  Compensates for voltage drops caused by long motor cables and the ohmic losses in the motor.  After commissioning, depending on the motor power rating and the technological application p0501, the converter sets p1310. |
| p1311 | **Starting current (voltage boost) when accelerating** (factory setting 0%)  Provides additional torque when the motor accelerates.  After commissioning, depending on the motor power rating and the technological application p0501, the converter sets p1311. |
| p1312 | **Starting current (voltage boost) when starting** (factory setting 0%)  Provides additional torque, however, only when the motor accelerates for the first time after it has been switched on ("break loose torque"). |

You can find more information about this function in the parameter list and in function diagram 6851 of the List Manual.

#### Protective functions

This section contains information on the following topics:

- [Motor temperature monitoring using a temperature sensor IP20](#motor-temperature-monitoring-using-a-temperature-sensor-ip20)
- [Converter temperature monitoring](#converter-temperature-monitoring)
- [Overcurrent protection](#overcurrent-protection)
- [Limiting the maximum DC-link voltage](#limiting-the-maximum-dc-link-voltage)
- [Load torque monitoring (system protection)](#load-torque-monitoring-system-protection)
- [Shutdown functions OFF1, OFF2 and OFF3](#shutdown-functions-off1-off2-and-off3)

##### Motor temperature monitoring using a temperature sensor IP20

![Figure](images/112854599307_DV_resource.Stream@PNG-en-US.png)

The converter can evaluate one of the following sensors to protect the motor against overtemperature:

| Symbol | Meaning |
| --- | --- |
| ![Figure](images/112847982859_DV_resource.Stream@PNG-en-US.png) | - KTY84 sensor - Temperature switch (e.g. bimetallic switch) - PTC sensor - Pt1000 sensor |

###### KTY84 sensor

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Overheating of the motor due to KTY sensor connected with the incorrect polarity**  If a KTY sensor is connected with incorrect polarity, the motor can become damaged due to overheating, as the inverter cannot detect a motor overtemperature condition.   - Connect the KTY sensor with the correct polarity. |  |

![KTY84 sensor](images/112911870091_DV_resource.Stream@PNG-en-US.png)

Using a KTY sensor, the inverter monitors the motor temperature and the sensor itself for wire-break or short-circuit:

- Temperature monitoring:   
  The converter uses a KTY sensor to evaluate the motor temperature in the range from -48° C ... +248° C.  
  Use the p0604 or p0605 parameter to set the temperature for the alarm and fault threshold.

  - Overtemperature alarm (A07910):  
    - motor temperature > p0604 and p0610 = 0
  - Overtemperature fault (F07011):  
    The converter responds with a fault in the following cases:   
    - motor temperature > p0605  
    - motor temperature > p0604 and p0610 ≠ 0
- Sensor monitoring (A07015 or F07016):

  - Wire-break:   
    The converter interprets a resistance > 2120 Ω as a wire-break and outputs the alarm A07015. After 100 milliseconds, the converter changes to the fault state with F07016.
  - Short-circuit:   
    The converter interprets a resistance < 50 Ω as a short-circuit and outputs the alarm A07015. After 100 milliseconds, the converter changes to the fault state with F07016

###### Temperature switch

![Temperature switch](images/112912330891_DV_resource.Stream@PNG-en-US.png)

The converter interprets a resistance ≥ 100 Ω as being an opened temperature switch and responds according to the setting for p0610.

###### PTC sensor

![PTC sensor](images/103440835723_DV_resource.Stream@PNG-en-US.png)

The converter interprets a resistance > 1650 Ω as being an overtemperature and responds according to the setting for p0610.

The converter interprets a resistance < 20 Ω as being a short-circuit and responds with alarm A07015. If the alarm is present for longer than 100 milliseconds, the converter shuts down with fault F07016.

###### Pt1000 sensor

![Pt1000 sensor](images/103440835723_DV_resource.Stream@PNG-en-US.png)

Using a Pt1000 sensor, the converter monitors the motor temperature and the sensor itself for wire breakage and/or short-circuit:

- Temperature monitoring:  
  Using a Pt1000 sensor, the converter evaluates the motor temperature in the range from -48 °C ... +248 °C.  
  You set the temperature for the alarm and fault thresholds using parameters p0604 and p0605.

  - Overtemperature alarm (A07910):  
    - motor temperature > p0604 and p0610 = 0
  - Overtemperature fault (F07011):  
    The converter responds with a fault in the following cases:   
    - motor temperature > p0605  
    - motor temperature > p0604 and p0610 ≠ 0
- Sensor monitoring (A07015 or F07016):

  - Wire-break:   
    The converter interprets a resistance > 2120 Ω as a wire-break and outputs the alarm A07015. After 100 milliseconds, the converter changes to the fault state with F07016.
  - Short-circuit:   
    The converter interprets a resistance < 603 Ω as a short-circuit and outputs the alarm A07015. After 100 milliseconds, the converter changes to the fault state with F07016.

###### Setting parameters for the temperature monitoring

| Parameter | Description |  |
| --- | --- | --- |
| p0335 | **Motor-cooling method** (factory setting: 0)  0: Natural cooling - with fan on the motor shaft 1: Forced ventilation - with a separately driven fan 2: Liquid cooling  128: No fan |  |
| p0601 | **Motor temperature sensor type**   0: No sensor (factory setting) 1: PTC 2: KTY84 4: Temperature switch 6: Pt1000 |  |
| p0604 | **Mot_temp_mod 2 / sensor alarm threshold** (factory setting 130° C)  For monitoring the motor temperature using KTY84/Pt1000. |  |
| p0605 | **Mot_temp_mod 1/2 / sensor threshold and temperature value** (factory setting: 145° C)  For monitoring the motor temperature using KTY84/Pt1000. |  |
| p0610 | **Motor overtemperature response** (factory setting: 12) Determines the inverter behavior when the motor temperature reaches the alarm threshold p0604. |  |
| 0: | Alarm (A07910), no fault |  |
| 1: | Alarm A07910 and fault F07011  The inverter reduces the current limit. |  |
| 2, 12: | Alarm A07910 and fault F07011  The inverter does not reduce the current limit. |  |
| p0640 | **Current limit** [A] |  |

Additional information on the motor temperature monitoring can be found in function diagram 8016 of the List Manual.

##### Converter temperature monitoring

![Figure](images/112854599307_DV_resource.Stream@PNG-en-US.png)

The converter temperature is essentially defined by the following effects:

- The ambient temperature
- The ohmic losses increasing with the output current
- Switching losses increasing with the pulse frequency

###### Monitoring types

The converter monitors its temperature using the following monitoring types:

- I<sup>2</sup>t monitoring (alarm A07805, fault F30005)
- Measuring the chip temperature of the Power Module (alarm A05006, fault F30024)
- Measuring the heat sink temperature of the Power Module (alarm A05000, fault F30004)

###### Converter response to thermal overload

| Parameter | Description |
| --- | --- |
| r0036 | **Power unit overload I** <sup>2</sup> **t** [%]  The I<sup>2</sup>t monitoring calculates the converter utilization based on a current reference value defined in the factory.  - Actual current > reference value: r0036 becomes higher. - Actual current < reference value: r0036 becomes lower or remains = 0. |
| r0037 | **Power unit temperatures** [°C] |
| p0290 | **Power unit overload response**   Factory setting and the ability to be changed depends on the hardware. The dependency is described in the List Manual.  A thermal overload is present if the converter temperature is greater than that specified in p0292.  You define how the converter responds if there is a risk of thermal overload using this parameter. The details are described below. |
| p0292 | **Power unit temperature warning threshold**  (factory setting: Heat sink [0] 5 °C, power semiconductor [1] 15 °C)  The value is set as a difference to the shutdown temperature. |
| p0294 | **Power unit warning at I2t overload** (factory setting: 95 %) |

###### Overload response for p0290 = 0

The converter responds depending on the control mode that has been set:

- In vector control, the converter reduces the output current.
- In V/f control, the converter reduces the speed.

Once the overload condition has been removed, the converter re-enables the output current or speed.

If the measure cannot prevent an converter thermal overload, then the converter switches off the motor with fault F30024.

###### Overload response for p0290 = 1

The converter immediately switches off the motor with fault F30024.

###### Overload response for p0290 = 2

We recommend this setting for drives with square-law torque characteristic, e.g. fans.

The converter responds in two stages:

1. If you operate the converter with increased pulse frequency setpoint p1800, then the converter reduces its pulse frequency starting at p1800.

   In spite of the temporarily reduced pulse frequency, the base load output current remains unchanged at the value that is assigned to p1800.

   ![Derating characteristic and base load output current for overload](images/112997126283_DV_resource.Stream@PNG-en-US.png)

   ![Derating characteristic and base load output current for overload](images/112997126283_DV_resource.Stream@PNG-en-US.png)

   Derating characteristic and base load output current for overload
2. If it is not possible to temporarily reduce the pulse frequency, or the risk of thermal overload cannot be prevented, then stage 2 follows:

   - In vector control, the converter reduces its output current.
   - In V/f control, the converter reduces the speed.

   Once the overload condition has been removed, the converter re-enables the output current or speed.

If both measures cannot prevent a power unit thermal overload, then the converter switches off the motor with fault F30024.

###### Overload response for p0290 = 3

If you operate the converter with increased pulse frequency, then the converter reduces its pulse frequency starting at the pulse frequency setpoint p1800.

In spite of the temporarily reduced pulse frequency, the maximum output current remains unchanged at the value that is assigned to the pulse frequency setpoint. Also see p0290 = 2.

Once the overload condition has been removed, the converter increases the pulse frequency back to the pulse frequency setpoint p1800.

If it is not possible to temporarily reduce the pulse frequency, or the measure cannot prevent a power unit thermal overload, then the converter switches off the motor with fault F30024.

###### Overload response for p0290 = 12

The converter responds in two stages:

1. If you operate the converter with increased pulse frequency setpoint p1800, then the converter reduces its pulse frequency starting at p1800.

   There is no current derating as a result of the higher pulse frequency setpoint.

   Once the overload condition has been removed, the converter increases the pulse frequency back to the pulse frequency setpoint p1800.
2. If it is not possible to temporarily reduce the pulse frequency, or the risk of converter thermal overload cannot be prevented, then stage 2 follows:

   - In vector control, the converter reduces the output current.
   - In V/f control, the converter reduces the speed.

   Once the overload condition has been removed, the converter re-enables the output current or speed.

If both measures cannot prevent a power unit thermal overload, then the converter switches off the motor with fault F30024.

###### Overload response for p0290 = 13

We recommend this setting for drives with high starting torque, e.g. horizontal conveyors or extruders.

If you operate the converter with increased pulse frequency, then the converter reduces its pulse frequency starting at the pulse frequency setpoint p1800.

There is no current derating as a result of the higher pulse frequency setpoint.

Once the overload condition has been removed, the converter increases the pulse frequency back to the pulse frequency setpoint p1800.

If it is not possible to temporarily reduce the pulse frequency, or the measure cannot prevent a power unit thermal overload, then the converter switches off the motor with fault F30024.

##### Overcurrent protection

![Figure](images/112854599307_DV_resource.Stream@PNG-en-US.png)

The vector control ensures that the motor current remains within the set torque limits.

If you use V/f control, you cannot set any torque limits. The V/f control prevents too high a motor current by influencing the output frequency and the motor voltage (I-max controller).

###### I_max controller

**Requirements**

The torque of the motor must decrease at lower speeds, which is the case, for example, with fans.

The load must not drive the motor continuously, e.g. when lowering hoisting gear.

**Function**

The I-max controller influences the output frequency and the motor voltage.

If the motor current reaches the current limit during acceleration, the I-max controller extends the acceleration operation.

If the load of the motor is so large during stationary operation that the motor current reaches the current limit, the I-max controller reduces the speed and the motor voltage until the motor current is in the permissible range again.

If the motor current reaches the current limit during deceleration, the I-max controller extends the deceleration operation.

###### Settings

You only have to change the factory settings of the I-max controller if the drive tends to oscillate when it reaches the current limit or if it is shut down due to overcurrent.

I-max controller parameters

| Parameter | Description |
| --- | --- |
| p0305 | **Rated motor current** |
| p0640 | **Motor current limit** |
| p1340 | **Proportional gain of the I-max controller for speed reduction** |
| p1341 | **Integral time of the I-max controller for speed reduction** |
| r0056.13 | **Status: I-max controller active** |
| r1343 | **Speed output of the I-max controller** Shows the amount to which the I-max controller reduces the speed. |

For more information about this function, see function diagram 6300 in the List Manual.

##### Limiting the maximum DC-link voltage

![Figure](images/112854599307_DV_resource.Stream@PNG-en-US.png)

To drive the load, an electric motor converts electrical energy into mechanical energy. If the motor is driven by its load, e.g. due to the load moment of inertia when braking, then the energy flow reverses: The motor temporarily operates as generator, and converts mechanical energy into electrical energy. The electrical energy flows from the motor to the converter. If the converter cannot output the electrical energy supplied by the motor, e.g. to a braking resistor, then the converter stores the energy in its DC link capacitance. As a consequence, the DC link voltage Vdc in the converter is higher.

An excessively high DC link voltage damages the converter and also the motor. As a consequence, the converter monitors its DC link voltage - and when necessary switches off the motor and outputs fault "DC link overvoltage".

###### Protecting the motor and converter against overvoltage

![Simplified representation of the Vdc_max control](images/127062877963_DV_resource.Stream@PNG-en-US.png)

Simplified representation of the Vdc_max control

The Vdc_max control extends the motor ramp-down time when braking. The motor then only feeds so much energy into the converter to cover the losses in the converter. The DC link voltage remains in the permissible range.

The Vdc_max control is not suitable for applications where the motor is in continuous regenerative operation, e.g. as is the case for cranes and centrifuges.

![Protecting the motor and converter against overvoltage](images/112999445259_DV_resource.Stream@PNG-en-US.png)
[Braking functions of the converter](#braking-functions-of-the-converter).

The Vdc_max control can only be used with PM240-2 Power Modules. The Vdc_max control is not required if you use a braking resistor.

PM250 Power Modules feed back regenerative energy into the line supply. Therefore, the Vdc_max control is not required for a PM250 Power Module.

###### Parameters of the Vdc_max control

The parameters differ depending on the motor control mode.

| Parameter for V/f control | Parameter for vector control | Description |
| --- | --- | --- |
| p1280 = 1 | p1240 = 1 | **Vdc controller configuration**(Factory setting: 1)  1: VDC controller is enabled |
| r1282 | r1242 | **Vdc_max control activation level** DC link voltage value above which the Vdc_max control is activated |
| p1283 | p1243 | **Vdc_max control dynamic factor** (factory setting: 100 %)  Scaling control parameters p1290, p1291 and p1292 |
| p1284 | --- | **Vdc_max controller time threshold**  Setting the monitoring time of the Vdc_max controller. |
| p1290 | p1250 | **Vdc_max control proportional gain** (factory setting: 1) |
| p1291 | p1251 | **Vdc_max control integral time** (factory setting p1291: 40 ms, p1251: 0 ms) |
| p1292 | p1252 | **Vdc_max control rate time** (factory setting p1292: 10 ms, p1252: 0 ms) |
| p1294 | p1254 | **Vdc_max control automatic ON level sensing**(factory setting, dependent on the Power Module)  Automatically sense switch-on levels of the Vdc_max control. 0: Automatic detection disabled 1: Automatic detection enabled |
| p0210 | p0210 | **Unit supply voltage**  If p1254 or p1294 = 0, the converter uses this parameter to calculate the switch-in thresholds of the Vdc_max control.  Set this parameter to the actual value of the input voltage. |

For more information about this function, see the List Manual (function diagrams 6320 and 6220).

##### Load torque monitoring (system protection)

![Figure](images/112854599307_DV_resource.Stream@PNG-en-US.png)

In many applications, the speed and the torque of the motor can be used to determine whether the driven load is in an impermissible operating state. The use of an appropriate monitoring function in the converter prevents failures and damage to the machine or plant.

Examples:

- For fans or conveyor belts, an excessively low torque can mean a broken drive belt.
- For pumps, insufficient torque can indicate a leakage or dry-running.
- For extruders and mixers, an excessive torque together with low speed can indicate machine blockage.

##### Shutdown functions OFF1, OFF2 and OFF3

###### Shutdown function OFF1

The shutdown function OFF1 is linked to a large extent to the ON command. The drive is braked by OFF1 with the ramp down time P1121. If the output frequency falls below the P2167 parameter value and the P2168 time has elapsed, the inverter pulses are suppressed.

###### Shutdown function OFF2

The inverter pulses are suppressed immediately with the OFF2 command. The motor then coasts to a standstill; controlled braking is not possible.

###### Shutdown function OFF3

The braking response of OFF3 is identical to that of OFF1 apart from the different OFF3 ramp-down time P1135. If the output frequency falls below the P2167 parameter value and the P2168 time has elapsed, the inverter pulses are suppressed as with the OFF1 command. The drive then coasts to a standstill.

#### Application-specific functions

This section contains information on the following topics:

- [Braking functions](#braking-functions)
- [Flying restart – switching on while the motor is running](#flying-restart-switching-on-while-the-motor-is-running)
- [Automatic switch-on](#automatic-switch-on)
- [Monitoring the speed via digital input](#monitoring-the-speed-via-digital-input)
- [Free function blocks](#free-function-blocks)
- [PID Technology controller](#pid-technology-controller)

##### Braking functions

This section contains information on the following topics:

- [Braking functions of the converter](#braking-functions-of-the-converter)
- [Comparison of the electrical braking methods](#comparison-of-the-electrical-braking-methods)
- [DC braking and dynamic braking](#dc-braking-and-dynamic-braking)
- [Braking methods with regenerative feedback](#braking-methods-with-regenerative-feedback)
- [Dynamic braking](#dynamic-braking)
- [Motor holding brake](#motor-holding-brake)
- [DC braking](#dc-braking)
- [Compound braking](#compound-braking)

###### Braking functions of the converter

###### Braking with the motor in generating mode

![Braking with the motor in generating mode](images/90967178635_DV_resource.Stream@PNG-de-DE.png)

If the motor brakes the connected load electrically, it will convert the kinetic energy of the motor to electrical energy. The electrical energy E released on braking the load is proportional to the moment of inertia J of the motor and load and to the square of the speed n. The motor attempts to pass the energy on to the inverter.

---

**See also**

[Motor holding brake](#motor-holding-brake)

###### Comparison of the electrical braking methods

###### Which Power Module permits which braking method?

| Electrical braking methods | Power Modules that can be used |
| --- | --- |
| DC braking, compound braking | PM240-2, PM240P-2 |
| Dynamic braking | PM240-2 |
| Braking with energy recovery into the line supply | PM250 |

###### Main features of the braking functions

| Symbol | Meaning |
| --- | --- |
| **DC braking**   DC braking prevents the motor from transferring braking energy to the converter. The converter impresses a DC current into the motor, therefore braking the motor. The motor converts braking energy E of the load into heat.  - Advantage:The motor brakes the load without the converter having to process regenerative power. - Disadvantages:significant increase in the motor temperature; no defined braking characteristics; no constant braking torque; no braking torque at standstill; braking energy is lost as heat; does not function when the power fails    **Compound braking**   One version of DC braking. The converter brakes the motor with a defined ramp-down time and superimposes a DC current on the output current. | ![Main features of the braking functions](images/93563612811_DV_resource.Stream@PNG-de-DE.png) |

| Symbol | Meaning |
| --- | --- |
| **Dynamic braking**   Using a braking resistor, the converter converts the electrical energy into heat.  - Advantages:defined braking response; motor temperature does not increase any further; constant braking torque - Disadvantages:Braking resistor required; braking energy E is lost in the form of heat | ![Main features of the braking functions](images/93565256971_DV_resource.Stream@PNG-de-DE.png) |

| Symbol | Meaning |
| --- | --- |
| **Braking with energy recovery into the line supply**   The converter feeds electrical energy back into the line supply (energy recovery).  - Advantages: Constant braking torque; the braking energy is not completely converted into heat, but regenerated into the line supply; is suitable for all applications; continuous regenerative operation is possible - e.g. when lowering a suspended load - Disadvantage: Does not function for a power failure | ![Main features of the braking functions](images/93565262731_DV_resource.Stream@PNG-de-DE.png) |

###### DC braking and dynamic braking

###### Main features of the braking functions

|  |  |  |
| --- | --- | --- |
| **DC braking**    The motor converts the regenerative power into heat.  - Advantage: The motor brakes without the converter having to process the regenerative energy - Disadvantages: Significant increase in the motor temperature; no defined braking characteristics; no constant braking torque; no braking torque at standstill; regenerative power is lost as heat; does not function when the line supply fails    **Compound braking**   The motor converts the regenerative power into heat.  - Advantage: Defined braking characteristics, the motor brakes without the converter having to convert any regenerative energy - Disadvantages: Significant motor temperature rise; no constant braking torque; regenerative power is dissipated as heat; does not function when the line supply fails |  | ![Main features of the braking functions](images/103441245323_DV_resource.Stream@PNG-en-US.png) |
|  |  |  |
| **Dynamic braking**   The converter converts the regenerative power into heat using a braking resistor.  - Advantages: Defined braking characteristics; no additional motor temperature increase; constant braking torque; in principle, also functions when the power fails - Disadvantages: Braking resistor required; regenerative power is dissipated as heat | ![Main features of the braking functions](images/103441249931_DV_resource.Stream@PNG-en-US.png) |  |

###### Braking methods with regenerative feedback

The typical applications for braking with energy recovery (regenerative feedback into the line supply) are as follows:

- Hoist drives
- Centrifuges
- Unwinders

For these applications, the motor must brake for longer periods of time.

The converter can feed back up to 100% of its rated power into the line supply (referred to "High Overload" base load).

###### Setting the braking with regenerative feedback to the line

| Parameter | Description |
| --- | --- |
| **Limiting the regenerative feedback for V/f control (p1300 < 20)** |  |
| p0640 | **Current limit** (factory setting: 0.00 A, default for quick commissioning)  Sets the current limit |
| **Limiting feedback with vector control (p1300 ≥ 20)** |  |
| p1531 | **Power limit generative** (factory setting: -0.01 kW)  The converter calculates the parameter based on the quick commissioning or with p0340 = 5. |

###### Dynamic braking

Typical applications for dynamic braking require continuous braking and acceleration operations or frequent changes of the motor direction of rotation:

- Horizontal conveyors
- Vertical and inclined conveyors
- Hoisting gear

###### Principle of operation

The DC link voltage increases as soon as the motor supplies regenerative power to the converter when braking. The regenerative power means that the DC link voltage in the converter increases. Depending on the DC link voltage, the converter outputs the regenerative power to the braking resistor through the braking chopper. The braking resistor converts the regenerative power into heat, therefore preventing DC link voltages > Vdc_max.

![Simplified representation of dynamic braking with respect to time](images/150647428491_DV_resource.Stream@PNG-en-US.png)

Simplified representation of dynamic braking with respect to time

###### Set dynamic braking

| Parameter | Description |  |
| --- | --- | --- |
| p0219 | **Braking power of the braking resistor** (factory setting: 0 kW)  For p0219 > 0, the converter deactivates the VDC_max controller.  For vector control, p0219 specifies the regenerative power limit p1531.    ![Set dynamic braking](images/94660379915_DV_resource.Stream@PNG-de-DE.png)   Set with p0219 the maximum braking power that the braking resistor must handle.  The converter extends the ramp-down time of the motor when the braking power is too low.  You can find the technical data of the braking resistor in the Power Module hardware installation manual.  The SIZER PC tool provides support for calculating the braking power. |  |
| p2106 | **BI: External fault 1** |  |
| p2106 = 722.x | Monitor the signal for overtemperature of the braking resistor with digital input x of the converter. |  |

An example for configuring a drive with braking resistor is provided in the Internet:

![Set dynamic braking](images/109219489803_DV_resource.Stream@PNG-de-DE.png)
[Engineering and commissioning series lifting equipment/cranes](https://support.industry.siemens.com/cs/de/en/view/103156155).

###### Motor holding brake

The motor holding brake prevents the motor turning when it is switched off. The converter has internal logic to optimally control a motor holding brake.

The converter-internal control of the motor holding brake is suitable typically for horizontal, inclined and vertical conveyors.

A motor holding brake can also be useful in several applications for pumps or fans to ensure that the powered-down motor does not rotate in the wrong direction through a liquid or air flow.

###### Commissioning

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Special settings of the motor holding brake**  The following applications require special settings of the motor holding brake. In these cases, the motor holding brake control may only be commissioned by experienced personnel:  - All applications that involve transporting people - Hoisting gear - Elevators - Cranes |  |

- Before commissioning, secure any dangerous loads (e.g. loads on inclined conveyors)
- Suppress the motor holding brake control, e.g. by disconnecting the control cables
- When opening the motor holding brake, ensure that a torque is established that prevents the load from briefly dropping.

  - Check the magnetizing time p0346; the magnetizing time is pre-assigned during commissioning and must be greater than zero
  - V/f control (p1300 = 0 to 3):  
    Set the boost parameters p1310 and p1311.  
    Define the motor torque when switching on using p1351 and p1352.
  - Vector control (p1300 ≥ 20):  
    Define the motor torque when switching on using p1475.
- Assigning parameters for the opening and closing times of the motor holding brake.   
  It is extremely important that electromechanical brakes are controlled with the correct timing in order to protect the brakes against long-term damage. The exact values can be found in the technical data of the connected brake. Typical values:

  - Depending on the brake size, brake opening times lie between 25 ms and 500 ms.
  - Depending on the brake size, brake closing times lie between 15 ms and 300 ms.
- Reestablish the control of the motor holding brake.  
  r0052.12 ("Motor holding brake open") controls the brake.

###### Method of operation after OFF2 or STO command

For the following signals, the brake closing time is not taken into account:

- OFF2 command
- For fail-safe applications, in addition, after "Safe Torque Off" (STO)

After these control commands, the signal to close the motor holding brake is immediately output independent of the motor speed. The converter does not monitor the motor speed until the brake closes.

![Controlling the motor holding brake after an OFF2 command or STO](images/103441540875_DV_resource.Stream@PNG-en-US.png)

Controlling the motor holding brake after an OFF2 command or STO

###### Method of operation after OFF1 and OFF3 command

![Controlling the motor holding brake when the motor is switched on and off](images/103441556235_DV_resource.Stream@PNG-en-US.png)

Controlling the motor holding brake when the motor is switched on and off

The motor brake is controlled as shown in the following diagram:

1. After the ON command (switch on motor), the converter magnetizes the motor. At the end of the magnetizing time (p0346), the converter issues the command to open the brake.
2. The motor remains at a standstill until the end of the brake opening time p1216. The motor holding brake must open within this time.
3. At the end of the brake opening time the motor accelerates to its speed setpoint.
4. After the OFF command (OFF1 or OFF3) the motor brakes to a standstill.
5. If the speed setpoint and the current speed fall below threshold p1226, the monitoring time p1227 or p1228 is started.
6. As soon as the first of the two monitoring times (p1227 or p1228) has elapsed, the converter issues the command to close the brake. The motor comes to a standstill but remains switched on.
7. At the end of the brake closing time p1217, the motor is switched off.   
   The motor holding brake must close within this time.

###### DC braking

DC braking is used for applications where the motor must be actively stopped; however, neither an inverter capable of energy recovery nor a braking resistor is available.

Typical applications for DC braking include:

- Centrifuges
- Saws
- Grinding machines
- Conveyor belts

DC braking is not permissible in applications involving suspended loads, e.g. lifting equipment/cranes and vertical conveyors.

###### Function

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Motor overheating as a result of DC braking**  The motor will overheat if you use DC braking too frequently or use it for too long. This may damage the motor.  - Monitor the motor temperature. - Allow the motor to adequately cool down between braking operations. - If necessary, select another motor braking method. |  |

With DC braking, the converter outputs an internal OFF2 command for the time that it takes to de-energize the motor p0347 - and then impresses the braking current for the duration of the DC braking.

The DC-braking function is possible only for induction motors.

4 different events initiate DC braking

**DC braking when falling below a starting speed**

| Symbol | Meaning |
| --- | --- |
| ![Function](images/93565798283_DV_resource.Stream@PNG-en-US.png) | Requirement:  p1230 = 1 and p1231 = 14  Function:  | Symbol | Meaning | | --- | --- | | 1. The motor speed has exceeded the starting speed. 2. The converter activates the DC braking as soon as the motor speed falls below the starting speed. |  | |

**DC braking when a fault occurs**

| Symbol | Meaning |
| --- | --- |
| ![Function](images/93566449547_DV_resource.Stream@PNG-en-US.png) | Requirement:  Fault number and fault response are assigned via p2100 and p2101.  Function:  | Symbol | Meaning | | --- | --- | | 1. A fault occurs, which initiates DC braking as response. 2. The motor brakes along the down ramp to the speed for the start of DC braking. 3. DC braking starts. |  | |

**DC braking initiated by a control command**

| Symbol | Meaning |
| --- | --- |
| ![Function](images/93566755211_DV_resource.Stream@PNG-en-US.png) | Requirement:  p1231 = 4 and p1230 = control command, e.g. p1230 = 722.3 (control command via DI 3)  Function:  | Symbol | Meaning | | --- | --- | | 1. The higher-level control issues the command for DC braking, e.g. using DI3: p1230 = 722.3. 2. DC braking starts. |  |   If the higher-level control withdraws the command during DC braking, the converter interrupts DC braking and the motor accelerates to its setpoint. |

**DC braking when the motor is switched off**

| Symbol | Meaning |
| --- | --- |
| ![Function](images/93566779275_DV_resource.Stream@PNG-en-US.png) | Requirement:  p1231 = 5 or p1230 = 1 and p1231 = 14  Function:  | Symbol | Meaning | | --- | --- | | 1. The higher-level control switches off the motor (OFF1 or OFF3). 2. The motor brakes along the down ramp to the speed for the start of DC braking. 3. DC braking starts. |  | |

###### Settings for DC braking

| Parameter | Description |  |
| --- | --- | --- |
| p0347 | **Motor de-excitation time** (calculated after quick commissioning)  The converter can trip due to an overcurrent during DC braking if the de-excitation time is too short. |  |
| p1230 | **DC braking activation** (factory setting: 0)  Signal source to activate DC braking  - 0 signal: Deactivated - 1 signal: Active |  |
| p1231 | **Configuring DC braking** (factory setting: 0) |  |
| 0 4 5 14 | No DC braking General release for DC braking DC braking for OFF1/OFF3 DC braking below the starting speed |  |
| p1232 | **DC braking braking current** (factory setting 0 A) |  |
| p1233 | **DC braking duration** (factory setting 1 s) |  |
| p1234 | **DC braking start speed**  (factory setting 210000 rpm) |  |
| r1239 | **DC braking status word** |  |
| .08 .10 .11 .12 .13 | DC braking active DC braking ready DC braking selected DC braking selection internally locked DC braking for OFF1/OFF3 |  |

Configuring DC braking as a response to faults

| Parameter | Description |
| --- | --- |
| p2100 | **Set fault number for fault response** (factory setting 0)   Enter the fault number for which DC braking should be activated, e.g. p2100[3] = 7860 (external fault 1). |
| p2101 = 6 | **Fault response setting** (factory setting 0)  Assigning the fault response: p2101[3] = 6. |
| The fault is assigned an index of p2100. Assign the same index of p2100 or p2101 to the fault and fault response.  The converter's List Manual lists in the "Faults and alarms" list the possible fault responses for every fault. Entry "DCBRK" means that you may set DC braking as response for this fault. |  |

---

**See also**

[Flying restart – switching on while the motor is running](#flying-restart-switching-on-while-the-motor-is-running)

###### Compound braking

Compound braking is suitable for applications in which the motor is normally operated at a constant speed and is only braked down to standstill in longer time intervals.

Typically, the following applications are suitable for compound braking:

- Centrifuges
- Saws
- Grinding machines
- Horizontal conveyors

Compound braking is not permissible for applications with suspended loads, e.g. lifting equipment/cranes all vertical conveyors.

###### Principle of operation

![Motor brakes with and without active compound braking](images/103441725067_DV_resource.Stream@PNG-en-US.png)

Motor brakes with and without active compound braking

Compound braking prevents the DC-link voltage increasing above a critical value. The converter activates compound braking depending on the DC-link voltage. Above a DC-link voltage threshold (r1282), the converters adds a DC current to the motor current. The DC current brakes the motor and prevents an excessive increase in the DC-link voltage.

> **Note**
>
> Compound braking is only active in conjunction with the V/f control.
>
> Compound braking does not operate in the following cases:
>
> - The "flying restart" function is active
> - DC braking is active
> - Vector control is selected

###### Setting and enabling compound braking

Parameters to enable and set compound braking

| Parameter | Description |
| --- | --- |
| P3856 | **Compound braking current (%)**   With the compound braking current, the magnitude of the DC current is defined, which is additionally generated when stopping the motor for operation with V/f control to increase the braking effect.  p3856 = 0 Compound braking locked  p3856 = 1 … 250 Current level of the DC braking current as a % of the rated motor current (p0305)  Recommendation: p3856 < 100% × (r0209 - r0331) / p0305 / 2 |
| r3859.0 | **Status word, compound braking**   r3859.0 = 1: Compound braking is active |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Overheating of the motor due to compound braking**   The motor will overheat if you use compound braking too frequently or for too long. This may damage the motor.  - Monitor the motor temperature. - Allow the motor to adequately cool down between braking operations. - If necessary, select another motor braking method. |  |

##### Flying restart – switching on while the motor is running

![Figure](images/91700305931_DV_resource.Stream@PNG-de-DE.png)

If you switch on the motor while it is still rotating, without the "Flying restart" function, there is a high probability that a fault will occur as a result of overcurrent (F30001 or F07801). Examples of applications involving an unintentionally rotating motor directly before switching on:

- The motor rotates after a brief line interruption.
- A flow of air turns the fan impeller.
- A load with a high moment of inertia drives the motor.

###### Principle of operation

The "Flying restart" function comprises the following steps:

1. After the on command, the converter impresses the search current in the motor and increases the output frequency.
2. When the output frequency reaches the actual motor speed, the converter waits for the motor excitation build up time.
3. The converter accelerates the motor to the actual speed setpoint.

![Principle of operation of the "flying restart" function](images/156531942795_DV_resource.Stream@PNG-en-US.png)

Principle of operation of the "flying restart" function

###### Setting "flying restart" function

| Parameter | Description |  |
| --- | --- | --- |
| p1200 | **Flying restart operating mode** (factory setting: 0) |  |
| 0 | Flying restart is disabled |  |
| 1 | Flying restart is enabled, search for the motor in both directions, start in the direction of the setpoint |  |
| 4 | Flying restart is enabled, search for the motor only in the direction of the setpoint |  |

**No "Flying restart" function for group drives**

It is not permissible that you enable the "Flying restart" function if the converter is simultaneously driving several motors.

Exception: a mechanical coupling ensures that all of the motors always operate with the same speed.

Advanced settings

| Parameter | Description |
| --- | --- |
| p0346 | **Motor excitation build up time**   Wait time between switching on the motor and enabling the ramp-function generator. |
| p0347 | **Motor de-excitation time**   Within the motor de-excitation time, after an OFF command, the inverter prevents the induction motor from being switched on again. |
| p1201 | **Flying restart enable signal source**  (factory setting: 1)  Defines a control command, e.g. a digital input, which enables the flying restart function. |
| p1202 | **Flying restart search current** (Factory setting depends on the Power Module)  Defines the search current with respect to the magnetizing current (r0331), which flows in the motor during the flying restart. |
| p1203 | **Flying restart search current factor** (Factory setting depends on the Power Module)  The value influences the speed with which the output frequency is changed during the flying restart. A higher value results in a longer search time.  If the converter does not find the motor, reduce the search speed (increase p1203). |

##### Automatic switch-on

![Figure](images/91700305931_DV_resource.Stream@PNG-de-DE.png)

The automatic restart includes two different functions:

- The converter automatically acknowledges faults.
- After a fault occurs or after a power failure, the converter automatically switches-on the motor again.

The converter interprets the following events as power failure:

- The converter signals fault F30003 (undervoltage in the DC link), after the converter line voltage has been briefly interrupted.
- All of the converter power supplies have been interrupted - and all of the energy storage devices in the inverter have discharged to such a level that the converter electronics fail.

###### Setting the automatic restart function

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected machine motion caused by the active automatic restart function**  When the "automatic restart" function is active (p1210 > 1), the motor automatically starts after a power failure. Unexpected movement of machine parts can result in serious injury and material damage.  - Block off hazardous areas within the machine to prevent inadvertent access. |  |

If it is possible that the motor is still rotating for a longer period of time after a power failure or after a fault, then you must also activate the "flying restart" function.

![Setting the automatic restart function](images/109220677643_DV_resource.Stream@PNG-de-DE.png)
[Flying restart – switching on while the motor is running](#flying-restart-switching-on-while-the-motor-is-running).

Using p1210, select the automatic restart mode that best suits your application.

![Automatic restart mode](images/113605068299_DV_resource.Stream@PNG-en-US.png)

Automatic restart mode

The principle of operation of the other parameters is explained in the following diagram and in the table below.

![Time response of the automatic restart](images/103441873419_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| <sup>1</sup> | The converter automatically acknowledges faults under the following conditions:  - p1210 = 1 or 26: Always. - p1210 = 4 or 6: If the command to switch-on the motor is available at a digital input or via the fieldbus (ON/OFF1 = 1). - p1210 = 14 or 16: Never. |
| <sup>2</sup> | The converter attempts to automatically switch on the motor under the following conditions:  - p1210 = 1: Never. - p1210 = 4, 6, 14, 16, or 26: If the command to switch-on the motor is available at a digital input or via the fieldbus (ON/OFF1 = 1). |
| <sup>3</sup> | If, after a flying restart and magnetization (r0056.4 = 1) no fault occurs within one second, then the start attempt was successful. |

Time response of the automatic restart

Setting the automatic restart

| Parameter | Explanation |  |
| --- | --- | --- |
| p1210 | **Automatic restart mode** (factory setting: 0) |  |
| 0: 1: 4: 6: 14: 16: 26: | Disable automatic restart. Acknowledge all faults without restarting. Restart after power failure without further restart attempts. Restart after fault with further restart attempts. Restart after power failure after manual acknowledgement. Restart after fault after manual acknowledgement. Acknowledgement of all faults and restart with ON/OFF1 = 1 command. |  |
| p1211 | **Automatic restart start attempts** (factory setting: 3)  This parameter is only effective for the settings p1210 = 4, 6, 14, 16, 26.  You define the maximum number of start attempts using p1211. After each successful acknowledgement, the converter decrements its internal counter of start attempts by 1.  p1211 = 0 or 1: The converter only tries to start once. After an unsuccessful start attempt, the converter issues fault F07320.  p1211 = n, n > 1: The converter tries to start n-times The converter outputs fault F07320 if the nth starting attempt was unsuccessful.  The converter sets the start attempt counter back again to the value of p1211, if one of the following conditions is fulfilled:  - After a successful start attempt, the time in p1213[1] has expired. - After fault F07320, switch off the motor (OFF1) and acknowledge the fault. - You change the start value p1211 or the mode p1210. |  |
| p1212 | **Automatic restart wait time start attempt** (factory setting: 1.0 s)  This parameter is only effective for the settings p1210 = 4, 6, 26.  Examples for setting this parameter:  |  |  |  | | --- | --- | --- | | 1. After a power failure, a certain time must elapse before the motor can be switched-on, e.g. because other machine components are not immediately ready. In this case, set p1212 longer than the time, after which all of the fault causes have been removed. 2. In operation, the converter develops a fault condition. The lower you select p1212, then the sooner the converter attempts to switch-on the motor again. |  |  | |  |
| p1213[0] | **Automatic restart monitoring time  for restart** (factory setting: 60 s)  This parameter is only effective for the settings p1210 = 4, 6, 14, 16, 26.  With this monitoring function, you limit the time in which the converter may attempt to automatically switch-on the motor again.  The monitoring function starts when a fault is identified and ends with a successful start attempt. If the motor has not successfully started after the monitoring time has expired, fault F07320 is signaled.  Set the monitoring time longer than the sum of the following times:  + p1212 + Time that the converter requires to start the motor on the fly. + Motor magnetizing time (p0346) + 1 second  You deactivate the monitoring function with p1213 = 0. |  |
| p1213[1] | **Automatic restart monitoring time  to reset the fault counter** (factory setting: 0 s)  This parameter is only effective for the settings p1210 = 4, 6, 14, 16, 26.  Using this monitoring time, you prevent that faults, which continually occur within a certain time period, are automatically acknowledged each time.  The monitoring function starts with a successful start attempt and ends after the monitoring time has expired.  If, during the monitoring time p1213[1], the converter made more successful starting attempts than defined in p1211, the converter interrupts the automatic restart function and signals fault F07320. To switch on the motor again you must acknowledge the fault and switch on the converter (ON/OFFS1 = 1). |  |

Additional information is provided in the parameter list of the List Manual.

###### Advanced settings

If you with to suppress the automatic restart function for certain faults, then you must enter the appropriate fault numbers in p1206[0 … 9].

Example: p1206[0] = 07331 ⇒ No restart for fault F07331.

Suppressing the automatic restart only functions for the setting p1210 = 6, 16 or 26.

> **Note**
>
> **Motor starts in spite of an OFF command via the fieldbus**
>
> The converter responds with a fault if fieldbus communication is interrupted. For one of the settings p1210 = 6, 16 or 26, the converter automatically acknowledges the fault and the motor restarts, even if the higher-level control attempts to send an OFF command to the converter.
>
> - In order to prevent the motor automatically starting when the fieldbus communication fails, you must enter the fault number of the communication error in parameter p1206.
>
>   Example for PROFINET:
>
>   Fault number F08501 means: Communication failure.
>
>   Set p1206[n] = 8501 (n = 0 … 9).

##### Monitoring the speed via digital input

With this function you can directly monitor not only the motor speed but also the speed of the driven load. Examples include:

- Gearbox monitoring, e.g. in traction drives or hoisting gear
- Drive belt monitoring, e.g. in fans or conveyor belts
- Monitoring for blocked driven load

###### Speed or velocity monitoring functions

There are two ways of directly monitoring speed in your application:

1. Load failure monitoring: The converter evaluates whether the sensor signal is present.
2. Speed deviation monitoring: The converter calculates a speed from the signal of the connected sensor and compares it with the internal motor control signal.

A sensor (e.g. a proximity switch) is required for speed monitoring. The converter evaluates the sensor signal via a digital input.

###### Load failure monitoring

![Load failure monitoring by means of a digital input](images/103442040971_DV_resource.Stream@PNG-en-US.png)

Load failure monitoring by means of a digital input

Setting load failure monitoring

| Parameter | Description |
| --- | --- |
| p2193 = 1 to 3 | **Load monitoring configuration** (factory setting: 1) 0: Monitoring is disabled 1: Torque and load failure monitoring  2: Speed and load failure monitoring  3: Load failure monitoring |
| p2192 | **Load monitoring delay time** (factory setting 10 s) If, after the motor is switched on, the "LOW" signal is present on the associated digital input for longer than this time, a load failure is assumed (F07936) |
| p3232 = 722.x | **Load monitoring failure detection** (factory setting: 1) Interconnect the load monitoring with a digital input of your choice. |

For more information, see the List Manual (the parameter list and function diagram 8013).

###### Speed deviation monitoring

This function is only available for Control Units CU240E-2, CU240E-2 DP, CU240E-2 F and CU240E-2 DP-F. The monitoring sensor is connected to digital input 3.

The converter can process a pulse sequence of up to 32 kHz.

![Speed deviation monitoring by means of digital input DI3](images/103442036363_DV_resource.Stream@PNG-en-US.png)

Speed deviation monitoring by means of digital input DI3

The speed is calculated from the pulse signal of the digital input in the "measuring input".

The calculated speed is compared with the actual speed value from the motor control and, if an (adjustable) deviation is detected, a response (also adjustable) is triggered.

Setting speed deviation monitoring

| Parameter | Description |
| --- | --- |
| P2193 = 2 | **Load monitoring configuration** (factory setting: 1) 2: Speed and load failure monitoring. |
| P2192 | **Load monitoring delay time** (factory setting 10 s) Setting of the delay time for evaluating load monitoring. |
| P2181 | **Load monitoring response** (factory setting 0) Setting of the response for evaluating load monitoring. |
| P3231 | **Load monitoring speed deviation** (factory setting 150 rpm) Permissible speed deviation of load monitoring. |
| P0580 = 23 | **Measuring input input terminal** (factory setting 0) Interconnection of speed calculation with DI 3. |
| P0581 | **Measuring input edge** (factory setting 0) Setting the edge for evaluation of the measuring input signal to measure actual speed value 0: 0/1 edge 1: 1/0 edge |
| P0582 | **Measuring input pulses per revolution** (factory setting 1) Setting of the number of pulses per revolution. |
| P0583 | **Measuring input maximum measuring time** (factory setting 10 s) Setting the maximum measuring time for the measuring input. If there is no new pulse before the maximum measuring time elapses, the actual speed value in r0586 is set to zero. With the next pulse, the time is restarted. |
| P0585 | **Measuring input gear ratio** (factory setting 1) The converter multiplies the measured speed by the gear ratio and then displays it in r0586. |
| P0490 | **Invert measuring input** (factory setting 0000bin) The 3rd bit of the parameter value inverts the input signals of digital input 3 for the measuring input. |
| p3230 = 586 | **Load monitoring actual speed value** (factory setting 0) Interconnection of the speed calculation result with speed monitoring evaluation. |

For more information, see the List Manual (the parameter list and function diagram 8013).

##### Free function blocks

This section contains information on the following topics:

- [Logical and arithmetic functions using function blocks](#logical-and-arithmetic-functions-using-function-blocks)
- [Activating the individual function blocks](#activating-the-individual-function-blocks)
- [Logical functions](#logical-functions)
- [Arithmetic functions](#arithmetic-functions)
- [Time functions](#time-functions)
- [Memory functions](#memory-functions)
- [Switch functions](#switch-functions)
- [Control functions](#control-functions)
- [Complex functions](#complex-functions)

###### Logical and arithmetic functions using function blocks

Additional signal interconnections in the converter can be established by means of free function blocks. Every digital and analog signal available via BICO technology can be routed to the appropriate inputs of the free function blocks. The outputs of the free function blocks are also interconnected to other functions using BICO technology.

Among others, the following free function blocks are available:

- Logic blocks AND, OR, XOR, NOT, NCM (numeric comparator)
- Arithmetic blocks ADD, SUB, MUL, DIV, AVA (absolute-value generator), PLI (polyline)
- Time modules MFP (pulse generator), PCL (pulse shortening), PDE (ON delay), PDF (OFF delay), PST (pulse stretching)
- Memories: RSR (RS flip-flop), DSR (D flip-flop)
- Switches NSW (numerical selector) BSW (binary selector)
- Controllers LIM (limiter), PT1 (smoothing element), INT (integrator), DIF (differentiating element)
- Limit value monitoring LVM

**You will find an overview of all of the free function blocks and their parameters in the List Manual, in Chapter "Function diagrams" in Section "Free function blocks" (function diagrams 7210 ff).**

###### Activating the free blocks

None of the free function blocks in the converter are used in the factory setting. In order to be able to use a free function block, you must perform the following steps:

- In the parameter list, select the function block from the function diagrams - there you will find all of the parameters that you require to interconnect the block.
- Assign the block to a runtime group.
- Define the run sequence within the runtime group - this is only required if you have assigned several blocks to the same runtime group.
- Interconnect the block's inputs and outputs with the corresponding signals on the converter.

The runtime groups are calculated at different intervals (time slices). Please refer to the following table to see which free function blocks can be assigned to which time slices.

Runtime groups and possible assignments of the free function blocks

|  | Runtime groups 1 … 6 with associated time slices |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Free function blocks | 1 | 2 | 3 | 4 | 5 | 6 |
| 8 ms | 16 ms | 32 ms | 64 ms | 128 ms | 256 ms |  |
| Logic blocks AND, OR, XOR, NOT | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Arithmetic blocks ADD, SUB, MUL, DIV, AVA, NCM, PLI | - | - | - | - | ✓ | ✓ |
| Time blocks MFP, PCL, PDE, PDF, PST | - | - | - | - | ✓ | ✓ |
| Memories RSR, DSR | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Switches NSW | - | - | - | - | ✓ | ✓ |
| Switches BSW | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Controllers LIM, PT1, INT, DIF | - | - | - | - | ✓ | ✓ |
| Limit value monitoring  LVM | - | - | - | - | ✓ | ✓ |
| ✓: The block can be assigned to the runtime group -: The block cannot be assigned to this runtime group |  |  |  |  |  |  |

###### Analog signal scaling

If you interconnect a physical quantity, e.g. speed or voltage to the input of a free function block using BICO technology, then the signal is automatically scaled to a value of 1. The analog output signals of the free function blocks are also available as scaled quantities (0 ≙ 0%, 1≙ 100%).

As soon as you have interconnected the scaled output signal of a free function block to functions which require physical input quantities - e.g. the signal source of the upper torque limit (p1522) - then the signal is automatically converted into the physical quantity.

The quantities with their associated scaling parameters are listed in the following:

|  |  |  |
| --- | --- | --- |
| - Speeds | P2000   Reference speed | (≙100%) |
| - Voltage values | P2001   Reference voltage | (≙100%) |
| - Current values | P2002   Reference current | (≙100%) |
| - Torque values | P2003   Reference torque | (≙100%) |
| - Power values | P2004   Reference power | (≙100%) |
| - Angle | P2005   Reference angle | (≙100%) |
| - Acceleration | P2007   Reference acceleration | (≙100%) |
| - Temperature | 100° C ≙ 100% |  |

**Scaling examples**

- Speed:  
  Reference speed p2000 = 3000 rpm, actual speed 2100 rpm. As a consequence, the following applies to the scaled input quantity: 2100 / 3000 = 0,7.
- Temperature:  
  Reference quantity is 100° C. For an actual temperature of 120° C, the input value is obtained from 120° C / 100° C = 1.2.

  > **Note**
  >
  > Limits within the function blocks should be entered as scaled values. The scaled value can be calculated as follows using the reference parameter: Scaled limit value = physical limit value / value of the reference parameter.
  >
  > The assignment to reference parameters is provided in the parameter list in the individual parameter descriptions.

###### Example: Logic combination of two digital inputs

You want to switch on the motor via digital input 0 and also via digital input 1:

1. Activate a free OR block by assigning it to a runtime group, and define the run sequence.
2. Interconnect the status signals of the two digital inputs DI 0 and DI 1 via BICO to the two inputs of the OR block.
3. Finally, interconnect the OR block output with the internal ON command (P0840).

Parameters for using the free function blocks

| Parameter | Description |
| --- | --- |
| P20048 = 1 | **Assignment of block**  **OR 0**  **to runtime group 1** (factory setting: 9999)  The block OR 0 is calculated in the time slice with 8 ms |
| P20049 = 60 | Definition of run sequence within runtime group 1 (factory setting: 60)  Within one runtime group, the block with the smallest value is calculated first. |
| P20046 [0] = 722.0 | **Interconnection of first**  **OR 0**  **input (factory setting: 0)**   The first OR 0 input is linked to digital input 0 (r0722.0) |
| P20046 [1] = 722.1 | **Interconnection of second**  **OR 0**  **input (factory setting: 0)**   The second OR 0 input is linked to digital input 1 (r0722.1) |
| P0840 = 20047 | **Interconnection of**  **OR 0**  **output (factory setting: 0)**   The OR 0 output (r20047) is connected with the motor's ON command |

###### Example: AND operation

An example of an AND logic operation, explained in detail, including the use of a time block is provided in [BICO technology: example](Configuring%20SINAMICS%20G120-G115D-G110M%20drives.md#bico-technology-example).

###### Activating the individual function blocks

Each individual function block is assigned to a runtime group via two parameters:

- The first parameter defines the runtime group.
- The second parameter defines the run sequence within the runtime group.

Within a runtime group, a function block with a lower value for the run sequence is computed before a function block with a higher value.

> **Note**
>
> In the factory setting, each function block is assigned to runtime group 9999. This means that the function block is not computed.

###### Logical functions

This section contains information on the following topics:

- [AND](#and)
- [OR](#or)
- [XOR (exclusive OR)](#xor-exclusive-or)
- [NOT (inverter)](#not-inverter)
- [NCM numeric comparator](#ncm-numeric-comparator)

###### AND

###### Brief description

BOOL-type AND function block with four inputs

###### Method of operation

This function block links the binary variables at inputs I to a logical AND and outputs the result to its digital output Q.

![Method of operation](images/103443087243_DV_resource.Stream@PNG-en-US.png)

Output Q = 1 when the value 1 is present at every input from I<sub>0</sub> to I<sub>3</sub>. In all other cases, output Q = 0.

###### OR

###### Brief description

BOOL-type OR function block with four inputs

###### Method of operation

This function block links the binary variables at inputs I to a logic OR (disjunction) and outputs the result to its digital output Q.

Q = I
<sub>0</sub>
 v I
<sub>1</sub>
 v I
<sub>2</sub>
 v I
<sub>3</sub>

Output Q = 0 when the value 0 is present at every input from I<sub>0</sub> to I<sub>3</sub>. In all other cases, output Q = 1.

###### XOR (exclusive OR)

###### Brief description

BOOL-type XOR function block with four inputs

###### Method of operation

This function block links the binary variables at the inputs I according to the exclusive OR logic function and outputs the result to its digital output Q.

Output Q = 0 when the value 0 is present at every input from I0 to I3 or when the value 1 is present at an even number of inputs from I0 to I3.

Output Q = 1 when the value 1 is present at an odd number of inputs from I0 to I3.

###### NOT (inverter)

###### Brief description

BOOL-type inverter

###### Method of operation

This function block inverts the binary variables at input I and outputs the result to output Q.

![Method of operation](images/103443213579_DV_resource.Stream@PNG-en-US.png)

Output Q = 1 when the value 0 is present at input I.

Output Q = 0 when the value 1 is present at input I.

###### NCM numeric comparator

###### Brief description

Function block for compare operations of two numeric variables of the REAL type.

###### Method of operation

The input variables X1 and X2 are compared and one of the binary outputs QU, QE, or QL is set depending on the result of the compare operation.

###### Arithmetic functions

This section contains information on the following topics:

- [ADD (adder)](#add-adder)
- [SUB (subtracter)](#sub-subtracter)
- [MUL (multiplier)](#mul-multiplier)
- [DIV (divider)](#div-divider)
- [AVA (absolute value generator with sign evaluation)](#ava-absolute-value-generator-with-sign-evaluation)
- [Polyline](#polyline)

###### ADD (adder)

###### Brief description

REAL-type adder with four inputs

###### Method of operation

This function block adds (in accordance with the sign) the values entered at inputs X<sub>0</sub> to X<sub>3</sub>.

The result is limited to a range of -3.4E38 to +3.4E38 and output at output Y.

Y = X
<sub>0</sub>
 + X
<sub>1</sub>
 + X
<sub>2</sub>
 +X
<sub>3</sub>

###### SUB (subtracter)

###### Brief description

REAL-type subtracter with two inputs

###### Method of operation

This function block subtracts (in accordance with the sign) the value entered at input X<sub>1</sub> from the value entered at input X<sub>0</sub>.

The result is limited to a range of -3.4E38 to +3.4E38 and output at output Y.

Y = X
<sub>0</sub>
 – X
<sub>1</sub>

###### MUL (multiplier)

###### Brief description

REAL-type multiplier with four inputs

###### Method of operation

This function block multiplies (in accordance with the sign) the values entered at inputs X<sub>0</sub> to X<sub>3</sub>.

The result is limited to a range of -3.4E38 to +3.4E38 and output at output Y.

Y = X
<sub>0</sub>
 · X
<sub>1</sub>
 · X
<sub>2</sub>
 · X
<sub>3</sub>

###### DIV (divider)

###### Brief description

REAL-type divider with two inputs

###### Method of operation

This function block divides the value entered at input X<sub>0</sub> by the value entered at input X<sub>1</sub>. The result is output at the outputs as follows:

- Y output: Quotient with places before and after the decimal point
- YIN output: Integer quotient
- MOD output: Division remainder (absolute remainder value, MOD = (Y - YIN) × X0)

The Y output is limited to a range of approx. -3.4E38 to +3.4E38.

![Method of operation](images/103443411851_DV_resource.Stream@PNG-en-US.png)

If output value Y exceeds the permissible value range of approx. -3.4E38 to 3.4E38 (because divisor X<sub>1</sub> is very small or zero), the limit value of the output range with the correct sign is output at the Y output. At the same time, digital output QF is set to 1.

With a division of 0/0, block output Y remains unchanged. Digital output QF is set to 1.

###### AVA (absolute value generator with sign evaluation)

###### Brief description

REAL-type arithmetic function block for generating absolute values

###### Method of operation

This function block generates the absolute value of the value present at input X. The result is output at output Y.

Y = |X|

If the input variable is negative, digital output SN is set to 1.

###### Polyline

###### Brief description

Polyline function block of the REAL type with four inputs

- For the linearization of characteristic curves
- For the simulation of non-linear transfer elements
- For controller gain defined in sections

###### Method of operation

This block adapts output variable Y to input variable X by means of up to 20 breakpoints in 4 quadrants. Interpolation is carried out linearly between the breakpoints. Outside of A1 to A20, the characteristic curve runs horizontally.

###### Engineering Information

Make sure that the values from A1 to A20 are sorted in ascending order during the configuration, otherwise incorrect values are output. The ordinate values B1 to B20 can be selected at random, i.e. independently of the previous value. If breakpoints are not needed (e.g. A16/B16 and higher), the following abscissas and ordinates (A16/B16 to A20/B20) must be assigned the same values as A15/B15.

![Polyline](images/103443521931_DV_resource.Stream@PNG-en-US.png)

Polyline

###### Time functions

This section contains information on the following topics:

- [MFP (pulse generator)](#mfp-pulse-generator)
- [PCL (pulse shortener)](#pcl-pulse-shortener)
- [PST (pulse stretcher)](#pst-pulse-stretcher)
- [PDE (ON delay)](#pde-on-delay)
- [PDF (OFF delay)](#pdf-off-delay)

###### MFP (pulse generator)

###### Brief description

- Timer for generating a pulse with a fixed duration
- Used as a pulse-contracting or pulse-stretching monoflop

###### Method of operation

The rising edge of a pulse at input I sets output Q to 1 for pulse duration T. The pulse generator cannot be retriggered.

###### Time flow chart

Output pulse Q as a function of pulse duration T and input pulse I.

![MFP (pulse generator): Time flow chart](images/103443597195_DV_resource.Stream@PNG-en-US.png)

MFP (pulse generator): Time flow chart

###### PCL (pulse shortener)

###### Brief description

Timer for limiting the pulse duration

###### Method of operation

The rising edge of a pulse at input I sets output Q to 1.

Output Q becomes 0 when input I becomes 0 or pulse duration T has expired.

###### Time flow chart

Output pulse Q as a function of pulse duration T and input pulse I.

![PCL (pulse shortener): Time flow chart](images/103443653899_DV_resource.Stream@PNG-en-US.png)

PCL (pulse shortener): Time flow chart

###### PST (pulse stretcher)

###### Brief description

Timer for generating a pulse with a minimum duration and an additional reset input

###### Method of operation

The rising edge of a pulse at input I sets output Q to 1.

Output Q does not return to 1 until input pulse I is 0 and pulse duration T has expired.

Output Q can be set to zero at any time via reset input R with R = 1.

###### Time flow chart

Output pulse Q as a function of pulse duration T and input pulse I (when R = 0).

![PST (pulse stretcher): Time flow chart](images/103443697803_DV_resource.Stream@PNG-en-US.png)

PST (pulse stretcher): Time flow chart

###### PDE (ON delay)

###### Brief description

BOOL-type timer with ON delay

###### Method of operation

The rising edge of a pulse at input I sets output Q to 1 after pulse delay time T.

Output Q becomes 0 when I becomes 0.

If the duration of input pulse I is less than pulse delay time T, Q remains 0.

If time T is so long that the maximum value that can be displayed internally (T/ta as 32 bit value, where ta = sampling time) is exceeded, the maximum value is set (e.g. when ta = 1 ms, approx. 50 days).

###### Time flow chart

Output pulse Q as a function of pulse duration T and input pulse I.

![PDE (ON delay): Time flow chart](images/103443754507_DV_resource.Stream@PNG-en-US.png)

PDE (ON delay): Time flow chart

###### PDF (OFF delay)

###### Brief description

Timer with OFF delay

###### Method of operation

The falling edge of a pulse at input I resets output Q to 0 after OFF delay time T.

Output Q becomes 1 when I becomes 1.

Output Q becomes 0 when input pulse I becomes 0 and OFF delay time T has expired.

If input I is reset to 1 before time T has expired, output Q remains 1.

###### Time flow chart

Output pulse Q as a function of pulse duration T and input pulse I.

![PDF (OFF delay): Time flow chart](images/103443811211_DV_resource.Stream@PNG-en-US.png)

PDF (OFF delay): Time flow chart

###### Memory functions

This section contains information on the following topics:

- [RSR (RS flip-flop, reset dominant)](#rsr-rs-flip-flop-reset-dominant)
- [DFR (D flip-flop, reset dominant)](#dfr-d-flip-flop-reset-dominant)

###### RSR (RS flip-flop, reset dominant)

###### Brief description

Reset dominant RS flip-flop for use as a static binary value memory

###### Method of operation

With logical 1 at input S, output Q is set to logical 1.

If input R is set to logical 1, output Q is set to logical 0.

If both inputs are logical 0, Q does not change.

If both inputs are logical 1, however, Q is logical 0 because the reset input dominates.

Output QN always has the opposite value to Q.

###### DFR (D flip-flop, reset dominant)

###### Brief description

BOOL-type function block for use as a D flip-flop with reset dominance

###### Method of operation

If inputs S and R are logical 0, the D input data is switched through to output Q when a rising edge is present at trigger input I.

Output QN always has the opposite value to Q. With logical 1 at input S, output Q is set to logical 1.

If input R is set to logical 1, output Q is set to logical 0. If both inputs are logical 0, Q does not change.

If inputs S and R are logical 1, however, Q is logical 0 because the reset input dominates.

###### Time flow chart

Output pulse Q as a function of the D input and input pulse I for S = R = 0.

![DFR (D flip-flop, reset dominant): Time flow chart](images/103443936779_DV_resource.Stream@PNG-en-US.png)

DFR (D flip-flop, reset dominant): Time flow chart

###### Switch functions

This section contains information on the following topics:

- [NSW (numerical selector)](#nsw-numerical-selector)
- [BSW (binary selector)](#bsw-binary-selector)

###### NSW (numerical selector)

###### Brief description

This function block switches one of two numeric input variables (REAL type) to the output.

###### Method of operation

If input I = 0, X0 is switched to output Y.

If input I = 1, X1 is switched to output Y.

###### BSW (binary selector)

###### Brief description

This function block switches one of two binary input variables (BOOL type) to the output.

###### Method of operation

If input I = 0, I0 is switched to output Q.

If input I = 1, I1 is switched to output Q.

###### Control functions

This section contains information on the following topics:

- [LIM (limiter)](#lim-limiter)
- [PT1 (smoothing element)](#pt1-smoothing-element)
- [INT (integrator)](#int-integrator)
- [DIF (derivative action element)](#dif-derivative-action-element)

###### LIM (limiter)

###### Brief description

- Function block for limiting
- Adjustable upper and lower limit
- Indication when set limits are reached

###### Method of operation

The function block transfers input variable X to its output Y. The input variable is limited depending on LU and LL.

If the input variable reaches the upper limit LU, output QU is set to 1.

If the input variable reaches the lower limit LL, output QL is set to 1.

If the lower limit is greater than or equal to the upper limit, output Y is set to the upper limit LU.

Algorithm:

![Method of operation](images/103444080779_DV_resource.Stream@PNG-en-US.png)

Constraint: LL < LU

###### PT1 (smoothing element)

###### Brief description

- First-order delay element with setting function
- Used as smoothing element

###### Method of operation

**Setting function not active (S = 0)**

Input variable X, dynamically delayed by smoothing time constant T, is switched to output Y.

T determines the steepness of the rise of the output variable. It specifies the time at which the transfer function has risen to 63% of its full-scale value.

When t = 3T, the transfer function reaches approximately 95% of its full-scale value.

The internally fixed proportional gain is 1 and cannot be changed.

If T/TA is sufficiently large (T/TA > 10), the transfer function has the following characteristic:

Y (t) = X · (1 - e-t/T)

Constraint: t = n · TA

The discrete values are calculated according to the following algorithm:

Y<sub>n</sub> = Y<sub>n-1</sub> + (TA/T) (X<sub>n</sub> - Y<sub>n-1</sub>)

| Symbol | Meaning |
| --- | --- |
| Y<sub>n</sub> | Value of Y in sampling time n |
| Y<sub>n-1</sub> | Value of Y in sampling time n-1 |
| X<sub>n</sub> | Value of X in sampling time n |

**Setting function active (S = 1)**

When the setting function is active, the current setting value SVn is accepted at the output variable:

Yn = SVn

> **Note**
>
> The larger T/TA is, the smaller the amplitude change at Y from one sampling time to the next. TA is the configured sampling time of the function block.
>
> T is limited internally: T ≥ TA

###### INT (integrator)

###### Brief description

- Function block with integrating action
- Integrator functions:

  - Set initial value.
  - Adjustable integral time constant
  - Adjustable limits
  - For normal integrator operation, a positive limit value must be specified for LU and a negative limit value for LL.

###### Method of operation

The change in output variable Y is proportional to input variable X and inversely proportional to the integral time constant TI.

Output Y of the integrator can be limited via the inputs LU and LL. If the output reaches one of the two limits, a signal is sent via the outputs QU or QL. If LL ≥ LU, then output Y = LU.

The discrete values (TA is the configured sampling time of the function block) are calculated according to the following algorithm:

Yn = Yn-1 + (TA/TI) Xn

| Symbol | Meaning |
| --- | --- |
| Y<sub>n</sub> | Value of Y in sampling time n |
| Y<sub>n-1</sub> | Value of Y in sampling time n-1 |
| X<sub>n</sub> | Value of X in sampling time n |

When S = 1, the output variable Y is set to the setting value SV. Two functions can be performed via S:

- Track integrator (Y = SV)

  The digital input is S = 1 and the setting value SV is changed. If applicable, the output makes a jump to the setting value immediately after the setting operation.
- Set integrator to initial value SV.

  S is switched to 1. S is then set to 0, and the integrator starts from SV in the direction specified by the polarity of input variable X.

  > **Note**
  >
  > TI is limited internally: TI = TA

###### DIF (derivative action element)

###### Brief description

Function block with derivative action behavior

###### Method of operation

Output variable Y is proportional to the rate of change of input variable X multiplied by differentiation time constant TD.

The discrete values are calculated according to the following algorithm:

Yn = (Xn – Xn-1) · TD/TA

| Symbol | Meaning |
| --- | --- |
| Y<sub>n</sub> | Value of Y in sampling time n |
| X<sub>n</sub> | Value of Y in sampling time n-1 |
| X<sub> n-1</sub> | Value of X in sampling time n |

> **Note**
>
> The bigger TD/TA, the bigger the amplitude change on Y from one sampling time to the next. TA is the configured sampling time of the function block.
>
> TD is limited internally to TD ≥ 0.
>
> Caution: Overcontrol possible!

###### Complex functions

This section contains information on the following topics:

- [LVM (double-sided limit monitor with hysteresis)](#lvm-double-sided-limit-monitor-with-hysteresis)

###### LVM (double-sided limit monitor with hysteresis)

###### Brief description

- This BOOL-type function block monitors an input variable by comparing it with selectable reference variables.
- Application:

  - Monitoring setpoints, actual and measured values.
  - Suppressing frequent switching (jitter).
- This function block provides a window discriminator function.

###### Method of operation

This function block uses a transfer characteristic (see transfer characteristic) with hysteresis to calculate an internal intermediate value.

The intermediate value is compared with the interval limits and the result is output at outputs QU, QM, and QL.

The transfer characteristic is configured with the values for the mean value M, the interval limit L, and the hysteresis HY.

###### Transfer characteristic

![LVM (double-sided limit monitor with hysteresis): Transfer characteristic](images/103444250123_DV_resource.Stream@PNG-en-US.png)

LVM (double-sided limit monitor with hysteresis): Transfer characteristic

##### PID Technology controller

This section contains information on the following topics:

- [Setting up and opimize the controller](#setting-up-and-opimize-the-controller)

###### Setting up and opimize the controller

###### Overview

The technology controller controls process variables, e.g. pressure, temperature, level or flow.

![Example: technology controller as a level controller](images/149913387019_DV_resource.Stream@PNG-en-US.png)

Example: technology controller as a level controller

###### Precondition

**Additional functions**

The motor closed-loop control is set

**Tools**

To change the function settings, you can use an operator panel or a PC tool, for example.

###### Function description

**Function diagram**

The technology controller is implemented as a PID controller (controller with proportional, integral, and derivative action).

![Simplified representation of the technology controller](images/106506728843_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | The converter uses the start value when all the following conditions are simultaneously satisfied:  - The technology controller supplies the main setpoint (p2251 = 0). - The ramp-function generator output of the technology controller has not yet reached the start value. |

Simplified representation of the technology controller

**Basic settings**

The settings required as a minimum are marked in gray in the function diagram:

- Interconnect setpoint and actual values with signals of your choice
- Set ramp-function generator and controller parameters K<sub>P</sub>, T<sub>I</sub> and T<sub>d</sub>.

###### Set controller parameters K<sub>P</sub>, T<sub>I</sub> and T<sub>d</sub>.

**Procedure**

1. Temporarily set the ramp-up and ramp-down times of the ramp-function generator (p2257 and p2258) to zero.
2. Enter a setpoint step and monitor the associated actual value, e.g. with the trace function of Startdrive.  
   The slower the response of the process to be controlled, the longer you must monitor the controller response. Under certain circumstances (e.g. for a temperature control), you need to wait several minutes until you can evaluate the controller response.

   | Symbol | Meaning |
   | --- | --- |
   | ![Set controller parameters KP, TIand Td.](images/94529364875_DV_resource.Stream@PNG-de-DE.png) | Optimum controller response for applications that do not permit any overshoot.  The actual value approaches the setpoint without any significant overshoot. |
   | ![Set controller parameters KP, TIand Td.](images/94529441419_DV_resource.Stream@PNG-de-DE.png) | Optimum controller behavior for fast correction and quick compensation of disturbance components.  The actual value approaches the setpoint and slightly overshoots, maximum 10% of the setpoint step. |

   | Symbol | Meaning |
   | --- | --- |
   | ![Set controller parameters KP, TIand Td.](images/94529543563_DV_resource.Stream@PNG-de-DE.png) | The actual value only slowly approaches the setpoint. - Increase the proportional component K<sub>P</sub> (p2280) and reduce the integration time T<sub>I</sub> (p2285). |
   | ![Set controller parameters KP, TIand Td.](images/94529581707_DV_resource.Stream@PNG-de-DE.png) | The actual value only slowly approaches the setpoint with slight oscillation. - Increase the proportional component K<sub>P</sub> (p2280) and reduce the rate time T<sub>d</sub> (p2274) |
   | ![Set controller parameters KP, TIand Td.](images/94529671051_DV_resource.Stream@PNG-de-DE.png) | The actual value quickly approaches the setpoint, but overshoots too much. - Decrease the proportional component K<sub>P</sub> (p2280) and increase the integration time T<sub>I</sub> (p2285). |
3. Set the ramp-up and ramp-down times of the ramp-function generator back to their original value.

You have manually set the technology controller.

**Limiting the output of the technology controller**

In the factory setting, the output of the technology controller is limited to ± maximum speed. You must change this limit, depending on your particular application.  
Example: The output of the technology controller supplies the speed setpoint for a pump. The pump should only run in the positive direction.

###### Parameter

Basic settings

| Parameter | Description | Setting |
| --- | --- | --- |
| p2200 | BI: Technology controller enable | 1 signal: Technology controller is enabled.  Factory setting: 0 |
| r2294 | CO: Technology controller output signal | To interconnect the main speed setpoint with the technology controller output, set p1070 = 2294. |
| p2253 | CI: Technology controller setpoint 1 | Setpoint for the technology controller.  Example: p2253 = 2224: Fixed setpoint p2201 is interconnected with the setpoint of the technology controller. p2220 = 1: The fixed setpoint p2201 is selected.  Factory setting: 0 |
| p2264 | CI: Technology controller actual value | Technology controller actual value.  Factory setting: 0 |
| p2257, p2258 | Technology controller ramp-up time and ramp-down time [s] | Factory setting: 0.0 s |
| p2274 | Technology controller differentiation time constant T<sub>d</sub> [s] | The differentiation improves the rise time for very slow controlled variables, e.g. a temperature control.  Factory setting: 0.0 s |
| p2280 | Technology controller proportional gain K<sub>P</sub> | Factory setting: 1.0 |
| p2285 | Technology controller integration time (integral time) T<sub>d</sub> | Factory setting: 30 s |

Limiting the output of the technology controller

| Parameter | Description | Setting |
| --- | --- | --- |
| p2297 | CI: Technology controller maximum limiting signal source | Factory setting: 1084 |
| p2298 | CI: Technology controller minimum limiting signal source | Factory setting: 2292 |
| p2291 | CO: Technology controller maximum limiting [%] | Factory setting: 100 % |
| p2292 | CO: Technology controller minimum limiting [%] | Factory setting: 0 % |

Adapting the actual value of the technology controller

| Parameter | Description | Setting |
| --- | --- | --- |
| p2267 | Technology controller upper limit actual value [%] | Factory setting: 100 % |
| p2268 | Technology controller lower limit actual value [%] | Factory setting: -100 % |
| p2269 | Technology controller gain actual value [%] | Factory setting: 100 % |
| p2271 | Technology controller actual value inversion | Technology controller actual value inversion  If the actual value decreases with increasing motor speed, then p2271 must be set = 1.  0: no inversion  1: actual value signal is inverted  Factory setting: 0 |
| p2270 | Technology controller actual value function | Technology controller actual value function   0: no function  1: √  2: x<sup>2</sup>  3: x<sup>3</sup>  Factory setting: 0 |

###### Further information

For additional information refer to the function diagrams 7950 ff of the List Manual.

You will find additional information on the following PID controller components in the Internet at:

- Setpoint input: Analog value or fixed setpoint
- Setpoint channel: Scaling, ramp-function generator and filter
- Actual value channel: Filter, limiting and signal processing
- PID controller Principle of operation of the D component, inhibiting the I component and the control sense
- Enable, limiting the controller output and fault response

![Further information](images/109219489803_DV_resource.Stream@PNG-de-DE.png)
[FAQ](http://support.automation.siemens.com/WW/view/en/92556266)

#### Specific G120P functions

This section contains information on the following topics:

- [Real-time clock (RTC)](#real-time-clock-rtc)
- [Time switch (DTC)](#time-switch-dtc)
- [Essential service mode](#essential-service-mode)
- [Multi-zone control](#multi-zone-control)
- [Cascade control](#cascade-control)
- [Bypass](#bypass)
- [Hibernation](#hibernation)

##### Real-time clock (RTC)

The real-time clock is the basis for time-dependent process controls, e.g.:

- To reduce the temperature of a heating control during the night
- Increase the pressure of a water supply at certain times during the day

###### Function and settings

The real-time clock starts as soon as the Control Unit power supply is switched on for the first time. The real-time clock comprises the clock time in a 24 hour format and the date in the "day, month, year" format.

After a Control Unit power supply interruption, the real-time clock continues to run for approx. five days.

If you wish to use the real-time clock, you must set the time and date once when commissioning. If you restore the converter factory setting, the real-time clock parameters are not reset.

| Parameter | Real-time clock (RTC) |  |
| --- | --- | --- |
| p8400 | **RTC time** (Factory setting: 0) |  |
| [0] | Hour (0 … 23) |  |
| [1] | Minute (0 … 59) |  |
| [2] | Second (0 … 59) |  |
| p8401 | **RTC date** (Factory setting: 1.1.1970) |  |
| [0] | Day: 1 … 31. |  |
| [1] | Month 1 (January) … 12 (December) |  |
| [2] | Year: 1970 … 9999 |  |
| p8402 | **RTC daylight saving time setting**   The factory setting corresponds to the changeover times for Central European Summer Time (CEST). To activate the CEST, only p8402[0] = 1 needs to be set. |  |
| [0] | Difference between daylight saving time and standard time (factory setting: 0 h) |  |
| [1] | Start of month (factory setting: 3), 1 (January) … 12 (December) |  |
| [2] | Start of week of month (factory setting: 6)  1: Day 1 … 7, 2: Day 8 … 14, 3: Day 15 … 21, 4: Day 22 … 28, 6: Last seven days of the month |  |
| [3] | Start weekday (factory setting: 7), 1 (Monday) … 7 (Sunday) |  |
| [4] | Start hour (factory setting: 2) |  |
| [5] | End month (factory setting: 10) |  |
| [6] | End week of month (factory setting: 6)  1: Day 1 … 7, 2: Day 8 … 14, 3: Day 15 … 21, 4: Day 22 … 28, 6: Last seven days of the month |  |
| [7] | End weekday (factory setting: 7), 1 (Monday) … 7 (Sunday) |  |
| [8] | End hour (factory setting: 3) |  |
| r8403 | **RTC daylight saving time difference actual** [hours]  Displays the actual difference between standard time and daylight saving time. |  |
| r8404 | **RTC weekday,** 1: Monday … 7: Sunday |  |
| p8405 | **RTC activate/deactivate alarm A01098** (Factory setting: 1)  Alarm for non synchronous time, e.g. after a longer power supply interruption. |  |
| 0: | No alarm |  |
| 1: | Alarm A01098 |  |

###### Accept the real-time clock in the alarm and fault buffer

Using the real-time clock, you can track the sequence of alarms and faults over time. When an appropriate message occurs, the converter converts the real-time clock into the UTC time format (Universal Time Coordinated):

Date, time ⇒ 01.01.1970, 0:00 + d (days) + m (milliseconds)

The converter takes the number "d" of the days and the number "m" of the milliseconds in the alarm and fault times of the alarm and/or fault buffer.

Refer Alarms, faults and system messages.

**Converting UTC to RTC**

An RTC can again be calculated in the UTC format from the saved fault or alarm time. In the Internet, you will find programs to convert from UTC to RTC, e.g.

[UTC to RTC](http://unixtime-converter.com/)

**Example:**

Saved as alarm time in the alarm buffer:

r2123[0] = 2345 [ms]  
r2145[0] = 14580 [days]

Number of seconds = 2345 / 1000 + 14580 × 86400 = 1259712002  
Converting this number of seconds to RTC provides the date: 02.12.2009, 01:00:02.

The times specified for alarms and faults always refer to standard time.

##### Time switch (DTC)

![Figure](images/91492236043_DV_resource.Stream@PNG-de-DE.png)

The "time switch" (DTC) function, along with the real-time clock in the converter, offers the option of controlling when signals are switched on and off.

**Examples:**

- Switching temperature control from day to night mode.
- Switching a process control from weekday to weekend.

###### Principle of operation of the time switch (DTC)

The converter has three independently adjustable time switches. The time switch output can be interconnected with every binector input of your converter, e.g. with a digital output or a technology controller's enable signal.

![Example of the response of the time switch.](images/149911591947_DV_resource.Stream@PNG-en-US.png)

Example of the response of the time switch.

**Settings for the example with DTC1**

- Enable parameterization of the DTC: p8409 = 0.   
  As long as the parameterization of the DTC is enabled, the converter holds the output of all three DTC (r84x3, x = 1, 2, 3; r84x3.0 normal, r84x3.1 inverted status message) at LOW.
- Activate/deactivate the weekday

  - p8410[0] = 0     Monday

  - p8410[1] = 1     Tuesday

  - p8410[2] = 1     Wednesday

  - p8410[3] = 0     Thursday

  - p8410[4] = 1     Friday

  - p8410[5] = 1     Saturday

  - p8410[6] = 0     Sunday
- Setting switching times:

  - ON: p8411[0] = 20 (hh),   p8411[1] = 0 (MM)
  - OFF: p8412[0] = 10 (hh),   p4812[1] = 0 (MM)
- Enable the setting: p8409 = 1.   
  The converter re-enables the DTC output.

Additional information is provided in the parameter list of the List Manual.

##### Essential service mode

This section contains information on the following topics:

- [Essential service mode](#essential-service-mode-1)
- [Faults which are not ignored in emergency operation](#faults-which-are-not-ignored-in-emergency-operation)

###### Essential service mode

![Figure](images/91700305931_DV_resource.Stream@PNG-de-DE.png)

In essential service mode (ESM), the converter attempts to operate the motor for as long as possible despite irregular ambient conditions.

The converter logs the essential service mode and any faults that occur during essential service mode. The log is accessible only for the service and repair organization.

> **Note**
>
> **Warranty is lost in the essential service mode**
>
> If you activate the essential service mode, all of the warranty claims associated with the converter become null and void. The essential service mode can have the following effects:
>
> - Exceptionally high temperatures inside and outside the converter
> - Open fire inside and outside the converter
> - Emissions of light, noise, particles or gases

###### Example

To improve the air circulation in the stairwells, the ventilation control creates an underpressure in the building. With this control, a fire would mean that flue gases enter into the stairwell. This would then mean that the stairs would be blocked as escape or evacuation route.

Using the essential service mode function, the ventilation switches over to the control of an overpressure. The essential service mode prevents the propagation of flue gas in the stairwell, thereby keeping the stairs free as an evacuation route as long as possible.

###### Special features of the essential service mode

**Activating and terminating essential service mode**

Signal p3880 = 1 activates the essential service mode:

- If the motor was switched off by activating essential service mode, the converter switches the motor on. The speed setpoint is die "ESM setpoint source".
- If the motor was switched on by activating essential service mode, the converter switches the speed setpoint to "ESM setpoint source".

Signal p3880 = 0 deactivates the essential service mode:

- If one of the OFF1, OFF2 or OFF3 commands is active, the converter switches off the motor.
- If neither OFF1, OFF2 nor OFF3 is active, the converter switches the speed setpoint from the "ESM setpoint source" to the normal setpoint source.

**Switch the motor on and off during active essential service mode via other signals**

The OFF1, OFF2 and OFF3 commands for switching off the motor have no effect.

The converter blocks all functions that switch off the motor to save energy, e.g. PROFIenergy or hibernation mode.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected exiting of the essential service mode by selecting "Safe Torque Off"**  The PM240‑2 and PM240P‑2, FSD … FSF Power Modules provide terminals for selecting the "Safe Torque Off" (STO) safety function. An active STO function switches the motor off and so terminates essential service mode. The termination of essential service mode can cause severe injury or death, e.g. for the failure of a flue gas extraction.  - Set both STO switches to the "OFF" position on the PM240‑2 or PM240P‑2, FSD … FSF Power Module. |  |

**Reaction to faults during active essential service mode**

In "essential service mode", the converter does not switch off the motor when faults develop, but rather reacts differently depending on the fault type:

- The converter ignores faults, which do not directly result in the destruction of the converter or the motor.
- The converter attempts to automatically acknowledge faults, which cannot be ignored, using the automatic restart function.
- For faults that cannot be acknowledged, it is possible to switch over the motor to line operation using the bypass function.

**Automatic restart during active essential service mode**

The converter ignores the settings in p1206 (faults without automatic restart) and works with the setting "restart after a fault with further start attempts" (p1210 = 6).

The converter carries out the maximum number of restart attempts set in p1211 corresponding to the settings in p1212 and p1213. If these attempts are not successful, then the converter goes into a fault condition with F07320.

**Speed setpoint during active essential service mode**

P3881 specifies the setpoint. If you have defined an analog input as setpoint source using p3881, then for wire breakage, the converter can switch over to setpoint p3882.

**Interaction for bypass and essential service mode**

- If, when activating the essential service mode, bypass operation is active, converter operation is selected internally in order to ensure that the setpoint is entered via the source intended for the essential service mode.
- If faults are still present after the number of start attempts parameterized in p1211, then the converter goes into a fault condition with F07320. In this case, there is an option of switching over to bypass operation and then directly connecting the motor to the line supply.

###### Commissioning the extended service mode

**Procedure**

1. Interconnect a free digital input as signal source for the ESM activation.

   You must use a negated digital input if the essential service mode should also be active for a ground fault – or if the control cable is interrupted.

   Example for negated digital input DI 3: Set p3880 = 723.3.

   It is not permissible to interconnect the digital input for ESM activation with other functions.
2. Set the ESM setpoint source via p3881.
3. Set the alternative ESM setpoint source via p3882.
4. Set the source to select the direction of rotation.

   - p3881 = 0, 1, 2, 3:

     When you interconnect p3883 with a free digital input of your choice, p3883 inverts the direction of rotation during essential service mode.

     For example, to interconnect p3883 with DI 4, set p3883 = 722.4.
   - p3881 = 4:

     The technology setpoint direction of rotation is valid.
5. Optional switching to bypass mode

   If the converter is not able to acknowledge pending faults with automatic restart, it signals fault F07320 and does not make any other attempts to restart.

   If the motor still continues to operate in this case, you must set the following:

   - Set p1266 = 3889.10. The converter switches the motor to bypass mode with r3889.10 = 1.
   - Ensure that the direction of rotation does not change when switching over to bypass operation.
   - Set p1267.0 = 1. The converter switches the motor to bypass mode independent of the speed with control signal p1266.
   - Commission the "Bypass" function.

     ![Commissioning the extended service mode](images/109220677643_DV_resource.Stream@PNG-de-DE.png)
     [Bypass](#bypass)

You have commissioned the essential service mode.

###### Settings

| Parameter | Description |  |
| --- | --- | --- |
| p3880 | **BI: ESM activation signal source** (factory setting 0)  Set the signal source to activate essential service mode (ESM) via the digital input |  |
| p3881 | **ESM setpoint source** (factory setting 0) |  |
| 0: | Last known setpoint (r1078 smoothed) |  |
| 1: | Fixed speed setpoint 15 (p1015) |  |
| 2: | Control Unit analog input 0 (AI 0, r0755[0]) |  |
| 3: | Fieldbus |  |
| 4: | Technology controller  Set the ESM setpoint source via p3884. |  |
| 6: | Enable OFF1 reaction |  |
| 7: | Enable OFF2 reaction |  |
| p3882 | **Alternative ESM setpoint source** (factory setting 0) |  |
| 0: | Last known setpoint (r1078 smoothed) |  |
| 1: | Fixed speed setpoint 15 (p1015) |  |
| 2: | Maximum speed (p1082) |  |
| p3883 | **BI: ESM direction of rotation signal source** (factory setting 0) |  |
| 0 signal: The direction of rotation of the setpoint configured for essential service mode is maintained  1 signal: Reversal of the direction of rotation of the setpoint configured for essential service mode. |  |  |
| p3884 | **CI: ESM technology controller setpoint** (factory setting 0) |  |
| Setpoint signal source for p3881 = 4.  If you do not connect a setpoint in p3884, the converter takes technology setpoint 1 (p2253). |  |  |
| r3887 | **Number of ESM activations/faults** |  |
| .00 | 1 signal: Essential service mode (ESM) activated |  |
| .01 | 1 signal: Direction of rotation inverted |  |
| .02 | 1 signal: Setpoint signal lost |  |
| .03 | 1 signal: Technology controller actual value lost (p2264) |  |
| .04 | 1 signal: Bypass active |  |
| .05 | 1 signal: Technology controller setpoint parameterized (p3884) |  |
| .06 | 1 signal: Technology controller active during essential service mode |  |
| .09 | 1 signal: Reaction OFF1/OFF2 activated |  |
| .10 | 1 signal: Automatic restart aborted (F07320) |  |

###### Application example

An application example for the essential service mode can be found on the Internet:

[http://support.automation.siemens.com/WW/view/en/63969509](http://support.automation.siemens.com/WW/view/en/63969509
// XmlEditor.InternalXmlClipboard:12331c4a-d160-c167-589e-1aa78d4d7700)

###### Faults which are not ignored in emergency operation

###### Faults, which are not ignored when operating in the essential service mode

| Symbol | Meaning |
| --- | --- |
| F01000 | Internal software error |
| F01001 | Floating Point Exception |
| F01002 | Internal software error |
| F01003 | Time-out for memory access |
| F01015 | Internal software error |
| F01040 | Back up parameters and perform a POWER ON |
| F01044 | Error in description data |
| F01205 | Time slice overflow |
| F01512 | BICO: No scaling |
| F01662 | Error, internal communications |
| F07901 | Drive: Motor overspeed |
| F30001 | Power unit: Overcurrent |
| F30002 | Power unit: DC-link voltage overvoltage |
| F30003 | Power unit: DC-link voltage undervoltage |
| F30004 | Power unit: Overtemperature heat sink inverter |
| F30005 | Power unit: Overload I2t |
| F30017 | Power unit: Hardware current limit has responded too often |
| F30021 | Power unit: Ground fault |
| F30024 | Power unit: Overtemperature, thermal model |
| F30025 | Power unit: Chip overtemperature |
| F30027 | Power unit: Time monitoring for DC link pre-charging |
| F30036 | Power unit: Overtemperature, inside area |
| F30071 | No new actual values received from the Power Module |
| F30072 | Setpoints can no longer be transferred to the Power Module |
| F30105 | PU: Actual value acquisition error |
| F30662 | Internal communication error |
| F30664 | Fault during power-up |
| F30802 | Power unit: Time slice overflow |
| F30805 | Power unit: EPROM checksum not correct |
| F30809 | Power unit: Switching information invalid |

##### Multi-zone control

Multi-zone control is used to control quantities such as pressure or temperature via the technology setpoint deviation. The setpoints and actual values are fed in via the analog inputs as current (0 … 20 mA) or voltage (0 … 10 V) or as a percentage via temperature-dependent resistances (NI1000 / PT1000, 0° C = 0%; 100° C = 100%).

###### Control variants for multi-zone control

There are three control variants for multi-zone control, which are selected via p31021:

- **One setpoint and one, two or three actual values**

  The actual value for the control can be calculated as mean value, maximum value or minimum value. You can find all of the setting options in the parameter list in parameter p31022.

  - Average value: The deviation from the setpoint of the average value of two or three actual values is controlled.
  - Minimum value: The deviation from the setpoint of the smallest actual value is controlled.
  - Maximum value: The deviation from the setpoint of the highest actual value is controlled.
- **Two setpoint / actual value pairs as maximum value control (cooling)**

  The maximum value control compares two setpoint / actual value pairs and controls the actual value which has the largest deviation upwards from its associated setpoint. No control takes place if both actual values lie below their setpoints.

  In order to avoid frequent changeover, the converter only switches over if the deviation of the controlled setpoint / actual value pair is more than two percent lower than the deviation of the uncontrolled value pair.
- **Two setpoint / actual value pairs as minimum value control (heating)**

  The minimum value control compares two setpoint / actual value pairs and controls the actual value, which has the highest deviation downwards from its associated setpoint. No control takes place if both actual values lie above their setpoints.

  In order to avoid frequent changeover, the converter only switches over if the deviation of the controlled setpoint / actual value pair is more than two percent lower than the deviation of the uncontrolled value pair.

###### Switching from day to night mode

You can modify the setpoints for day and night mode individually. You have the following opportunities to switch from day to night mode:

- Signal via the digital input DI 4
- via p31025 with the aid of free blocks and the real-time clock

> **Note**
>
> If you activate the multi-zone control, the inverter switches its analog inputs as sources for the setpoint and actual value of the technology controller (refer to table).

Parameters to set the multi-zone control:

| Parameter | Description |  |
| --- | --- | --- |
| p2200 | **Technology controller enable** |  |
| p2251 | **Set technology controller as main setpoint** |  |
| P31020 | **Multi-zone control interconnection** (factory setting = 0) A subsequent parameterization is performed by activating or deactivating the multi-zone control. |  |
| Subsequent connection for p31020 = 1 (activate multi-zone control) | Subsequent connection for p31020 = 0 (deactivate multi-zone control) |  |
| p31023[0] = 0755.0 (AI0) p31023[2]  = 0755.1 (AI1) p31026[0] = 0755.2 (AI2) p31026[1] = 0755.3 (AI3) p2253 = 31024 (setpoint output, technology controller) p2264 = 31027 (actual value output, technology controller) | p31023[0] = 0 p31023[2]  = 0 p31026[0] = 0 p31026[1] = 0 p2253 = 0 p2264 = 0 |  |
| P31021 | **Configuration of multi-zone control**   - 0 = Setpoint 1 / several actual values (factory setting) - 1 = Two zones / maximum value setting - 2 = Two zones / minimum value setting |  |
| p31022 | **Processing of actual values for multi-zone control** (only for p31021 = 0) Possible values: 0 … 11 (factory setting = 0) |  |
| p31023[0 … 3] | **Setpoints for multi-zone control** Parameters for selecting the source for setpoints in multi-zone control (factory setting = 0) |  |
| r31024 | **Multi-zone control setpoint output for technology controller**  CO parameters |  |
| p31025 | **Day/night changeover for multi-zone control**  Parameter for selecting the source for day/night changeover of the multi-zone control (factory setting = 0) |  |
| p31026[0 … 2] | **Actual values for multi-zone control**  Parameters for selecting the source for actual values of the multi-zone control (factory setting = 0) |  |
| r31027 | **Multi-zone control actual value output for technology controller** CO parameters |  |

> **Note**
>
> If you deactivate the multi-zone control, the inverter resets the interconnection of its analog inputs to the default setting.

###### Example

In an open plan office, temperature sensors (Lg-Ni1000) are installed in three different places. The converter receives the measured values and temperature setpoint via its analog inputs. Temperature setpoints between 8° C … 30° C are permissible. Overnight, the average temperature should be 16° C.

**Parameter settings**

| Symbol | Meaning |
| --- | --- |
| p2200[0] = 1 | Technology controller enable |
| p2251 = 0 | Technology closed-loop controller as main setpoint |
| p2900[0] = 16 | Temperature setpoint overnight as a fixed percentage value |
| p31020 = 1 | Activate multi-zone control |
| p31021 = 0 | Multi-zone control with one setpoint and three actual values |
| p31022 = 7 | Three actual values, one setpoint. The actual value of the closed-loop control is the average value of three actual values. |
| p31023[0] = 755[0] | Temperature setpoint via analog input AI 0 |
| p0756[0] = 0 | Select analog input type (voltage input 0 … 10 V) |
| p0757[0] = 0 / p0758[0] = 8 | Lower value = 8° C (0 V ≙ 8° C) |
| p0759[0] = 10 / p0760[0] = 30 | Upper value = 30° C (10 V ≙ 30° C) |
| p31023[1] = 2900[0] | Interconnect p31023[1] with the value from p2900 for the reduction overnight |
| p31026[0]= 755.2 | Temperature actual value 1 via analog input 2 as a percentage value |
| p0756[2] = 6 | Analog input type (temperature sensor LG-Ni1000) |
| p0757[2] = 0 / p0758[2] = 0 | Lower value of the scaling characteristic |
| p0759[2] = 100 / p0760[2] = 100 | Upper value of the scaling characteristic |
| p31026[1] = 755[3] | Temperature actual value 2 via analog input 3 as a % |
| p0756[3] = 6 | Select analog input type (temperature sensor LG-Ni1000) |
| p0757[3] = 0 / p0758[3] = 0 | Lower value of the scaling characteristic |
| p0759[3] = 100 / p0760[3] = 100 | Upper value of the scaling characteristic |
| p31026[2] = 755[1] | Temperature actual value 3 via a temperature sensor with current output (0 mA … 20 mA) via analog input AI 1 |
| p0756[1] = 2 | Analog input type (current input 0 … 20 mA) |
| p0757[1] = 0 / p0758[1] = 0 | Lower value of the scaling characteristic (0 mA ≙ 0° C) |
| p0759[1] = 20 / p0760[1] = 100 | Upper value of the scaling characteristic (20 mA ≙ 100%) |
| p31025 = 722[4] | Switchover from day to night using digital input DI 4 |

You will find more information about this multi-zone control in the parameter list and in function diagram 7032 of the List Manual.

##### Cascade control

###### Overiew

![Overiew](images/91492236043_DV_resource.Stream@PNG-de-DE.png)

The cascade control is ideal for applications in which, for example, significantly fluctuating pressures or flow rates are equalized.

![Example: Cascade control for the pressure in a liquid pipe](images/90732591499_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| DM | Speed-controlled motor |
| M1 … M3 | Uncontrolled motors |
| P | Pressure sensor. Interconnect the signal of the pressure sensor with the actual-value input of the technology controller. |

Example: Cascade control for the pressure in a liquid pipe

To deploy the cascade control, you must activate the technology controller.

Depending on the set-actual variance of the technology controller, the cascade control of the converter switches a maximum of three additional motors directly to the line supply via contactors.

###### Activating M1...M3 uncontrolled motors

![Conditions for connecting a motor](images/149911485835_DV_resource.Stream@PNG-en-US.png)

Conditions for connecting a motor

Procedure for connecting an uncontrolled motor:

1. The speed-controlled motor turns with maximum speed p1082.
2. The control deviation of the technology controller is greater than p2373.
3. Time p2374 has expired.

   The converter brakes the speed-controlled motor with ramp-down time p1121 to the activation/deactivation speed p2378. Until the activation/deactivation speed p2378 is attained, the converter deactivates the technology controller temporarily.
4. After switch-on delay p2384, the converter connects an uncontrolled motor.

###### Switching off M1 ... M3 uncontrolled motors

![Conditions for switching off a motor](images/149911548299_DV_resource.Stream@PNG-en-US.png)

Conditions for switching off a motor

Procedure for switching off an uncontrolled motor:

1. The speed-controlled motor turns with minimum speed p1080.
2. The control deviation of the technology controller is less than -p2373.
3. Time p2375 has expired.

   The converter accelerates the speed-controlled motor with ramp-up time p1120 to the activation/deactivation speed p2378. Until the activation/deactivation speed p2378 is attained, the converter deactivates the technology controller temporarily.
4. After shutdown delay p2386, the converter disconnects an uncontrolled motor.

###### Sequence for activating and deactivating the M1 … M3 motors

p2371 specifies the sequence for activating and deactivating the motors

| p2371 | → → → Sequence for activating motors → → → |  |  |  |  |  | Power of the activated M1 … M3 motors compared with the speed-controlled DM motor |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| → → → Sequence for deactivating motors → → → |  |  |  |  |  |  |  |  |  |
| Stage 1 | Stage 2 | Stage 3 | Stage 4 | Stage 5 | Stage 6 | 1 × DM | 2 × DM | 3 × DM |  |
| 1 | M1 |  |  |  |  |  | M1 | --- | --- |
| 2 | M1 | M1+M2 |  |  |  |  | M1, M2 | --- | --- |
| 3 | M1 | M2 | M1+M2 |  |  |  | M1 | M2 | --- |
| 4 | M1 | M1+M2 | M1+M2+M3 |  |  |  | M1, M2, M3 | --- | --- |
| 5 | M1 | M3 | M1+M3 | M1+M2+M3 |  |  | M1, M2 | M3 | --- |
| 6 | M1 | M2 | M1+M2 | M2+M3 | M1+M2+M3 |  | M1 | M2, M3 | --- |
| 7 | M1 | M1+M2 | M3 | M1+M3 | M1+M2+M3 |  | M1, M2 | --- | M3 |
| 8 | M1 | M2 | M3 | M1+M3 | M2+M3 | M1+M2+M3 | M1 | M2 | M3 |

###### Interaction with the "Hibernation mode" function

In order that the "Cascade control" and "Hibernation mode" functions operate together without any conflict, you must make the following settings in the cascade control:

- p2392 < p2373

  The restart value of the hibernation mode (p2392) must be lower than the activation threshold for the cascade control (p2373).
- p2373 < p2376

  The activation threshold for cascade control (p2373) must be lower than the overload threshold for the cascade control (p2376).
- It is not permissible that the main drive is in the hibernation mode.
- The actual speed must be higher than the restart speed for hibernation mode (p1080 + p2390) × 1.05.
- The value for the activation delay of the cascade control (p2374) must be longer than the ramp-up time from hibernation mode (t<sub>y</sub>).

  t<sub>y</sub> = [(p1080 + p2390) × 1.05 × p1120 × p1139] / p1082

###### Setting parameters and activating the cascade control

| Parameter | Description |  |
| --- | --- | --- |
| p2200 | **Technology controller enable** (factory setting: 0)  1: Activate technology controller |  |
| p2251 | **Technology controller mode** (factory setting: 0)  0: Technology controller as main speed setpoint |  |
| p2370 | **Cascade control enable** (factory setting: 0)  1 signal: Cascade control is enabled |  |
| p2371 | **Cascade control configuration** (factory setting: 0)  See also p2372 and the above table. |  |
| p2372 | **Cascade control - motor selection mode** (factory setting: 0)  Specifying the motor connection sequence |  |
| 0: | Fixed procedure as set in p2371 |  |
| 1: | Cascade control after absolute operating hours |  |
| 2: | Automatic replacement after completed operating hours |  |
| 3: | Automatic replacement after absolute operating hours |  |
| p2373 | **Cascade control - activation threshold** (factory setting: 20%) |  |
| p2374 | **Cascade control - activation delay** (factory setting: 30 s) |  |
| p2375 | **Cascade control - deactivation delay** (factory setting: 30 s) |  |
| p2376 | **Cascade control - overload threshold** (factory setting: 25%) |  |
| p2377 | **Cascade control - interlock time** (factory setting: 0 s) |  |
| p2378 | **Cascade control - activation/deactivation speed** (factory setting: 50 %) |  |
| r2379 | **Cascade control - status word** |  |
| .00 | 1 signal = start uncontrolled M1 motor |  |
| .01 | 1 signal = start uncontrolled M2 motor |  |
| .02 | 1 signal = start uncontrolled M3 motor |  |
| .03 | 1 signal = activate motor |  |
| .04 | 1 signal = activation/deactivation active |  |
| .05 | 1 signal = all motors active |  |
| .06 | 1 signal = automatic replacement not possible |  |
| .07 | 1 signal = alarm active |  |
| p2380 | **Cascade control - operating hours** (factory setting: 0 h) |  |
| [00] | M1 motor |  |
| [01] | M2 motor |  |
| [02] | M3 motor |  |
| p2381 | **Cascade control - maximum time for continuous mode** (factory setting: 24 h)  Time limit for continuous uninterrupted operation of uncontrolled motors |  |
| p2382 | **Cascade control - absolute operating time limit** (factory setting: 24 h)  Limit for the total operating time of the uncontrolled motors |  |
| p2383 | **Cascade control - deactivation sequence** (factory setting: 0) |  |
| 0: | Normal stop |  |
| 1: | Sequential stop:  For OFF1, the converter deactivates the motors in the following sequence:  M3 → M2 → M1 → controlled motor  p2387 is the time between the deactivations. |  |
| p2384 | **Cascade control - motor switch-on delay** (factory setting: 0 s) |  |
| p2385 | **Cascade control - stop time activation speed** (factory setting: 0 s) |  |
| p2386 | **Cascade control - motor deactivation delay** (factory setting: 0 s) |  |
| p2387 | **Cascade control - stop time deactivation speed** (factory setting: 0 s)  See p2383 |  |

For more information, see the parameter descriptions and function diagram 7036 in the List Manual.

##### Bypass

###### Function

![Function](images/156535507211_DV_resource.Stream@PNG-en-US.png)

The "Bypass" function switches the motor between converter and line operation. The "Bypass" function is supported only for induction motors.

![Bypass with control via the converter](images/120131241995_DV_resource.Stream@PNG-en-US.png)

Bypass with control via the converter

Requirements placed on the K1 converter contactor and K2 line contactor:

- K1 and K2 are designed for switching under load.
- K2 is designed for switching an inductive load.
- K1 and K2 are interlocked against closing at the same time.

###### Switching between converter operation and line operation

**Switching from converter operation to line operation**

1. The converter switches the motor OFF.
2. The converter opens the K1 converter contactor via a digital output.
3. The converter waits for the unlocking time of the motor.
4. The converter waits for the feedback that the K1 converter contactor is open.
5. The converter closes the K2 line contactor via a digital output.

The motor is now operated directly on the line supply. A multiple of the motor rated current can flow before the motor speed has reached the line frequency.

**Switching from line operation to converter operation**

1. The converter opens the K2 line contactor via a digital output.
2. The converter waits for the unlocking time of the motor.
3. The converter waits for the feedback that the K2 line contactor is open.
4. The converter closes the K1 converter contactor via a digital output.
5. The converter switches the motor ON.
6. The converter adjusts with the "Flying restart" function its output frequency to the speed of the motor.

The motor is now operated on the converter.

**How is the changeover triggered?**

The following options are provided to switch between converter operation and line operation:

- Changeover for activation via a control command
- Changeover depending on the speed

###### Changeover for activation via a control command

![Changeover when activating via a control signal (p1267.0 = 1)](images/156535425419_DV_resource.Stream@PNG-en-US.png)

Changeover when activating via a control signal (p1267.0 = 1)

The converter switches the motor between converter operation and line operation depending on the bypass control command p1266.

###### Changeover depending on the speed

With this function, changeover to line operation is realized corresponding to the following diagram, if the setpoint lies above the bypass threshold.

![Changeover depending on the speed (p1267.1 = 1)](images/156535430539_DV_resource.Stream@PNG-en-US.png)

Changeover depending on the speed (p1267.1 = 1)

If the speed setpoint r1119 lies above the bypass speed threshold p1265, the converter switches the motor to line operation.

If the speed setpoint falls below the bypass speed threshold, the converter switches the motor to converter operation.

###### Interaction with other functions

- Flying restart

  The "Flying restart" function must be activated for the "Bypass" function (p1200 = 1 or 4).

  ![Interaction with other functions](images/109220677643_DV_resource.Stream@PNG-de-DE.png)
  [Flying restart – switching on while the motor is running](#flying-restart-switching-on-while-the-motor-is-running)
- Emergency operation

  The activated "Essential service mode" function influences the "Bypass" function.

  ![Interaction with other functions](images/109220677643_DV_resource.Stream@PNG-de-DE.png)
  [Essential service mode](#essential-service-mode)
- Converter control

  For operation of the motor on the line supply, the converter no longer responds to the OFF1 command, but rather only to OFF2 and OFF3.
- Temperature monitoring for the motor

  The converter evaluates the temperature sensor in the motor, also for line operation of the motor.

  ![Interaction with other functions](images/109220677643_DV_resource.Stream@PNG-de-DE.png)
  [Motor protection with temperature sensor](#motor-temperature-monitoring-using-a-temperature-sensor-ip20)
- Disconnecting the converter from the line supply

  If for line operation of the motor, you disconnect the converter from the line supply, the converter opens the K2 contactor and the motor coasts down.

  To operate the motor on the line supply also for deactivated converter, the higher-level control must supply the signal for the K2 line contactor.

###### Setting parameters of the bypass function

| Parameter | Description |  |
| --- | --- | --- |
| p0347 | **Motor de-excitation time** |  |
| p1260 | **Bypass configuration** (factory setting: 0)  0: Bypass is deactivated  3: Bypass is activated |  |
| r1261 | **Bypass control/status word** |  |
| .00 | 1 signal: Close K1 converter contactor command |  |
| .01 | 1 signal: "Close K2 converter contactor" command |  |
| .05 | 1 signal: "K1 converter contactor is closed" feedback |  |
| .06 | 1 signal: "K2 line contactor is closed" feedback |  |
| .07 | 1 signal: Bypass command (for p1266) is active |  |
| .10 | 1 signal: Bypass in the process operation is active |  |
| .11 | 1 signal: Bypass is enabled |  |
| p1262 | **Bypass dead time** (factory setting: 1 s)  Changeover time of the contactor. Setting condition: p1262 > p0347 |  |
| p1263 | **Bypass delay time** (factory setting: 1 s)  Delay time for switching from line operation to converter operation. |  |
| p1264 | **Bypass delay time** (factory setting: 1 s)  Delay time for switching from converter operation to line operation. |  |
| p1265 | **Bypass speed threshold** (factory setting: 1480 rpm)  Speed threshold for switching to line operation. |  |
| p1266 | **BI: Bypass control command** (factory setting: 0)  Signal source for the "Bypass" function control command |  |
| p1267 | **Bypass changeover source configuration** (factory setting: 0000 bin)  Changeover to bypass mode via the speed threshold or the control signal. |  |
| .00 | 1 signal: Changeover for activation via the control command p1266 |  |
| .01 | 1 signal: Bypass when reaching the speed threshold |  |
| p1269 | **BI: Bypass switch feedback**   Signal source for contactor feedback of the contactor. |  |
| [00] | K1 converter contactor (factory setting: 1261.0) |  |
| [01] | K2 line contactor (factory setting: 1261.1) |  |
| p1274 | **Bypass switch monitoring time** (factory setting: 1000 ms)  Setting the monitoring time of the bypass contactor. Monitoring is deactivated for p1274 = 0 ms. |  |
| [00] | K1 converter contactor |  |
| [01] | K2 line contactor |  |

For more information, see the parameter descriptions and function diagram 7035 in the List Manual.

##### Hibernation

![Figure](images/91486048267_DV_resource.Stream@PNG-de-DE.png)

The hibernation mode saves energy, reduces mechanical wear and noise.

Pressure and temperature controls involving pumps and fans are typical applications for the hibernation mode.

###### Function

If the plant/system conditions permit it, the converter switches off the motor and switches it on again when there is a demand from the process.

The hibernation mode starts as soon as the motor speed drops below the hibernation mode start speed. The converter switches off the motor after an adjustable time. If, during this time, the speed setpoint increases above the hibernation mode start speed due to pressure or temperature changes, the converter exits the hibernation mode.

In the hibernation mode the motor is switched off, but the converter continues to monitor the speed setpoint or technology controller deviation.

- **For an external setpoint input (without technology controller), the converter monitors the speed setpoint** and switches on the motor again as soon as the setpoint increases above the restart speed.

  In the factory setting, the converter monitors the positive speed setpoint. The converter switches on the motor as soon as the setpoint exceeds the restart speed.

  If you also want to monitor the negative speed setpoint, you have to monitor the setpoint amount. To do this, set p1110 = 0.

Additional setting options are described in the List Manual, in function diagrams 3030 and 3040 as well as in the associated parameter descriptions.

- **When the setpoint is input from the technology controller, the converter monitors the technology controller deviation (r2273)** and switches on the motor again if the deviation of the technology controller exceeds the hibernation mode restart value (p2392).

  In the factory setting, the converter monitors the positive deviation of the technology controller. The converter switches on the motor as soon as the technology controller deviation is higher than the hibernation mode restart value (p2392).

  You must monitor the absolute value of the deviation to switch on the motor again for a negative technology controller deviation.

  Set p2298 = 2292 and set the minimum threshold in p2292.

> **Note**
>
> **Hibernation mode after switching on the converter**
>
> After switching the converter on, a wait time starts in the converter. The longest wait time is at the following times:
>
> - p1120 (ramp-up time)
> - p2391 (hibernation mode delay time)
> - 20 s
>
> If the motor does not reach the hibernation mode start speed within this wait time, the converter activates the hibernation mode and switches off the motor.

Additional setting options are provided in the List Manual in function block diagram 7038 and in the associated parameter descriptions.

If you want to prevent frequent activation and deactivation, before deactivation you still have to set a short speed boost. The boost is deactivated with p2394 = 0.

To avoid tank deposits, particularly where liquids are involved, it is possible to exit the hibernation mode after an adjustable time (p2396) has expired and switch to normal operation.

The settings required for the respective variant can be found in the following tables.

###### Interaction of the function with the cascade control

It is not possible to activate the hibernation mode as long as a motor is directly operated from the line supply using the cascade control function.

![Interaction of the function with the cascade control](images/109220677643_DV_resource.Stream@PNG-de-DE.png)
[Cascade control](#cascade-control)

###### Activating the hibernation mode with setpoint input via the internal technology controller

With this operating mode you have to set the technology controller as the setpoint source (p2200) and use the output of the technology controller as the main setpoint (p2251). The boost can be deactivated.

![Hibernation mode using the technology setpoint as main setpoint with boost](images/108413062027_DV_resource.Stream@PNG-en-US.png)

Hibernation mode using the technology setpoint as main setpoint with boost

###### Activating the hibernation mode with external setpoint input

With this operating mode, an external source – e.g. a temperature sensor – inputs the main setpoint.

![Hibernation mode using an external setpoint with boost](images/64606966795_DV_resource.Stream@PNG-en-US.png)

Hibernation mode using an external setpoint with boost

![Hibernation mode using an external setpoint without boost](images/64608814859_DV_resource.Stream@PNG-en-US.png)

Hibernation mode using an external setpoint without boost

###### Setting the hibernation mode

| Parameter | Description | Via tech. setpoint | Via external setpoint |
| --- | --- | --- | --- |
| p1080 | **Minimum speed** 0 (factory setting) … 19,500 rpm. Lower limit of the motor speed, independently of the speed target value. | ✓ | ✓ |
| p1110 | **Block negative direction** Parameter to block the negative direction | **-** | ✓ |
| p2200 | **Technology controller enable**   0: Technology controller deactivated (factory setting),  1: Technology controller activated | ✓ | **-** |
| p2251 = 1 | **Technology controller mode**   0: Technology controller as main setpoint (factory setting),  1: Technology controller as supplementary setpoint | ✓ | **-** |
| p2292 | **Technology controller minimum limiting** Parameter for the minimum limiting of the technology controller | ✓ | **-** |
| p2398 | **Hibernation mode**  0: Hibernation mode inhibited (factory setting) 1: Hibernation mode enabled | ✓ | ✓ |
| p2390 | **Hibernation mode start speed**  0 (factory setting) … 21,000 rpm. As soon as this speed is fallen below, the hibernation mode delay time starts and switches off the motor once it expires. The hibernation mode start speed is calculated as follows: Start speed = p1080 + p2390 p1080 = minimum speed  p2390 = hibernation mode start speed | ✓ | ✓ |
| p2391 | **Hibernation mode delay time**   0 ... 3599 s (factory setting 120). The hibernation mode delay time starts as soon as the output frequency of the converter drops below the hibernation mode start speed p2390. If the output frequency increases above this threshold during the delay time, the hibernation mode delay time is interrupted. Otherwise, the motor is switched off after the delay time has expired (if necessary, after a short boost). | ✓ | ✓ |
| p2392 | **Hibernation mode restart value (as a %)** Is required if the technology controller is used as the main setpoint.   As soon as the technology controller deviation (r2273) exceeds the hibernation restart value, the converter switches to normal operation and the motor starts up with a setpoint of 1.05 * (p1080 + p2390). As soon as this value is reached, the motor continues to operate with the setpoint of the technology controller (r2260). | ✓ | **-** |
| p2393 | **Hibernation mode restart speed (rpm)** Required for external setpoint input. The motor starts as soon as the setpoint exceeds the restart speed. The restart speed is calculated as follows: Restart speed = p1080 + p2390 + p2393  p1080 = minimum speed  p2390 = hibernation mode start speed p2393 = hibernation mode restart speed | **-** | ✓ |
| p2394 | **Hibernation mode boost duration** 0 (factory setting) … 3599 s. Before the converter switches over into the hibernation mode, the motor is accelerated for the time set in p2394 according to the acceleration ramp, however, as a maximum to the speed set in p2395. | ✓ | ✓ |
| p2395 | **Hibernation mode boost speed**  0 (factory setting) … 21,000 rpm. Before the converter switches over to hibernation mode, the motor is accelerated for the time set in p2394 along the acceleration ramp, but not to more than the speed set in p2395.    **Caution:** The boost may not result in any overpressure or overrun. | ✓ | ✓ |
| p2396 | **Maximum hibernation mode shutdown time** 0 (factory setting) to 863,999 s. At the latest when this time expires, the converter switches to normal operation and accelerates up to the start speed (p1080 + p2390). If the converter is switched to normal operation in advance, the shutdown time is reset to the value set in this parameter.  With p2396 = 0, automatic changeover to normal operation after a certain time is deactivated. | ✓ | ✓ |

> **Note**
>
> Activate the motorized potentiometer as ramp-function generator to use the motorized potentiometer of the converter as setpoint for the hibernation mode.
>
> - Motorized potentiometer: p1030.4 = 1
> - Technology motorized potentiometer: p2230. = 1.

###### Status of the hibernation mode

| Parameter | Description |
| --- | --- |
| r2273 | **Display of the setpoint/actual value deviation of the technology controller** |
| r2397 | **Actual hibernation mode output speed**  Actual boost speed before the pulses are inhibited or the actual start speed after restart. |
| r2399 | **Hibernation mode status word**  00 Hibernation mode enabled (p2398 <> 0) 01 Hibernation mode active  02 Hibernation mode delay time active  03 Hibernation mode boost active  04 Hibernation mode motor switched off  05 Hibernation mode motor switched off, cyclic restart active 06 Energy-saving mode motor restarts  07 Hibernation mode supplies the total setpoint of the ramp-function generator 08 Hibernation mode bypasses the ramp-function generator in the setpoint channel |

### Technology

This section contains information on the following topics:

- [Basic positioner and position control](#basic-positioner-and-position-control)
- [Permissible encoder combinations](#permissible-encoder-combinations)

#### Basic positioner and position control

This section contains information on the following topics:

- [Basic positioner and position control](#basic-positioner-and-position-control-1)
- [Commissioning sequence](#commissioning-sequence)
- [Normalize the encoder signal](#normalize-the-encoder-signal)
- [Limiting the positioning range](#limiting-the-positioning-range)
- [Setting the position controller](#setting-the-position-controller)
- [Setting the monitoring functions](#setting-the-monitoring-functions)
- [Referencing](#referencing)
- [Jog](#jog)
- [Traversing blocks](#traversing-blocks)
- [Direct setpoint specification (MDI)](#direct-setpoint-specification-mdi)

##### Basic positioner and position control

###### Overview

![Overview](images/103426195851_DV_resource.Stream@PNG-en-US.png)

Position control means controlling the position of an axis. An "axis" is a machine or system component that comprises the converter with active position control and the driven mechanical system.

The basic positioner (EPOS) calculates the traversing profile for the time-optimized traversing of the axis to the target position.

![Basic positioner and position control](images/103426191243_DV_resource.Stream@PNG-en-US.png)

Basic positioner and position control

| Symbol | Meaning |
| --- | --- |
| The basic positioner has the following operating modes: |  |
| - Direct setpoint specification (MDI): | The external control specifies the position setpoint for the axis. |
| - Traversing block selection: | Position setpoints are saved in different traversing blocks in the converter. The external control selects a traversing block. |
| - Homing: | Homing establishes the reference of the position measurement in the converter to the machine. |
| - Jogging: | This function is used to incrementally traverse the axis (Set up). |
| - Travel to fixed stop: | The converter positions the axis with a defined torque against a mechanical fixed stop. |

##### Commissioning sequence

The screen forms to commission the basic positioner in Startdrive essentially have the same structure. Commissioning using Startdrive is described in this manual.

|  |  |  |
| --- | --- | --- |
| ![Figure](images/96416764427_DV_resource.Stream@PNG-en-US.png) |  |  |
|  |  |  |
|  |  |  |
| ① | Assign encoders to the axes.  → Operating instructions |  |
|  |  |  |
| ② | Set the communication via the fieldbus.    ![Figure](images/90957697291_DV_resource.Stream@PNG-de-DE.png) |  |
|  |  |  |
| ③ | Optimize the speed control  → Operating instructions |  |
|  |  |  |
| ④ | ![Figure](images/90957697291_DV_resource.Stream@PNG-de-DE.png) [Normalizing the encoder signal](#normalize-the-encoder-signal) |  |
|  |  |  |
| ⑤ | ![Figure](images/90957697291_DV_resource.Stream@PNG-de-DE.png) [Limiting the positioning range](#limiting-the-positioning-range) |  |
|  |  |  |
| ⑥ | ![Figure](images/90957697291_DV_resource.Stream@PNG-de-DE.png) [Setting the position controller](#setting-the-position-controller) |  |
|  |  |  |
| ⑦ | ![Figure](images/90957697291_DV_resource.Stream@PNG-de-DE.png)  [Setting the monitoring functions](#setting-the-monitoring-functions) |  |
|  |  |  |
| ⑧ | ![Figure](images/90957697291_DV_resource.Stream@PNG-de-DE.png) [Referencing](#referencing) |  |
|  |  |  |
| ⑨ | ![Figure](images/90957697291_DV_resource.Stream@PNG-de-DE.png) [Jogging](#jog) |  |
|  |  |  |
| ⑩ | ![Figure](images/90957697291_DV_resource.Stream@PNG-de-DE.png) [Traversing blocks](#traversing-blocks) |  |
|  | or |  |
|  | ![Figure](images/90957697291_DV_resource.Stream@PNG-de-DE.png) [Direct setpoint input (MDI)](#direct-setpoint-specification-mdi) |  |

---

**See also**

[Encoder](Running%20through%20the%20wizard.md#encoder)
  
[Using a higher-level controller](Configuring%20SINAMICS%20G120-G115D-G110M%20drives.md#using-a-higher-level-controller)
  
[Define the resolution](#define-the-resolution)
  
[Optimizing the position controller](#optimizing-the-position-controller)
  
[Standstill and positioning monitoring](#standstill-and-positioning-monitoring)
  
[Referencing methods](#referencing-methods)
  
[Traversing blocks](#traversing-blocks-1)

##### Normalize the encoder signal

This section contains information on the following topics:

- [Define the resolution](#define-the-resolution)
- [Modulo range setting](#modulo-range-setting)
- [Read actual position value](#read-actual-position-value)
- [Setting the backlash](#setting-the-backlash)

###### Define the resolution

###### Path unit (LU): The resolution of the actual position value in the converter

The converter calculates the actual position value of the axis using the neutral position unit LU (length unit). The path unit LU is independent of whether the converter controls, e.g. the position of an elevating platform or the angle of a rotary table.

Firstly, for your application define the required resolution. In other words: Which distance or which angle must the path unit LU correspond to?

The following rules apply when selecting the path unit LU:

1. The higher the resolution of the path unit LU, the higher the accuracy of the position control.
2. If you select a resolution that is too high, then the converter cannot represent the actual position value over the complete axis traversing range. The converter responds with a fault in the case of an overflow when representing the number.
3. The resolution of the path unit LU must be less than the maximum resolution that is obtained from the resolution of the position encoder.

###### Procedure

- Go online with Startdrive .
- Select the "Mechanical system" screen:

  ![Procedure](images/127715039755_DV_resource.Stream@PNG-en-US.png)
- ① Enable the settings so they can be edited:
- ②, ③ Enter the gear ratio of the axis:
- **Unknown gear ratio**If you do not know the gear ratio, then you must measure it, for example, by manually rotating the motor and counting the load revolutions.  
  Example: After 5 motor revolutions, the load has turned through 37°. The ratio is therefore 37° / (5 × 360°). You must then enter the following values in Startdrive:

  - ② 37 [load revolution]
  - ③ 1800 [motor revolution]
- For your particular application, define the required resolution, e.g. 1 LU ≙ 1 µm or 1 LU ≙ 1/1000° (1 millidegree).
- Startdrive shows the maximum resolution based on your encoder data. Check whether the required resolution is less than the maximum resolution. If this is not the case, you must reduce the required resolution or use another encoder.
- Calculate:   
  Value = 360° / required resolution, e.g. 360°/ 0.1° = 3600.   
  ④ Enter this value into Startdrive.

Parameters for this function

| Parameter | Meaning |  |
| --- | --- | --- |
| p2502 | Encoder assignment |  |
| 0 | No encoder |  |
| 1 | Encoder 1 |  |
| 2 | Encoder 2 |  |
| p2503 | Length unit LU per 10 mm |  |
| p2504 | Motor/load motor revolutions |  |
| p2505 | Motor/load load revolutions |  |
| p2506 | Length unit LU per load revolution |  |

###### Modulo range setting

###### Description

**Linear axis**

A linear axis is an axis whose traversing range is limited in both motor directions of rotation by the mechanical system of the machine, e.g.:

|  |  |  |
| --- | --- | --- |
| - Stacker crane - Elevating platform - Tilting station - Gate/door drive |  | ![The converter maps the complete traversing range to the actual position value.](images/103426323595_DV_resource.Stream@PNG-en-US.png)   The converter maps the complete traversing range to the actual position value. |

**Modulo axis**

A modulo axis is an axis with an infinite traversing range, e.g.:

|  |  |  |
| --- | --- | --- |
| - Rotary table - Conveyor belt - Roller conveyor |  | ![The converter maps the modulo range on the actual position value. If the load position leaves the modulo range, then the value range of the actual position value repeats in the converter.](images/103426353803_DV_resource.Stream@PNG-en-US.png)   The converter maps the modulo range on the actual position value. If the load position leaves the modulo range, then the value range of the actual position value repeats in the converter. |

###### Procedure

- Go online with Startdrive .
- Select the "Mechanical system" screen:

  ![Procedure](images/110435259275_DV_resource.Stream@PNG-en-US.png)
- ①
  ② If you are using a modulo axis in your application, define the modulo range and specify the modulo correction.   
  Example 1: In the case of a rotary table, one load revolution corresponds to 3600 LU. In this case, the modulo correction is also 3600.   
  Example 2: For a roller conveyor, 100 motor revolutions corresponds to one production cycle. For a resolution of 3600 LU per motor revolution, the modulo range is 360000 LU.

Parameters for this function

| Parameter | Meaning |
| --- | --- |
| p2576 | Modulo offset, modulo range |
| p2577 | Modulo correction activation (signal = 1) |
| r2685 | Offset value |

###### Read actual position value

After normalization of the encoder signal you should check the actual position value.

###### Procedure

- Go online with Startdrive .
- Select the screen form for Actual value processing:

  ![Procedure](images/127701870091_DV_resource.Stream@PNG-en-US.png)
- Check the following:

  - There must be no overflow of the actual position value in the entire traverse range. The converter can show as a maximum the value range of -2147483648 … 2147483647. If this maximum value is exceeded, the converter reports fault F07493.
  - If you have defined a modulo range, the converter resets the actual position value after passing through the range.

Parameters for this function

| Parameter | Meaning |
| --- | --- |
| r2521[0] | Actual position value for position control |

###### Setting the backlash

###### Description

Backlash (also called play, dead travel on reversing, etc.) is the distance or the angle that a motor must travel through when the direction of rotation reverses until the axis actually moves in the other direction.

![Backlash in a spindle](images/103426551051_DV_resource.Stream@PNG-en-US.png)

Backlash in a spindle

With the appropriate setting, the converter corrects the positioning error caused by the backlash when reversing.

The converter corrects the backlash under the following condition:

- For an incremental encoder, the axis must be homed.  
  See also Section: [Referencing](#referencing).
- For an absolute encoder, the axis must be adjusted.   
  See also Section: [Absolute encoder adjustment](#absolute-encoder-adjustment).

###### Procedure

**Measuring backlash**

![Measuring backlash](images/103426555659_DV_resource.Stream@PNG-en-US.png)

Measuring backlash

1. Move the axis to position A in the machine. Mark this position in the machine and note down the actual position value in the converter, see also Section: [Read actual position value](#read-actual-position-value).
2. Move the axis a little bit more in the same direction.
3. Move the axis in the opposite direction until the actual position value in the converter shows the same value as at position A. Due to the backlash when reversing, the axis is now at position B.
4. Measure the position difference Δ = A - B in the machine.

**Correcting backlash**

- Select the "Mechanical system" screen:

  ![Procedure](images/127702551307_DV_resource.Stream@PNG-en-US.png)
- Set the backlash in Startdrive :

  - If the axis has not traveled far enough, then set a positive backlash.
  - If the axis has traveled too far, then set a negative backlash.

Parameters for this function

| Parameter | Meaning |
| --- | --- |
| p2583 | Backlash compensation |
| r2685 | Offset value |

##### Limiting the positioning range

###### Description

**Positioning range for linear axes**

The converter limits the positioning range of a linear axis using a software limit switch. The converter only accepts position setpoints that lie within the software limit switches.

![Limiting the positioning range of a linear axis](images/103426591115_DV_resource.Stream@PNG-en-US.png)

Limiting the positioning range of a linear axis

In addition, using its digital inputs, the converter evaluates signals from STOP cams. When passing a STOP cam, the converter responds - depending on the setting - either with a fault or an alarm.

**Fault as response**

When passing the STOP cam, the converter brakes the axis at the OFF3 ramp-down time, switches the motor off, and reports fault F07491 or F07492. To switch the motor on again, you must do the following:

- Switch the motor off (OFF1).
- Acknowledge the fault.
- Move the axis away from the STOP cam, e.g. using the jogging function.

**Alarm as response**

- When passing the STOP cam, the converter brakes the axis with the maximum deceleration (see Section: [Limiting the traversing profile](#limiting-the-traversing-profile)), maintains the axis in closed-loop control and outputs alarm A07491 or A07492. In order to bring the axis back into the valid traversing range, you must move the axis from the STOP cam, e.g. using the jogging function.

###### Procedure

- Select the "Limit" -> "Traversing range limitation" screen:

  ![Procedure](images/127715191307_DV_resource.Stream@PNG-en-US.png)
- ① Enable the software limit switch.
- ②, ③ Move the axis to the respective limit switch position in your machine. Set the position of the software limit switches to the respective actual position value.
- ④ Enable the STOP cams.
- ⑤, ⑥ Interconnect the signals of the STOP cams with the corresponding signals of your machine.  
  Signal = 0 means an active STOP cam.

Parameters for this function

| Parameter | Meaning |
| --- | --- |
| p2568 | STOP cam activation |
| p2569 | STOP cam, minus |
| p2570 | STOP cam, plus |
| p2578 | Software limit switch, minus signal source |
| p2579 | Software limit switch, plus signal source |
| p2580 | Software limit switch, minus |
| p2581 | Software limit switch, plus |
| p2582 | Software limit switch activation |
| r2683.6 | Software limit switch, minus actuated |
| r2683.7 | Software limit switch, plus actuated |
| r2684.13 | STOP cam minus active |
| r2684.14 | STOP cam plus active |

##### Setting the position controller

This section contains information on the following topics:

- [Precontrol and gain](#precontrol-and-gain)
- [Optimizing the position controller](#optimizing-the-position-controller)
- [Limiting the traversing profile](#limiting-the-traversing-profile)

###### Precontrol and gain

###### Preconditions and constraints

Before you optimize the position controller, the closed-loop drive speed control must be optimally set, see also Section: [Motor control](#motor-control).

Dynamic response and accuracy of the closed-loop position control depend heavily on the lower-level closed-loop or open-loop control or the motor speed:

- Position control in connection with an optimally set vector control with speed encoder provides the best results.
- Position control with vector control without encoder (sensorless vector control) provides satisfactory results for most applications. We recommend that you use a speed encoder for hoisting/lifting applications.
- If you operate the position control with the V/f control of drive, then you must take into account some significant reduction in closed-loop control performance and precision.

  > **Note**
  >
  > **Position controllers in hoisting gear**
  >
  > V/f control is not suitable for vertical axes, such as elevating platforms or hoisting gear used in high-bay racking units, because the axis generally cannot reach the target position as a result of the limited precision of the V/f control.

###### Description

![Position controller with precontrol  Precontrol](images/103426719243_DV_resource.Stream@PNG-en-US.png)

Position controller with precontrol

If the speed control of the converter has an encoder to feedback the actual speed, then deactivate the integral component T<sub>N</sub> of the position controller.

If you use the position control together with the encoderless vector control (SLVC, SensorLess Vector Control) then you must activate the integral time. For SLVC, the integral time significantly improves the positioning accuracy.

###### Optimizing the position controller

To assess the control performance of the position controller, you must move the axis with the position control and assess the control performance e.g. via the timing of the following error.

###### Optimizing the position controller

**Procedure**

1. Adjust the proportional gain.
2. Adjust the integral time.

   ![Optimizing the position controller](images/127718792459_DV_resource.Stream@PNG-en-US.png)
3. Set the precontrol of the position controller to 100 %.

   ![Optimizing the position controller](images/127718797195_DV_resource.Stream@PNG-en-US.png)

   You have optimized the position controller.  
   ❒

| Parameter | Meaning |
| --- | --- |
| p2534 | **Speed precontrol factor** |
| p2538 | **Proportional gain / Kp** |
| p2539 | **Integral time / Tn** |
| p2731 | **Signal = 0: activate position controller** |

###### Advanced settings

If you permanently activate the integral time of the position controller, the characteristics of the position control change as follows:

- The following error during positioning goes to zero.
- When positioning the axis, it tends to overshoot. This means that the axis briefly moves beyond the target position.

###### Limiting the traversing profile

###### Description

The traversing profile is the acceleration, velocity and position characteristics of an axis when being positioned.

You can influence the traversing profile by limiting velocity, acceleration or jerk (= change of the acceleration over time).

![Example: Effect of jerk limitation   Jerk limiting](images/103426840843_DV_resource.Stream@PNG-en-US.png)

Example: Effect of jerk limitation

If the axis must traverse more slowly or must accelerate at a lower rate or "softly", then you must set the relevant limits to lower values. The lower that one of the limits is, the longer the converter needs to position the axis.

###### Setting the traversing profile limitation

**Requirement**

You have selected the "Limit" screen and the "Traversing profile limitation" tab.

**Procedure**

![Setting the traversing profile limitation](images/127721438347_DV_resource.Stream@PNG-en-US.png)

1. Set the maximum velocity with which the converter may position the axis.
2. Set the maximum acceleration.
3. Set the maximum delay.

   The "override" in the traversing blocks or for the direct setpoint input refers to the values ② and ③.
4. Reduce the maximum jerk, if you require softer acceleration and braking.
5. For permanent jerk limiting, set this signal to 1.

You have now set the limitation of the traversing profile.  
❒

Parameters for this function

| Parameter | Meaning |
| --- | --- |
| p2571 | **Maximum velocity** |
| p2572 | **Maximum acceleration** |
| p2573 | **Maximum deceleration** |
| p2574 | **Jerk limitation** |
| p2575 | **Activating jerk limiting**  1 signal: Jerk limiting is active |

##### Setting the monitoring functions

This section contains information on the following topics:

- [Standstill and positioning monitoring](#standstill-and-positioning-monitoring)
- [Following error monitoring](#following-error-monitoring)
- [Cam sequencer](#cam-sequencer)

###### Standstill and positioning monitoring

###### Description

As soon as the setpoint for the position within a positioning operation no longer changes, then the converter sets the "Setpoint stationary" signal to 1. With this signal, the converter starts to monitor the position actual value:

- As soon as the axis has reached the positioning window, the converter signals that the target has been reached, and maintains the axis in closed-loop control.
- If the axis does not come to a standstill within the standstill monitoring time, the converter reports fault F07450.
- If the axis does not enter the positioning window within the positioning monitoring time, the converter reports fault F07451.

  ![Standstill monitoring and positioning monitoring](images/111268856843_DV_resource.Stream@PNG-en-US.png)

  Standstill monitoring and positioning monitoring

###### Setting standstill monitoring and positioning monitoring

**Requirement**

You have selected the "Monitoring" screen and the "Position monitoring" tab.

**Procedure**

![Setting standstill monitoring and positioning monitoring](images/127718899723_DV_resource.Stream@PNG-en-US.png)

1. Set the required positioning accuracy.
2. Set the time within which the axis must be positioned.
3. Set the required standstill window.

   The standstill window must be larger than the positioning window.
4. Set the time within which the axis must be at standstill.
5. Define the signal "Target position reached" as a message to a higher-level control.

You have now set the standstill and position monitoring.  
❒

Parameters for this function

| Parameter | Meaning |
| --- | --- |
| p2542 | Standstill window (target position ±p2542) |
| p2543 | Standstill monitoring time |
| p2544 | Positioning window (target position ±p2544) |
| p2545 | Positioning monitoring time |

###### Following error monitoring

###### Description

The following error is the deviation between the position setpoint and the position actual value while the converter is positioning the axis.

![Monitoring the following error](images/111292475019_DV_resource.Stream@PNG-en-US.png)

Monitoring the following error

The converter reports fault F07452 if the following error is too high. If you set the tolerance to 0, monitoring is deactivated.

###### Setting following error monitoring

**Requirement**

You have selected the "Monitoring" screen and the "Following error monitoring" tab.

**Procedure**

![Setting following error monitoring](images/127758552075_DV_resource.Stream@PNG-en-US.png)

1. Set the monitoring window.

   Start with the factory setting value.

   Test your setting by positioning the axis at maximum velocity, e.g. from the control panel. If the converter stops the travel with fault F07452 , you will need to either increase the monitoring window or increase the dynamics of the position controller.
2. If you want to evaluate the message in your higher-level control, interconnect this signal with, for example, a status bit in the fieldbus telegram.

You have now set the monitoring of the following error.

❒

| Parameter | Meaning |
| --- | --- |
| p2546 | **Dynamic following error monitoring tolerance** |
| r2563 | **Following error, dynamic model** |

###### Cam sequencer

###### Description

The converter compares the position actual value with two different positions and therefore simulates two independent cam switching signals.

![Description](images/127716221707_DV_resource.Stream@PNG-en-US.png)

Set the cam switching position to match your particular application and interconnect the cam switching signal appropriately.

Parameters for this function

| Parameter | Meaning |
| --- | --- |
| p2547 | **Cam switching position 1** |
| p2548 | **Cam switching position 2** |
| r2683.8 | **Position actual value <= cam switching position 1** |
| r2683.9 | **Position actual value <= cam switching position 2** |

##### Referencing

This section contains information on the following topics:

- [Referencing methods](#referencing-methods)
- [Setting the reference point approach](#setting-the-reference-point-approach)
- [Setting the flying referencing](#setting-the-flying-referencing)
- [Set reference point](#set-reference-point)
- [Absolute encoder adjustment](#absolute-encoder-adjustment)

###### Referencing methods

###### Overview

If you are using an incremental encoder for the position actual value, after the supply voltage is switched off, the converter loses its valid position actual value. After the supply voltage is switched on again, the converter no longer knows the reference of the axis position to the machine.

Referencing re-establishes the reference between the zero point of the position calculated in the converter and the machine zero point.

Absolute encoders retain their position information, even after the supply has been switched off.

The converter offers various ways of referencing the axis:

- Reference point approach - only with incremental encoders
- Flying referencing - with all encoder types
- Set reference point - with all encoder types
- Absolute encoder adjustment - with absolute encoders

**Reference point approach**

The converter automatically traverses the axis to a defined reference point.

| Symbol | Meaning |
| --- | --- |
| Example: A workpiece must be positioned at a starting point before machining starts. | ![Overview](images/103427125387_DV_resource.Stream@PNG-en-US.png) |

**Flying referencing**

The converter corrects its position actual value while traversing and reduces errors, e.g. caused by wheel slip or a gear ratio that has not been precisely set.

Example: A pallet on a roller conveyor must be stopped at a specific position. However, the exact position of the pallet on the conveyor is only known when a sensor is passed.

![Positioning an item to be transported on a roller conveyor](images/111293930763_DV_resource.Stream@PNG-en-US.png)

Positioning an item to be transported on a roller conveyor

**Set the reference point and adjust the absolute encoder**

The converter takes the reference point coordinate as the new axis position.

###### Setting the reference point approach

###### Description

A reference point approach generally consists of the following three steps:{"Reference point approach"}

1. Travel to reference cam.

   When it receives a signal, the axis searches for the reference cam in a specified direction.
2. Travel to zero mark.

   Once the reference cam is reached, the axis changes the traversing direction and evaluates the zero mark of the encoder.
3. Travel to reference point.

   Once the zero mark is reached, the axis traverses to the reference point and synchronizes the actual position value in the converter with the machine.

###### Step 1: Travel to reference cam

The converter accelerates the axis in the start direction to the "Approach velocity". Once the axis has reached the reference cam, in step 2, the converter switches to the reference point approach.

Reversing cams make sense if the reference cam does not extend up to the end of the traversing range. After reaching a reversing cam, the converter continues to search for the reference cam in the opposite direction.

![Step 1: Travel to homing cam](images/111301494411_DV_resource.Stream@PNG-en-US.png)

Step 1: Travel to homing cam

Under one of the following conditions, the converter skips the first step and starts with step 2:

- The axis is already at the reference cam.
- There is no reference cam available.

###### Step 2: Travel to zero mark

The behavior of the axis in step 2 depends on whether a homing cam is available:

| Symbol | Meaning |
| --- | --- |
| - Reference cam available: | When the converter reaches the reference cam, the axis accelerates in the opposite direction to the start direction, to the "approach velocity zero mark". |
| - No reference cam is available: | The converter accelerates the axis in the start direction to the "approach velocity zero mark". |

![Step 2: Travel to zero mark if a homing cam is available](images/111306691211_DV_resource.Stream@PNG-en-US.png)

Step 2: Travel to zero mark if a homing cam is available

![Travel to the zero mark if a homing cam is not available](images/111308479627_DV_resource.Stream@PNG-en-US.png)

Travel to the zero mark if a homing cam is not available

###### Step 3: Travel to reference point

After the converter has detected a zero mark, the axis moves with the "approach velocity reference point" to the reference point coordinate.

![Step 3: Travel to reference position](images/111306896011_DV_resource.Stream@PNG-en-US.png)

Step 3: Travel to reference position

After the load has reached the reference point coordinate, the converter sets its position setpoint and actual value to this value.

###### Setting the reference point approach

**Requirements**

1. You have selected the "Homing" screen.
2. You have come to the settings via the button on the screen.
3. You have selected "Active homing".

**Procedure**

![Setting the reference point approach](images/127756746507_DV_resource.Stream@PNG-en-US.png)

1. You specify the referencing mode:

   - Only using the encoder zero mark
   - With external zero mark
   - With reference cam and encoder zero mark
2. Specify the start direction.
3. Set the approach velocity to the reference cam.
4. Set the approach velocity to the reference point.
5. Set the approach velocity to the zero mark.
6. Specify the reference point coordinate.
7. Specify the reference point offset.
8. Specify the max. permissible distance to the reference cam in step 1 of active referencing.
9. If a reference cam is available: Define the maximum permitted distance to the zero mark.
10. If no reference cam is available: Define the tolerance for travel to the zero mark.
11. Close the screen form.

You have set the USB reference point approach.  
❒

###### Defining the digital signals for controlling referencing

**Procedure**

![Defining the digital signals for controlling referencing](images/127757166091_DV_resource.Stream@PNG-en-US.png)

1. This signal starts the reference point approach.
2. This signal must be 0 for the reference point approach.
3. Interconnect the signal of the reference cam with the corresponding signal of your machine.
4. If you use the reversing cam minus, interconnect the reversing cam with the corresponding signal, e.g. with the fieldbus.  
   0 = Reversing cams active.
5. If you use the reversing cam plus, interconnect the reversing cam with the corresponding signal, e.g. with the fieldbus.  
   0 = Reversing cams active.

You have now defined the digital signals for controlling.  
❒

###### Defining the analog signals for controlling referencing

**Procedure**

![Defining the analog signals for controlling referencing](images/127723887371_DV_resource.Stream@PNG-en-US.png)

1. Define the signal source for the velocity override.

   ![Defining the analog signals for controlling referencing](images/111333398667_DV_resource.Stream@PNG-en-US.png)
   [Direct setpoint specification (MDI)](#direct-setpoint-specification-mdi)
2. Change the source for the reference point coordinate, if necessary.

You have now defined the analog signals for controlling.  
❒

| Parameter | Meaning |
| --- | --- |
| p2595 | **Start referencing** |
| p2598 | **Reference point coordinate, signal source** |
| p2599 | **Reference point coordinate value** |
| p2600 | **Reference point approach, reference point offset** |
| p2604 | **Reference point approach, start direction** |
| p2605 | **Reference point approach, approach velocity, reference cam** |
| p2606 | **Reference point approach reference cam, maximum distance** |
| p2607 | **Reference point approach reference cam available** |
| p2608 | **Reference point approach, approach velocity, zero mark** |
| p2609 | **Reference point approach, max distance reference cam and zero mark** |
| p2610 | **Reference point approach, tolerance band for the distance to the zero mark** |
| p2611 | **Reference point approach, approach velocity, reference point** |
| p2612 | **Reference point approach, reference cam** |
| p2613 | **Reference point approach reversing cam, minus** |
| p2614 | **Reference point approach reversing cam, plus** |
| r2684.0 | **Reference point approach active** |
| r2684.11 | **Reference point set** |

###### Setting the flying referencing

###### Descriptionin

During motion, the load passes a reference cam. The converter evaluates the reference cam signal via a suitable fast digital input, and corrects its calculated position during travel. The fast digital inputs of the converter used for flying referencing are also called probe inputs.

For flying referencing, the converter corrects the position setpoint and actual value simultaneously.

If the position actual value correction means that the axis has already passed the point where it should start braking, then the axis travels beyond the target and approaches the target from the opposite direction.

![Flying referencing](images/111384212619_DV_resource.Stream@PNG-en-US.png)

Flying referencing

The converter sets the "Reference point set" signal back to zero after its supply voltage is switched off and switched on again. The converter only corrects its position actual value for a 1 signal from "Start referencing". In this way, you can define, for example, the direction of travel when the converter is referencing.

###### Setting flying referencing

**Requirement**

1. You have selected the "Homing" screen.
2. You have come to the settings via the button on the screen.
3. You have selected "Passive homing".

**Procedure**

![Setting flying referencing](images/127723839499_DV_resource.Stream@PNG-en-US.png)

1. Set the edge of the reference cam signal the converter should use to reference its actual position value:

   0: Rising edge

   1: Falling edge
2. Interconnect the switchover of reference cams 1 and 2 with a signal of your choice.
3. Select the digital input with which reference cam 1 is interconnected.
4. Select the digital input with which reference cam 2 is interconnected.

   **Several reference points:**
     
   If you require several reference points for an axis, then you must do the following:

   - Assign the corresponding digital input to the respective reference point.
   - Change the reference point coordinate during operation, e.g. using the non-cyclic communication of the fieldbus.
5. Set the inner window for referencing. You deactivate the inner window with the value 0.
6. Set the outer window for referencing. You deactivate the outer window with the value 0.

   Referencing can be suppressed depending on the deviation of the actual position value:

   Inner window: For excessively small deviations, the converter does not correct its position actual value.

   Outer window: The converter signals an excessive deviation, but does not correct its position actual value.

   ![Outer and inner window for flying referencing](images/111385421835_DV_resource.Stream@PNG-en-US.png)

   Outer and inner window for flying referencing
7. Specify the following:

   - Taking into account the offset in traversing distance: The converter corrects both the actual position as well as the setpoint. The relative traversing distance is shorter or longer by the value of the correction.  
     Example: 500 LU is the axis start position. The axis should travel relatively through 1000 LU. The converter corrects the reference point during travel by 2 LU, and travels to the corrected target position 1498 LU.
   - Not taking into account the correction in the traversing distance: The converter corrects both the actual position as well as the setpoint. The relative travel distance remains unchanged.  
     Example: 500 LU is the axis start position. The axis should travel relatively through 1000 LU. The converter corrects the reference point during travel by 2 LU, however, moves to the old target position 1500 LU.
8. Set the reference point coordinate p2599 via the expert list in the Startdrive.
9. Close the screen form.

You have set flying referencing.

❒

###### Defining digital signals for controlling referencing

**Procedure**

![Defining digital signals for controlling referencing](images/127723882635_DV_resource.Stream@PNG-en-US.png)

1. This signal starts flying referencing.
2. For flying referencing, this signal must be 1.  
   The other signals are of no significance for flying referencing.

You have now defined the digital signals for controlling.  
❒

###### Defining the analog signals for controlling referencing

**Procedure**

![Defining the analog signals for controlling referencing](images/127723887371_DV_resource.Stream@PNG-en-US.png)

1. Define the signal source for the velocity override.

   ![Defining the analog signals for controlling referencing](images/111333398667_DV_resource.Stream@PNG-en-US.png)
   [Direct setpoint specification (MDI)](#direct-setpoint-specification-mdi)
2. Change the source for the reference point coordinate, if necessary.

You have now defined the analog signals for controlling.

❒

| Parameter | Meaning |
| --- | --- |
| p2595 | **Start referencing** |
| p2598 | **Reference point coordinate, signal source** |
| p2599 | **Reference point coordinate value** |
| p2601 | **Flying referencing, inner window** |
| p2602 | **Flying referencing, outer window** |
| p2603 | **Flying referencing, relative positioning mode** |
| p2612 | **Reference point approach, reference cam** |
| r2684.11 | **Reference point set** |
| p2660 | **Measured value referencing** |

###### Set reference point

###### Description

Position the load, e.g. using the "jog" function, at the reference position in the machine.

![Set reference point](images/111419213835_DV_resource.Stream@PNG-en-US.png)

Set reference point

###### Activate 'set home position'

**Requirement**

You have selected the "Homing" screen:

**Procedure**

![Activate 'set home position'](images/111419218443_DV_resource.Stream@PNG-en-US.png)

1. Interconnect this bit with the corresponding signal of your machine.  
   If the axis is stationary, with the signal change 0 → 1, the converter sets its actual position value to the reference point coordinate.  
   For this function, all of the other signals are of no significance.
2. In Startdrive, proceed in the expert list and set p2599 to the reference point coordinate.

You have now activated 'set home position'.  
❒

Parameters for this function

| Parameter | Meaning |
| --- | --- |
| p2596 | **Set reference point** |
| p2598 | **Reference point coordinate, signal source** |
| p2599 | **Reference point coordinate value** |
| r2684.11 | **Reference point set** |

###### Absolute encoder adjustment

**Requirement**

1. You have positioned the axis (e.g. using the "jog" function) to the reference position in the machine.
2. You can use an absolute encoder for the position control.

**Procedure**

![Figure](images/127831560971_DV_resource.Stream@PNG-en-US.png)

1. Specify the reference point coordinate.
2. Accept the reference point coordinate in the position actual value.

You have now adjusted the absolute encoder.

❒

| Parameter | Meaning |  |
| --- | --- | --- |
| p2598 | **Reference point coordinate, signal source** |  |
| p2599 | **Reference point coordinate value** |  |
| p2507 | **Absolute encoder adjustment status** |  |
| 0 | Error has occurred in the adjustment |  |
| 1 | Absolute encoder was not adjusted |  |
| 2 | Absolute encoder was not adjusted and encoder adjustment was initiated |  |
| 3 | Absolute encoder adjusted |  |

##### Jog

This section contains information on the following topics:

- [Jog velocity](#jog-velocity)
- [Incremental jogging](#incremental-jogging)
- [Setting jogging](#setting-jogging)

###### Jog velocity

###### Description

Only input a setpoint velocity for the converter for velocity jog. With the signal "Jogging 1" or "Jogging 2", the converter accelerates the axis to the relevant setpoint velocity. The converter stops the axis when the respective "Jog" signal returns to zero.

![Jog velocity](images/111431190539_DV_resource.Stream@PNG-en-US.png)

Jog velocity

###### Incremental jogging

###### Description

In the case of incremental jogging, input a relative traversing distance and a velocity setpoint into the converter. With the signals "Jogging 1" or "Jogging 2" the converter positions the axis by the respective travel path.

![Incremental jogging](images/111441819915_DV_resource.Stream@PNG-en-US.png)

Incremental jogging

###### Setting jogging

**Requirement**

You have selected the "Jog" screen.

**Procedure**

![Figure](images/127731491211_DV_resource.Stream@PNG-en-US.png)

1. Interconnect the signal that defines the mode for the "jog" function.

   0: Velocity jogging

   1: Incremental jogging
2. Interconnect the signal for jogging 1
3. Interconnect the signal for jogging 2.
4. Select the button for the other settings.
5. Set the velocities for the "jogging 1" function.
6. Set the velocities for the "jogging 2" function.
7. If you use the incremental jog, set the relative position setpoint for the "jogging 1" function.

   This value has no significance for velocity jogging.
8. If you use the incremental jog, set the relative position setpoint for the "jogging 2" function.

   This value has no significance for velocity jogging.

You have set the "jog" function.

❒

| Parameter | Meaning |
| --- | --- |
| p2585 | **Jogging 1 setpoint velocity** |
| p2586 | **Jogging 2 setpoint velocity** |
| p2587 | **Jogging 1 traversing distance** |
| p2588 | **Jogging 2 traversing distance** |
| p2589 | **Jogging 1 signal source** |
| p2590 | **Jogging 2 signal source** |
| p2591 | **Incremental jogging** |

##### Traversing blocks

This section contains information on the following topics:

- [Traversing blocks](#traversing-blocks-1)
- [Setting traversing blocks](#setting-traversing-blocks)
- [Travel to fixed stop](#travel-to-fixed-stop)
- [Application examples](#application-examples)

###### Traversing blocks

###### Description

A traversing block describes a positioning instruction for the drive.

The converter saves 16 different traversing blocks, which it normally executes one after the other. However, you can also directly select a specific traversing block or skip traversing blocks.

Components of a traversing block

| Element | Meaning |  |  |
| --- | --- | --- | --- |
| Number | With this number in the range 0 to 15, every traversing block can be selected using binary-coded control signals. |  |  |
| Job | Positioning command: You can give the converter various commands. For some jobs, you must also specify a parameter. See the table below. |  |  |
| Parameter |  |  |  |
| Mode | Positioning mode: Positioning relative to the start position or absolute to the machine zero point. |  |  |
| Position | Target position |  |  |
| Velocity | v | ![Description](images/111446237707_DV_resource.Stream@PNG-en-US.png) | Setpoints for the traversing profile. |
| Acceleration | a |  |  |
| Braking | -a |  |  |
| Advance | Jump condition to the next traversing block. See the table below. |  |  |

###### Job and parameters

Job and parameters

| Job | Parameter |  | Meaning |
| --- | --- | --- | --- |
| Positioning | --- |  | - Axis absolute or relative positioning. - Rotary axis with modulo correction in a positive or negative direction, absolute positioning. |
| Travel to fixed stop | Force [N] or torque [0.01 Nm] |  | Traverse axis to a fixed stop:  - Linear axis with reduced force. - Rotary axis with reduced torque.   See also Section: [Travel to fixed stop](#travel-to-fixed-stop). |
| Endless travel | --- |  | Traverse the axis at the specified velocity to the positive or negative end of the traversing range. |
| Wait | Time [ms] |  | Wait the specified time. |
| Go to | Number |  | The converter then executes the next traversing block with the specified number. |
| Set, reset | 1 | Set output 1 | Set or reset internal signals in the converter:  - Output 1: r2683.10 - Output 2: r2683.11   You can interconnect the signals with digital outputs of the converter or with bit 10 and 11 of the positioning status word of the fieldbus. |
| 2 | Set output 2 |  |  |
| 3 | Set outputs 1 and 2 |  |  |
| Jerk | 0 | Inactive | Activate or deactivate jerk limiting.  See also Section: [Limiting the traversing profile](#limiting-the-traversing-profile). |
| 1 | active |  |  |

###### Conditions for transition

Advance: Jump condition to the next traversing block

| Condition | Meaning |  |  | Traversing block |
| --- | --- | --- | --- | --- |
| CONTINUE WITH STOP | If the axis has reached the setpoint position and has come to a standstill, the converter executes the next traversing block. |  |  | ![Conditions for transition](images/103427740171_DV_resource.Stream@PNG-en-US.png) |
| CONTINUE FLYING | The converter goes to next traversing block at the braking instant. |  |  | ![Conditions for transition](images/103427736715_DV_resource.Stream@PNG-en-US.png) |
| CONTINUE EXTERNAL | At the external E signal, the converter goes to the next traversing block. | If the E signal is not present, the drive behaves just the same as for "CONTINUE FLYING". |  | ![Conditions for transition](images/103427743627_DV_resource.Stream@PNG-en-US.png) |
| CONTINUE EXTERNAL WAIT | If the E signal is not present, the converter exits the current traversing block and continues to wait for the signal. | --- | ![Conditions for transition](images/103427747083_DV_resource.Stream@PNG-en-US.png) |  |
| CONTINUE EXTERNAL ALARM | As long as the axis is at a standstill, the converter signals alarm A07463. | ![Conditions for transition](images/103427763339_DV_resource.Stream@PNG-en-US.png) |  |  |
| END | The converter exits the current traversing block if the target position has been reached. The converter does not go to the next traversing block. |  |  | ![Conditions for transition](images/103427766795_DV_resource.Stream@PNG-en-US.png) |

###### Setting traversing blocks

###### Programming traversing blocks

**Requirement**

1. You have selected the "Traversing blocks" screen.
2. You select the "Program traversing blocks" button.

**Procedure**

![Programming traversing blocks](images/127809483147_DV_resource.Stream@PNG-en-US.png)

1. Assign a unique number for each traversing block.
2. Define the command and the corresponding parameters.
3. Set the job-specific values.
4. Define the step enabling condition for the next job.

You have programmed the traversing blocks.  
❒

###### Define digital signals for controlling

**Procedure**

![Define digital signals for controlling](images/127789571211_DV_resource.Stream@PNG-en-US.png)

1. Define the signal for the start of the traversing block.

   The signal change 0 → 1 starts the currently selected traversing block.
2. In the factory setting, this signal is interconnected with the appropriate internal signals of the converter. We recommend that you do not change this setting.
3. See ②.
4. See ②.
5. Define the signal for the settings for the intermediate stop.

   The axis temporarily stops for the "intermediate stop" = 0 signal. The axis continues its travel with "intermediate stop" = 1. The same traversing block as before the stop is active.

   ![Define digital signals for controlling](images/111333398667_DV_resource.Stream@PNG-en-US.png)
   [Application examples](#application-examples)
6. Define the signal for "reject signaling task".

   For the signal "reject traversing task" = 0, the converter stops the axis with the maximum deceleration (p2573). If you start the axis again with "Activate traversing request" = 0 → 1, the converter starts again with the currently selected traversing block.

You have now defined the digital signals for controlling the traversing blocks.

❒

###### Define analog signals for controlling

**Procedure**

![Define analog signals for controlling](images/127819213451_DV_resource.Stream@PNG-en-US.png)

1. Change the signal source for the velocity override, if required.  
   The velocity override refers to the velocity values you have set in the screen for programming the traversing blocks.

You have now defined the analog signals for controlling the traversing blocks.

❒

###### Define an external signal for block change

**Requirement**

You have selected the "External block change" button.

**Procedure**

![Define an external signal for block change](images/127826319499_DV_resource.Stream@PNG-en-US.png)

1. Specify whether the external signal is received via a fast digital input (probe) or from another source, e.g. via the fieldbus.
2. To initiate a block change via the machine control system, you must interconnect this signal with a signal of your choice.
3. Select the input with which cam signal 1 is interconnected.
4. Select the input with which cam signal 2 is interconnected.
5. Specify the edge with which the converter jumps to the next traversing block:  
   0: Rising edge  
   1: Falling edge

You have now defined an external signal for the block change.  
❒

| Parameter | Meaning |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| p0488 | **Probe 1, input terminal** |  |  |  |  |  |  |
| p0489 | **Probe 2, input terminal** |  |  |  |  |  |  |
| p0581 | **Probe edge** |  |  |  |  |  |  |
| 0 | Positive edge 0 → 1 |  |  |  |  |  |  |
| 1 | Negative edge 1 → 0 |  |  |  |  |  |  |
| p2584 | **Configuration functions** |  |  |  |  |  |  |
| .00 | 1 signal: activates position feedback signal (p2688 and r2689) |  |  |  |  |  |  |
| p2615 | **Maximum number of traversing blocks** |  |  |  |  |  |  |
| p2616[0…n] | **Traversing block, block number** |  |  |  |  |  |  |
| p2617[0…n] | **Traversing block, position** |  |  |  |  |  |  |
| p2618[0…n] | **Traversing block, velocity** |  |  |  |  |  |  |
| p2619[0…n] | **Traversing block, acceleration override** |  |  |  |  |  |  |
| p2620[0…n] | **Traversing block, deceleration override** |  |  |  |  |  |  |
| p2621[0…n] | **Traversing block, job** |  |  |  |  |  |  |
| 1 |  | POSITIONING |  |  | 6 | GOTO |  |
| 2 |  | FIXED STOP |  |  | 7 | SET_O |  |
| 3 |  | ENDLESS_POS |  |  | 8 | RESET_O |  |
| 4 |  | ENDLESS_NEG |  |  | 9 | JERK |  |
| 5 |  | WAIT |  |  |  |  |  |
| p2622[0…n] | **Traversing block, job parameter** |  |  |  |  |  |  |
| p2623[0…n] | **Traversing block, job mode**  Value = 0000 cccc bbbb aaaa |  |  |  |  |  |  |
| cccc = 0000 |  |  | Positioning mode | Absolute |  |  |  |
| cccc = 0001 |  |  | Relative |  |  |  |  |
| cccc = 0010 |  |  | Absolute positive (only for rotary axis with modulo correction) |  |  |  |  |
| cccc = 0011 |  |  | Absolute negative (only for rotary axis with modulo correction) |  |  |  |  |
| bbbb = 0000 |  |  | Advance condition | End |  |  |  |
| bbbb = 0001 |  |  | Continue with stop |  |  |  |  |
| bbbb = 0010 |  |  | Continue flying |  |  |  |  |
| bbbb = 0011 |  |  | Continue external |  |  |  |  |
| bbbb = 0100 |  |  | Continue external wait |  |  |  |  |
| bbbb = 0101 |  |  | Continue external alarm |  |  |  |  |
| aaaa = 0001 |  |  | Identifiers: Skip block |  |  |  |  |
| p2624 | **Sort traversing block**  To sort the traversing blocks according to their block number: p2624 = 0 → 1. |  |  |  |  |  |  |
| p2625 | **Traversing block selection, bit 0** |  |  |  |  |  |  |
| p2626 | **Traversing block selection, bit 1** |  |  |  |  |  |  |
| p2627 | **Traversing block selection, bit 2** |  |  |  |  |  |  |
| p2628 | **Traversing block selection, bit 3** |  |  |  |  |  |  |
| p2631 | **Activate traversing block (0 → 1)** |  |  |  |  |  |  |
| p2632 | **External block change evaluation** |  |  |  |  |  |  |
| 0 | External block change via probe |  |  |  |  |  |  |
| 1 | External block change via BI: p2633 |  |  |  |  |  |  |
| p2633 | **External block change (0 → 1)** |  |  |  |  |  |  |
| p2640 | **Intermediate stop (0 signal)** |  |  |  |  |  |  |
| p2641 | **Reject traversing job (0 signal)** |  |  |  |  |  |  |
| p2646 | **Velocity override** |  |  |  |  |  |  |
| p2688 | **Position feedback signal tolerance window**    The parameter is only active for p2584.0 = 1  If, for a positioning operation, the actual position (r2521) is within the tolerance window of the target position, then r2689 indicates the traversing block number. |  |  |  |  |  |  |
| r2689 | **Position feedback signal display**    The parameter is only active for p2584.0 = 1   The block number of the traversing block, whose target position lies in the tolerance window around the actual position. |  |  |  |  |  |  |
| [0] | Bit-coded display of the traversing block numbers 0 to 31 |  |  |  |  |  |  |
| [1] | Bit-coded display of the traversing block numbers 32 to 63 |  |  |  |  |  |  |

###### Travel to fixed stop

###### Requirement

The "Travel to fixed stop" function is only possible with the control type vector control with encoder (VC):

"Travel to fixed stop" is not possible with the following types of control:

- V/f control
- Vector control without encoder (SLVC)

###### Description

With this function, the converter positions a machine part to another machine part with force locking – and presses both machine parts together with an adjustable force.

Examples:

1. A door is pressed against a frame so that it is reliably closed.
2. A rotary table is pressed against a mechanical fixed stop, in order to secure a specific alignment.

| Symbol | Meaning |
| --- | --- |
| When traveling to a fixed stop, the following applies:   - You must specify the position setpoint far enough behind the mechanical fixed stop. The load must reach the mechanical fixed stop before the converter brakes the axis. | ![Description](images/103427881611_DV_resource.Stream@PNG-en-US.png) |
| - If the start of braking point is located in front of the mechanical fixed stop, the converter cancels the travel and outputs fault F07485. - Before starting the travel, the converter calculates the traversing profile for accelerating and braking the axis. The selected torque limit for the fixed stop has no influence on this calculation. However, the torque limit for the fixed stop reduces the available drive torque for the complete traversing distance. If the torque available for the predicted acceleration is not sufficient, then the following error is higher.    If the following error monitoring for travel to fixed stop responds, then you must reduce the acceleration override. |  |

**Fixed stop has been reached**

You have two options to define when the fixed stop is reached:

1. Fixed stop via an external sensor:   
   At the fixed stop, the load actuates an external sensor. The sensor signals the converter that the fixed stop has been reached. Depending on the transition condition, the converter maintains the axis at the position with the set torque or goes to the next traversing block.
2. Fixed stop using maximum following error:   
   If the axis comes into contact with the mechanical fixed stop, then the actual position value remains stationary. However, the converter still increases its position setpoint. The converter detects the fixed stop from a settable difference between the position setpoint and actual position value. Depending on the transition condition, the converter maintains the axis at the position with the set torque or goes to the next traversing block.

###### Example: Fixed stop using maximum following error

Traversing blocks

| Ind. | No. | Job | Par. | Mode | s | v | a | -a | Transition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | TRAVEL TO FIXED STOP | 5 | RELATIVE | 10000 | 10 | 100 | 100 | CONTINUE WITH STOP |
| 2 | 2 | POSITIONING | 0 | ABSOLUTE | 0 | 500 | 100 | 100 | END |

![Converter detects the fixed stop using the following error   Following error](images/112707624331_DV_resource.Stream@PNG-en-US.png)

Converter detects the fixed stop using the following error

###### Set travel to fixed stop

1. You have programmed "Travel to fixed stop" as the traversing block.

   ![Set travel to fixed stop](images/111333398667_DV_resource.Stream@PNG-en-US.png)
   [Setting traversing blocks](#setting-traversing-blocks)
2. If you select the "Programming traversing blocks" button, the "Configuration of fixed stop" button appears.

![Set travel to fixed stop](images/112716549515_DV_resource.Stream@PNG-en-US.png)

**Procedure: Fixed stop using an external signal**

![Set travel to fixed stop](images/112715971723_DV_resource.Stream@PNG-en-US.png)

1. Select "Fixed stop using an external signal".
2. Interconnect the sensor that signals when the fixed stop is reached with this signal.
3. Set the tolerance.

   After the fixed stop is detected, the converter monitors the actual position of the axis. If the position actual value changes by more than this distance, then the converter stops the axis and outputs fault F07484. Therefore, the converter detects that the fixed stop has "broken away".

You have now set "Travel to fixed stop" using an external signal.

❒

**Procedure: Fixed stop using maximum following error**

![Set travel to fixed stop](images/112714062731_DV_resource.Stream@PNG-en-US.png)

1. Select "Fixed stop using maximum following error":
2. Set the following error that the converter uses to detect the fixed stop.
3. Set the tolerance.

   After the fixed stop is detected, the converter monitors the actual position of the axis. If the position actual value changes by more than this distance, then the converter stops the axis and outputs fault F07484. Therefore, the converter detects that the fixed stop has "broken away".

You have now set "Travel to fixed stop" using maximum following error.  
❒

| Parameter | Meaning |  |
| --- | --- | --- |
| p2634 | **Fixed stop, maximum following error** |  |
| p2635 | **Fixed stop, monitoring window** |  |
| p2637 | **Fixed stop reached** |  |
| 0 | Fixed stop has not been reached. |  |
| 1 | Fixed stop has been reached. |  |
| p2638 | **Fixed stop outside the monitoring window** |  |
| p2639 | **Torque limit reached** |  |
| 0 | Torque limit has not been reached. |  |
| 1 | Torque limit has been reached. |  |

###### Application examples

###### 1st example

Traversing blocks

| Ind. | No. | Job | Par. | Mode | s | v | a | -a | Transition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | POSITIONING | 0 | RELATIVE | 10000 | 5000 | 100 | 100 | CONTINUE WITH STOP |
| 2 | 2 | POSITIONING | 0 | ABSOLUTE | 0 | 5000 | 100 | 100 | END |

![Positioning an axis using traversing blocks](images/112717389963_DV_resource.Stream@PNG-en-US.png)

Positioning an axis using traversing blocks

###### 2nd Example

Traversing blocks

| Ind. | No. | Job | Par. | Mode | s | v | a | -a | Transition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | POSITIONING | 0 | RELATIVE | 10000 | 2000 | 100 | 100 | CONTINUE EXTERNAL ALARM |
| 2 | 2 | POSITIONING | 0 | RELATIVE | 10000 | 5000 | 100 | 100 | CONTINUE EXTERNAL ALARM |
| 3 | 3 | POSITIONING | 0 | ABSOLUTE | 0 | 5000 | 100 | 100 | END |

The converter only goes to the next traversing block for the 0 → 1 change of the "External block selection" signal.

![Positioning an axis using traversing blocks](images/112718508171_DV_resource.Stream@PNG-en-US.png)

Positioning an axis using traversing blocks

##### Direct setpoint specification (MDI)

###### Description

For direct setpoint input (MDI, Manual Data Input), a higher-level control provides the converter with the position setpoint and traversing profile

**Example 1**

The higher-level control specifies the value of the setpoint either as a relative or an absolute position setpoint:

![Position axis with direct setpoint input (MDI)](images/112794427275_DV_resource.Stream@PNG-en-US.png)

Position axis with direct setpoint input (MDI)

**Example 2**

The higher-level control selects the mode "Set-up":

![Set up axis with direct setpoint input (MDI)](images/112794824075_DV_resource.Stream@PNG-en-US.png)

Set up axis with direct setpoint input (MDI)

###### Defining digital signals to control the direct setpoint input

You have selected the "Direct setpoint input (MDI)" screen.

**Procedure**

![Defining digital signals to control the direct setpoint input](images/127811730187_DV_resource.Stream@PNG-en-US.png)

Interconnect the signals to control the direct setpoint input using the appropriate signals from your machine control.

|  |  |  |
| --- | --- | --- |
| ① | The signal enables MDI. The signal must be = 1 if you control the converter using MDI. |  |
| ② | Specifies the MDI mode:  0: Positioning: Traverse the axis with position control over the target position.  1: Set up: Traverse the axis position-controlled using velocity input  While operational, the axis operating mode can be switched over from "Set up" to "Positioning".  If "Set up" is active, then the two bits ⑥ and ⑦ define the direction of travel. |  |
| ③ | Intermediate stop:  0: The converter stops the axis and maintains the axis in position after standstill. The current traversing block remains valid.  1: The axis continues the interrupted traversing block. |  |
| ④ | Discard traversing block:  0: The converter stops the axis and maintains the axis in position after standstill. The converter can no longer continue the current traversing block, however.  1: Axis waits for a new start command. |  |
| ⑤ | Positioning mode:   0: Relative (see also Bit ⑨).   1: Absolute (the axis must be referenced). | These signals are only effective if, in the interface for analog signals, the value ⑥ is not interconnected. See also the table below. |
| ⑥ | Direction selection for "Set up" (Bit ② = 1): |  |
| ⑦ | Bit ⑥ = 1: Positive direction.   Bit ⑦ = 1: Negative direction.  If both bits are the same, the axis stops. |  |
| ⑧ | Accept setpoint:0 → 1:  Start axis  Is only active, if bit ⑨ = 0. |  |
| ⑨ | 1: Continuous mode:   The converter continually accepts changes to the position setpoint. In this mode, relative positioning is not permitted (see bit ⑤).   0: The converter starts using bit ⑧. |  |

You have now interconnected the digital signals for controlling the direct setpoint input.

❒

###### Defining the signals to control the direct setpoint input

**Requirement**

You have selected the "Direct setpoint input (MDI)" screen.

**Procedure**

![Defining the signals to control the direct setpoint input](images/127714536715_DV_resource.Stream@PNG-en-US.png)

Interconnect the signals to control the direct setpoint input using the appropriate signals from your machine control:

|  |  |  |
| --- | --- | --- |
| ① | Override velocity, referred to ③ |  |
| ② | Position setpoint |  |
| ③ | Velocity setpoint for the traversing profile. |  |
| ④   ⑤ | Acceleration override and deceleration, referred to the values of the traversing profile limitation.    [Limiting the traversing profile](#limiting-the-traversing-profile) |  |
| ⑥ | **"Mode adaptation" is interconnected with a signal:** |  |
| xx0x hex | Absolute positioning. |  |
| xx1x hex | Relative positioning. |  |
| xx2x hex | Position the rotary axis in the positive direction. |  |
| xx3x hex | Position the rotary axis in the negative direction. |  |
| **"Mode adaptation" is not interconnected (=0):** |  |  |
| The signals ⑤, ⑥ and ⑦ of the upper table are effective. |  |  |

You have now interconnected the analog signals for controlling the direct setpoint input.

❒

###### Set fixed setpoint

In some applications it is sufficient if the converter moves the axis for each task in the same way, absolute or relative to the position setpoint. This approach can be achieved with fixed setpoints.

**Procedure**

![Set fixed setpoint](images/127810409483_DV_resource.Stream@PNG-en-US.png)

1. Select the button for configuring the fixed setpoint:
2. Set the values suitable to your application:

You have set the fixed setpoints.  
❒

Parameters for this function

| Parameter | Meaning |  |
| --- | --- | --- |
| p2640 | **Intermediate stop (0 signal)** |  |
| p2641 | **Reject traversing block (0 signal)** |  |
| p2642 | **Direct setpoint specification / MDI, position setpoint** |  |
| p2643 | **Direct setpoint specification / MDI, velocity setpoint** |  |
| p2644 | **Direct setpoint specification / MDI, acceleration override** |  |
| p2645 | **Direct setpoint specification / MDI, deceleration override** |  |
| p2646 | **Velocity override** |  |
| p2647 | **Direct setpoint specification / MDI selection** |  |
| p2648 | **Direct setpoint specification / MDI, positioning type** |  |
| 0 | Absolute positioning is selected |  |
| 1 | Relative positioning is selected |  |
| p2649 | **Direct setpoint specification / MDI, acceptance method selection** |  |
| 0 | Values are accepted when p2650 = 0 → 1 |  |
| 1 | Continuous acceptance of values |  |
| p2650 | **Direct setpoint specification / MDI, setpoint acceptance, signal edge**  p2650 = 0 → 1 and p2649 = 0 signal |  |
| p2651 | **Direct setpoint specification / MDI, positive direction selection** |  |
| p2652 | **Direct setpoint specification / MDI, negative direction selection** |  |
| p2653 | **Direct setpoint specification / MDI, set up selection**  Signal = 1: Set up is selected. |  |
| p2654 | **Direct setpoint specification / MDI, mode adaptation** |  |
| p2690 | **Position fixed setpoint**  Interconnect fixed setpoint: p2642 = 2690 |  |
| p2691 | **Velocity fixed setpoint**  Interconnect fixed setpoint: p2643 = 2691 |  |
| p2692 | **Acceleration override fixed setpoint**  Interconnect fixed setpoint: p2644 = 2692 |  |
| p2693 | **Deceleration override fixed setpoint**  Interconnect fixed setpoint: p2645 = 2693 |  |

#### Permissible encoder combinations

This section contains information on the following topics:

- [Permissible encoder combinations](#permissible-encoder-combinations-1)

##### Permissible encoder combinations

###### Overview

You can connect two encoders to the inverter. The encoder for the speed controller must be mounted on the motor shaft.

Encoder combinations

| Encoders for the speed controller |  | Encoders for the position controller |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | SUB-D connector    ![Overview](images/94521013131_DV_resource.Stream@PNG-de-DE.png) |  | Terminal strip    ![Overview](images/94520810379_DV_resource.Stream@PNG-de-DE.png) |  | DRIVE-CLiQ interface    ![Overview](images/94520898955_DV_resource.Stream@PNG-de-DE.png) |  |  |  |  |  |
| HTL or TTL encoder | SSI encoder | Resolver | HTL encoder | Connection via Sensor Module SMC or SME |  |  |  |  | DRIVE-CLiQ encoder |  |  |
| HTL or TTL encoder | SSI encoder | Resolver | EnDat + SIN/COS encoder | sin/cos encoder |  |  |  |  |  |  |  |
|  | Encoderless | ② | ② | ② | ② | ② | ② | ② | ② | ② | ② |
| ![Overview](images/94521013131_DV_resource.Stream@PNG-de-DE.png) | HTL or TTL encoder | ① | --- | --- | ③ | ③ | ③ | ③ | ③ | ③ | ③ |
| ![Overview](images/94520810379_DV_resource.Stream@PNG-de-DE.png) | Resolver | --- | --- | ① | --- | --- | --- | --- | --- | --- | --- |
| HTL encoder | ③ | ③ | --- | ① | ③ | ③ | ③ | ③ | ③ | ③ |  |
| ![Overview](images/94520898955_DV_resource.Stream@PNG-de-DE.png) | HTL or TTL encoder | ③ | ③ | --- | ③ | ① | --- | --- | --- | --- | --- |
| Resolver | ③ | ③ | --- | ③ | --- | --- | ① | --- | --- | --- |  |
| EnDat + SIN/COS encoder | ③ | ③ | --- | ③ | --- | --- | --- | ① | --- | --- |  |
| DRIVE-CLiQ encoder | ③ | ③ | --- | ③ | --- | --- | --- | --- | --- | ① |  |
| sin/cos encoder | ③ | ③ | --- | ③ | --- | --- | --- | --- | ① | --- |  |
| Symbols ---, ①, ②, ③ and ④ are explained in the following table. |  |  |  |  |  |  |  |  |  |  |  |

Explanation regarding encoder combinations

|  |  |  |
| --- | --- | --- |
| --- | This combination is not permissible. |  |
| ① | Position controllers and speed controllers use the same encoder on the motor shaft. |  |
| ![Overview](images/96211083275_DV_resource.Stream@PNG-en-US.png) | Advantage:   Favorably-priced solution  Disadvantages:  - Depending on the gear ratio, restrictions regarding the accuracy of the position control. - Not suitable for position control in the case of mechanical slip on the load side |  |
| ② | The position controller evaluates an encoder on the motor shaft or on the load side.  The speed controller operates without an encoder. |  |
| ![Overview](images/96209880075_DV_resource.Stream@PNG-en-US.png) | Advantages:  - You can use an encoder that is already present on the load side, e.g. an SSI encoder, for position control. - Favorably-priced solution   Disadvantages:  - Restrictions regarding the accuracy and dynamic performance of the position control - Not suitable for the position control of hoisting gear - The "Travel to fixed stop" EPos function is not possible. |  |
| ③ | The position controller evaluates an encoder on the load side.  The speed controller evaluates an encoder on the motor shaft. |  |
| ![Overview](images/96208510475_DV_resource.Stream@PNG-en-US.png) | Compared to the other options of encoder assignment, this configuration provides the best control results. |  |

###### Example

| Symbol | Meaning |
| --- | --- |
| ![Example](images/94520810379_DV_resource.Stream@PNG-de-DE.png) | An HTL encoder is connected to the terminal strip. |

|  |  |  |
| --- | --- | --- |
| You have the following options in this case:  - You use the HTL encoder for the speed controller and operate the drive without position control. - You use the HTL encoder both for the speed controller and for the position controller ①. - You operate the drive with encoderless speed control and use the encoder for the position controller ②. |  |  |
| - You use the HTL encoder at the terminal strip only for the speed controller and a second encoder for the position controller ③. | ![Example](images/94521013131_DV_resource.Stream@PNG-de-DE.png) | You can connect the second encoder for the position controller either to the SUB-D-connector or to the DRIVE-CLiQ interface. |
| ![Example](images/94520898955_DV_resource.Stream@PNG-de-DE.png) |  |  |

### Safety functions

This section contains information on the following topics:

- [Descriptions of functions](#descriptions-of-functions)
- [Configuring Safety functions](#configuring-safety-functions)

#### Descriptions of functions

This section contains information on the following topics:

- [Safe Torque Off (STO)](#safe-torque-off-sto)
- [Safe Brake Control (SBC)](#safe-brake-control-sbc)
- [Safe Stop 1](#safe-stop-1)
- [Safely Limited Speed (SLS)](#safely-limited-speed-sls)
- [Safe Direction (SDI)](#safe-direction-sdi)
- [Safe Speed Monitor (SSM)](#safe-speed-monitor-ssm)

##### Safe Torque Off (STO)

###### What is the effect of the STO safety function?

The converter with active STO function prevents energy supply to the motor. The motor can no longer generate torque on the motor shaft.

Consequently, the STO function prevents the starting of an electrically-driven machine component.

| Symbol | Meaning |
| --- | --- |
| ![What is the effect of the STO safety function?](images/103405132171_DV_resource.Stream@PNG-en-US.png) |  |

The STO principle of operation as overview

|  | Safe Torque Off (STO) | Standard converter functions linked with STO |
| --- | --- | --- |
| 1. | The converter identifies when STO is selected via a fail-safe input or via PROFIsafe | --- |
| 2. | The converter prevents the energy supply to the motor. | If you use a motor holding brake, the converter closes the motor holding brake.   If you use a line contactor, the converter opens the line contactor. |
| 3. | The converter signals "STO is active" via a fail-safe digital output or via PROFIsafe. | --- |

![Functionality of STO when the motor is at standstill (A) and rotating (B)](images/109639567371_DV_resource.Stream@PNG-en-US.png)

Functionality of STO when the motor is at standstill (A) and rotating (B)

(A): When selecting STO, if the motor is already stationary (zero speed), then STO prevents the motor from starting.

(B): If the motor is still rotating (B) when STO is selected, it coasts down to standstill.

###### The STO safety function is standardized

The STO function is defined in IEC/EN 61800-5-2:

"[…] [The converter] does not supply any energy to the motor which can generate a torque (or force in the case of a linear motor)."

⇒The STO converter function conforms to IEC/EN 61800-5-2.

###### Application examples for the STO function

The STO function is suitable for applications where the motor is already at a standstill or will come to a standstill in a short, safe period of time through friction. STO does not shorten the run-on time of machine components.

| Examples | Possible solution |
| --- | --- |
| When the Emergency Stop button is pressed, a stationary motor should not unintentionally start. | - Interconnect the Emergency Stop pushbutton with a fail-safe converter digital input. Select STO via the fail-safe digital input. - Select STO via the fail-safe digital input. |
| A central emergency Stop button must prevent the unintentional acceleration of several motors that are at a standstill. | - Evaluate an emergency stop button in a central control. - Select STO via PROFIsafe. |

###### The distinction between Emergency Off and Emergency Stop

"Emergency Off" and "Emergency Stop" are commands that minimize different risks in the machine or plant.

The STO function is suitable for achieving an Emergency Stop, but not an Emergency Off.

|  |  |  |
| --- | --- | --- |
| Risk: | Risk of electrical shock:    ![The distinction between Emergency Off and Emergency Stop](images/103405142155_DV_resource.Stream@PNG-en-US.png) | Risk of unexpected movement:    ![The distinction between Emergency Off and Emergency Stop](images/103405197323_DV_resource.Stream@PNG-en-US.png) |
| Measure to minimize risk: | **Safely switch off**   Switching off the electric power supply for the installation, either completely or partially. | **Safely stop and prevent a restart**   Stopping or preventing the dangerous movement |
| Command: | **Emergency Off** | **Emergency Stop** |
| Classic solution: | Switch off the power supply:    ![The distinction between Emergency Off and Emergency Stop](images/103405201291_DV_resource.Stream@PNG-en-US.png) | Switch off the drive power supply:    ![The distinction between Emergency Off and Emergency Stop](images/103405205259_DV_resource.Stream@PNG-en-US.png) |
| Solution with the STO safety function integrated in the drive: | STO is not suitable for safely switching off an electric voltage. | Select STO:    ![The distinction between Emergency Off and Emergency Stop](images/103405222027_DV_resource.Stream@PNG-en-US.png)   It is permissible that you switch off the converter power supply as well. However, switching off the voltage is not required as a risk-reduction measurement. |

##### Safe Brake Control (SBC)

###### What is the effect of the SBC safety function?

An converter equipped with the SBC function monitors the cables to an electromagnetic brake and when requested, safely shuts down the 24 V control of the brake.

You must supplement the converter with a Safe Brake Relay for the SBC function.

![The brake can be integrated in the motor or externally mounted.](images/110114134411_DV_resource.Stream@PNG-en-US.png)

The brake can be integrated in the motor or externally mounted.

An overview of the principle of operation of SBC

|  | Safe Brake Control (SBC) | Standard brake function |
| --- | --- | --- |
| 1. | When the STO function is active, the converter requests the SBC function via the connecting cable to the Safe Brake Relay.  The Safe Brake Relay safely switches off the supply voltage for the connected brake. | The brake closes. |
| 2. | The converter signals "STO is active" via a fail-safe digital output or via PROFIsafe. | --- |

![The principle of operation of SBC](images/110126127371_DV_resource.Stream@PNG-en-US.png)

The principle of operation of SBC

The SBC function is not able to identify as to whether the brake is mechanically worn, for example.

###### The SBC safety function is standardized

The SBC function is defined in IEC/EN 61800-5-2:

"The SBC function supplies a safe output signal to control an external brake."

⇒The SBC converter function is in conformance with IEC/EN 61800-5-2.

###### Application example for the SBC function

| Example | Possible solution |
| --- | --- |
| After a hoisting gear stops, the converter must close the brake in order to minimize the risk of the load falling. | - Connect the motor holding brake to the converter via the Safe Brake Relay. - Select STO when the drive stops. |

##### Safe Stop 1

###### What is the effect of the SS1 safety function?

The converter with active SS1 function initially brakes the motor and then prevents energy being supplied to the motor.

As a consequence, the SS1 function reduces the kinetic energy of electrically driven machine components to the lowest possible level.

The principle of operation of SS1 differs depending on whether you use SS1 with basic functions or with extended functions.

SS1 of the basic functions

| Symbol | Meaning |
| --- | --- |
| ![What is the effect of the SS1 safety function?](images/103405337227_DV_resource.Stream@PNG-en-US.png) |  |

An overview of the principle of operation of SS1, selected when the motor is rotating

|  | Safe Stop 1 (SS1) | Standard converter functions linked with SS1 |
| --- | --- | --- |
| 1. | The converter identifies when SS1 is selected via a fail-safe input or via PROFIsafe. | --- |
| 2. | SS1 starts a safety timer T.  The converter signals "SS1 is active". | The converter brakes the motor along the OFF3 ramp. |
| 3. | After the timer expires, the converter safely switches off the motor torque with the STO function.  The converter signals "STO is active" via a fail-safe digital output or via PROFIsafe. | --- |

![Principle of operation of SS1 of the basic functions](images/110126127371_DV_resource.Stream@PNG-en-US.png)

Principle of operation of SS1 of the basic functions

SS1 of the extended functions

| Symbol | Meaning |
| --- | --- |
| ![What is the effect of the SS1 safety function?](images/103405337227_DV_resource.Stream@PNG-en-US.png) |  |

An overview of the principle of operation of SS1, selected when the motor is rotating

|  | Safe Stop 1 (SS1) | Standard converter functions linked with SS1 |
| --- | --- | --- |
| 1. | The converter identifies when SS1 is selected via a fail-safe input or via PROFIsafe. | --- |
| 2. | The converter monitors as to whether the motor speed decreases.  The converter signals "SS1 is active". | The converter brakes the motor along the OFF3 ramp. |
| 3. | If the motor speed is low enough, the converter safely switches off the motor torque using STO.  The converter signals "STO is active" via a fail-safe digital output or via PROFIsafe. | --- |

![Principle of operation of SS1 of the extended functions](images/103405342219_DV_resource.Stream@PNG-en-US.png)

Principle of operation of SS1 of the extended functions

###### The SS1 safety function is standardized

The SS1 function is defined in IEC/EN 61800-5-2:

"[…] [1] Initiate and monitor the magnitude of the motor deceleration within the defined limits and initiate the STO function if the motor speed falls below a defined limit value

or

[2] Initiate motor deceleration and activate the STO function after an application-specific time delay."

⇒ Converter function SS1 of the extended functions is in conformance with the definition [1] of IEC/EN 61800-5-2.

⇒ Converter function SS1 of the basic functions is in conformance with the definition [2] of IEC/EN 61800-5-2.

###### Application example

| Example | Possible solution |
| --- | --- |
| The drive must brake as quickly as possible after the Emergency Stop button has been pressed. It is not permissible that the stationary motor undesirably restarts. | Select SS1 in the converter via a fail-safe digital input or via PROFIsafe. |

###### The distinction between EMERGENCY SWITCHING OFF and EMERGENCY STOP

EN 60204‑1 defines "EMERGENCY SWITCHING OFF" and "EMERGENCY STOP" as actions taken in an emergency. Further, it defines various stop categories for EMERGENCY STOP. "EMERGENCY SWITCHING OFF" and "EMERGENCY STOP" minimize different risks in the system or machine.

| Action | EMERGENCY SWITCHING OFF | EMERGENCY STOP |
| --- | --- | --- |
| Stop category 1 according to EN 60204‑1 |  |  |
| Risk | ![The distinction between EMERGENCY SWITCHING OFF and EMERGENCY STOP](images/114108135435_DV_resource.Stream@PNG-en-US.png)   Electric shock | ![The distinction between EMERGENCY SWITCHING OFF and EMERGENCY STOP](images/114114435083_DV_resource.Stream@PNG-en-US.png)   Movement |
| Measure to minimize risk | **Switch off**   Either completely or partially switch off hazardous voltages. | **Stop movement**    Stop hazardous movement and prevent any restart. |
| Classic solution | ![The distinction between EMERGENCY SWITCHING OFF and EMERGENCY STOP](images/114114627083_DV_resource.Stream@PNG-en-US.png) | ![The distinction between EMERGENCY SWITCHING OFF and EMERGENCY STOP](images/114115087883_DV_resource.Stream@PNG-en-US.png)   Brake the motor and switch off the drive power supply |
| Solution based on the SS1 safety function integrated in the drive | Not possible.   SS1 is not suitable for switching off a voltage. | ![The distinction between EMERGENCY SWITCHING OFF and EMERGENCY STOP](images/114115267083_DV_resource.Stream@PNG-en-US.png)   It is not necessary to switch off the voltage to minimize risk. |

##### Safely Limited Speed (SLS)

###### What is the effect of the SLS safety function?

The converter with active SLS function monitors the motor speed. When the monitoring limit is exceeded, the converter stops the motor as quickly as possible.

As a consequence, the SLS function allows an electrically driven machine component to be operated with a temporarily reduced speed or velocity that is not hazardous.

| Symbol | Meaning |
| --- | --- |
| ![What is the effect of the SLS safety function?](images/103405545099_DV_resource.Stream@PNG-en-US.png) |  |

An overview of the principle of operation of SLS, selected when the motor is rotating

|  | Safely Limited Speed (SLS) | Standard converter functions linked with SLS |
| --- | --- | --- |
| 1. | The converter identifies when SLS is selected via a fail-safe input or via safety-related PROFIsafe communication. | --- |
| 2. | SLS allows a motor to reduce its possibly inadmissibly high speed within a defined time – or to reduce it along a defined braking ramp. | The converter limits the speed setpoint to values below the SLS monitoring.  If the motor rotates faster than the SLS monitoring value, then the converter brakes the motor along the OFF3 ramp. |
| 3. | The converter monitors the absolute actual speed against the set SLS monitoring.  The converter signals "SLS is active" via a fail-safe digital output or via PROFIsafe.  If the motor speed exceeds the SLS monitoring, the converter responds with a "safe stop" and brakes the motor as quickly as possible. | The converter limits the speed setpoint to values below the SLS monitoring. |

![Principle of operation of SLS](images/103405550091_DV_resource.Stream@PNG-en-US.png)

Principle of operation of SLS

###### The SLS safety function is standardized

The SLS function is defined in IEC/EN 61800-5-2:

"The SLS function prevents the motor from exceeding the defined speed limit."

⇒ The SLS converter function is in conformance with IEC/EN 61800-5-2.

###### Application examples for the SLS function

| Examples | Possible solution |
| --- | --- |
| Setup mode: The machine operator must enter the dangerous area of a machine and manually introduce material into a machine part. | - Select SLS in the converter via a fail-safe digital input or via PROFIsafe. - The converter limits and monitors the speed of the machine part. |
| A turning machine must not exceed a specific maximum torque in order to protect the drill chuck from damage. |  |

###### Functional expansion: selecting SLS levels

Expansion of the SLS function to include several SLS levels:

- The speed monitoring of the SLS function can be extended to include a maximum of 4 different SLS levels.
- The converter requires additional safety-related signals to select an SLS level and to signal back which SLS level is active.

It is only possible to select SLS levels via PROFIsafe.

The switchover from a higher SLS level 2 to a lower SLS level 1 is described as example in the following.

| Symbol | Meaning |
| --- | --- |
| ![Functional expansion: selecting SLS levels](images/103405606283_DV_resource.Stream@PNG-en-US.png) |  |

Switching over from SLS level 2 to SLS level 1

|  | Safely Limited Speed (SLS) | Standard converter functions linked with SLS |
| --- | --- | --- |
| 1. | The converter signals "SLS level 2 is active" via the safety-related PROFIsafe communication. | The converter limits the speed setpoint to values below SLS level 2. |
| 2. | The converter recognizes the selection of SLS level 1 via the safety-related PROFIsafe communication. |  |
| 3. | SLS allows a motor to reduce its possibly inadmissibly high speed within a defined time – or to reduce it along a defined braking ramp. | The converter limits the speed setpoint to values below SLS level 1.  If the motor rotates faster than the SLS monitoring value, then the converter brakes the motor along the OFF3 ramp. |
| 4. | The converter monitors the absolute actual speed against SLS level 1.  The converter signals "SLS level 1 is active" via the safety-related PROFIsafe communication. | The converter limits the speed setpoint to values below SLS level 1. |

![Switching over from SLS level 2 to SLS level 1](images/103405611275_DV_resource.Stream@PNG-en-US.png)

Switching over from SLS level 2 to SLS level 1

###### Application example for selecting of SLS levels

| Examples | Possible solution |
| --- | --- |
| Depending on the diameter of the saw blade, a circular saw must not exceed a specific maximum speed. | - Select the SLS and the corresponding SLS level in the converter via PROFIsafe. |

##### Safe Direction (SDI)

###### What is the effect of the SDI safety function?

The converter with active SDI function monitors the motor direction of rotation. If the motor rotates in the inhibited direction, the converter stops the motor as quickly as possible.

The SDI function therefore prevents that an electrically driven machine component moves in the inhibited direction.

| Symbol | Meaning |
| --- | --- |
| ![What is the effect of the SDI safety function?](images/103405795083_DV_resource.Stream@PNG-en-US.png) |  |

An overview of the principle of operation of SDI, selected when the motor is rotating

|  | Safe Direction (SDI) | Standard functions of the converter linked with SDI |
| --- | --- | --- |
| 1. | The converter identifies when SDI is selected via a fail-safe input or via safety-related PROFIsafe communication. | --- |
| 2. | SDI allows a motor to stop moving in the inhibited direction of rotation within a defined time – or along a defined braking ramp. | The converter limits the speed setpoint to values in the selected direction of rotation.  If the motor rotates in the inhibited direction, then the converter brakes the motor along the OFF3 ramp. |
| 3. | The converter monitors the direction of the actual speed.  The converter signals "SDI is active" via a fail-safe digital output or via PROFIsafe.  If the motor rotates in the inhibited direction, the converter responds with a "safe stop" and brakes the motor as quickly as possible. | The converter limits the speed setpoint to values in the selected direction of rotation. |

![Principle of operation of SDI](images/103405800075_DV_resource.Stream@PNG-en-US.png)

Principle of operation of SDI

###### The SDI safety function is standardized

The SDI function is defined in IEC/EN 61800-5-2:

"The SDI function prevents the motor shaft moving in the wrong direction."

⇒ The SDI converter function is in conformance with IEC/EN 61800-5-2.

###### Application examples

| Example | Possible solution |
| --- | --- |
| When replacing the pressure cylinders of the plates, it is only permissible that the drive moves in the safe direction. | - Select SDI in the converter via a fail-safe digital input or via PROFIsafe. - In the converter, inhibit the direction of rotation that is not permitted. |
| After a protective device to detect a jammed door responds, a rolling shutter gate may only move in the opening direction. |  |
| When a crane trolley is at the operating limit switch then it may only start in the opposite direction. |  |
| To manually clean the roller in a printing machine, the roller must only turn in a specific direction. |  |

##### Safe Speed Monitor (SSM)

###### What is the effect of the SSM safety function?

The converter with active SSM function monitors the motor speed. The converter signals whether the speed is above or below a limit value.

| Symbol | Meaning |
| --- | --- |
| ![What is the effect of the SSM safety function?](images/103405881483_DV_resource.Stream@PNG-en-US.png) |  |

An overview of the principle of operation of SSM

|  | Safe Speed Monitoring (SSM) | Standard functions of the converter linked with SSM |
| --- | --- | --- |
| 1. | The SSM function cannot be selected or deselected using external control signals, in the appropriate setting, it is always active | --- |
| 2. | The converter compares the motor speed with an adjustable limit value. |  |
| 3. | If the speed is less than the limit value, the converter signals "Speed below limit value" via a fail-safe digital output or via PROFIsafe. |  |

![The principle of operation of SSM](images/103405924875_DV_resource.Stream@PNG-en-US.png)

The principle of operation of SSM

###### The SSM safety function is standardized

The SSM function is defined in IEC/EN 61800-5-2:

"The SSM function supplies a safe output signal to indicate whether the motor speed is below a specified limit value."

The SSM converter function is in conformance with IEC/EN 61800-5-2.

###### Application example

| Example | Possible solution |
| --- | --- |
| A centrifuge may only be filled below a certain minimum velocity. | The converter safely monitors the centrifuge speed and enables the process to advance to the next step using the status bit "Speed below limit value" via PROFIbus. |

#### Configuring Safety functions

This section contains information on the following topics:

- [Commissioning guidelines](#commissioning-guidelines)
- [Password](#password)
- [Securing user passwords](#securing-user-passwords)
- [Changing settings](#changing-settings)
- [Resetting the safety function parameters to the factory setting](#resetting-the-safety-function-parameters-to-the-factory-setting)
- [Configuring the safety functions](#configuring-the-safety-functions)
- [Basic functions](#basic-functions)
- [Extended functions](#extended-functions)
- [Offline commissioning](#offline-commissioning)
- [Acceptance test](#acceptance-test)
- [Configuring the safety functions and PROFIsafe](#configuring-the-safety-functions-and-profisafe)

##### Commissioning guidelines

The following overview shows the procedure when commissioning an converter with integrated safety functions.

The steps for commissioning the safety functions form part of the activities for commissioning the entire drive.

###### Procedure

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/127678368267_DV_resource.Stream@PNG-en-US.png) | 1. Connect the fieldbus to the converter, and configure the communication in the higher-level control.     - manual of your control system    - operating instructions of your converter 2. Configure the PROFIsafe communication in the higher-level control system.       ![Procedure](images/110540731787_DV_resource.Stream@PNG-en-US.png)    [Configure PROFIsafe in the higher-level control system](#profisafe-properties-and-configuration). 3. Carry out the basic commissioning of the drive.     - operating instructions of your converter 4. Set the converter safety functions.       ![Procedure](images/110540731787_DV_resource.Stream@PNG-en-US.png) The following pages in the Function Manual 5. Commission all of the other converter functions required, e.g. motor control or the protective functions.    - operating instructions of your converter 6. Perform an acceptance test for the safety functions.       ![Procedure](images/110540731787_DV_resource.Stream@PNG-en-US.png)    [Acceptance tests for the safety functions.](#recommended-acceptance-test) |

You have commissioned the converter with integrated safety functions.

##### Password

###### What is the purpose of the password?

The password protects the settings of the safety function from being changed by unauthorized persons.

###### Does the password need to be set?

The password does not need to be set.

The machine manufacturer decides whether or not a password is required.

The probabilities of failure (PFH) and the certification of the safety functions also apply when no password has been set.

###### What do I do if I lose the password?

**Requirement**

You have forgotten the password, however, you would nevertheless like to change the setting of the safety functions.

**Procedure**

If you no longer know the password but still want to change the settings for safety functions, proceed as follows:

1. Create a new project for the converter with Startdrive.

   Leave all the factory setting in the project.
2. Load the project in the converter.

   After loading, the converter has the factory settings.
3. If a memory card inserted in the converter, remove it.
4. Recommission the converter.

You can obtain more information or learn about alternative procedures from Technical Support.

##### Securing user passwords

You can protect user passwords by enabling the "Security settings" in the project. When you modify the password (e.g. – "Safety commissioning password"), a banner is displayed asking to protect the project.

You get the banner in online diagnostics, parameter and commissioning editors. The banner is not displayed once the project is protected. For more information on "Security setting" refer: TIA online help, chapter "Using user administration".

###### Procedure

The banner gets displayed by following the below steps:

1. Create a new project with a drive added.
2. Commissionin the drive online.
3. Start safety commissioning and modify the safety password online.  
   Banner is displayed in online diagnostics, parameter and commissioning editors to upload the configuration and enable "Security Setting" to protect the project.

   ![Procedure](images/117470185099_DV_resource.Stream@PNG-en-US.png)
4. Upload the drive configuration to the project and go offline.  
   Banner is displayed in online diagnostics, parameter and commissioning editors to enable "Security Setting" to protect the project.

   ![Procedure](images/117476059147_DV_resource.Stream@PNG-en-US.png)
5. Click "Security setting" on the banner.
6. Enable the "Security setting".  
   Project and the passwords are protected and the banner disappears.

> **Note**
>
> If the Safety commissioning password is set from the Online access for an accessible device, then the below banner is displayed.

![Procedure](images/117476417547_DV_resource.Stream@PNG-en-US.png)

###### Restriction

Following are the restrictions to copy drive from a protected project:

- Copying a drive from a protected project in one TIA portal instance to a protected/unprotected project in another TIA portal instance is not allowed.

  ![Restriction](images/117481063947_DV_resource.Stream@PNG-en-US.png)
- Copying a drive from a protected project to a global library or unprotected projects is not allowed.

  ![Restriction](images/117481072523_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> To copy a drive from a protected project, open the target protected project and open the source protected project as a "Reference project".

###### User defined roles

You can assign read only or read/write role to the project users in "Security Setting".

**Read only role**

Project user can only view the configurations of the drive and cannot modify the parameters.

**Read / Write role**

Project user can view and modify the configurations of the drive.

##### Changing settings

###### Procedure

1. ① Go online with the drive
2. In Startdrive, select the fail-safe functions.
3. ② Click the "Activate safety settings" icon and enter the safety password.
4. Parameterize the safety functions.
5. To trigger the following actions, click the icon again:

   - Accept settings
   - Copy parameters from CPU 1 to CPU 2
   - Copy data from RAM to ROM

   ![Activating the safety commissioning](images/117270410635_DV_resource.Stream@PNG-en-US.png)

   ![Activating the safety commissioning](images/117270410635_DV_resource.Stream@PNG-en-US.png)

   Activating the safety commissioning

Parameter

| Parameter | Description |
| --- | --- |
| p0010 = 95 | **Drive commissioning parameter filter**  Safety Integrated commissioning |

##### Resetting the safety function parameters to the factory setting

**Procedure**

![Figure](images/127831747851_DV_resource.Stream@PNG-en-US.png)

1. Go online.
2. Select "Commissioning".
3. Select "Backing up/reset".
4. Select "Safety parameters are reset".
5. Press the "Start" button.
6. Enter the password for the safety functions.
7. Confirm that the parameters have been saved (RAM to ROM).
8. Go offline.
9. Switch off the inverter power supply.
10. Wait until all LEDs on the inverter are dark.
11. Switch on the inverter power supply again.

You have restored the safety functions in the inverter to the factory settings.  
❒

Exception: The password for the safety functions is not reset.

[Reset the password for safety functions](#password)

| Parameter | Description |  |
| --- | --- | --- |
| p0010 | **Drive commissioning parameter filter** |  |
| 0 | Ready |  |
| 30 | Parameter reset |  |
| p9761 | **SI password entry** (factory setting: 0000 hex)   Permissible passwords lie in the range 1 … FFFF FFFF. |  |
| p9762 | **New SI password** |  |
| p9763 | **Confirm SI password**   Confirm the new Safety Integrated password. |  |
| p0970 | **Reset drive parameters** |  |
| 5 | Starts a safety parameter reset.  After the reset, the converter sets p0970 = 0. |  |

> **Note**
>
> Enable "Security Settings" to protect the modified password. For more information on "Security setting" refer:
>
> TIA online help, chapter "Using user administration".

##### Configuring the safety functions

You define the following when configuring the safety functions:

- Which safety functions are available?
- Which interfaces are available for the safety functions?

![Figure](images/110658782475_DV_resource.Stream@PNG-en-US.png)

<sup>1</sup>The "STO via Power Module terminals" function is only possible with the PM240‑2 and PM240P‑2, FSD … FSE Power Modules. There are three options when configuring the function:

- You use the "STO via Power Module terminals " function together with the basic functions.
- You use the "STO via Power Module terminals " function together with the extended functions.
- You use the "STO via Power Module terminals " function as the only safety function.

Overview of the possible configurations

| Symbol | Meaning |
| --- | --- |
| **Selected configuration** | **Scope and interfaces of the safety functions** |
| Selecting STO via Power Module terminals | Select STO via the Power Module terminals |
| Basic functions via onboard terminals | - Select STO via the fail-safe digital input.  Additionally, with CU250S-2:   - Select SS1 via the fail-safe digital input. - Control the motor holding brake via SBC. |
| Extended functions via onboard terminals | - Select safety functions via the fail-safe digital input. - Only one monitoring limit of SLS can be used (SLS level 0).  In addition, for converters with safety-related output:   - Evaluating the status of the safety functions via the fail-safe digital output |
| Basic functions via PROFIsafe | - Select STO via PROFIsafe.  Additionally, with CU250S-2:  - Select SS1 via PROFIsafe. - Control the motor holding brake via SBC. |
| Extended functions via PROFIsafe | - Select safety functions via PROFIsafe. - All four monitoring limits of SLS can be used (SLS levels 0 … 3) - Evaluating the status of the fail-safe digital inputs via PROFIsafe |
| Basic functions via PROFIsafe and onboard terminals | - Select STO via fail-safe digital input as well as also via PROFIsafe.  Additionally, with CU250S-2:   - Select SS1 via the fail-safe digital input or PROFIsafe. - Control the motor holding brake via SBC. |
| Extended functions via PROFIsafe and basic functions via onboard terminals | - Select safety functions via PROFIsafe. - Additionally select STO via the fail-safe digital input. - All four monitoring limits of SLS can be used (SLS levels 0 … 3) - Evaluating the status of the fail-safe digital inputs via PROFIsafe  Additionally, with CU250S-2:  - Select basic function SS1 via the fail-safe digital input. - Control the motor holding brake via SBC. |

---

**See also**

[Setting basic functions](#setting-basic-functions)
  
[Extended functions](#extended-functions)

##### Basic functions

This section contains information on the following topics:

- [Setting basic functions](#setting-basic-functions)
- [Setting STO via Power Module terminals](#setting-sto-via-power-module-terminals)
- [In Startdrive, how are the safe terminals assigned to a safety function?](#in-startdrive-how-are-the-safe-terminals-assigned-to-a-safety-function)
- [Setting the filter for safe inputs](#setting-the-filter-for-safe-inputs)
- [Setting the forced checking procedure (test stop)](#setting-the-forced-checking-procedure-test-stop)
- [Setting the delay time for SS1](#setting-the-delay-time-for-ss1)
- [Enabling SBC](#enabling-sbc)
- [Activate settings](#activate-settings)
- [Checking the assignment of the digital inputs](#checking-the-assignment-of-the-digital-inputs)
- [Check the assignment of the feedback signal input for the F-DO](#check-the-assignment-of-the-feedback-signal-input-for-the-f-do)

###### Setting basic functions

###### Overview

Set the basic functions as follows:

1. First select "Basic functions" as safety functionality.
2. Then click "Control type / safety functions" to select the control type and safety functions.

   ![Control type / safety functions](images/103406274571_DV_resource.Stream@PNG-en-US.png)

   Control type / safety functions
3. Click F-DI/F-DO/PROFIsafe to call the interface parameterization.

   Depending on the interface that has been selected, the F-DI/F-DO/PROFIsafe screen form either shows the onboard terminals ① or the PROFIsafe interface ② or both:

   ![Overview](images/103406278539_DV_resource.Stream@PNG-en-US.png)

###### Setting STO via Power Module terminals

**Requirement**

You are online with Startdrive.

**Procedure**

![Figure](images/127809050635_DV_resource.Stream@PNG-en-US.png)

![Figure](images/127762666123_DV_resource.Stream@PNG-en-US.png)

![Figure](images/127761832075_DV_resource.Stream@PNG-en-US.png)

1. Select "STO / SBC / SS1"
2. Select "Enable STO via PM terminals".
3. Select "Test stop".
4. Set the monitoring time to a value to match your application.
5. Using this signal, the converter signals that a forced checking procedure (test stop) is required for the "STO via Power Module terminals" function.
6. Select "F-DI / F-DO / PROFIsafe".
7. Set the discrepancy time (simultaneity monitoring) of the terminals on the Power Module.

   The setting not only applies for the terminals of the Power Module, but also for the failsafe digital input on the Control Unit for selecting STO.

   [Setting the filter for safe inputs](#setting-the-filter-for-safe-inputs)

   The "F-DI input filter" has no significance for the terminals on the Power Module.

You have set the "STO via Power Module terminals" function.  
❒

| Parameter | Description |
| --- | --- |
| p9601.7 | **Enable functions integrated in the drive** (factory setting: 0)  1 signal: STO via the Power Module terminals has been enabled |
| p9650 | **F-DI switchover discrepancy time** (Factory setting: 500 ms) |
| p9661 | **Forced checking procedure STO via PM terminals time** (Factory setting: 8 h) |
| r9662 | **Forced checking procedure STO via PM terminals remaining time** |
| r9773.30 | **SI status**   1 signal: The forced checking procedure (test stop) for the "STO via Power Module terminals" function is required. |

###### In Startdrive, how are the safe terminals assigned to a safety function?

If you require the feedback signal "STO active" of the converter in your higher-level control system, then you must appropriately interconnect the signal.

###### **Requirement**

You are online with Startdrive.

###### **Procedure with Startdrive**

![Procedure with Startdrive](images/127869310475_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| The screen form varies depending on the inverter and the interface that has been selected. |  |
| (A) | Control type |
| (B) | Delay time for SS1 and enable SBC for an converter with CU250S‑2 Control Unit |
| (C) | STO via the Power Module terminals for a PM240‑2 or PM240P‑2, FSD … FSF Power Module |
| (D) | Enable SBC for an inverter with CU250S‑2 Control Unit |

1. Select the button for the feedback signal.
2. Select the signal that matches your particular application.

You have interconnected the "STO active" checkback signal.  
❒

After STO has been selected, the converter signals "STO active" to the higher-level control.

| Parameter | Description |
| --- | --- |
| r9773.01 | **1 signal:** STO is active in the drive |

###### Setting the filter for safe inputs

**Requirement**

You are online with Startdrive.

**Procedure**

![Figure](images/127757246859_DV_resource.Stream@PNG-en-US.png)

1. Navigate to the filter settings.
2. Set the debounce time for the F-DI input filter.
3. Set the discrepancy time for the simultaneity monitoring.

You have set the input filter and the simultaneity monitoring of the failsafe digital input.  
❒

###### Description of the signal filter

The following filters are available for the fail-safe digital inputs:

- One filter for the simultaneity monitoring
- A filter to suppress short signals, e.g. test pulses.

###### Set the discrepancy time for the simultaneity monitoring.

The converter checks that the two input signals of the fail-safe digital input always have the same signal state (high or low).

With electromechanical sensors (e.g. emergency stop buttons or door switches), the two sensor contacts never switch at exactly the same time and are therefore temporarily inconsistent (discrepancy). A permanent discrepancy signifies a fault in the fail-safe digital input circuit, e.g. wire breakage.

When appropriately set, the converter tolerates brief discrepancies.

The discrepancy time does not extend the converter response time. The converter selects its safety function as soon as one of the two F-DI signals changes its state from high to low.

![Simultaneity monitoring with discrepancy time](images/113619952651_DV_resource.Stream@PNG-en-US.png)

Simultaneity monitoring with discrepancy time

###### Filter to suppress short signals

In the following cases, an immediate converter response to signal changes of the fail-safe digital inputs is not desirable:

- If a fail-safe digital input of the converter is interconnected with an electromechanical sensor, signal changes can occur due to contact bounce.
- In order to identify faults due to short-circuit or cross faults, several control modules test their fail-safe digital outputs with "bit pattern tests" (bright/dark test). If a fail-safe digital input of the converter is interconnected with a fail-safe digital output of an open-loop control module, then the converter responds with a bit pattern test.  
  The typical duration of the signal change within a bit pattern test:

  - On test: 1 ms
  - Off test: 4 ms

If the fail-safe digital input responds to many signal changes within a certain time, then the converter responds with a fault.

![Converter response to a bit pattern test](images/113635815819_DV_resource.Stream@PNG-en-US.png)

Converter response to a bit pattern test

A filter in the converter suppresses brief signals as a result of the bit pattern test or contact bounce.

![Filter to suppress brief signals](images/113635819787_DV_resource.Stream@PNG-en-US.png)

Filter to suppress brief signals

The filter extends the response time of the safety function by the debounce time.

###### Filter parameter

| Parameter | Description |
| --- | --- |
| p9650<sup> 1)</sup> | **F-DI switchover discrepancy time** (factory setting: 500 ms)  Tolerance time to change over the fail-safe digital input for the basic functions. |
| p9651 | **STO debounce time** (factory setting: 1 ms)  Debounce time of the fail-safe digital input for the basic functions. |

<sup>1) </sup>For SIMATIC ET 200pro FC-2, the tolerance time is always 0 ms.

**Debounce times for standard and safety functions**

The debounce time p0724 for "standard" digital inputs has no influence on the fail-safe digital input signals. Conversely, the same applies: The debounce time of the fail-safe digital inputs does not affect the signals of the "standard" inputs.

If you use an input as a standard input, set the debounce time using parameter p0724.

If you use an input as a fail-safe digital input, set the debounce time as described above.

###### Setting the forced checking procedure (test stop)

**Requirement**

You are online with Startdrive.

**Procedure**

![Figure](images/127756540427_DV_resource.Stream@PNG-en-US.png)

1. Select the screen form for setting the forced checking procedure.
2. Set the monitoring time to a value to match your application.
3. Using this signal, the converter signals that a forced checking procedure (test stop) is required.

   Interconnect this signal with an converter signal of your choice.

You have set the forced checking procedure (test stop) for the Basic Functions.  
❒

###### Description

The forced checking procedure (test stop) of the basic functions is an converter self test. The converter checks its circuits to switch off the torque. If you are using the Safe Brake Relay, for a forced checking procedure, the converter also checks the circuits of this component.

You start the forced checking procedure each time that the STO function is selected.

Using a timer block, the converter monitors as to whether the forced checking procedure is regularly performed.

![Starting and monitoring the forced checking procedure (test stop)](images/103406715275_DV_resource.Stream@PNG-en-US.png)

Starting and monitoring the forced checking procedure (test stop)

| Parameter | Description |
| --- | --- |
| p9659 | **Forced dormant error detection timer** (Factory setting: 8 h)  Monitoring time for the forced dormant error detection. |
| r9660 | **Forced dormant error detection remaining time** Displays the remaining time until the forced dormant error detection and testing the safety switch-off signal paths. |
| r9773.31 | **1 signal: Safety Integrated status**   Displays the Safety Integrated status on the drive. Test the shutdown paths. |

###### Setting the delay time for SS1

**Requirement**

You are online with Startdrive.

**Procedure**

![Figure](images/127624550795_DV_resource.Stream@PNG-en-US.png)

Set a delay time > OFF3 ramp down time.  
❒

| Parameter | Description |
| --- | --- |
| p9652 | **Safe Stop 1 delay time**  Sets the delay time of the pulse suppression for the "Safe Stop 1" (SS1) function to brake with the OFF3 ramp-down time. |
| p1135 | **OFF3 ramp-down time** |

**Description: the SS1 function without monitoring the speed**

![SS1 without monitoring the speed](images/152476078987_DV_resource.Stream@PNG-en-US.png)

SS1 without monitoring the speed

When SS1 is selected, the converter brakes the motor with the OFF3 ramp-down time.

After the delay time, independent of the actual speed, the converter switches off the motor torque using the STO function.

---

**See also**

[Safe Stop 1](#safe-stop-1)

###### Enabling SBC

**Requirement**

You are online with Startdrive.

**Procedure**

![Figure](images/127698988555_DV_resource.Stream@PNG-en-US.png)

Set "[1] enable SBC".  
❒

| Parameter | Description |
| --- | --- |
| p9602 | **Enable safe brake control**  0: SBC is locked 1: SBC is enabled |

---

**See also**

[Safe Brake Control (SBC)](#safe-brake-control-sbc)

###### Activate settings

###### Activate settings

**Requirement**

You are online with Startdrive.

**Procedure**

![Activate settings](images/113597741707_DV_resource.Stream@PNG-en-US.png)

1. Press the "End safety commissioning" button.
2. Confirm the prompt for saving your settings (copy RAM to ROM).
3. Disconnect the online connection.
4. Select the "Load from device (software)" button.
5. Save the project.
6. Switch off the converter power supply.
7. Wait until all LEDs on the converter go dark (no voltage condition).
8. Switch the converter power supply on again.

Your settings are now active.  
❒

| Parameter | Description |
| --- | --- |
| p9700 = D0 hex | **SI copy function** (factory setting: 0)Start the SI parameter copy function. |
| p9701 = DC hex | **Confirm data change** (factory setting: 0) Confirm SI Basic parameter change |
| p0010 = 0 | **Drive commissioning parameter filter** 0: Ready |
| p0971 = 1 | **Save parameter**  1: Save the drive object (copy from RAM to ROM) After the inverter has saved the parameters in a non-volatile fashion, then p0971 = 0. |

---

**See also**

[Password](#password)

###### Checking the assignment of the digital inputs

###### Checking the interconnection of digital inputs

The simultaneous connection of digital inputs with a safety function and a "standard" function may lead to the drive behaving in unexpected ways.

If you control the safety functions in the converter via failsafe digital inputs, then you must check as to whether the failsafe digital inputs are in some instances interconnected with a "standard" function.

**Procedure**

![Checking the interconnection of digital inputs](images/127699906827_DV_resource.Stream@PNG-en-US.png)

1. Select the screen for the digital inputs.
2. Remove all interconnections of the digital inputs that you use as failsafe digital input F-DI:
3. You must delete the digital input connections for all CDS if you use the switchover of the command data sets (CDS).

   You can find a description of the CDS switchover in the operating instructions.

You have ensured that the failsafe digital inputs only control the safety functions in the converter.  
❒

###### Check the assignment of the feedback signal input for the F-DO

###### Checking the interconnection of the feedback signal input for the failsafe digital output

The interconnection of the feedback signal input with a "standard" function may lead to the drive behaving in unexpected ways.

**Requirements**

- You are using the failsafe digital output of the converter.
- You use one of the test modes 2 or 3, where the inverter evaluates the status of the connected actuator via a digital input.

You must check whether this digital input is assigned a "Standard" function.

**Procedure**

![Checking the interconnection of the feedback signal input for the failsafe digital output](images/127699906827_DV_resource.Stream@PNG-en-US.png)

1. Select the digital inputs.
2. Remove the interconnection of the digital input that you use as feedback signal input for the failsafe digital output:

   - SINAMICS G120 with CU250S-2 Control Unit: Digital input DI 6 (see diagram).
   - SINAMICS G120D: Digital input DI 5.
3. If you are using several command data sets (CDS), then remove the interconnection of the feedback signal input for all CDS.

You have now prevented the feedback signal input of the failsafe digital output controlling "Standard" functions in the converter.  
❒

##### Extended functions

This section contains information on the following topics:

- [Overview screen form](#overview-screen-form)
- [Basic settings](#basic-settings)
- [Fail-safe inputs](#fail-safe-inputs)
- [Setting STO via Power Module terminals](#setting-sto-via-power-module-terminals-1)
- [Fail-safe output](#fail-safe-output)
- [Selecting safety functions](#selecting-safety-functions)
- [Completing commissioning](#completing-commissioning)

###### Overview screen form

###### Overview

If you have selected the extended functions, then you go to the following main screen form.

![Safety extended functions](images/103124217611_DV_resource.Stream@PNG-en-US.png)

Safety extended functions

Starting with this screen form you must do the following:

1. Basic settings for all safety functions. See Section  
   [Basic settings](#basic-settings).
2. If necessary, interconnect the fail-safe inputs and outputs. See Sections

   - [Fail-safe inputs](#fail-safe-inputs)
   - [Fail-safe output](#fail-safe-output).
3. If necessary, configure the communication using PROFIsafe. See Section [Configuring the safety functions and PROFIsafe](#configuring-the-safety-functions-and-profisafe).
4. Adapt the safety functions to suit your application. See Sections

   - [Setting SS1](#setting-ss1)
   - [Setting SLS](#setting-sls)
   - [Setting SSM](#setting-ssm)
   - [Setting SDI](#setting-sdi)
5. Activate the settings. See also Section  
   [Completing commissioning](#completing-commissioning).

###### Basic settings

This section contains information on the following topics:

- [Setting the forced checking procedure (test stop)](#setting-the-forced-checking-procedure-test-stop-1)
- [Setting the gear ratio and tolerance](#setting-the-gear-ratio-and-tolerance)
- [Setting encoderless actual value acquisition](#setting-encoderless-actual-value-acquisition)

###### Setting the forced checking procedure (test stop)

**Requirement**

You are online with Startdrive.

**Procedure**

![Figure](images/127688995467_DV_resource.Stream@PNG-en-US.png)

1. Select "Test stop":
2. This signal starts the forced checking procedure (test stop) and resets the remaining time of the monitoring to the value ④. Interconnect this signal, for example, with a digital input or a bit in the fieldbus control word.
3. For this signal, you must carry out a forced checking procedure (test stop) as quickly as possible. Interconnect this signal, for example with a digital output of your choice or a status bit in the fieldbus.
4. Time until the next test stop.
5. Set the monitoring time to the maximum value (9000 hours). This means that the forced checking procedure monitoring for the Basic Functions is deactivated.

   This monitoring is not required when using the Extended Functions, as the forced checking procedure for the Extended Functions also includes the forced checking procedure for the Basic Functions.
6. Setting not required.

You have set the forced checking procedure (test stop) of the Extended Functions.  
❒

###### Description

The forced dormant error detection (test stop) of the extended functions is an converter self test. The converter checks its circuits to monitor the speed and to switch off the torque.

Using a timer block, the converter monitors as to whether the forced dormant error detection is regularly performed.

You must start the forced dormant error detection with a signal of your choice.

![Starting and monitoring the forced dormant error detection (test stop)](images/113030463371_DV_resource.Stream@PNG-en-US.png)

Starting and monitoring the forced dormant error detection (test stop)

| Parameter | Description |
| --- | --- |
| p9559 | **Forced dormant error detection timer of the motion monitoring function** (Factory setting: 8 h)  Sets the time interval for carrying out the forced dormant error detection procedure and testing the safety motion monitoring functions integrated in the drives.  This monitoring time is reset each time the test is carried out. |
| p9659 | **Forced dormant error detection timer** (Factory setting: 8 h)  Monitoring time for the forced dormant error detection of the basic functions. |
| r9660 | **Forced dormant error detection remaining time** Displays the remaining time up to performing the forced dormant error detection of the basic functions. |
| p9705 | **Forced dormant error detection signal source** (Factory setting: 0) Signal source for the forced dormant error detection of the basic functions and the extended functions. |
| r9723.0 | **1 signal: Forced dormant error detection of the extended functions is necessary** Signal for the higher-level control. |
| r9765 | **Forced dormant error detection remaining time** Displays the remaining time up to performing the forced dormant error detection of the extended functions. |
| r9773.31 | **1 signal: Safety Integrated status**   Displays the Safety Integrated status on the drive. Test the shutdown paths. |

###### Setting the gear ratio and tolerance

###### Procedure

- Select "Actual value acquisition" in the secondary navigation of the extended safety functions.

  ![Actual value acquisition configuration](images/103407441547_DV_resource.Stream@PNG-en-US.png)

  Actual value acquisition configuration
- Click "Configuration" in the "Actual value acquisition" screen form.

  The "Encoderless actual value acquisition configuration" dialog box is displayed.

  ![Gear ratio](images/103407445515_DV_resource.Stream@PNG-en-US.png)

  Gear ratio

  Set the following:

  - ①

    **Actual value tolerance**:  
    In most cases, you do not have to change this value. If the inverter responds with message C01711 or C30711 to the "Flying restart" function, increase this value step-by-step until the message no longer occurs.  
    **Note:**  If you increase this value, the speed monitoring of the inverter becomes less sensitive to limit violations.
  - ②
    ③

    **Gear ratio**:   
    Read the motor pole pair number and set the data of your machine according to the following table.
- Close the screen forms.

###### Description of the gear ratio

|  | ②  Number of load revolutions | ③  Number of motor revolutions |
| --- | --- | --- |
| Without gearbox | 1 | Number of pole pairs ④ |
| Gearbox with speed ratio  Load/Motor = L/M | L | M x number of pole pairs ④ |
| Example: Gearbox with speed ratio Load/motor = 1/3 | 1 | 3 x number of pole pairs ④ |

###### Setting encoderless actual value acquisition

**Requirement**

You are online with Startdrive.

**Procedure**

![Figure](images/127694418571_DV_resource.Stream@PNG-en-US.png)

1. Press the "Actual value sensing" button.
2. Select the "Configuration actual value sensing" button.

   Set the following:

   - **(A)** 
     **Actual value tolerance**:  
     In most cases you do not have to change this value. If, in operation, the converter issues message C01711 or C30711 (fault value 3 or 44 … 57), increase this value step-by-step until the message to longer occurs.  
     **Note:** If you increase this value, the speed monitoring of the converter becomes less sensitive to limit violations.
   - **(B), (C), (D)**
      **Gearbox ratio**:  
     Read the number of pole pairs (D) of the motor, and set the data of your machine according to the following table.

     |  | Number of load revolutions | Number of motor revolutions |
     | --- | --- | --- |
     | Without gear | Value (B) = 1 | Value (C) = number of pole pairs (D) |
     | Gearbox with speed ratio load/motor = L/M | Value (B) = L | Value (C) = M x number of pole pairs (D) |
   - **Example**: The drive has a gearbox with a load/motor speed ratio = 23/50

     ⇒ Value (B) = 23, value (C) = 50 × number of pole pairs (D)
   - **(E)** 
     **Delay time actual value sensing**:  
     In most cases you do not have to change this value. If you switch on the motor with the safety functions active (SLS, SDI or SSM) and the converter responds when switching on with a safety fault, increase this value in the range 50 % … 100 % of the motor excitation build-up time (p0346).
   - **(F)** 
     **Minimum current actual value sensing**:  
     In most cases you do not have to change the setting. When the motor draws a low current, and the converter responds with a fault, then reduce this value in steps of 1 % until the fault no longer occurs.
   - **(G)** 
     **Voltage tolerance acceleration**
     **:**In most cases you do not have to change this parameter. During acceleration with very short ramp-up and ramp-down times, if the converter responds with a safety function fault, increase this value step-by-step by approx. 10%.
   - **(H)**
     **Fault tolerance**:  
     In most cases you do not have to change this parameter. This parameter can suppress sporadic faults of the safety functions. The parameter defines how often the converter tolerates its internal plausibility monitoring per second.
3. Close the screen form.

You have set encoderless actual value sensing.  
❒

| Parameter | Description |
| --- | --- |
| p9521 | **Number of load revolutions** (Factory setting: 1) Denominator for the gearbox ratio between the motor and load. |
| p9522 | **Number of motor revolutions** (Factory setting: 2000 rpm) Numerator for the gearbox ratio between the motor and load. |
| p9542 | **Actual value tolerance** (Factory setting: 12 °) Tolerance for the crosswise comparison of the actual position between processor 1 and 2. |
| p9585 | **Fault tolerance** (Factory setting: -1)  Tolerance of the plausibility monitoring of current and voltage angle. |
| p9586 | **Delay time actual value sensing** (Factory setting: 100 ms)  Delay time for evaluating the encoderless actual value sensing after the motor has been switched on. |
| p9588 | **Minimum current actual value sensing** (Factory setting: 10 %) Minimum current for encoderless actual value sensing (1 % ≙ 10 mA). |
| p9589 | **Voltage tolerance acceleration** (factory setting: 100 %) Acceleration limit to filter discontinuity in the velocity. |

###### Fail-safe inputs

This section contains information on the following topics:

- [Interconnect a safety function with a fail-safe input](#interconnect-a-safety-function-with-a-fail-safe-input)
- [Setting the filter for fail-safe inputs](#setting-the-filter-for-fail-safe-inputs)
- [Connecting the signal for fail-safe acknowledgement](#connecting-the-signal-for-fail-safe-acknowledgement)

###### Interconnect a safety function with a fail-safe input

**Requirements**

- You are online with Startdrive.
- You have selected the Extended Functions via onboard terminals.

**Procedure**

![Figure](images/127066154763_DV_resource.Stream@PNG-en-US.png)

1. Select "Control type/safety functions".
2. Press the "F-DI assignment" button.
3. If you do not use a safety function, set the associated "Select F-DI" = "[255] statically deselected".
4. Interconnect the failsafe digital inputs with the corresponding safety functions.
5. If a safety function should always be active, set the associated "Select F-DI" = "[0] statically active".
6. Close the screen form.

You have assigned specific safety functions to the failsafe digital inputs.  
❒

| Parameter | Description |  |
| --- | --- | --- |
| p10022 | **STO input terminal**(Factory setting: 0) | 0: Statically selected 1: F-DI 0 2: F-DI 1 3: F-DI 2 255: Statically deselected |
| p10023 | **SS1 input terminal**(Factory setting: 0) |  |
| p10026 | **SLS input terminal**(Factory setting: 0) |  |
| p10030 | **SDI positive input terminal**(Factory setting: 0) |  |
| p10031 | **SDI negative input terminal**(Factory setting: 0) |  |

###### Setting the filter for fail-safe inputs

**Requirements**

- You are online with Startdrive.
- You have selected one of the two following settings:

  - Extended Functions via onboard terminals
  - Extended Functions via PROFIsafe and onboard terminals

**Procedure**

![Figure](images/113048172043_DV_resource.Stream@PNG-en-US.png)

1. Select "F-DI / F-DO / PROFIsafe".
2. The discrepancy time (simultaneity monitoring) tolerates signal changes at the failsafe digital input that do not occur simultaneously.
3. The input filter suppresses brief signal changes.

You have set the filter for the failsafe digital inputs.  
❒

###### Description of the signal filter

The following filters are available for the fail-safe digital inputs:

- One filter for the simultaneity monitoring
- A filter to suppress short signals, e.g. test pulses.

###### Set the discrepancy time for the simultaneity monitoring

The converter checks that the two input signals of the fail-safe digital input always have the same signal state (high or low).

With electromechanical sensors (e.g. emergency stop buttons or door switches), the two sensor contacts never switch at exactly the same time and are therefore temporarily inconsistent (discrepancy). A permanent discrepancy signifies a fault in the fail-safe digital input circuit, e.g. wire breakage.

When appropriately set, the converter tolerates brief discrepancies.

The discrepancy time does not extend the converter response time. The converter selects its safety function as soon as one of the two F-DI signals changes its state from high to low.

![Simultaneity monitoring with discrepancy time](images/113043232395_DV_resource.Stream@PNG-en-US.png)

Simultaneity monitoring with discrepancy time

###### Filter to suppress short signals

In the following cases, an immediate converter response to signal changes of the fail-safe digital inputs is not desirable:

- If a fail-safe digital input of the converter is interconnected with an electromechanical sensor, signal changes can occur due to contact bounce.
- In order to identify faults due to short-circuit or cross faults, several control modules test their fail-safe digital outputs with "bit pattern tests" (bright/dark test). If a fail-safe digital input of the converter is interconnected with a fail-safe digital output of an open-loop control module, then the converter responds with a bit pattern test.  
  The typical duration of the signal change within a bit pattern test:

  - On test: 1 ms
  - Off test: 4 ms

If the fail-safe digital input responds to many signal changes within a certain time, then the converter responds with a fault.

![Converter response to a bit pattern test](images/113045854347_DV_resource.Stream@PNG-en-US.png)

Converter response to a bit pattern test

A filter in the converter suppresses brief signals as a result of the bit pattern test or contact bounce.

![Filter to suppress brief signals](images/113046044299_DV_resource.Stream@PNG-en-US.png)

Filter to suppress brief signals

The filter extends the response time of the safety function by the debounce time.

| Parameter | Description |
| --- | --- |
| p9650 | **F-DI switchover discrepancy time** (Factory setting: 500 ms)  Tolerance time to change over the fail-safe digital input for the basic functions. |
| p9651 | **STO debounce time** (factory setting: 1 ms)  Debounce time of the fail-safe digital input for the basic functions. |
| p10002 | **F-DI switchover discrepancy time** (Factory setting: 500 ms)  Tolerance time to change over the fail-safe digital inputs for the extended functions. |
| p10017 | **Digital inputs debounce time** (factory setting: 1 ms)  Debounce time of the fail-safe digital inputs for the extended functions. |

**Debounce times for standard and safety functions**

The debounce time p0724 for "standard" digital inputs has no influence on the fail-safe digital input F-DI signals. Conversely, the same applies: The debounce time of the fail-safe digital inputs does not affect the signals of the "standard" inputs.

If you use an input as a standard input, set the debounce time using parameter p0724 .

If you use an input as a fail-safe digital input, set the debounce time as described above.

---

**See also**

[Connecting the signal for fail-safe acknowledgement](#connecting-the-signal-for-fail-safe-acknowledgement)

###### Connecting the signal for fail-safe acknowledgement

**Requirements**

- You are online with Startdrive.
- You have selected the Extended Functions via onboard terminals.

**Procedure**

![Figure](images/113096876683_DV_resource.Stream@PNG-en-US.png)

1. Select "F-DI / F-DO / PROFIsafe".
2. Select a free failsafe digital input for the failsafe acknowledgment signal.

   If there are no free failsafe digital inputs available, you have to acknowledge the safety function faults using a different method.

You have interconnected the failsafe acknowledge signal with a failsafe digital input.  
❒

###### Setting STO via Power Module terminals

**Requirement**

You are online with Startdrive.

**Procedure**

![Figure](images/113097410315_DV_resource.Stream@PNG-en-US.png)

![Figure](images/113098297739_DV_resource.Stream@PNG-en-US.png)

![Figure](images/113098391563_DV_resource.Stream@PNG-en-US.png)

1. Select "STO".
2. Select "Enable STO via PM terminals".
3. If required in the higher-level control, interconnect the feedback signal "STO active".
4. Select "Test stop".
5. Set the monitoring time to a value to match your application.
6. Using this signal, the converter signals that a forced checking procedure (test stop) is required for the "STO via Power Module terminals" function.
7. Select "F-DI / F-DO / PROFIsafe".
8. Set the discrepancy time (simultaneity monitoring) of the terminals on the Power Module.

   The setting not only applies for the Power Module terminals, but also for selecting the STO Basic Function via F‑DI.

You have set the "STO via Power Module terminals" function.  
❒

| Parameter | Description |  |
| --- | --- | --- |
| p9601.7 | **Enable functions integrated in the drive** (factory setting: 0)  1 signal: STO via the Power Module terminals has been enabled |  |
| p9650 | **F-DI switchover discrepancy time** (Factory setting: 500 ms) |  |
| p9661 | **Forced checking procedure STO via PM terminals time** (Factory setting: 8 h) |  |
| r9662 | **Forced checking procedure STO via PM terminals remaining time** |  |
| r9773 | **SI status** |  |
| .1 | 1 signal: STO is active in the drive |  |
| .30 | 1 signal: The forced checking procedure (test stop) for the "STO via Power Module terminals" function is required. |  |

###### Fail-safe output

This section contains information on the following topics:

- [Output signal and setting the test mode](#output-signal-and-setting-the-test-mode)
- [Setting the forced checking procedure (test stop)](#setting-the-forced-checking-procedure-test-stop-2)

###### Output signal and setting the test mode

**Requirements**

- You are online with Startdrive.
- You have selected the Extended Functions via onboard terminals.

**Procedure**

![Figure](images/113184121227_DV_resource.Stream@PNG-en-US.png)

1. Select "F-DI / F-DO / PROFIsafe".
2. Interconnect this signal, for example with a digital input or a control bit in the fieldbus. This signal starts the forced checking procedure (test stop) of the failsafe digital output - and resets the remaining time of the monitoring to the value ③.

   We recommend that the failsafe digital output is tested together with the forced checking procedure of the safety functions. To do this, interconnect the signal source with the same signal as the forced checking procedure of the safety functions.

   ![Figure](images/113184591883_DV_resource.Stream@PNG-en-US.png)
   [Setting the filter for fail-safe inputs](#setting-the-filter-for-fail-safe-inputs)
3. Set the monitoring time for the forced checking procedure.

   The time must be longer than or equal to the time for monitoring the forced checking procedure of the Extended Functions.

   ![Figure](images/113184591883_DV_resource.Stream@PNG-en-US.png)
   [Setting the filter for fail-safe inputs](#setting-the-filter-for-fail-safe-inputs)

You have defined which signal the converter uses to start the forced checking procedure (test stop) of its failsafe digital output.  
❒

###### Description: Forced checking procedure of the fail-safe output

The forced checking procedure of the fail-safe digital output is the regular self-test of the converter, where the converter checks whether the output can be shut down (deactivated).

The converter monitors the regular forced checking procedure of the fail-safe digital output using a time block.

You must start the forced checking procedure with a signal of your choice.

![Start and monitoring of the forced checking procedure of the fail-safe digital output](images/113210432907_DV_resource.Stream@PNG-en-US.png)

Start and monitoring of the forced checking procedure of the fail-safe digital output

| Parameter | Description |
| --- | --- |
| p10003 | **Forced checking procedure timer** (Factory setting: 8 h)  Setting the time to perform the forced checking procedure. |
| p10007 | **Forced checking procedure F-DO signal source** (Factory setting: 0)  Select an input terminal to start the forced checking procedure. |

###### Setting the forced checking procedure (test stop)

**Requirements**

- You are online with Startdrive.
- You have selected the Extended Functions via onboard terminals.

**Procedure**

![Figure](images/113282329483_DV_resource.Stream@PNG-en-US.png)

1. Select "F-DI / F-DO / PROFIsafe".
2. Interconnect the status signals of your choice with the failsafe digital output. The "Safestate"signal is described below.The converter logically combines the status signals according to the following rules:

   - The converter ignored inputs without interconnection.
   - If none of the inputs is interconnected, then the output signal = 0.
3. Activate the test for the failsafe digital output.
4. Select the test mode that is compatible with your application.
5. Adjust the wait time. The following lower limits apply for the setting:

   - The wait time must be longer than the response time tR of the connected actuator.
   - The wait time must be longer than or equal to 24 ms.
   - The wait time must be longer than the time for the input filter of the feedback input (p10017).  
     [Setting the filter for fail-safe digital inputs](#setting-the-filter-for-fail-safe-inputs)

You have defined which signal the converter transfers via its failsafe digital output, and how the converter tests its failsafe digital output.

❒

**Signal "Safestate"**

![The Safetstate signal in the factory setting](images/113281772939_DV_resource.Stream@PNG-en-US.png)

The Safetstate signal in the factory setting

You must set parameter p10039 via the parameter view in Startdrive in order to adapt the "Safestate" signal

**The test mode of the fail-safe output**

Using its adjustable test mode, the converter checks as to whether the fail-safe digital output can be shut down.

The test mode is aligned according to the interconnection of the fail-safe digital output. For test modes 2 and 3, you must adapt the appropriate wait time to your particular application.

**Test mode 1**

![Expected response at digital output DO 2 for test mode 1](images/113360413707_DV_resource.Stream@PNG-en-US.png)

Expected response at digital output DO 2 for test mode 1

When testing the fail-safe digital output, the converter switches the two digital outputs on and off alternating - and evaluates the voltage signal at output DO 2.

**Test mode 2**

![Expected response at the digital input for test mode 2Test mode F-DO](images/113365367307_DV_resource.Stream@PNG-en-US.png)

Expected response at the digital input for test mode 2

When testing the fail-safe digital output, the converter switches the two digital outputs on and off alternating, and evaluates the feedback via a digital input.

**Test mode 3**

![Expected response at the digital input for test mode 3](images/113365597707_DV_resource.Stream@PNG-en-US.png)

Expected response at the digital input for test mode 3

When testing the fail-safe digital output, the converter switches the two digital outputs on and off alternating, and evaluates the feedback via a digital input.

**Test mode 4**

![Test mode 4](images/113365636107_DV_resource.Stream@PNG-en-US.png)

Test mode 4

When testing the fail-safe digital output, the converter switches the two digital outputs on and off alternating.

SINAMIC G120D converters monitor their transistor outputs using internal signals.

For SINAMICS G120, the connected fail-safe digital input F‑DI must monitor its input signals for discrepancy.

|  |  |
| --- | --- |
| p10039 | **Safe State signal selection** (factory setting: 0000 0001 bin)   Setting the signals for the "Safe State" signal. |
| p10042[0…5] | **F-DO signal sources** (Factory setting: 0)Setting the 6 signal sources for F-DO. |
| p10046 | **F-DO feedback signal input activation** (Factory setting: 0000 bin)Activation of the feedback input for the fail-safe digital output. |
| p10047 | **F-DO test mode** (Factory setting: 0100 bin)Setting the test mode for the safety-related digital output{ |
| p10001 | **Wait time for the forced checking procedure at DO** (Factory setting: 500 ms) Within this time, for a forced checking procedure of the fail-safe digital output, the signal must have been detected via the corresponding feedback input (p10047). The converter always waits for a minimum of 24 ms. |

---

**See also**

[Setting the forced checking procedure (test stop)](#setting-the-forced-checking-procedure-test-stop-1)
  
[Connecting the signal for fail-safe acknowledgement](#connecting-the-signal-for-fail-safe-acknowledgement)

###### Selecting safety functions

This section contains information on the following topics:

- [Control type / safety functions for extended functions](#control-type-safety-functions-for-extended-functions)
- [Setting SS1](#setting-ss1)
- [Setting SLS](#setting-sls)
- [Setting SSM](#setting-ssm)
- [Setting SDI](#setting-sdi)

###### Control type / safety functions for extended functions

###### Description

You select the safety functions for the extended functions here.

![Selecting safety functions](images/103278075275_DV_resource.Stream@PNG-en-US.png)

Selecting safety functions

###### Safety functions

You can reach the various safety functions via the buttons in the screen form:

- ① STO to parameterize Safe Torque Off
- ② SS1 to parameterize Safe Stop 1
- ③ SLS to parameterize Safely-Limited S​peed
- ④ SDI to parameterize Safe Direction
- ⑤ SSM to parameterize Safe Speed Monitor

###### Enabling safety functions

To enable the safety functions, select "Enable" in the drop-down lists.

###### Setting SS1

This section contains information on the following topics:

- [Braking ramp monitoring and acceleration monitoring](#braking-ramp-monitoring-and-acceleration-monitoring)
- [Setting SS1 with braking ramp monitoring](#setting-ss1-with-braking-ramp-monitoring)
- [Setting SS1 with acceleration monitoring](#setting-ss1-with-acceleration-monitoring)

###### Braking ramp monitoring and acceleration monitoring

###### Monitoring modes

You can select between two different monitoring modes of the SS1 function.

| Braking ramp monitoring | Acceleration monitoring |
| --- | --- |
| ![Monitoring modes](images/103408395403_DV_resource.Stream@PNG-en-US.png) | ![Monitoring modes](images/103408400011_DV_resource.Stream@PNG-en-US.png) |
| - Using the SBR (Safe Brake Ramp) function, the converter monitors whether the motor speed decreases. - The gradient of the SBR function can be adjusted. The SBR function only starts after the "Delay time for braking ramp". The SBR function starts with the speed setpoint that was applicable when SS1 was selected. - When the standstill monitoring threshold is fallen below, the converter safely switches off the motor torque (STO). | - The converter monitors the motor speed using the SAM (Safe Acceleration Monitor) function. - The converter prevents the motor from re-accelerating by continuously adjusting the monitoring threshold to the decreasing speed. - The converter reduces the monitoring threshold until the "Shutdown speed" has been reached. - The converter safely switches off the motor torque (STO) if one of the following conditions is fulfilled:   - The converter detects that the motor is stationary.   - The maximum time until the torque is switched off has expired. |

###### Setting SS1 with braking ramp monitoring

###### Requirement

You are online with Startdrive.

**Procedure**

![Requirement](images/113466681227_DV_resource.Stream@PNG-en-US.png)

1. Press the button for the SS1 function.
2. Select "with SBR".
3. The shutdown speed SS1 is a condition for the transition into the STO function.
4. Press the "SBR" button.
5. If the ramp-down time (OFF3) in your application is less than 10 seconds, then leave the delay time at its factory setting. If SS1 goes into a fault condition during the function test, increase this value until the motor brakes normally without a fault.  
   If the ramp-down time (OFF3) is set to several minutes, you must extend the delay time to several seconds in order to avoid any unwanted faults when selecting SS1.
6. The monitoring time defines the gradient of the monitoring curve when braking the load.  
   If the monitoring curve should be parallel to the down ramp of the load, then you must set the following: **Monitoring time = ramp-down time (OFF3) / gear ratio**.  
   Gear ratio = load/motor revolutions.  
   Example: Gear ratio = 1 / 3 ⇒ monitoring time = ramp-down time (OFF3) × 3.  
   A monitoring time shorter than the above calculated value does not make sense, as the converter can reduce its monitoring curve faster than the load can be braked.  
   The longer you set the monitoring times, the more tolerant the monitoring.
7. Set the reference speed to the value of the maximum speed.
8. Close the screen forms.

You have set the SS1 function with braking ramp monitoring.  
❒

###### Description: SS1 with braking ramp monitoring

![SS1 with braking ramp monitoring](images/103408498443_DV_resource.Stream@PNG-en-US.png)

SS1 with braking ramp monitoring

**Reference speed and monitoring time**

The two values define the gradient of the SBR monitoring .

**Delay time**

The SBR function only starts after an adjustable time. To begin with, the converter monitors the speed setpoint that applied when SS1 was selected.

**Braking**

The converter brakes the motor with the OFF3 ramp-down time.

**Shutdown speed**

The converter safely switches off the motor torque using the STO function if the speed has reached the shutdown speed.

| Parameter | Description |  |  |
| --- | --- | --- | --- |
| p9501.00 | **Enable safety functions**    **1 signal:** Enable extended functions. **0 signal:** Disable extended functions. |  |  |
| p9506 | **Function specification:** (Factory setting: 1) |  |  |
| 1: | With braking ramp monitoring |  |  |
| 3: | With acceleration monitoring |  |  |
| p9546 | **SSM speed limit** (factory setting: 20 rpm)  Only relevant to the SS1 function if p9560 = 0. |  |  |
| p9560 | **Pulse cancellation shutdown speed** (factory setting: 10 rpm) Shutdown speed |  |  |
| p9581 | **Brake ramp reference value** (factory setting: 1500 rpm)  Reference speed for SBR |  |  |
| p9582 | **Brake ramp delay time** (factory setting: 250 ms) |  |  |
| p9583 | **Brake ramp monitoring time** (factory setting: 10 s) |  |  |
| r9722.1 | **Status signals**    **1 signal**: SS1 active |  |  |
| r9714 | **Speed diagnostics** [rpm] |  |  |
| [0] | **Load-side speed actual value** Electrical speed of the motor. For induction motors, the mechanical speed is obtained from the electrical speed and slip. |  |  |
| [1] | **Actual SAM/SBR speed limit** |  |  |
| r9723.16 | **1 signal**: SAM/SBR active |  |  |
| p1135 | **OFF3 ramp-down time** |  |  |
| p1226 | **Standstill detection, speed threshold** (Factory setting: 20 rpm) |  | The converter switches off the motor torque if the speed either fulfills the condition for standstill detection or the shutdown speed p9569 has been reached. |
| p1227 | **Standstill detection monitoring time** (Value depends on the power unit) |  |  |

###### Setting SS1 with acceleration monitoring

###### Requirement

You are online with Startdrive.

**Procedure**

![Requirement](images/113492077067_DV_resource.Stream@PNG-en-US.png)

1. Press the button for the SS1 function.
2. Select "with SAM/delay time".
3. After the "delay time", the converter safely switches off the motor torque – regardless of the actual speed.
4. The "shutdown speed SS1" is a condition for the transition into the STO function.
5. Press the "SAM" button.
6. The "speed tolerance" is used to track the monitoring to the actual speed.
7. The "shutdown speed acceleration monitoring" is a condition for the transition into the STO function.
8. Close the screen forms.

You have set the SS1 function with acceleration monitoring.  
❒

###### Description: SS1 with acceleration monitoring

![SS1 with acceleration monitoring](images/103408553611_DV_resource.Stream@PNG-en-US.png)

SS1 with acceleration monitoring

**Speed tolerance**

As long as the speed is less, the converter continuously adds the tolerance to the actual speed so that the monitoring tracks the speed.

**Shutdown speed acceleration monitoring**

The converter reduces the monitoring threshold until it reaches the value of the "Shutdown speed acceleration monitoring".

**Shutdown speed SS1 and delay time**

The converter safely switches off the motor torque with the function STO if one of the two conditions is fulfilled:

- The actual speed reaches the value of the shutdown speed SS1.
- The delay time has expired.

| Parameter | Description |  |  |
| --- | --- | --- | --- |
| p9501.00 | **1 signal:** Enable extended functions. **0 signal:** Disable extended functions. |  |  |
| p9506 | **Function specification:** (Factory setting: 1) |  |  |
| 3: | With acceleration monitoring |  |  |
| p9548 | **Speed tolerance** (Factory setting: 300 rpm) |  |  |
| p9556 | **Delay time STOP B → STO** (Factory setting: 600000 ms) |  |  |
| p9560 | **Shutdown speed SS1** (Factory setting: 10 rpm) |  |  |
| p9568 | **Shutdown speed acceleration monitoring** (Factory setting: 0 rpm) |  |  |
| r9714 | **Speed diagnostics** [rpm] |  |  |
| [0] | **Load-side speed actual value** Electrical speed of the motor. For induction motors, the mechanical speed is obtained from the electrical speed and slip. |  |  |
| [1] | **Actual SAM/SBR speed limit** |  |  |
| r9722.1 | **1 signal**: SS1 active |  |  |
| r9723.16 | **1 signal**: SAM/SBR active |  |  |
| p1226 | **Standstill detection, speed threshold** (Factory setting: 20 rpm) |  | The converter switches off the motor torque if the speed either fulfills the condition for standstill detection or the shutdown speed p9569 has been reached. |
| p1227 | **Standstill detection monitoring time** (Value depends on the power unit) |  |  |

###### Setting SLS

This section contains information on the following topics:

- [Setting the monitoring functions](#setting-the-monitoring-functions-1)
- [Settings for acceptance test](#settings-for-acceptance-test)
- [Stop responses](#stop-responses)

###### Setting the monitoring functions

**Requirement**

You are online with Startdrive.

**Procedure**

![Figure](images/113493760011_DV_resource.Stream@PNG-en-US.png)

1. Press the button for the SLS function.
2. Select between one of the two monitoring modes:

   - with delay time
   - with SBR
3. If you have selected "with delay time"  
   The delay time must be longer than the time, when SLS is selected, that the motor needs to brake with the maximum load from the maximum speed down to the lowest SLS level.

   If you have selected "with SBR": Press the button to set the safe braking ramp (SBR).  
   [Setting SS1 with braking ramp monitoring](#setting-ss1-with-braking-ramp-monitoring)
4. Setpoint speed limiting as a % of the currently selected SLS level, see also ⑦, ⑧.
5. Load speed to be monitored.  
   Levels 2 … 4 are only possible when PROFIsafe is selected as interface.
6. Response when monitoring responds.

   [STOP A, STOP B and STOP F](#stop-responses)
7. If you leave this signal interconnection at the factory setting, when SLS is selected, the converter limits the speed setpoint in the positive direction.
8. If you leave this signal interconnection at the factory setting, when SLS is selected, the converter limits the speed setpoint in the negative direction.
9. Close the screen form.

You have set the SLS function.  
❒

###### Operating principle of SLS

![Behavior after selecting SLS. Left: With braking ramp monitoring. Right: Without braking ramp monitoring](images/103408612875_DV_resource.Stream@PNG-en-US.png)

Behavior after selecting SLS. Left: With braking ramp monitoring. Right: Without braking ramp monitoring

After selecting SLS, the converter brakes the motor according to the OFF3 ramp-down time.

[Setting SS1 with braking ramp monitoring](#setting-ss1-with-braking-ramp-monitoring)

| Parameter | Description |  |
| --- | --- | --- |
| p1051 | **Speed limit RFG positive direction of rotation** (Factory setting depends on the Control Unit) |  |
| p1052 | **Speed limit RFG negative direction of rotation** (Factory setting depends on the Control Unit) |  |
| p1135 | OFF3 ramp-down time |  |
| p9501.00 | **Enable safety functions**     **1 signal**: Enable SLS and extended functions.   **0 signal**:Inhibit SLS and extended functions. |  |
| p9506 | **Function specification**: (Factory setting: 1) |  |
| 1: | With braking ramp monitoring |  |
| 3: | Without braking ramp monitoring |  |
| p9531[0…3] | **SLS limit values** (factory setting for all levels: 2000 rpm) |  |
| p9533 | **SLS setpoint speed limiting** (factory setting: 80 %)  The converter limits the setpoint to the value r9733.  r9733[0] = p9531[x] × p9533. |  |
| p9551 | **SLS changeover delay time** (factory setting: 100 ms)  Delay time SLS selection → SLS active, inactive for brake ramp monitoring |  |
| p9563[0…3] | **SLS-specific stop response** (Factory setting: STOP A) |  |
| 0: | STOP A |  |
| 1: | STOP B |  |
| p9581 | **Brake ramp reference value** (factory setting: 1500 rpm)   Reference speed for SBR |  |
| p9582 | **Brake ramp delay time** (factory setting: 250 ms) |  |
| p9583 | **Brake ramp monitoring time** (factory setting: 10 s)  The gradient of the braking ramp depends on p9581 and p9583. |  |
| r9714 | **Speed diagnostics** [rpm] |  |
| [0] | **Load-side speed actual value**  Electrical speed of the motor. For induction motors, the mechanical speed is obtained from the electrical speed and slip. |  |
| [1] | **Actual SAM/SBR speed limit** |  |
| [2] | **Actual SLS speed limit** |  |
| r9722.04 | **Status signals**    **1 signal**: SLS active   **0 signal:** SLS not active |  |
| r9733 | **Effective setpoint speed limiting** |  |
| [0] | Positive setpoint limitation |  |
| [1] | Negative setpoint limitation |  |
| [2] | Absolute setpoint speed limitation |  |

###### Settings for acceptance test

In order to be able to approach the monitoring limit of the safety function during the acceptance test, you must temporarily deactivate speed limiting of the converter.

**Requirement**

You are online with Startdrive.

**Procedure**

![Figure](images/113493941387_DV_resource.Stream@PNG-en-US.png)

1. Open the screen form for the "Acceptance mode".
2. Set the time in which the converter deactivates its internal speed limiting. During the acceptance test, you must reach the monitored limit value within this time.

   After this time expires, the converter exits the acceptance mode and reactivates its internal speed limiting.

You have made the preparations for the function to be accepted.  
❒

| Parameter |  |
| --- | --- |
| p9558 | **Acceptance test mode time limit** (factory setting 40000 ms)   Maximum time limit: 100 seconds. |

###### Stop responses

For an "internal event", the converter responds with a STOP (STOP A, STOP B or STOP F).

###### Response of the motor in the event of a STOP

**STOP A**

For a STOP A, the converter safely switches off the torque of the connected motor immediately.

**STOP B**

For a STOP B, the converter brakes the motor with the OFF3 ramp-down time until standstill is detected. This is then followed by a STOP A .

If you operate the motor with torque control, then the converter switches over the control mode to speed control.

The converter monitors the braking of the motor. The monitoring type corresponds to the monitoring mode of SS1, also see Section [Setting SS1](#setting-ss1).

![Monitoring the speed for a STOP B](images/103408693259_DV_resource.Stream@PNG-en-US.png)

Monitoring the speed for a STOP B

If the motor does not follow the defined braking ramp, the converter interrupts the braking of the motor and responds with a STOP A.

**STOP F**

A STOP F either initiates a STOP A or a STOP B:

- If fault F01611 is the cause of the STOP F, then the converter immediately initiates a STOP A.
- If alarm C01711 is the cause of the STOP F, then the converter response depends on the active safety function:

  - If no safety function is active, the alarm stops and does not affect motor operation.
  - If STO is active, then the converter initiates aSTOP A.
  - In all other cases, the converter initiates a STOP B.

###### Setting SSM

**Requirement**

You are online with Startdrive.

**Procedure**

![Figure](images/113547186955_DV_resource.Stream@PNG-en-US.png)

1. Open the screen form for the SSM safety function.
2. Selects the function with or without hysteresis.
3. Set the behavior when the motor is switched off.

   If you have set the SSM feedback signal for pulse cancellation as "remains active", when switching on the motor, you must maintain a specific signal sequence.
4. Set the speed to be monitored.
5. You only have to set the filter time when the hysteresis ② is enabled.
6. You only have to set the hysteresis when hysteresis is enabled ②.

You have set the SSM function.  
❒

The SSM function is active immediately after commissioning has been completed.

###### SSM without hysteresis

**Speed monitoring**

When the motor is switched on, the converter compares the load speed with the speed limit.

![Time response of the SSM safety function without hysteresis](images/113547135243_DV_resource.Stream@PNG-en-US.png)

Time response of the SSM safety function without hysteresis

| Parameter | Description |
| --- | --- |
| p9501.00 | **1 signal:** Enable extended functions. **0 signal:** Disable extended functions. |
| p9501.16 | **1 signal:** Enable hysteresis and filtering **0 signal:** Disable hysteresis and filtering |
| p9546 | **Speed limit** (Factory setting: 20 rpm) |
| r9714[0] | **Load-side speed actual value** [rpm] Electrical speed of the motor. For induction motors, the mechanical speed is obtained from the electrical speed and slip. |
| r9722.15 | **1 signal**: Absolute value of the speed is lower than the speed limit |

###### SSM with hysteresis

If you wish to monitor speeds that are very close to the speed limit, you may find it useful to set the hysteresis.

**Speed monitoring**

- When the motor is switched on, the converter compares the load speed with the speed limit, taking the hysteresis into account.

  ![Time response of the SSM safety function with hysteresis](images/103408758539_DV_resource.Stream@PNG-en-US.png)

  Time response of the SSM safety function with hysteresis

**Filter**

The signal filters smoothes the speed measured by the converter. Use the filter if you wish to monitor speeds that lie just below the speed limit.

![Time response of the safety function SSM (Safe Speed Monitor)SSMDiagnosticsSSMTime response](images/103408753931_DV_resource.Stream@PNG-en-US.png)

Time response of the safety function SSM (Safe Speed Monitor)

| Parameter | Description |
| --- | --- |
| p9501.00 | **1 signal:** Enable extended functions. **0 signal:** Disable extended functions. |
| p9501.16 | **1 signal:** Enable hysteresis and filtering **0 signal:** Disable hysteresis and filtering |
| p9545 | **Filter time** (Factory setting: 0 ms) |
| p9546 | **Speed limit** (Factory setting: 20 rpm) |
| p9547 | **Hysteresis** (Factory setting: 10 rpm) |
| r9714[0] | **Load-side speed actual value** [rpm] Electrical speed of the motor. For induction motors, the mechanical speed is obtained from the electrical speed and slip. |
| r9722.15 | **1 signal**: Absolute value of the speed is lower than the speed limit |

###### Feedback signal SSM when the motor is switched off

You can select as to whether the SSM function should remain active when the motor is switched off.

The following occurs if SSM remains active:

- With the motor switched off, the converter freezes the "Speed below limit value" signal.
- When the motor is switched off, STO is active.

![Feedback signal SSM when the motor is switched offLeft: SSM becomes inactive. Right: SSM remains active](images/103408763147_DV_resource.Stream@PNG-en-US.png)

Feedback signal SSM when the motor is switched off  
Left: SSM becomes inactive. Right: SSM remains active

| Parameter | Description |
| --- | --- |
| p9509.00 | **1 signal:** SSM becomes inactive when the motor is switched off **0 signal:** SSM remains active when the motor is switched off |

###### Setting SDI

This section contains information on the following topics:

- [Setting the monitoring functions](#setting-the-monitoring-functions-2)
- [Settings for acceptance test](#settings-for-acceptance-test-1)

###### Setting the monitoring functions

**Requirement**

You are online with Startdrive.

**Procedure**

![Figure](images/113547269003_DV_resource.Stream@PNG-en-US.png)

1. Enable the SDI safety function.
2. Press the button for the SDI safety function.
3. Delay time up to active monitoring.
4. Tolerance for motion in the monitored direction.
5. Response when the monitoring function responds.  
   [Stop responses](#stop-responses)
6. Behavior when the motor is switched off.
7. If you leave this signal interconnection at the factory setting, when SDI- is selected, the converter limits the speed setpoint.
8. If you leave this signal interconnection at the factory setting, when SDI+ is selected, the converter limits the speed setpoint.
9. Close the screen form.

You have set the SDI function.  
❒

###### The SDI function

**Time response**

If you select SDI, the converter limits the speed or velocity setpoint to a value of zero in the inhibited direction of rotation.

![Delay time and tolerance](images/103408881547_DV_resource.Stream@PNG-en-US.png)

Delay time and tolerance

**Delay time**

The converter monitors the direction of rotation of the motor after the delay time has expired. When SDI is selected, the delay time must be longer than the time that the motor requires to brake the maximum load from maximum speed down to standstill. The converter brakes the motor with the OFF3 ramp-down time.

**Tolerance**

The converter permits brief motion in the monitored direction, for example for brief speed overshoots after braking down to standstill. To do this, the converter converts the motor speed into an angle. With the tolerance, you limit the maximum permissible angle in the monitored direction.

**Feedback signal SDI when the motor is switched off**

You can select as to whether the SDI function should remain active when the motor is switched off.

- With the motor switched off, the converter freezes the "SDI active" signal.
- When the motor is switched off, STO is active.

![Feedback signal SDI when the motor is switched offLeft: SDI becomes inactive. Right: SDI remains active](images/103408886155_DV_resource.Stream@PNG-en-US.png)

Feedback signal SDI when the motor is switched off  
Left: SDI becomes inactive. Right: SDI remains active

| Parameter | Description |  |
| --- | --- | --- |
| p1051 | **Speed limit RFG positive direction of rotation** (Factory setting depends on the Control Unit) |  |
| p1052 | **Speed limit RFG negative direction of rotation** (Factory setting depends on the Control Unit) |  |
| p1135 | **OFF3 ramp-down time** |  |
| p9501.00 | **1 signal:** Enable extended functions. **0 signal:** Disable extended functions. |  |
| p9501.17 | **1 signal:** Enable SDI **0 signal:** Inhibit SDI |  |
| p9509.08 | **1 signal:** SDI becomes inactive when the motor is switched off **0 signal:** SDI remains active when the motor is switched off |  |
| p9564 | **Tolerance** (Factory setting: 12 degrees) |  |
| p9565 | **Delay time** (Factory setting: 100 ms) |  |
| p9566 | **Stop response** (Factory setting: 1) |  |
| 0: | STOP A |  |
| 1: | STOP B |  |
| r9714[0] | **Load-side speed actual value** [rpm] Electrical speed of the motor. For induction motors, the mechanical speed is obtained from the electrical speed and slip. |  |
| r9722.12 | **1 signal:** SDI positive active |  |
| r9722.13 | **1 signal:** SDI negative active |  |
| r9733 | **Effective setpoint speed limiting** |  |
| [0] | Positive setpoint limitation |  |
| [1] | Negative setpoint limitation |  |
| [2] | Absolute setpoint speed limitation |  |

###### Settings for acceptance test

In order to be able to approach the monitoring limit of the safety function during the acceptance test, you must temporarily deactivate speed limiting of the inverter.

**Requirement**

You are online with Startdrive.

**Procedure**

![Figure](images/113547378699_DV_resource.Stream@PNG-en-US.png)

1. Open the screen form for the "Acceptance mode".
2. Set the time in which the converter deactivates its internal speed limiting. During the acceptance test, you must reach the monitored limit value within this time.

   After this time expires, the converter exits the acceptance mode and reactivates its internal speed limiting.

You have made the preparations for the function to be accepted.  
❒

| Parameter |  |
| --- | --- |
| p9558 | **Acceptance test mode time limit** (factory setting 40000 ms)   Maximum time limit: 100 seconds. |

###### Completing commissioning

This section contains information on the following topics:

- [Enabling safety functions](#enabling-safety-functions)
- [Activate settings](#activate-settings-1)
- [Checking the assignment of the digital inputs](#checking-the-assignment-of-the-digital-inputs-1)
- [Check the assignment of the feedback signal input for the F-DO](#check-the-assignment-of-the-feedback-signal-input-for-the-f-do-1)

###### Enabling safety functions

- In the main screen, enable the safety functions

  ![Enabling safety functions](images/103408923275_DV_resource.Stream@PNG-en-US.png)

  Enabling safety functions

###### Activate settings

###### Activate settings

**Requirement**

You are online with Startdrive.

**Procedure**

![Activate settings](images/113597741707_DV_resource.Stream@PNG-en-US.png)

1. Press the "End safety commissioning" button.
2. Confirm the prompt for saving your settings (copy RAM to ROM).
3. Disconnect the online connection.
4. Select the "Load from device (software)" button.
5. Save the project.
6. Switch off the converter power supply.
7. Wait until all LEDs on the converter go dark (no voltage condition).
8. Switch the converter power supply on again.

Your settings are now active.  
❒

| Parameter | Description |
| --- | --- |
| p9700 = D0 hex | **SI copy function** (factory setting: 0)Start the SI parameter copy function. |
| p9701 = DC hex | **Confirm data change** (factory setting: 0) Confirm SI Basic parameter change |
| p0010 = 0 | **Drive commissioning parameter filter** 0: Ready |
| p0971 = 1 | **Save parameter**  1: Save the drive object (copy from RAM to ROM) After the inverter has saved the parameters in a non-volatile fashion, then p0971 = 0. |

###### Checking the assignment of the digital inputs

###### Checking the interconnection of digital inputs

The simultaneous connection of digital inputs with a safety function and a "standard" function may lead to the drive behaving in unexpected ways.

If you control the safety functions in the converter via failsafe digital inputs, then you must check as to whether the failsafe digital inputs are in some instances interconnected with a "standard" function.

**Procedure**

![Checking the interconnection of digital inputs](images/113597964811_DV_resource.Stream@PNG-en-US.png)

1. Select the screen for the digital inputs.
2. Remove all interconnections of the digital inputs that you use as failsafe digital input F-DI:
3. You must delete the digital input connections for all CDS if you use the switchover of the command data sets (CDS).

   You can find a description of the CDS switchover in the operating instructions.

You have ensured that the failsafe digital inputs only control the safety functions in the converter.  
❒

###### Check the assignment of the feedback signal input for the F-DO

###### Checking the interconnection of the feedback signal input for the failsafe digital output

The interconnection of the feedback signal input with a "standard" function may lead to the drive behaving in unexpected ways.

**Requirements**

- You are using the failsafe digital output of the converter.
- You use one of the test modes 2 or 3, where the converter evaluates the status of the connected actuator via a digital input.

You must check whether this digital input is assigned a "Standard" function.

**Procedure**

![Checking the interconnection of the feedback signal input for the failsafe digital output](images/113598608779_DV_resource.Stream@PNG-en-US.png)

1. Select the digital inputs.
2. Remove the interconnection of the digital input that you use as feedback signal input for the failsafe digital output:

   - SINAMICS G120 with CU250S-2 Control Unit: Digital input DI 6 (see diagram).
   - SINAMICS G120D: Digital input DI 5.
3. If you are using several command data sets (CDS), then remove the interconnection of the feedback signal input for all CDS.

You have now prevented the feedback signal input of the failsafe digital output controlling "Standard" functions in the converter.  
❒

##### Offline commissioning

This section contains information on the following topics:

- [Offline parameterization](#offline-parameterization)
- [Downloading parameters](#downloading-parameters)

###### Offline parameterization

###### Setting the safety functions offline

**Procedure**

1. Select the safety functions in Startdrive.
2. Set the safety function parameters offline.   
   When doing this, orient yourself to the descriptions provided in the online commissioning.  
   [Configuring the safety functions and PROFIsafe](#configuring-the-safety-functions)
3. Back up your project.

You have set the safety functions of the converter offline, and saved them to your PC or PG.  
❒

In the next step, you must load the settings from your PC or PG to the converter.

---

**See also**

[Basic functions](#basic-functions)
  
[Extended functions](#extended-functions)

###### Downloading parameters

###### Procedure

- Go online with Startdrive and start to download to the converter using the "Load to device" button.  
  After the download, the converter signals faults. Ignore these faults, as they will be automatically acknowledged by the following steps.
- Call the safety functions screen form.
- Click the "Activate safety commissioning" icon to change the settings.
- Click the icon again to activate the settings.
- Save your settings (copy RAM to ROM ).
- Switch off the converter power supply.
- Wait until all LED on the converter go dark. Now switch on the converter supply voltage again. Your settings only become effective after this power-on reset.

##### Acceptance test

This section contains information on the following topics:

- [Acceptance - completion of commissioning](#acceptance---completion-of-commissioning)
- [Recommended acceptance test](#recommended-acceptance-test)
- [Acceptance test STO (basic functions)](#acceptance-test-sto-basic-functions)
- [Acceptance test STO (extended functions)](#acceptance-test-sto-extended-functions)
- [SS1 acceptance test](#ss1-acceptance-test)
- [Acceptance test SLS](#acceptance-test-sls)
- [SSM acceptance test](#ssm-acceptance-test)
- [Acceptance test SDI](#acceptance-test-sdi)
- [Reduced acceptance test after expanding the function](#reduced-acceptance-test-after-expanding-the-function)

###### Acceptance - completion of commissioning

###### What is an acceptance?

The machine manufacturer is responsible in ensuring that his plant or machine functions perfectly. As a consequence, after commissioning, the machine manufacturer must check those functions or have them checked by specialist personnel, which represent an increased risk of injury or material damage. This acceptance or validation is, for example, also specified in the European machinery directive and essentially comprises two parts:

- Checking the safety-relevant functions and machine parts.

  → **Acceptance test**.
- Generate an "Acceptance report" that describes the test results.

  → **Documentation**.

Supply information for the validation, e.g. the harmonized European standards EN ISO 13849‑1 and EN ISO 13849‑2.

###### Acceptance test of the machine or plant

The acceptance test checks whether the safety-relevant functions in the plant or machine function correctly. The documentation of the components used in the safety functions can also provide information about the necessary tests.

Testing the safety-related functions includes, e.g. the following:

- Are all safety equipment such as protective door monitoring devices, light barriers or emergency-off switches connected and ready for operation?
- Does the higher-level control respond as expected to the safety-relevant feedback signals of the converter?
- Do the converter settings match the configured safety-relevant function in the machine?

###### Acceptance test of the converter

The acceptance test of the converter is a part of the acceptance test of the entire machine or plant.

The acceptance test of the converter checks whether the integrated drive safety functions are set up correctly for the planned safety function of the machine.

[Examples for acceptance tests.](#acceptance-test)

###### Documentation of the converter

The following must be documented for the converter:

- The results of the acceptance test.
- The settings of the integrated drive safety functions.

The documentation must be signed.

###### Who may perform the acceptance test of the converter?

Personnel from the machine manufacturer, who, on account of their technical qualifications and knowledge of the safety functions, are in a position to perform the acceptance test in the correct manner are authorized to perform the acceptance testing of the converter.

###### Wizard for the acceptance test

The "Startdrive Advanced" commissioning tool (requires an appropriate license) includes a wizard for the acceptance test of the safety functions integrated in the drive.

"Startdrive Advanced" guides you through the acceptance test, generates the appropriate traces to analyze the machine response – and generates an acceptance report as Excel file.

Further information is provided on the Internet:

[Startdrive, system requirements and download](https://support.industry.siemens.com/cs/ww/en/view/109752254)

###### Recommended acceptance test

The following descriptions for the acceptance test are recommendations that illustrate the principle of acceptance. You may deviate from these recommendations if you check the following once you have completed commissioning:

- Correct assignment of the interfaces of each converter with safety function:

  - Fail-safe inputs
  - Fail-safe outputs
  - PROFIsafe address, see also [Checking the PROFIsafe address](#checking-the-profisafe-address).
- Correct setting for the limit values and brake and monitoring times.

  > **Note**
  >
  > Perform the acceptance test with the maximum possible velocity and acceleration in order to test the expected maximum braking distances and braking times.

  > **Note**
  >
  > **Non-critical alarms**
  >
  > The following alarms are issued following each system ramp-up and are not critical for acceptance:
  >
  > - A01697
  > - A01796

###### Acceptance test STO (basic functions)

![STO acceptance test for basic functions](images/103409536907_DV_resource.Stream@PNG-en-US.png)

STO acceptance test for basic functions

Function "Safe Torque Off" (STO)

| No. | Description |  |  | Status |
| --- | --- | --- | --- | --- |
| 1. | **Initial state** |  |  |  |
| - The converter is "ready" (p0010 = 0). |  |  |  |  |
| - The converter signals neither faults nor alarms for the safety functions (r0945[0…7], r2122[0…7]). |  |  |  |  |
| - STO is not active (r9773.1 = 0). |  |  |  |  |
| 2. | **Switch on the motor** |  |  |  |
| - Enter a speed setpoint ≠ 0, and switch on the motor (ON command). |  |  |  |  |
| - Ensure that the correct motor is running. |  |  |  |  |
| 3. | **STO**  **select** |  |  |  |
| - Select STO while the motor is running  **Note:** Test each configured control, e.g. via digital inputs and via PROFIsafe. |  |  |  |  |
| - Check the following: |  |  |  |  |
|  | For control via PROFIsafe | For control via terminal |  |  |
| - The converter signals the following:  "STO Selection via PROFIsafe" (r9772.20 = 1) | - The converter signals the following:  "STO Selection via terminal " (r9772.17 = 1) |  |  |  |
| - If a mechanical brake is not available, the motor coasts down.  A mechanical brake brakes the motor and holds it to ensure that it remains at a standstill. |  |  |  |  |
| - The converter signals neither faults nor alarms for the safety functions (r0945[0…7], r2122[0…7]). |  |  |  |  |
| - The converter signals the following:  "STO is selected" (r9773.0 = 1).  "STO is active" (r9773.1 = 1). |  |  |  |  |
| 4. | **STO**  **deselect** |  |  |  |
| - Deselect STO . |  |  |  |  |
| - Check the following: |  |  |  |  |
|  | - The converter signals neither faults nor alarms for the safety functions (r0945[0…7], r2122[0…7]). |  |  |  |
| - The converter signals the following:  "STO is not selected " (r9773.0 = 0).  "STO is not active" (r9773.1 = 0). |  |  |  |  |
| - The converter is in the "switching on inhibited" state (r0046.0 = 1). |  |  |  |  |
| 5. | **Switch on the motor** |  |  |  |
| - Switch the motor off (OFF1 command) and then on again (ON command). |  |  |  |  |
| - Ensure that the correct motor is running. |  |  |  |  |

###### Acceptance test STO (extended functions)

![STO acceptance test for extended functions](images/103409596811_DV_resource.Stream@PNG-en-US.png)

STO acceptance test for extended functions

Function "Safe Torque Off" (STO)

| No. | Description |  | Status |
| --- | --- | --- | --- |
| 1. | **Initial state** |  |  |
| - The converter is "ready" (p0010 = 0). |  |  |  |
| - The converter signals neither faults nor alarms for the safety functions (r0945[0…7], r2122[0…7]). |  |  |  |
| - STO is not active (r9722.0 = 0). |  |  |  |
| 2. | **Switch on the motor** |  |  |
| - Enter a speed setpoint ≠ 0, and switch on the motor (ON command). |  |  |  |
| - Ensure that the correct motor is running. |  |  |  |
| 3. | **STO**  **Select** |  |  |
| - Select STO while the motor is running  **Note:** Test each configured control, e.g. via digital inputs and via PROFIsafe. |  |  |  |
| - Check the following: |  |  |  |
|  | - If a mechanical brake is not available, the motor coasts down.  A mechanical brake brakes the motor and holds it to ensure that it remains at a standstill. |  |  |
| - The converter signals neither faults nor alarms for the safety functions (r0945[0…7], r2122[0…7]). |  |  |  |
| - The converter signals the following:  "STO is selected" (r9720.0 = 0).  "STO is active" (r9722.0 = 1). |  |  |  |
| 4. | **STO**  **Deselect** |  |  |
| - Deselect STO . |  |  |  |
| - Check the following: |  |  |  |
|  | - The converter signals neither faults nor alarms for the safety functions (r0945[0…7], r2122[0…7]). |  |  |
| - The converter signals the following:  "STO is deselected" (r9720.0 = 1).  "STO is not active" (r9722.1 = 0). |  |  |  |
| - The converter is in the "switching on inhibited" state (r0046.0 = 1). |  |  |  |
| 5. | **Switch on the motor** |  |  |
| - Switch the motor off (OFF1 command) and then on again (ON command). |  |  |  |
| - Ensure that the correct motor is running. |  |  |  |

###### SS1 acceptance test

The two diagrams show the recommended steps to take during the acceptance test. The behavior of the drive differs according to the settings you have made for SSM :

- Upper diagram: Once SS1 has been selected, the converter monitors the speed using braking ramp monitoring.
- Lower diagram: Once SS1 has been selected, the converter monitors the speed using acceleration monitoring.

  ![SS1 acceptance test with braking ramp monitoring](images/103409709707_DV_resource.Stream@PNG-en-US.png)

  SS1 acceptance test with braking ramp monitoring

  ![SS1 acceptance test with acceleration monitoring](images/103409714315_DV_resource.Stream@PNG-en-US.png)

  SS1 acceptance test with acceleration monitoring

Acceptance test for function "Safe Stop 1" (SS1)

| No. | Description |  | Status |
| --- | --- | --- | --- |
| 1. | **Initial state** |  |  |
| - The converter is "ready" (p0010 = 0). |  |  |  |
| - The converter signals neither faults nor alarms for the safety functions (r0945[0…7], r2122[0…7]). |  |  |  |
| - SS1 is not active (r9722.1 = 0). |  |  |  |
| - In Startdrive, configure a trace recording with the following signals: |  |  |  |
|  | - Trigger: On variable bit pattern |  |  |
| - Signals: r9714[0], r9720, r9722 and r9723.16. |  |  |  |
| - Select the time interval to be recorded and the pre-trigger so that the SS1 selection and the SS1 → STO transition are displayed. |  |  |  |
| 2. | **Switch on the motor** |  |  |
| - Enter a speed setpoint ≠ 0, and switch on the motor (ON command). |  |  |  |
| - Ensure that the correct motor is running. |  |  |  |
| 3. | **Select SS1** |  |  |
| - Select SS1 while the motor is switched on.  **Note:** Test each configured control, e.g. via digital inputs and via PROFIsafe. |  |  |  |
| - Check the following on the basis of the trace recording: |  |  |  |
|  | - The motor brakes with the OFF3 ramp-down time. |  |  |
| - The converter signals the following during braking:   - "SS1 is selected" (r9720.1 = 0).   - "SS1 is active" (r9722.1 = 1).   - "SAM/SBR is active" (r9723.16 = 1). |  |  |  |
| - Once the motor has braked, the converter signals the following: "STO is active" (r9772.0 = 1). |  |  |  |
| - If a mechanical brake is not available, the motor will coast down. A mechanical brake brakes the motor and then holds it to ensure it remains at a standstill. |  |  |  |
| - The converter signals the active function STO via PROFIsafe (status word 1, bit 15 = 1) or via its fail-safe output. |  |  |  |
| - The converter signals neither faults nor alarms for the safety functions. |  |  |  |
| 4. | **Deselect SS1** |  |  |
| - Deselect SS1 . |  |  |  |
| - Check the following on the basis of the trace recording: |  |  |  |
|  | - The converter signals neither faults nor alarms for the safety functions (r0945[0…7], r2122[0…7]). |  |  |
| - The converter signals the following:   - "STO is not active" (r9722.0 = 0).   - "SS1 is deselected" (r9720.1 = 1). |  |  |  |
| - The converter is in the "switching on inhibited" state (r0046.0 = 1). |  |  |  |
| 5. | **Switch on the motor** |  |  |
| - Switch the motor off (OFF1 command) and then on again (ON command). |  |  |  |
| - Ensure that the correct motor is running. |  |  |  |

###### Acceptance test SLS

The two diagrams show the recommended steps to take during the acceptance test. The behavior of the drive differs according to the settings you have made for SLS :

- Upper diagram: If the speed is too high, the drive responds with a STOP A.
- Lower diagram: If the speed is too high, the drive responds with a STOP B.

  ![SLS acceptance test with STOP response STOP A](images/103409802251_DV_resource.Stream@PNG-en-US.png)

  SLS acceptance test with STOP response STOP A

  ![SLS acceptance test with STOP response STOP B](images/103409819659_DV_resource.Stream@PNG-en-US.png)

  SLS acceptance test with STOP response STOP B

"Safely-Limited Speed" (SLS) function

| No. | Description |  |  | Status |
| --- | --- | --- | --- | --- |
| **Notes:** If you are using multiple SLS levels, repeat the test for each of the SLS levels.  Test each configured control, e.g. via digital inputs and via PROFIsafe. |  |  |  |  |
| 1. | **Initial state** |  |  |  |
| - The converter is "ready" (p0010 = 0). |  |  |  |  |
| - The converter signals neither faults nor alarms for the safety functions (r0945[0…7], r2122[0…7]). |  |  |  |  |
| - SLS is not active (r9722.4 = 0). |  |  |  |  |
| - In Startdrive, configure a trace recording with the following signals: |  |  |  |  |
|  | - Trigger: On variable bit pattern |  |  |  |
| - Signals: r9714[0], r9720 and r9722 |  |  |  |  |
| - Select the time interval to be recorded and the pre-trigger so that the SLS selection and the approach to the SLS limit are displayed. |  |  |  |  |
| 2. | **Switch on the motor** |  |  |  |
| - Select SLS with the SLS level to be checked. |  |  |  |  |
| - The converter signals the active function SLS via PROFIsafe (status word 1, bit 4 = 1) or via its fail-safe output. |  |  |  |  |
| - Specify a speed setpoint < SLS level. |  |  |  |  |
| - Switch on the motor within five seconds of selecting SLS (ON command). Note: If you wait longer than five seconds for the ON command, STO is activated. In this case, deselect SLS and then select it again. |  |  |  |  |
| - Ensure that the correct motor is running. |  |  |  |  |
| 3. | **Deactivate the setpoint limitation for the acceptance test** |  |  |  |
| - Go online with Startdrive . |  |  |  |  |
| - Activate the Acceptance mode: |  |  |  |  |
|  | ![Acceptance test](images/113493941387_DV_resource.Stream@PNG-en-US.png)   Acceptance test |  |  |  |
| 4. | **Test the set limit value** |  |  |  |
| - Check the speed of the motor in your machine by measuring the velocity of the conveyor belt being monitored, for example. |  |  |  |  |
| - Increase the setpoint until the converter detects an excessively high speed. |  |  |  |  |
| Upper diagram:  The converter responds with STOP A in the event of a limit value violation. |  | Lower diagram:  The converter responds with STOP B in the event of a limit value violation. STOP A follows when the motor comes to a standstill. |  |  |
| - The motor coasts down to a standstill. |  | - The converter brakes the motor to a standstill. |  |  |
| - The converter signals the following:   - C01714 and C30714 (safely-limited speed exceeded)   - C01700 and C30700 (STOP A triggered) |  | - The converter signals the following:   - C01714 and C30714 (safely-limited speed exceeded)   - C01701 and C30701 (STOP B triggered)   - C01700 and C30700 (STOP A triggered) |  |  |
| - The converter signals the internal event via PROFIsafe (status word 1, bit 7 = 1) or via its fail-safe output. |  |  |  |  |
| 5. | **Acknowledge fault** |  |  |  |
| - Deselect SLS . |  |  |  |  |
| - Switch the motor off (OFF1 command). |  |  |  |  |
| - Acknowledge the fault messages with a fail-safe signal. |  |  |  |  |

###### SSM acceptance test

The two diagrams show the recommended steps to take during the acceptance test. The acceptance test differs depending on the settings you have made for SSM :

- Upper diagram: The "speed below limit value" checkback signal remains active when the motor is switched off.
- Lower diagram: The "speed below limit value" checkback signal becomes inactive when the motor is switched off.

  ![SSM acceptance test with active checkback signal when motor is switched off](images/103409867787_DV_resource.Stream@PNG-en-US.png)

  SSM acceptance test with active checkback signal when motor is switched off

  ![SSM acceptance test with inactive checkback signal when motor is switched off](images/103409872395_DV_resource.Stream@PNG-en-US.png)

  SSM acceptance test with inactive checkback signal when motor is switched off

Function "Safe Speed Monitor" (SSM)

| No. | Description |  |  | Status |
| --- | --- | --- | --- | --- |
| 1. | **Initial state** |  |  |  |
| - The converter is in the "ready" state (p0010 = 0). |  |  |  |  |
| - The converter signals neither faults nor alarms for the safety functions (r0945[0…7], r2122[0…7]). |  |  |  |  |
| - In Startdrive, configure a trace recording with the following signals: |  |  |  |  |
|  | - Trigger: On variable bit pattern (r9722.15 = 1). |  |  |  |
| - Signals: r9714[0], r9720 and r9722. |  |  |  |  |
| - Select the time interval to be recorded and the pre-trigger so that the SS1 selection and the SS1 → STO transition are displayed. |  |  |  |  |
| 2. | **Switch on the motor** |  |  |  |
| - Specify a speed setpoint > SSM limit. |  |  |  |  |
| Upper diagram:  The "speed below limit value" checkback signal remains active when the motor is switched off. |  | Lower diagram:  The "speed below limit value" checkback signal becomes inactive when the motor is switched off. |  |  |
| - Select STO . |  | - Switch on the motor (ON command). |  |  |
| - Deselect STO again. |  |  |  |  |
| - Switch on the motor within five seconds of deselecting STO (ON command). |  |  |  |  |
| - Ensure that the correct motor is running. |  |  |  |  |
| - Wait until the motor speed reaches the setpoint. |  |  |  |  |
| - Check the following on the basis of the trace recording: If r9714[0] exceeds the SSM limit, r9722.15 = 0 applies. |  |  |  |  |
| - The converter signals that the SSM limit has been exceeded via PROFIsafe (status word 1, bit 15 = 0) or via its fail-safe output. |  |  |  |  |
| 3. | **Switch off the motor** |  |  |  |
| - Switch the motor off (OFF1 command). |  |  |  |  |
| - Ensure that the correct motor is braked. |  |  |  |  |
| - Wait until the motor is at a standstill. |  |  |  |  |
| - Check the following on the basis of the trace recording: If r9714[0] is below the SSM limit (minus the hysteresis), r9722.15 = 1 applies. |  |  |  |  |
| - The converter signals that the SSM limit has been undershot via PROFIsafe (status word 1, bit 15 = 1) or via its fail-safe output. |  |  |  |  |

###### Acceptance test SDI

The section below describes the acceptance test for SDI+ and SDI- separately. If you configure the SDI function in both directions of rotation, you must carry out both acceptance tests.

###### Acceptance test for SDI positive

The two diagrams show the recommended steps to take during the acceptance test. The acceptance test differs depending on the settings you have made for SDI :

- Upper diagram: The "SDI active" checkback signal remains active when the motor is switched off.
- Lower diagram: The "SDI active" checkback signal becomes inactive when the motor is switched off.

  ![SDI acceptance for a positive direction of rotation; "SDI active" remains active when the motor is switched off](images/103409923211_DV_resource.Stream@PNG-en-US.png)

  SDI acceptance for a positive direction of rotation; "SDI active" remains active when the motor is switched off

  ![SDI acceptance for a positive direction of rotation; "SDI active" becomes inactive when the motor is switched off](images/103409927819_DV_resource.Stream@PNG-en-US.png)

  SDI acceptance for a positive direction of rotation; "SDI active" becomes inactive when the motor is switched off

"Safe Direction" (SDI) function; positive direction of rotation permitted

| No. | Description |  |  | Status |
| --- | --- | --- | --- | --- |
| 1. | **Initial state** |  |  |  |
| - The converter is in the "ready" state (p0010 = 0). |  |  |  |  |
| - The converter signals neither faults nor alarms for the safety functions (r0945[0…7], r2122[0…7]). |  |  |  |  |
| - In Startdrive, configure a trace recording with the following signals: |  |  |  |  |
|  | - Trigger: On variable bit pattern (r9722.12 = 1). |  |  |  |
| - Signals: r9714[0], r9720 and r9722. |  |  |  |  |
| - Select the time interval to be recorded and the pre-trigger so that the SDI selection and the move to the direction of rotation being monitored are displayed. |  |  |  |  |
| 2. | **Switch on the motor** |  |  |  |
| - Enter a positive speed setpoint. |  |  |  |  |
| Upper diagram:  The "SDI active" checkback signal remains active when the motor is switched off. |  | Lower diagram:  The "SDI active" checkback signal becomes inactive when the motor is switched off. |  |  |
| - Switch on the motor within five seconds of deselecting SDI (ON command). Note: If you wait longer than five seconds for the ON command, STO is activated. In this case, deselect SDI and then select it again. |  | - Switch on the motor (ON command). |  |  |
| - Check that the correct motor is rotating in the expected direction. |  |  |  |  |
| 3. | **Deactivate the setpoint limitation for the acceptance test** |  |  |  |
| - Go online with Startdrive . |  |  |  |  |
| - Activate the Acceptance mode: |  |  |  |  |
|  | ![Acceptance test](images/113493941387_DV_resource.Stream@PNG-en-US.png)   Acceptance test |  |  |  |
| 4. | **Test the set limit value** |  |  |  |
| - Change the setpoint so that the motor rotates slightly in the negative direction. |  |  |  |  |
| - In your machine, check when the drive stops when it is turning in a negative direction. |  |  |  |  |
| The rest of the process depends on the settings you made for the SDI function during commissioning: |  |  |  |  |
| If the converter is to respond with STOP A if the limit value is violated: |  | If the converter is to respond with STOP B if the limit value is violated: |  |  |
| - The motor coasts down to a standstill. |  | - The converter brakes the motor to a standstill. |  |  |
| - The converter signals the following:   - C01716 and C30716 (tolerance for safe direction of motion exceeded)   - C01700 and C30700 (STOP A triggered) |  | - The converter signals the following:   - C01716 and C30716 (tolerance for safe direction of motion exceeded)   - C01701 and C30701 (STOP B triggered)   - C01700 and C30700 (STOP A triggered) |  |  |
| 5. | **Acknowledge fault** |  |  |  |
| - Deselect SDI . |  |  |  |  |
| - Switch the motor off (OFF1 command). |  |  |  |  |
| - Acknowledge the fault messages with a fail-safe signal. |  |  |  |  |

###### Acceptance test for SDI negative

The two diagrams show the recommended steps to take during the acceptance test. The acceptance test differs depending on the settings you have made for SDI :

- Upper diagram: The "SDI active" checkback signal remains active when the motor is switched off.
- Lower diagram: The "SDI active" checkback signal becomes inactive when the motor is switched off.

  ![SDI acceptance for a negative direction of rotation; "SDI active" remains active when the motor is switched off](images/103409996427_DV_resource.Stream@PNG-en-US.png)

  SDI acceptance for a negative direction of rotation; "SDI active" remains active when the motor is switched off

  ![SDI acceptance for a negative direction of rotation; "SDI active" becomes inactive when the motor is switched off](images/103410001035_DV_resource.Stream@PNG-en-US.png)

  SDI acceptance for a negative direction of rotation; "SDI active" becomes inactive when the motor is switched off

"Safe Direction" (SDI) function; negative direction of rotation permitted

| No. | Description |  |  | Status |
| --- | --- | --- | --- | --- |
| 1. | **Initial state** |  |  |  |
| - The converter is in the "ready" state (p0010 = 0). |  |  |  |  |
| - The converter signals neither faults nor alarms for the safety functions (r0945[0…7], r2122[0…7]). |  |  |  |  |
| - In Startdrive , configure a trace recording with the following signals: |  |  |  |  |
|  | - Trigger: On variable bit pattern (r9722.12 = 1). |  |  |  |
| - Signals: r9714[0], r9720 and r9722. |  |  |  |  |
| - Select the time interval to be recorded and the pre-trigger so that the SDI selection and the move to the direction of rotation being monitored are displayed. |  |  |  |  |
| 2. | **Switch on the motor** |  |  |  |
| - Enter a negative speed setpoint. |  |  |  |  |
| Upper diagram:  The "SDI active" checkback signal remains active when the motor is switched off. |  | Lower diagram:  The "SDI active" checkback signal becomes inactive when the motor is switched off. |  |  |
| - Switch on the motor within five seconds of deselecting SDI (ON command). Note: If you wait longer than five seconds for the ON command, STO is activated. In this case, deselect SDI and then select it again. |  | - Switch on the motor (ON command). |  |  |
| - Check that the correct motor is rotating in the expected direction. |  |  |  |  |
| 3. | **Deactivate the setpoint limitation for the acceptance test** |  |  |  |
| - Go online with Startdrive . |  |  |  |  |
| - Activate the Acceptance mode: |  |  |  |  |
|  | ![Acceptance test](images/113493941387_DV_resource.Stream@PNG-en-US.png)   Acceptance test |  |  |  |
| 4. | **Test the set limit value** |  |  |  |
| - Change the setpoint so that the motor rotates slightly in the positive direction. |  |  |  |  |
| - In your machine, check when the drive stops when it is turning in a positive direction. |  |  |  |  |
| The rest of the process depends on the settings you made for SDI during commissioning: |  |  |  |  |
| If the converter is to respond with STOP A if the limit value is violated: |  | If the converter is to respond with STOP B if the limit value is violated: |  |  |
| - The motor coasts down to a standstill. |  | - The converter brakes the motor to a standstill. |  |  |
| - The converter signals the following:   - C01716 and C30716 (tolerance for safe direction of motion exceeded)   - C01700 and C30700 (STOP A triggered) |  | - The converter signals the following:   - C01716 and C30716 (tolerance for safe direction of motion exceeded)   - C01701 and C30701 (STOP B triggered)   - C01700 and C30700 (STOP A triggered) |  |  |
| 5. | **Acknowledge fault** |  |  |  |
| - Deselect SDI . |  |  |  |  |
| - Switch the motor off (OFF1 command). |  |  |  |  |
| - Acknowledge the fault messages with a fail-safe signal. |  |  |  |  |

###### Reduced acceptance test after expanding the function

A full acceptance test is necessary only after first commissioning. A reduced acceptance test is sufficient when safety functions are expanded.

Reduced acceptance test after expanding the function

| Measure | Acceptance test | Documentation |
| --- | --- | --- |
| Changing a single limit (e.g. SLS level). | Check the modified limit value. | - Supplement function table - Log modified settings - Document the changed checksum and time stamp<sup> 1)</sup> - Countersignature |
| Functional expansion of the machine (additional drive). | Check the safety functions of the new drive. | - Supplement machine overview - Supplement article number and firmware version of the drive - Supplement function table - Log the settings of the new drive - Document the changed checksum and time stamp<sup> 1)</sup> - Countersignature |
| Functional expansion of a drive (e.g. additional SLS level or new safety function following a firmware update). | Check the additional functions. | - Supplement function table - Log modified settings - Document the changed checksum and time stamp<sup> 1)</sup> - Countersignature |
| Transfer of converter settings to other identical machines by means of series commissioning. | Check the control and feedback signal of all safety functions. | - Supplement machine description - Log modified settings - Check the changed checksum and time stamp<sup> 1)</sup> - Check the firmware versions |
| <sup>1) </sup>The converter changes the following parameters after changing the settings of the safety functions:  - checksum r9781  - time stamp r9782 |  |  |

##### Configuring the safety functions and PROFIsafe

This section contains information on the following topics:

- [Configuring safety functions](#configuring-safety-functions-1)
- [Configuring PROFISafe](#configuring-profisafe)
- [Configuring Telegram 900, Startdrive](#configuring-telegram-900-startdrive)
- [PROFIsafe properties and configuration](#profisafe-properties-and-configuration)
- [Activate settings](#activate-settings-2)
- [Setting the PROFIsafe address under cyclic data exchange](#setting-the-profisafe-address-under-cyclic-data-exchange)
- [Setting the PROFIsafe address for basic functions](#setting-the-profisafe-address-for-basic-functions)
- [Setting the PROFIsafe address for extended functions](#setting-the-profisafe-address-for-extended-functions)
- [Checking the PROFIsafe address](#checking-the-profisafe-address)
- [Starting communication via PROFIsafe](#starting-communication-via-profisafe)

###### Configuring safety functions

###### Requirement

You are offline with Startdrive

###### **Procedure**

1. Select "Select safety functionality".

   ![Procedure](images/110718754187_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/110718754187_DV_resource.Stream@PNG-en-US.png)
2. Define the configuration of the safety functions:

   ![Procedure](images/110719259531_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/110719259531_DV_resource.Stream@PNG-en-US.png)

   - (A) You want to exclusively use the basic converter functions.

     (B) You want to use the extended safety functions.

     (C) This option is only available with a PM240‑2 or PM240P‑2 FSD ... FSF Power Module. Select this option if you only use the "STO via Power Module terminals" function
3. If you selected the basic functions or the extended functions, then you must define how the safety functions are controlled.

   ![Procedure](images/110719464331_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/110719464331_DV_resource.Stream@PNG-en-US.png)
4. Define the interface for controlling the safety functions.

You have configured the safety functions.

If you selected the onboard terminals as interface, you can now start to commission the safety functions.

For control via PROFIsafe, you must configure the PROFIsafe interface before you start to commission the safety functions.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Parameter** | **Description** |  |  |  |
| p0010 = 95 | **Drive commissioning parameter filter**   Safety Integrated commissioning |  |  |  |
| p9601 | **Enable functions integrated in the drive** (factory setting: 0000 bin) |  |  |  |
|  | Functions that have been enabled: |  | Functions that have been enabled: |  |
| 0 hex | None | 80 hex | STO via Power Module terminals |  |
| 1 hex | Basic functions via onboard terminals | 81 hex | - Basic functions via onboard terminals - STO via Power Module terminals |  |
| 4 hex | Extended functions via onboard terminals | 84 hex | - Extended functions via onboard terminals - STO via Power Module terminals |  |
| 8 hex | Basic functions via PROFIsafe | 88 hex | - Basic functions via PROFIsafe - STO via Power Module terminals |  |
| 9 hex | - Basic functions via PROFIsafe - Basic functions via onboard terminal | 89 hex | - Basic functions via PROFIsafe - Basic functions via onboard terminals - STO via Power Module terminals |  |
| C hex | Extended functions via PROFIsafe | 8C hex | - Extended functions via PROFIsafe - STO via Power Module terminals |  |
| D hex | - Extended functions via PROFIsafe - Basic functions via onboard terminals | 8D hex | - Extended functions via PROFIsafe - Basic functions via onboard terminals - STO via Power Module terminals |  |
| p9761 | **Enter a password** (factory setting: 0000 hex)  Permissible passwords lie in the range 1 … FFFF FFFF. |  |  |  |
| p9762 | **New password** |  |  |  |
| p9763 | **Confirm password** |  |  |  |

###### Configuring PROFISafe

###### **Precondition**

You are offline with Startdrive.

###### **Procedure**

Proceed as follows to set the PROFIsafe address and telegram 30:

![Procedure](images/111160917131_DV_resource.Stream@PNG-en-US.png)

1. Select "F-DI / F-DO / PROFIsafe".
2. Enter the same address as hexadecimal value that you defined in the hardware configuration for the higher-level control system.
3. Press the "Telegram configuration" button.

   Startdrive opens the "Properties" of the cyclic data exchange.
4. Select "Add telegram".
5. Insert a "Safety telegram".

You have established communication between the converter and higher-level control (F-CPU) via PROFIsafe telegram 30.

❒

| Parameter | Description |
| --- | --- |
| p9610 | **PROFIsafe address** (factory setting: 0000 hex) |

###### Configuring Telegram 900, Startdrive

###### Configuring telegram 900

**Procedure**

![Configuring telegram 900](images/111179426315_DV_resource.Stream@PNG-en-US.png)

![Configuring telegram 900](images/111180749451_DV_resource.Stream@PNG-en-US.png)

1. Select "F-DI / F-DO / PROFIsafe".
2. Press the "Telegram configuration" button.

   Startdrive opens the "Properties" of the cyclic data exchange.
3. Select "Add telegram".
4. Insert a "Safety telegram".
5. Set telegram 900.
6. Set which F-DI status of the converter is transferred via PROFIsafe status word 5.

   > **Note**
   >
   > You can transfer the status of a failsafe digital input via PROFIsafe and simultaneously use the same input to control a safety function.

You have configured PROFIsafe telegram 900.  
❒

| Parameter | Description |  |
| --- | --- | --- |
| p9501.30 | **Enable F-DI in PROFIsafe telegram**(Factory setting: 0 bin) 0 signal: F-DI is inhibited in the PROFIsafe telegram 1 signal: F-DI is enabled in PROFIsafe telegram |  |
| p10050 | **Transfer PROFIsafe F-DI** (Factory setting: 0000 bin) |  |
| Bit 0 | 0 signal: No transfer 1 signal: PROFIsafe status word 5 transfers the status of F-DI 0 |  |
| Bit 1 | 0 signal: No transfer 1 signal: PROFIsafe status word 5 transfers the status of F-DI 1 |  |
| Bit 2 | 0 signal: No transfer 1 signal: PROFIsafe status word 5 transfers the status of F-DI 2 |  |
| Settings for the discrepancy time and the signal filter of the fail-safe digital inputs:   [Setting the filter for fail-safe inputs](#setting-the-filter-for-fail-safe-inputs) |  |  |

###### PROFIsafe properties and configuration

###### Description

The safety functions can be controlled via PROFIBUS DP or PROFINET using the PROFIsafe profile. Telegrams are available for the data exchange with the higher-level controller which enable the triggering of the safety functions in the converter by the controller as well as the feedback of the status of the safety functions from the converter to the controller.

SINAMICS drives are classified as devices with PROFIsafe address type 1 for SIMATIC Safety. This means that the devices only use one fail-safe destination address (F_DEST_ADD). The fail-safe source address has no effect on the uniqueness of the PROFIsafe address.

###### Adding safety telegrams

You add a safety telegram in the standard telegram configuration for the configuration of PROFIsafe, see also [Editing telegrams](Communication%20and%20telegrams.md#editing-telegrams).

The safety-relevant parameters, such as the fields for the PROFIsafe addresses, are then displayed.

###### Unique PROFIsafe addresses

For safe operation, you must check whether the used PROFIsafe addresses are unique before starting the communication.

The uniqueness of the PROFIsafe address is only ensured by the fail-safe destination address. The PROFIsafe address must be unique throughout the network and the CPU.

- [Setting the PROFIsafe address for basic functions](#setting-the-profisafe-address-for-basic-functions)
- [Setting the PROFIsafe address for extended functions](#setting-the-profisafe-address-for-extended-functions)

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unique PROFIsafe addresses**  You must ensure the unique assignment of the PROFIsafe address throughout the network and the CPU.   - The fail-safe I/O of PROFIsafe address type 1 is addressed clearly by its fail-safe destination address. - The fail-safe destination address of the fail-safe I/O (drive units in this case) must be unique for the entire fail-safe I/O throughout the network and the CPU (system-wide). The fail-safe I/O of PROFIsafe address type 2, e.g. modules of the ET 200SP type, must also be taken into account. - Note also the corresponding documentation in the TIA Portal online help in Section "SIMATIC Safety - Configuration and programming".   (SDR001) |  |

###### Acceptance of the system

Information on the acceptance of a safety configuration with controller can be found in the TIA Portal online help under "Acceptance of the system".

> **Note**
>
> **Error-free HW and SW transmission**
>
> Error-free HW and SW transmission is the prerequisite for the creation of the safety printout for acceptance purposes. Only then is it assured that all consistency checks have been performed and therefore the safety printout created for a consistent project.

###### Recommendation for PROFIsafe addresses of drives

Use a separate number range for the PROFIsafe addresses of drives in order to distinguish the drives from all other modules. The classification of number ranges facilitates the check for uniqueness.

Example:

- PROFIsafe addresses of the drives (F_DEST_ADD) from 1100 onwards
- All other fail-safe modules from 1 to 1099

###### Activate settings

###### Loading the settings into the drive

**Procedure**

![Loading the settings into the drive](images/114171544971_DV_resource.Stream@PNG-en-US.png)

1. Save the project.
2. Select "Load to device".
3. Connect Startdrive online with the drive.
4. Press the "Start safety commissioning" button.
5. Enter the password for the safety functions.

   If the password is the factory default, you are prompted to change the password.   
   If you try to set a password that is not permissible, the old password will not be changed.
6. Press the "End safety commissioning" button.
7. Confirm the prompt for saving your settings (copy RAM to ROM).
8. Disconnect the online connection.
9. Switch off the converter power supply.
10. Wait until all LEDs on the converter go dark (no voltage condition).
11. Switch the converter power supply on again.

Your settings are now active.  
❒

| Parameter | Description |
| --- | --- |
| p9700 = D0 hex | **SI copy function** (factory setting: 0)Start the SI parameter copy function. |
| p9701 = DC hex | **Confirm data change** (factory setting: 0) Confirm the SI basic parameter change. |
| p0010 = 0 | **Drive commissioning parameter filter** 0: Ready |
| p0971 = 1 | **Save parameter**  1: Save the drive object (copy from RAM to ROM) After the converter has saved the parameters in a non-volatile fashion, then p0971 = 0. |

###### Setting the PROFIsafe address under cyclic data exchange

###### Procedure

**Setting the address**

The PROFIsafe address is displayed in the inspector window under "Cyclic data exchange".

If you work with a higher-level controller, the PROFIsafe address is automatically assigned by the controller.

If you still want to change the PROFIsafe address, proceed as described below.

> **Note**
>
> **Setting the address**
>
> You can only set the PROFIsafe address offline.
>
> The PROFIsafe address is checked for uniqueness when entered in the telegram configuration. If you enter the PROFIsafe address in parameter p9610 or via the safety parameterization in the drive, no check is made for uniqueness. You must then check the safety printout of the F-CPU and the safety messages during the compilation.

**Entering the PROFIsafe address in the telegram configuration**

1. In the inspector window, click "Cyclic data exchange" below the respective interface.
2. Click <Insert telegram> under "Cyclic data exchange".
3. Select the safety telegram that you want to use in the "Telegram" drop-down list.
4. Click "Safety setpoints / actual values" to display the "Safety setpoints / actual values" dialog box.

   The safety address is displayed in the telegram configuration at "F-address" (F_Dest_Add).

   ![PROFIsafe address in the telegram configuration](images/103409028619_DV_resource.Stream@PNG-en-US.png)

   PROFIsafe address in the telegram configuration
5. Enter the PROFIsafe address at "F address".  
   See also [Parameterizing sending (actual value/safety actual value)](Communication%20and%20telegrams.md#parameterizing-sending-actual-valuesafety-actual-value) and [Parameterizing receiving (setpoint/safety setpoint)](Communication%20and%20telegrams.md#parameterizing-receiving-setpointsafety-setpoint).
6. If the address has already been assigned in the project, an error message is displayed.

   ![PROFIsafe address error message](images/103409032331_DV_resource.Stream@PNG-en-US.png)

   PROFIsafe address error message
7. Assign a different PROFIsafe address.
8. Check the setting in the parameter view at parameter p9610.

###### Setting the PROFIsafe address for basic functions

###### Procedure

**Setting the address**

The PROFIsafe address is displayed in the following places:

- In the safety configuration in "PROFIsafe configuration"
- In the parameter view in parameter p9610 (at "Extended parameters")

If you work with a higher-level controller, the PROFIsafe address is automatically assigned by the controller.

**Checking the uniqueness of the PROFIsafe addresses through compilation**

- After changing the PROFIsafe address, compile the safety program of the controller (compile the CPU in the project navigator) in order to check the uniqueness of the PROFIsafe addresses.

If you still want to change the PROFIsafe address, proceed as described below.

> **Note**
>
> **Setting the PROFIsafe address**
>
> You can set the PROFIsafe address online and offline here.
>
> The PROFIsafe address is checked for uniqueness when entered in the telegram configuration. If you enter the PROFIsafe address in parameter p9610 or via the safety parameterization in the drive, no check is made for uniqueness. You must then check the safety printout of the F-CPU and the safety messages during the compilation.
>
> Also check whether the PROFIsafe address entered here matches the value displayed in the telegram configuration at "Cyclic data exchange".

**Enter the PROFIsafe address in the safety configuration:**

1. If you use via PROFIsafe for the basic functions, select the "Via PROFIsafe" option in the "Control type / safety functions" screen form.
2. Select "F-DI/F-DO/PROFIsafe" in the secondary navigation.
3. ① Enter the PROFIsafe address in hexadecimal format.
4. ② Click the button to jump to the telegram configuration. The PROFIsafe address is displayed there at "Safety setpoint" or "Safety actual value".

   Check whether the two values match. See [Parameterizing sending (actual value/safety actual value)](Communication%20and%20telegrams.md#parameterizing-sending-actual-valuesafety-actual-value) and [Parameterizing receiving (setpoint/safety setpoint)](Communication%20and%20telegrams.md#parameterizing-receiving-setpointsafety-setpoint).

![Setting the PROFIsafe address](images/103409103883_DV_resource.Stream@PNG-en-US.png)

Setting the PROFIsafe address

**Entering the PROFIsafe address in the parameter view**

Parameter

| Parameter | Description |
| --- | --- |
| p9610 | **PROFIsafe address** (factory setting: 0000 hex) |

###### Setting the PROFIsafe address for extended functions

###### Procedure

**Setting the address**

The PROFIsafe address is displayed in the following places:

- In the safety configuration in "PROFIsafe configuration"
- In the parameter view in parameter p9610 (at "Extended parameters")

If you work with a higher-level controller, the PROFIsafe address is automatically assigned by the controller.

**Checking the uniqueness of the PROFIsafe addresses through compilation**

- After changing the PROFIsafe address, compile the safety program of the controller (compile the CPU in the project navigator) in order to check the uniqueness of the PROFIsafe addresses.

If you still want to change the PROFIsafe address, proceed as described below.

> **Note**
>
> **Setting the PROFIsafe address**
>
> You can set the PROFIsafe address online and offline here.
>
> The PROFIsafe address is checked for uniqueness when entered in the telegram configuration. If you enter the PROFIsafe address in parameter p9610 or via the safety parameterization in the drive, no check is made for uniqueness. You must then check the safety printout of the F-CPU and the safety messages during the compilation.
>
> Also check whether the PROFIsafe address entered here matches the value displayed in the telegram configuration at "Cyclic data exchange".

**Entering the PROFIsafe address in the safety configuration**

- If you use the extended functions via PROFIsafe ①, select the "Via PROFIsafe" option in the "Control type / safety functions" screen form.

  ![Extended functions via PROFIsafe](images/103409189131_DV_resource.Stream@PNG-en-US.png)

  Extended functions via PROFIsafe
- Select "F-DI/F-DO/PROFIsafe" in the secondary navigation.

  - ① Enter the PROFIsafe address in hexadecimal format.
  - ③ Click the button to configure the routing to the F-DIs.
  - ③ Click the button to jump to the telegram configuration. The PROFIsafe address is displayed there at "Safety setpoint" or "Safety actual value".

    Check whether the two values match. See [Parameterizing sending (actual value/safety actual value)](Communication%20and%20telegrams.md#parameterizing-sending-actual-valuesafety-actual-value) and [Parameterizing receiving (setpoint/safety setpoint)](Communication%20and%20telegrams.md#parameterizing-receiving-setpointsafety-setpoint).

  ![PROFIsafe configuration](images/103409193099_DV_resource.Stream@PNG-en-US.png)

  PROFIsafe configuration

**Entering the PROFIsafe address in the parameter view**

| Parameter | Description |
| --- | --- |
| p9610 | **PROFIsafe address** (factory setting: 0000 hex) |

###### Checking the PROFIsafe address

###### Unique PROFIsafe address

To ensure safe communication, unique PROFIsafe addresses are required throughout the CPU and the network. For further information, see also [PROFIsafe properties and configuration](#profisafe-properties-and-configuration).

For this reason, it is also necessary that you check the settings of the PROFIsafe addresses carefully.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unique PROFIsafe addresses**  You must ensure the unique assignment of the PROFIsafe address throughout the network and the CPU.   - The fail-safe I/O of PROFIsafe address type 1 is addressed clearly by its fail-safe destination address. - The fail-safe destination address of the fail-safe I/O (drive units in this case) must be unique for the entire fail-safe I/O throughout the network and the CPU (system-wide). The fail-safe I/O of PROFIsafe address type 2, e.g. modules of the ET 200SP type, must also be taken into account. - Note also the corresponding documentation in the TIA Portal online help in Section "SIMATIC Safety - Configuration and programming".   (SDR001) |  |

1. For each drive, ensure that:

   - Parameter p9610 in the parameter view = "F-address" (F_Dest_Add) in the inspector window at "Cyclic data exchange".

     Or
   - Parameter p9610 in the function view of the "F-DI / F-DO PROFIsafe" dialog = "F-address" (F_Dest_Add) in the inspector window at "Cyclic data exchange".
2. Check the messages in the inspector window when compiling the safety program of the controller (compiling the CPU in the project navigator). If an address is not unique, an error is displayed for each ambiguous address.

   ![Compiler message](images/103409247499_DV_resource.Stream@PNG-en-US.png)

   Compiler message

   Switch to the telegram configuration of the appropriate device and assign a different PROFIsafe address.
3. Check the safety printout of the PLC you are using.

   Create the printout by right-clicking "Safety administration" and selecting "Print" in the shortcut menu.

   All the relevant data is listed in the printout. In the following example of a drive used as IO device, the PROFIsafe address is displayed at "F_Dest_Add".

   > **Note**
   >
   > **Error-free HW and SW transmission**
   >
   > Error-free HW and SW transmission is the prerequisite for the creation of the safety printout for acceptance purposes. Only then is it assured that all consistency checks have been performed and therefore the safety printout created for a consistent project.

   ![PROFIsafe address in the safety printout](images/103409251851_DV_resource.Stream@PNG-en-US.png)

   PROFIsafe address in the safety printout

   Compare the PROFIsafe address with the value of the drive in p9610.

   Compare this PROFIsafe address with the values of all other nodes and ensure uniqueness.

###### Starting communication via PROFIsafe

###### Start communication via PROFIsafe

When you connect the converter to the central controller via the fieldbus for the first time, the central controller sends the PROFIsafe configuration to the converter. Once the configuration data has been received, the converter interconnects its internal signals to the PROFIsafe telegram.

> **Note**
>
> **Monitoring PROFIsafe communication**
>
> The converter monitors communication with the central controller. The converter does not start monitoring communication until the configuration data has been received from the central controller.

## Parameterizing standard drives

This section contains information on the following topics:

- [G120 CU240-2](G120%20CU240-2.md#g120-cu240-2)
- [G120C](G120C.md#g120c)
- [G120D-2](G120D-2.md#g120d-2)
- [G120P](G120P.md#g120p)
- [G110M](G110M.md#g110m)
- [G120 CU250S-2 vector](G120%20CU250S-2%20vector.md#g120-cu250s-2-vector)
- [G115D](G115D.md#g115d)
