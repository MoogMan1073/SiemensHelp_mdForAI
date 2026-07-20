---
title: "Commissioning SINAMICS S210 drives"
package: StdrS210CommenUS
topics: 74
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Commissioning SINAMICS S210 drives

This section contains information on the following topics:

- [Overview](#overview)
- [Parameterization](#parameterization)
- [Rotate &amp; optimize](#rotate-optimize)

## Overview

The S210 converter can only be operated with 1FK2 type servo motors. For motors with servo control, small losses in the control precision and control quality are accepted in favor of maximum dynamic response.

Characteristic properties of the servo control are:

- Maximum computing speed
- Very short sampling times
- Maximum dynamic response
- Preferably used with permanent magnet synchronous motors with the appropriate dynamic response

Since a model calculation of the actual values cannot be used with servo control because of the required computing speed, servo control can only be operated with encoders.

## Parameterization

This section contains information on the following topics:

- [Basic parameter assignment](#basic-parameter-assignment)
- [Safety Integrated](#safety-integrated)
- [Inputs/outputs](#inputsoutputs)

### Basic parameter assignment

This section contains information on the following topics:

- [Basic parameter assignment](#basic-parameter-assignment-1)

#### Basic parameter assignment

##### Description

You can parameterize the most important operating parameters for S210 in the basic settings. These include:

- Device supply voltage
- Direction of rotation
- Speed limit
- Torque limit
- Ramp-down times (following an OFF1 command and for a fast stop OFF3)
- Forced opening of the brake

> **Note**
>
> **Basic parameterization also possible online**
>
> Basic parameterization of the S210 Control Unit is possible offline as well as online.
>
> By contrast, basic parameterization for other Control Units (e.g. S120) is only possible offline.

##### Performing basic parameterization

1. The device supply voltage is preset and depends on the selected drive version.   
   Should you wish to specify another supply voltage, correct the specified supply voltage in the input field of the same name ([p0210](SINAMICS%20Parameter%20SINAMICS%20S210.md#p0210-drive-unit-line-supply-voltage)).
2. The motor ambient temperature is preassigned with 40 °C. Correct the value in the text box "Motor ambient temperature" ([p0613](SINAMICS%20Parameter%20SINAMICS%20S210.md#p06130-motor-temperature-model-ambient-temperature)) if the ambient temperature is different.

   The underlying temperature model uses the motor ambient temperature to calculate the thermal motor utilization.
3. The direction of rotation last set for the motor is displayed in the "Direction of rotation" drop-down list ([p1821](SINAMICS%20Parameter%20SINAMICS%20S210.md#p18210-direction-of-rotation)[0]). If you want to adjust the counter-rotational direction, select the desired direction of rotation from the drop-down list:

   - [0] Right
   - [1] Left
4. The positive and negative speed limit is preassigned.   
   If you want to change this pre-assignment, correct the values in the "Speed limit positive" ([p1083](SINAMICS%20Parameter%20SINAMICS%20S210.md#p10830-speed-limit-positive)[0]) or "Speed limit negative" fields ([p1086](SINAMICS%20Parameter%20SINAMICS%20S210.md#p10860-speed-limit-negative)[0]).
5. If you want to define the fixed upper or motor torque limit, enter an appropriate value in the "Torque limit upper" field ([p1520](SINAMICS%20Parameter%20SINAMICS%20S210.md#p15200-torque-limit-upper)[0]).
6. If you want to define the fixed lower torque limit or torque limit when generating, enter an appropriate value in the "Torque limit lower" field ([p1521](SINAMICS%20Parameter%20SINAMICS%20S210.md#p15210-torque-limit-lower)[0]).
7. A ramp-down time in which the speed setpoint is decelerated from maximum speed to a complete stop following OFF3 can be specified for the deceleration ramp.   
   In this case, enter a ramp-down time in the "Quick stop (OFF3 ramp-down time)" field ([p1135](SINAMICS%20Parameter%20SINAMICS%20S210.md#p11350-off3-ramp-down-time)).
8. Then save the project to accept the settings.

##### Switching the positive opening of the brake on/off

You can activate positive opening of the brake if the motor being used is equipped with a standard motor holding brake.

By default, an existing motor holding brake is controlled in an S210 drive unit depending on the operating state of the drive. A pulse suppression then automatically leads to the closing of the brake.

You can change this default S210 setting and activate a positive opening of the brake instead. The motor holding brake is then always open.

1. Click on the "Positive opening of brake" button ([p1215](SINAMICS%20Parameter%20SINAMICS%20S210.md#p1215-motor-holding-brake-configuration) = 2).

   The motor holding brake is now permanently open.
2. If you want to switch the motor holding brake on again, click on the "End positive opening of brake" button.

##### Additional parameters

---

---

**See also**

[Inserting and specifying motors](Configuring%20SINAMICS%20S210%20drives.md#inserting-and-specifying-motors)

### Safety Integrated

This section contains information on the following topics:

- [Safety Integrated overview (S210)](#safety-integrated-overview-s210)
- [Specific safety instructions and information](#specific-safety-instructions-and-information)
- [Basic settings](#basic-settings)
- [Basic Functions](#basic-functions)
- [Extended Functions](#extended-functions)
- [Response to Safety faults](#response-to-safety-faults)
- [Actual value acquisition/mechanical system](#actual-value-acquisitionmechanical-system)
- [Control](#control)
- [Test stop](#test-stop)
- [Function status](#function-status)
- [Acceptance mode](#acceptance-mode)

#### Safety Integrated overview (S210)

##### Description

The SINAMICS S210 drives feature the following drive-integrated safety functions:

Overview of Safety Integrated Functions

|  | Functions | Abbr. | Brief description |
| --- | --- | --- | --- |
| Basic  Functions | Safe Torque Off | STO | Safe Torque Off |
| Safe Stop 1 | SS1 | Safe stop according to stop category 1 |  |
| Safe Brake Control | SBC | Safe Brake Control |  |
| Extended  Functions | Safe Torque Off | STO | Safe Torque Off |
| Safe Stop 1 | SS1 | Safe stop according to stop category 1 |  |
| Safe Brake Control | SBC | Safe Brake Control |  |
| Safe Operating Stop | SOS | Safe monitoring of the standstill position |  |
| Safe Stop 2 | SS2 | Safe stop according to stop category 2 |  |
| Safely-Limited Speed | SLS | Safe monitoring of the maximum velocity |  |
| Safe Speed Monitor | SSM | Safe detection of the violation of a low velocity threshold |  |
| Safe Direction | SDI | Safe monitoring of the direction of motion |  |
| Safe Brake Test<sup>1)</sup> | SBT | **Diagnostic function**   Safe test of the required holding torque  of a brake |  |
| Safe Acceleration Monitor | SAM | Safe monitoring of drive acceleration |  |
| Safely-Limited Acceleration | SLA | Safely-Limited Acceleration |  |
| Safe Brake Ramp | SBR | Safe Brake Ramp |  |
| <sup>1)</sup> The Safe Brake Test is purely a **diagnostic function**, but for organizational reasons is included in the list of Safety Integrated Extended Functions. |  |  |  |

> **Note**
>
> **Safety-capable encoders**
>
> The SIMOTIC 1FK2 motors for SINAMICS S210 drives are generally equipped with safety-capable encoders.
>
> However, safety-capable encoders are not used for SINAMICS S120 drives with other motor types. Therefore, when using S210 and S120 drives together in one system, please note that Safety Integrated Functions cannot be used in conjunction with non-safety-capable encoders.

**Activating the Safety commissioning**

Before the safety functions are edited, the Safety commissioning must be activated and the safety functionality selected:

- [Starting and Ending Safety Integrated commissioning](#starting-and-ending-safety-integrated-commissioning)
- [Selecting the safety functionality (S210)](#selecting-the-safety-functionality-s210)

**Safety Integrated Functions**

Detailed information about Safety Integrated Functions can be found at:

- [Basic Functions](#basic-functions)
- [Extended Functions](#extended-functions)

**PROFIsafe**

For PROFIsafe, you require a telegram extension that you can set in the "Control" screen form under the "Telegram configuration" link.

#### Specific safety instructions and information

This section contains information on the following topics:

- [Safety Integrated safety instructions](#safety-integrated-safety-instructions)
- [Residual risk](#residual-risk)
- [Further information](#further-information)

##### Safety Integrated safety instructions

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Inactive Safety Integrated Functions during ramp-up after switching on**  The Safety Integrated Functions are only activated after the system has completely powered up. System startup is a critical operating state with increased risk. When accidents occur, this can result in death or severe injury.   - Stay completely away from any hazardous areas while the system powers up. - For vertical axes, check that the drives are in a no-torque state. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Undesirable motor movements during automatic restart**  The Emergency Stop function must bring the machine to a standstill according to stop category 0 or 1 (STO or SS1) (EN 60204-1). Persons within the hazardous area are at risk of serious injury or even fatalities whenever an automatic restart is initiated following an emergency stop.   If individual safety functions (Extended Functions) are deactivated, an automatic restart is permitted under certain circumstances depending on the risk analysis (except when Emergency Stop is reset). An automatic start is permitted when a protective door is closed, for example.  - For the cases listed above, ensure that an automatic restart is absolutely not possible. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Undesirable drive movements during power up of the system following modification or replacement of hardware and/or software**  After hardware and/or software components have been modified or replaced, it is only permissible for the system to run up and the drives to be activated with the protective devices closed. Changes to the system that have not been thoroughly tested can initiate undesirable functions. For persons in the hazardous area, this can result in death or severe injury.   - Carry out the following tests after a change or replacement (see [Acceptance test](Safety%20Integrated%20acceptance%20test.md#sinamics-safety-integrated-acceptance-test)):    - A complete acceptance test   - A partial acceptance test   - A simplified function test - Before personnel may re-enter the hazardous area, the drives MUST be tested to ensure that they exhibit stable control behavior by briefly moving them in both the plus and minus directions (+/–). - Ensure that nobody is in the hazardous area during the test. - When switching on, carefully observe that Safety Integrated Functions are only available and can only be selected after the system has completely powered up. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unanticipated movement of the drive**  When the energy supply has been disconnected (STO active), unanticipated movements of the drive may occur (e.g. coasting down) and thus pose a hazard to persons.  - Take suitable measures to prevent undesirable movement, e.g. by using a brake with safe monitoring. |  |

> **Note**
>
> **Risk minimization through Safety Integrated**
>
> Safety Integrated can be used to minimize the level of risk associated with machines and plants.   
> However, safe operation of a system or machine based on Safety Integrated is only possible if the following requirements are fully satisfied:
>
> - The machine builder (OEM) precisely knows and observes this technical user documentation – including the documented limitations, safety information and residual risks.
> - The machine builder (OEM) carefully and professionally designs, constructs and configures the system/machine. This must then be verified through careful and thorough acceptance tests by qualified personnel and the results documented.
> - The machine builder (OEM) implements and validates all the measures required in accordance with the system/machine risk analysis by means of the programmed and configured Safety Integrated Functions or by other means.
>
> The use of Safety Integrated does not replace the machine/plant risk assessment carried out by the machine manufacturer as required by the EC machinery directive.   
> In addition to using Safety Integrated Functions, further risk reduction measures must be implemented.

##### Residual risk

The fault analysis enables machine manufacturers to determine the residual risk at their machine with regard to the drive unit. The following residual risks are known:

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Brief limited movements of the motor**  Simultaneous breakdown of 2 power transistors in the power unit can cause a short, limited movement. This can result in accidents leading to death or severe injury.  - If there is a danger of undesirable movement in your application, you must take the appropriate measures to prevent this, e.g. by using a brake with safe monitoring (see "Safe Brake Control") |  |

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Overshooting the speed or position that briefly violates the limit value**  A limit violation may briefly lead to a speed higher than the speed setpoint, depending on the dynamic response of the drive and on parameter settings. The prescribed position can be more or less overtraveled. This can cause damage to the drive.   - Configure the machine to ensure that the prescribed position can be overtraveled as minimally as possible. |  |

If the encoder signals become static (that is, they no longer follow a movement while still returning a correct level) for a stationary drive (e.g. in SOS), this fault will not be detected.

| Possible causes | Consequences/Remedies |
| --- | --- |
| Single electrical fault in the encoder | The fault must be entered in the risk analysis of the machine manufacturer. Additional safety measures must be taken for drives with suspended/vertical or pulling loads, e.g. in order to exclude the fault.   - Use an encoder with analog signal generation. |
| An encoder shaft breakage (or slipping of the encoder shaft coupling) or loosening of the encoder enclosure fastening | Run an FMEA:   - for the encoder shaft breakage (or the encoder shaft coupling slips) - to loosen the encoder housing fastening and using a fault exclusion according to, e.g. IEC 61800-5-2 |

Generally, the drive is held by the active closed-loop control. Especially for drives with suspended load, from a closed-loop control perspective, it is conceivable that drives such as these move without this being detected.

##### Further information

As well as the information regarding "Safety Integrated" in this online help, further detailed information may also be obtained in the SINAMICS S120 Safety Integrated Function Manual. In particular, we recommend the following chapters in this Function Manual for additional information:

- System features

  Information regarding certifications, probabilities of failure, and response times.
- Maintenance

  Information regarding component replacement, firmware updates, Safety faults, and Safety message buffer.
- Standards and regulations

  Information on standards and regulations in the EU, USA and Japan, as well as equipment specifications and additional sources of information pertaining to "Safety".

#### Basic settings

This section contains information on the following topics:

- [License for Extended Functions required](#license-for-extended-functions-required)
- [Starting and Ending Safety Integrated commissioning](#starting-and-ending-safety-integrated-commissioning)
- [Selecting the safety functionality (S210)](#selecting-the-safety-functionality-s210)
- [Making basic settings](#making-basic-settings)
- [Accepting the safety settings](#accepting-the-safety-settings)
- [Changing the Safety Integrated password](#changing-the-safety-integrated-password)
- [Difference between Emergency Off and Emergency Stop](#difference-between-emergency-off-and-emergency-stop)

##### License for Extended Functions required

For function packages subject to license, such as Safety Integrated Extended Functions, a memory card is required with a license key. An insufficient license is indicated via the following fault and LED:

- F13000 → License not sufficient
- LED RDY → flashes red at 2 Hz

  ![Figure](images/147857939211_DV_resource.Stream@PNG-en-US.png)

**Overview of licenses**

Startdrive provides a "License overview" page. This shows the most important information about the licenses and the license status of your drive system; see [License overview](Configuring%20SINAMICS%20S-G-MV%20drives.md#overview-of-licenses).

**Trial License Mode**

The drive system can only be operated with an insufficient license for an option during commissioning and servicing. For this purpose, the Trial License Mode must be activated explicitly, see [Trial License Mode](Configuring%20SINAMICS%20S-G-MV%20drives.md#activate-trial-license-mode).

**Displaying/acquiring the license key**

You can display the currently entered license key or enter a new license key via the "License overview" page; see [License key](Configuring%20SINAMICS%20S-G-MV%20drives.md#displayingentering-a-license-key).

##### Starting and Ending Safety Integrated commissioning

###### Requirement

For safety reasons, you can only set the Safety Integrated-relevant parameters of the 1st channel offline with the Startdrive commissioning tool. If the drive is online, the data of the 1st channel is automatically duplicated in the 2nd channel. You can protect the settings with a password.

###### Activate/deactivate editing mode

The editing mode must be activated in the online mode in order to configure the safety functions.

| Symbol/button | Description |
| --- | --- |
| ![Activate/deactivate editing mode](images/147854075915_DV_resource.Stream@PNG-en-US.png) | Startdrive is not online. You can only edit the Safety Integrated Functions offline.   - Activate the online mode. |
| ![Activate/deactivate editing mode](images/147854079883_DV_resource.Stream@PNG-en-US.png) | Status: The editing mode is not activated yet.   - Click the ![Activate/deactivate editing mode](images/147857968779_DV_resource.Stream@PNG-en-US.png) icon to activate the editing mode. |
| ![Activate/deactivate editing mode](images/147854083851_DV_resource.Stream@PNG-en-US.png) | Status: The editing mode is active. In addition to the safety marking, a "pencil" ![Activate/deactivate editing mode](images/147857964811_DV_resource.Stream@PNG-en-US.png) is displayed in the secondary navigation.   - Click the ![Activate/deactivate editing mode](images/147857972747_DV_resource.Stream@PNG-en-US.png) icon to exit the editing mode. |

###### Activating the Safety Integrated settings and entering the password​

Proceed as follows to activate the Safety Integrated settings:

1. Click the "Connect online" symbol.
2. Click the ![Activating the Safety Integrated settings and entering the password​](images/147857968779_DV_resource.Stream@PNG-en-US.png) symbol in the toolbar of the parameterization editor.

   The "Password input" screen form is displayed.
3. Enter the password.

   You only have to enter a new password at the first start to replace the "not secure" default password.
4. Once all necessary settings have been made, click "Close".

   The dialog closes.

##### Selecting the safety functionality (S210)

###### Making basic settings

1. In the secondary navigation, execute "Safety Integrated &gt; Function selection".
2. Select between the following in the first drop-down list:

   - No Safety Integrated Function
   - Basic Functions
   - Extended Functions

     A drop-down list for setting the encoder option becomes active:
3. Select from the "Control type" drop-down list between:

   - via onboard terminals (Basic Functions only)

     if you want to use the fail-safe digital I/Os of a drive.
   - via PROFIsafe

     if you want to control the safety functions from a higher-level controller (see [Control](#control)).  
     With the "Extended Functions" setting, the control type "via PROFIsafe" is preset and cannot be changed.
4. The "Basic Functions via onboard terminals" option can be selected for the following settings:

   - "Basic Functions" with "via PROFIsafe" control type
   - "Extended" with "via PROFIsafe" control type

   With this setting, you can use the fail-safe digital I/Os of a drive as well as control the safety functions from a higher-level controller (see [Control](#control)).
5. Then activate the Safety Integrated Functions that you require in the lower part of the dialog.

   Startdrive only displays the functions that belong to the function selection you made. The preselected functions cannot be deselected. The entries for the selected and preselected functions are displayed in the secondary navigation.
6. Click the buttons (or the entry in the secondary navigation) to parameterize the desired Safety function.

###### Result

The basic settings for Safety Integrated have been made. The desired Safety Integrated Functions have been activated and also enabled with the activation. The activated Safety Integrated Functions are active with specified default settings. You can change these default settings in the Details screen forms according to your requirements.

##### Making basic settings

###### Making the basic settings for the Safety Integrated Basic Functions

1. Select the "Basic Functions" safety function in the first drop-down list:

   The screen form is then extended with the additional setting options (see below).
2. Select one of the following settings in the "Control type" drop-down list:

   - via PROFIsafe

     if you want to control the safety functions from a higher-level controller.
   - via onboard terminals

     if you want to use the fail-safe digital I/Os of a drive.

   The associated Basic Functions are then active in the lower part of the screen form and can be parameterized.
3. Activate or deactivate the "Basic Functions via onboard terminals" option.

   The associated extended Safety Integrated Functions are then active in the lower part of the screen form and can be parameterized:

   - Stop functions
   - Braking functions
4. Activate all Safety Integrated Functions which you would like to use.

   Startdrive only displays the functions that belong to the function selection you made. The preselected functions cannot be deselected. The entries for the selected and preselected functions are displayed in the secondary navigation.
5. Click on the button for the desired Safety Integrated Basic Function.

   The corresponding screen form is displayed and can be parameterized (see "[Basic Functions](#basic-functions)").

###### Making the basic settings for the Safety Integrated Extended Functions

1. Select the "Extended Functions" safety function in the first drop-down list:

   The screen form is then extended with the additional setting options (see below). The "via PROFIsafe" option is a fixed control type setting. The safety functions are controlled by a higher-level controller with this option.
2. Activate or deactivate the "Basic Functions via onboard terminals" option.

   The associated Extended Functions are then active in the lower part of the screen form and can be parameterized:

   - Stop functions
   - Braking functions
   - Motion monitoring functions
3. Activate all Safety Integrated Functions which you would like to use.

   Startdrive only displays the functions that belong to the function selection you made. The preselected functions cannot be deselected. The entries for the selected and preselected functions are displayed in the secondary navigation.
4. Click the button for the required Safety Integrated Extended Function.

   The corresponding screen form is displayed and can be parameterized (see "[Extended Functions](#extended-functions)").

###### Result

The basic settings for Safety Integrated have been made. The desired Safety Integrated Functions have been activated and also enabled with the activation. The activated Safety Integrated Functions are active with specified default settings. You can change these default settings in the Details screen forms according to your requirements.

##### Accepting the safety settings

After you have parameterized all safety functions, the drive must accept the settings.

> **Note**
>
> To accept the settings in the drive, it must be online.

1. To accept the settings and deactivate the safety functions, click the symbol in the title bar.

   ![Figure](images/147858070923_DV_resource.Stream@PNG-en-US.png)

   ![Figure](images/147858070923_DV_resource.Stream@PNG-en-US.png)

   The following steps are executed:

   - The parameter settings are copied from CPU 1 to CPU 2.
   - Copy RAM to ROM is offered.
   - Safety mode is deactivated, the symbol now has a yellow border.
2. Go offline with the drive.

You can now continue with the parameter assignment of the "normal" settings. The dialog are no longer deactivated.

##### Changing the Safety Integrated password

The Safety Integrated password protects Safety Integrated parameters against maloperation. Always assign a strong password, to enable protection. To reset the password to the factory setting, you require the valid password.

> **Note**
>
> The Safety password is write protection specified in the appropriate standards to prevent against maloperation by unauthorized users.
>
> The password must include the following elements to provide better protection against unauthorized access, e.g. by hackers:
>
> - At least 8 characters
> - Upper and lower case letters
> - Numbers and special characters (e.g.: ?!%+ ...)
>
> The Safety password must not be used anywhere else.
>
> **Checking the password**
>
> The drive checks the length of the password. There is no check for special characters or upper and lower case letters.

> **Note**
>
> **Project protection to encrypt passwords**
>
> Using a message ![Figure](images/147853400715_DV_resource.Stream@PNG-en-US.PNG), Startdrive recommends encrypting Safety Integrated passwords using the project protection ("Security settings").
>
> - If you activate project protection for user administration in the TIA Portal, then all parameters and passwords within the project are encrypted.
>
> Detailed information on project protection can be found in the online help under "Managing users and roles".

###### Requirement

- The drive axis is ONLINE.

  The Safety Integrated password can only be read or changed in online mode.

###### Changing the Safety Integrated password

To change the Safety Integrated password, proceed as follows:

1. Click "Enter password" in the secondary navigation.
2. Enter the current password.
3. Enter the new password.
4. Repeat entry of the new password.
5. Click the "Change password" button to accept the new password.

##### Difference between Emergency Off and Emergency Stop

"Emergency Off" and "Emergency Stop" are commands that minimize different risks in the machine or plant.

| Symbol | Meaning |
| --- | --- |
| **Emergency Off**   Risk of electric shock.    ![Figure](images/147857881867_DV_resource.Stream@PNG-en-US.png) | **Emergency Stop**   Risk of unexpected motion.    ![Figure](images/147857886091_DV_resource.Stream@PNG-en-US.png) |

Measures and solutions

| Command | Emergency Off | Emergency Stop |
| --- | --- | --- |
| Measure to minimize risk | **Safe switch off**   Switching off the electric power supply for the installation, either completely or partially. | **Safely stop and safely prevent restarting**   Stopping or preventing the dangerous movement |
| Classic solution | Switch off the power supply.    ![Figure](images/147857890315_DV_resource.Stream@PNG-en-US.png) | Switch off the drive power supply.    ![Figure](images/147857894539_DV_resource.Stream@PNG-en-US.png) |
| Solution with the STO safety function integrated in the drive | STO is not suitable for safely switching off a voltage. | Select STO.    ![Figure](images/147857898763_DV_resource.Stream@PNG-en-US.png)   It is permissible that you switch off the converter power supply as well. However, switching off the voltage is not required as a risk-reduction measure. |

#### Basic Functions

This section contains information on the following topics:

- [Safe Torque Off (STO) mode of operation](#safe-torque-off-sto-mode-of-operation)
- [Safe Brake Control (SBC) mode of operation](#safe-brake-control-sbc-mode-of-operation)
- [Safe Stop 1 (time-controlled) mode of operation](#safe-stop-1-time-controlled-mode-of-operation)
- [Configuring STO/SS1/SBC](#configuring-stoss1sbc)

##### Safe Torque Off (STO) mode of operation

###### Overview

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/148125270667_DV_resource.Stream@PNG-en-US.png) |  |

The safety function "Safe Torque Off" (STO) causes no torque or force-producing energy to be supplied to the motor. This function corresponds to stop category 0 to EN 60204-1.

If the motor is still rotating when STO is selected, then it coasts down to standstill.

###### Functional characteristics

The switching on inhibited prevents an automatic restart after deselection of STO and therefore satisfies the requirements of EN 60204-1. Consequently, the STO function prevents an electrically-driven machine component from restarting.

> **Note**
>
> There is no galvanic isolation between motor and drive.

You can select the STO function via PROFIsafe and/or the Failsafe Digital Input (F-DI).

###### Applications

- Applications include all machines and systems with moving axes (e.g. conveyor technology, handling).
- STO is suitable for applications where the motor is already at a standstill or will come to a standstill in a short, safe period of time as a result of friction.
- STO allows you to work safely on the machine with the protective door open. A classic Emergency Stop with electromechanical isolation is not required. The drive remains connected to the line and can be fully diagnosed.

> **Note**
>
> **The distinction between Emergency Off and Emergency Stop**
>
> "Emergency Off" and "Emergency Stop" are commands that minimize different risks in the machine or plant.
>
> The STO function is suitable for implementing an Emergency Stop - but not an Emergency Off.

###### Flow diagram

![Sequence: STO](images/148125274891_DV_resource.Stream@PNG-en-US.png)

Sequence: STO

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - During operation, STO is selected via PROFIsafe and/or F-DI. |
| 2 | - After the response time, the drive immediately initiates safe pulse suppression.    This safely interrupts the torque-generating energy fed to the motor. - The motor coasts down to a standstill. - STO safely prevents the motor restarting. |
| 3 | - STO is deactivated by the drive with (manual or automatic program-controlled) deselection. - The drive is again "ready for switching on". |
| 4 | - You restart the drive with a positive signal edge at ON/OFF1. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - STO is selected via the control bit of the selected PROFIsafe telegram or via the F-DI. |
| B | - The "STO_active" status is signaled in the status bit of the PROFIsafe telegram.   This value can be applied in the higher-level controller. |
| C | - The Safety error is acknowledged with selection/deselection of the STO function.    Any active messages of additional safety functions are acknowledged simultaneously with extended message acknowledgment (p9507.0 = 1). The standard acknowledgment mechanism must be executed in addition. |

###### Selecting/deselecting "Safe Torque Off"

If "Safe Torque Off" is selected, the motor holding brake is closed (if connected and configured).

Deselecting "Safe Torque Off" represents an internal safety acknowledgment. The following happens once the cause of the fault has been eliminated:

1. The Safety requirement "Close motor holding brake" is canceled.
2. The possibly active F01611 message or STO is withdrawn.
3. In addition, reset the messages in the fault buffer using the general acknowledgment mechanism.

##### Safe Brake Control (SBC) mode of operation

###### Overview

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/148125311499_DV_resource.Stream@PNG-en-US.png) |  |

The "Safe Brake Control" function (SBC) is used to safely control the motor-integrated holding brake, which operates according to the closed-circuit principle.

###### Functional characteristics

You must enable the function when commissioning in order that SBC can become active.

> **Note**
>
> You cannot select SBC as an autonomous function: SBC is activated (if enabled) immediately upon selection of STO.

###### Applications

Use SBC in applications where the drive must maintain a safe position, even when the motor is in a no-current condition. SBC thus prevents suspended or passing loads from dropping (e.g. for lifting gear, passenger elevators, winders). No external logic or switching elements required, as the functionality is completely integrated in the drive.

> **Note**
>
> **Condition of the motor holding brake**
>
> SBC is not able to identify as to whether a holding brake is mechanically worn or is a defective.
>
> As a consequence, observe the maximum permissible number of emergency braking operations for the motor holding brake being used.

###### Flow diagram

![Sequence: SBC](images/148125315595_DV_resource.Stream@PNG-en-US.png)

Sequence: SBC

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - STO is selected in operation. - At the same time, the drive activates SBC. - Taking the brake closing time into account, the command to close the motor holding brake closes the brake, thus supporting the shutdown process initiated by STO. |
| 2 | - The mechanical brake brakes the motor to a standstill. |
| 3 | - STO is deactivated by the drive with (manual or automatic program-controlled) deselection. - The drive is again "ready for switching on". - SBC is also simultaneously deactivated with deselection of STO. The brake remains (unsafely) closed, however, until the standard program executes the command to open the brake |
| 4 | - You restart the drive with the ON/OFF1 signal.    Taking the brake opening time into account, the command to open the brake opens the brake. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - STO is selected via the control bit of the selected PROFIsafe telegram or via the F-DI. - The drive activates SBC when the safe brake control is enabled (p9602 = 1). - The drive triggers SBC simultaneously with STO. - Brake management is resulted within the context of standard parameterization of the drive. |

For the "Safe Brake Control" function, the drive assumes a control function and ensures the following behavior:

- If the drive detects a fault or failure of the brake, it deactivates the brake current.
- The brake closes and a safe state is reached.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected movements of the motor due to defective brake**  "Safe Brake Control" function does not detect mechanical defects of the brake. An interrupted cable or a short-circuit in the brake winding is only detected when the state changes, i.e. when the brake either opens or closes.   The defects described above may initiate unwanted motor motion, which may result in injury or death.  - In particular, ensure the brake is not powered from an external source. Information on this topic can be found in EN 61800‑5‑2:2007, Appendix D. - If you use the Safety Integrated Extended Functions, perform a test of the brakes during commissioning with the aid of the "Safe Brake Test (SBT)" diagnostic function: |  |

##### Safe Stop 1 (time-controlled) mode of operation

###### Overview

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/148125378315_DV_resource.Stream@PNG-en-US.png) |  |

The "Safe Stop 1" function (SS1, time-controlled) causes a drive-autonomous deceleration of the motor and initiates the "Safe Torque Off" (STO) function after a predefined time interval has elapsed. This function corresponds to stop category 1 to EN 60204‑1.

###### Functional characteristics

The Safety Integrated Basic Function "Safe Stop 1" is available in the following versions:

- SS1 with OFF3 (SS1-t according to IEC 61800-5-2)
- SS1 with external stop (SS1E-t)

Set the SS1 response for Safety commissioning in the "Parameterization" step.

###### Applications

SS1 can be applied in the following cases:

- The load torque cannot reduce the motor to a standstill through friction within a sufficiently short time.
- Coasting down of the drive (STO) will pose risks to safety.

###### SS1 with OFF3 (SS1-t)

When SS1-t is selected, the motor speed is reduced along the OFF3 ramp for the duration of the selected delay time. After the delay time expires, the drive activates the STO function (independent of the actual speed).

> **Note**
>
> Braking at the OFF3 ramp is not monitored!

**Flow diagram SS1 with OFF3 (SS1-t)**

![Sequence: SS1](images/148125382539_DV_resource.Stream@PNG-en-US.png)

Sequence: SS1

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - SS1 is selected in operation. |
| 2 | - The drive immediately initiates braking following the response time via the OFF3 ramp. - At the same time, the drive initiates the SS1 delay time. |
| 3 | - The drive triggers STO once the SS1 delay time has elapsed. - The motor coasts down to a standstill. - STO safely prevents the motor restarting. |
| 4 | - SS1 and STO are deactivated by the drive with (manual or automatic program-controlled) deselection. - The drive is again "ready for switching on". |
| 5 | - You restart the drive with the ON/OFF1 signal. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - SS1 is selected via the control bit of the selected PROFIsafe telegram or via the F-DI. |
| B | - The drive brakes the motor along the OFF3 ramp. - Once the SS1 delay time (p9652) has expired, the drive automatically triggers STO independently of the current speed. |
| C | - The "SS1_active" status is signaled in the status bit of the PROFIsafe telegram. - This value can be applied in the higher-level controller. - When STO becomes active, the "SS1_active" status is also signaled in the status bit of the PROFIsafe telegram. |

###### SS1 with external stop (SS1E-t)

If several drives are connected with one another through a material web, then braking initiated by a single drive at the related OFF3 ramp can damage the machine or system.

When the safety function SS1E-t is used, the drive is shut down using the user program of a higher-level control system. Although the safe delay time is activated when SS1E-t is selected, OFF3 is not activated. Using an appropriate program, the control must then ramp down the drives involved within the delay time to the safe state. After the delay time has elapsed, the drive activates the STO function and safely interrupts the energy feed to the motor (independent of the actual speed).

**Sequence diagram, SS1 with external stop (SS1E-t)**

![Sequence: SS1](images/148125382539_DV_resource.Stream@PNG-en-US.png)

Sequence: SS1

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - SS1 is selected in operation. |
| 2 | - The control system initiates stopping using the setpoint that is entered. - At the same time, the drive initiates the SS1 delay time. |
| 3 | - The drive triggers STO once the SS1 delay time has elapsed. - The motor coasts down to a standstill. - The pulse inhibit safely prevents the motor restarting. |
| 4 | - SS1 and STO are deactivated by the drive with (manual or automatic program-controlled) deselection. - The drive is again "ready for switching on". |
| 5 | - You restart the drive with the ON/OFF1 signal. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - To use SS1E, set the braking response (p9507.3 = 1) to "SS1E external stop". - SS1 is selected via the control bit of the selected PROFIsafe telegram or via the F-DI. |
| B | - The motor is braked by the external setpoint that is entered. - Once the SS1 delay time (p9652) has expired, the drive automatically triggers STO independent of the actual speed. |
| C | - The "SS1_active" status is signaled in the status bit of the PROFIsafe telegram. - This value can be applied in the higher-level controller. - When STO becomes active, the "SS1_active" status is also signaled in the status bit of the PROFIsafe telegram. |

> **Note**
>
> **SS1 cannot be interrupted**
>
> - If SS1 is deselected again during this time, the STO function is selected and deselected again by the drive immediately after the delay time has elapsed or the speed has dropped below the shutdown speed. This terminates the SS1 function normally. It cannot be interrupted.
> - During the delay time, SS1 cannot be deselected by withdrawing the control command, therefore fulfilling the requirements of EN 60204‑1 relating to an Emergency Stop function.

###### Setting the delay time for SS1

Select the SS1 delay time so that the drive can travel the complete OFF3 ramp, and close any motor holding brake before the torque is safely switched off.

The OFF3 ramp-down time must be orientated to the actual braking capacity of the system or machine.

Use the following procedure to select the SS1 delay time:

- SS1 delay time with parameterized motor holding brake

  SS1 delay time (p9652) ≥ OFF3 ramp-down time (p1135) + pulse suppression delay time (p1228) + motor holding brake closing time (p1217)
- SS1 delay time, without parameterized motor holding brake:

  SS1 delay time (p9652) ≥ OFF3 ramp-down time (p1135) + pulse suppression delay time (p1228)

##### Configuring STO/SS1/SBC

###### Description

In the "STO/SS1/SBC" screen form you can parameterize the Safe Torque Off (STO), Safe Stop 1 (SS1) and Safe Brake Control (SBC) functions via onboard terminals and PROFIsafe.

###### Configuring Safety Integrated Functions

1. Click the ![Configuring Safety Integrated Functions](images/148125432331_DV_resource.Stream@PNG-en-US.png) button (Select STO) to configure the "STO" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Basic Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Call the "STO/SS1/SBC" Safety Integrated Function again.
3. To configure the "SS1" function, set the delay time until the start of "STO" in the "Safe Stop 1 delay time" ([p9652](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9652-si-ss1-delay-time)) field.
4. Click "Save project" in the toolbar to save the changes in the project.

**Result**

You have configured the Safety Integrated Basic Functions.

###### Additional parameters

- [p9601](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9601-si-enable-functions-integrated-in-the-drive)
- [r9720](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9720028-si-motion-control-signals-integrated-in-the-drive)
- [r9722](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9722028-si-motion-drive-integrated-status-signals)

---

#### Extended Functions

This section contains information on the following topics:

- [STO/SBC](#stosbc)
- [SS1](#ss1)
- [SS2](#ss2)
- [SOS](#sos)
- [SBT](#sbt)
- [SLS](#sls)
- [SSM](#ssm)
- [SDI](#sdi)
- [SLA](#sla)

##### STO/SBC

This section contains information on the following topics:

- [Safe Torque Off (STO) mode of operation](#safe-torque-off-sto-mode-of-operation-1)
- [Safe Brake Control (SBC) mode of operation](#safe-brake-control-sbc-mode-of-operation-1)
- [Configuring STO/SBC](#configuring-stosbc)

###### Safe Torque Off (STO) mode of operation

###### Overview

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/148125270667_DV_resource.Stream@PNG-en-US.png) |  |

The safety function "Safe Torque Off" (STO) causes no torque or force-producing energy to be supplied to the motor. This function corresponds to stop category 0 to EN 60204-1.

If the motor is still rotating when STO is selected, then it coasts down to standstill.

###### Functional characteristics

The switching on inhibited prevents an automatic restart after deselection of STO and therefore satisfies the requirements of EN 60204-1. Consequently, the STO function prevents an electrically-driven machine component from restarting.

> **Note**
>
> There is no galvanic isolation between motor and drive.

You can select the STO function via PROFIsafe and/or the Failsafe Digital Input (F-DI).

###### Applications

- Applications include all machines and systems with moving axes (e.g. conveyor technology, handling).
- STO is suitable for applications where the motor is already at a standstill or will come to a standstill in a short, safe period of time as a result of friction.
- STO allows you to work safely on the machine with the protective door open. A classic Emergency Stop with electromechanical isolation is not required. The drive remains connected to the line and can be fully diagnosed.

> **Note**
>
> **The distinction between Emergency Off and Emergency Stop**
>
> "Emergency Off" and "Emergency Stop" are commands that minimize different risks in the machine or plant.
>
> The STO function is suitable for implementing an Emergency Stop - but not an Emergency Off.

###### Flow diagram

![Sequence: STO](images/148125274891_DV_resource.Stream@PNG-en-US.png)

Sequence: STO

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - During operation, STO is selected via PROFIsafe and/or F-DI. |
| 2 | - After the response time, the drive immediately initiates safe pulse suppression.    This safely interrupts the torque-generating energy fed to the motor. - The motor coasts down to a standstill. - STO safely prevents the motor restarting. |
| 3 | - STO is deactivated by the drive with (manual or automatic program-controlled) deselection. - The drive is again "ready for switching on". |
| 4 | - You restart the drive with a positive signal edge at ON/OFF1. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - STO is selected via the control bit of the selected PROFIsafe telegram or via the F-DI. |
| B | - The "STO_active" status is signaled in the status bit of the PROFIsafe telegram.   This value can be applied in the higher-level controller. |
| C | - The Safety error is acknowledged with selection/deselection of the STO function.    Any active messages of additional safety functions are acknowledged simultaneously with extended message acknowledgment (p9507.0 = 1). The standard acknowledgment mechanism must be executed in addition. |

###### Selecting/deselecting "Safe Torque Off"

If "Safe Torque Off" is selected, the motor holding brake is closed (if connected and configured).

Deselecting "Safe Torque Off" represents an internal safety acknowledgment. The following happens once the cause of the fault has been eliminated:

1. The Safety requirement "Close motor holding brake" is canceled.
2. The possibly active F01611 message or STO is withdrawn.
3. In addition, reset the messages in the fault buffer using the general acknowledgment mechanism.

###### Safe Brake Control (SBC) mode of operation

###### Overview

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/148125311499_DV_resource.Stream@PNG-en-US.png) |  |

The "Safe Brake Control" function (SBC) is used to safely control the motor-integrated holding brake, which operates according to the closed-circuit principle.

###### Functional characteristics

You must enable the function when commissioning in order that SBC can become active.

> **Note**
>
> You cannot select SBC as an autonomous function: SBC is activated (if enabled) immediately upon selection of STO.

###### Applications

Use SBC in applications where the drive must maintain a safe position, even when the motor is in a no-current condition. SBC thus prevents suspended or passing loads from dropping (e.g. for lifting gear, passenger elevators, winders). No external logic or switching elements required, as the functionality is completely integrated in the drive.

> **Note**
>
> **Condition of the motor holding brake**
>
> SBC is not able to identify as to whether a holding brake is mechanically worn or is a defective.
>
> As a consequence, observe the maximum permissible number of emergency braking operations for the motor holding brake being used.

###### Flow diagram

![Sequence: SBC](images/148125315595_DV_resource.Stream@PNG-en-US.png)

Sequence: SBC

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - STO is selected in operation. - At the same time, the drive activates SBC. - Taking the brake closing time into account, the command to close the motor holding brake closes the brake, thus supporting the shutdown process initiated by STO. |
| 2 | - The mechanical brake brakes the motor to a standstill. |
| 3 | - STO is deactivated by the drive with (manual or automatic program-controlled) deselection. - The drive is again "ready for switching on". - SBC is also simultaneously deactivated with deselection of STO. The brake remains (unsafely) closed, however, until the standard program executes the command to open the brake |
| 4 | - You restart the drive with the ON/OFF1 signal.    Taking the brake opening time into account, the command to open the brake opens the brake. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - STO is selected via the control bit of the selected PROFIsafe telegram or via the F-DI. - The drive activates SBC when the safe brake control is enabled (p9602 = 1). - The drive triggers SBC simultaneously with STO. - Brake management is resulted within the context of standard parameterization of the drive. |

For the "Safe Brake Control" function, the drive assumes a control function and ensures the following behavior:

- If the drive detects a fault or failure of the brake, it deactivates the brake current.
- The brake closes and a safe state is reached.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected movements of the motor due to defective brake**  "Safe Brake Control" function does not detect mechanical defects of the brake. An interrupted cable or a short-circuit in the brake winding is only detected when the state changes, i.e. when the brake either opens or closes.   The defects described above may initiate unwanted motor motion, which may result in injury or death.  - In particular, ensure the brake is not powered from an external source. Information on this topic can be found in EN 61800‑5‑2:2007, Appendix D. - If you use the Safety Integrated Extended Functions, perform a test of the brakes during commissioning with the aid of the "Safe Brake Test (SBT)" diagnostic function: |  |

---

**See also**

[Safe Brake Test (SBT) mode of operation](#safe-brake-test-sbt-mode-of-operation)

###### Configuring STO/SBC

###### Description

The "Safe Torque Off" (STO) function is used to safely disconnect the torque-generating energy supply to the motor for a machine function or in the event of a fault. A restart is prevented by the two-channel pulse suppression. The switching on inhibited prevents an automatic restart after deselection of STO.

The "Safe Brake Control" (SBC) function supplies a safe output signal for controlling a holding brake.

**Cable break**

A cable break or short-circuit in the brake winding is only detected at a change of state, i.e. when opening and/or closing the brake.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unwanted motor movements due to a defective brake**  "Safe Brake Control" function does not detect mechanical defects of the brake.   A cable break or short-circuit can cause unwanted movements of the motor, which can lead to bodily injury or death.  - In particular, ensure the brake is not powered from an external source. Information on this can be found in EN 61800‑5‑2, Appendix D. - During commissioning, test the brake with the "Safe Brake Test (SBT)" diagnostic function.  You will find more information here "[Safe Brake Test](#configuring-sbt)". |  |

###### Configuring Safety Functions

1. Click the ![Configuring Safety Functions](images/148125432331_DV_resource.Stream@PNG-en-US.png) button (Select STO) in the "STO/SBC" screen form to configure control of the "STO" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#making-basic-settings)").
2. Optional: Call the "STO/SBC" Safety Integrated Function again.
3. Click "Save project" in the toolbar to save the changes in the project.

**Result**

You have configured the "STO/SBC" Safety Integrated Function.

###### Additional parameters

- [p9601](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9601-si-enable-functions-integrated-in-the-drive)
- [r9720](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9720028-si-motion-control-signals-integrated-in-the-drive)
- [r9722](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9722028-si-motion-drive-integrated-status-signals)

---

##### SS1

This section contains information on the following topics:

- [Safe Stop 1 (time-controlled) mode of operation](#safe-stop-1-time-controlled-mode-of-operation-1)
- [SS1 with braking ramp monitoring (SS1-r) mode of operation](#ss1-with-braking-ramp-monitoring-ss1-r-mode-of-operation)
- [SS1 with acceleration monitoring (SS1-a) mode of operation](#ss1-with-acceleration-monitoring-ss1-a-mode-of-operation)
- [Configuring SS1](#configuring-ss1)
- [Configuring SAM/SBR](#configuring-samsbr)

###### Safe Stop 1 (time-controlled) mode of operation

###### Overview

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/148125378315_DV_resource.Stream@PNG-en-US.png) |  |

The "Safe Stop 1" function (SS1, time-controlled) causes a drive-autonomous deceleration of the motor and initiates the "Safe Torque Off" (STO) function after a predefined time interval has elapsed. This function corresponds to stop category 1 to EN 60204‑1.

###### Functional characteristics

The Safety Integrated Basic Function "Safe Stop 1" is available in the following versions:

- SS1 with OFF3 (SS1-t according to IEC 61800-5-2)
- SS1 with external stop (SS1E-t)

Set the SS1 response for Safety commissioning in the "Parameterization" step.

###### Applications

SS1 can be applied in the following cases:

- The load torque cannot reduce the motor to a standstill through friction within a sufficiently short time.
- Coasting down of the drive (STO) will pose risks to safety.

###### SS1 with OFF3 (SS1-t)

When SS1-t is selected, the motor speed is reduced along the OFF3 ramp for the duration of the selected delay time. After the delay time expires, the drive activates the STO function (independent of the actual speed).

> **Note**
>
> Braking at the OFF3 ramp is not monitored!

**Flow diagram SS1 with OFF3 (SS1-t)**

![Sequence: SS1](images/148125382539_DV_resource.Stream@PNG-en-US.png)

Sequence: SS1

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - SS1 is selected in operation. |
| 2 | - The drive immediately initiates braking following the response time via the OFF3 ramp. - At the same time, the drive initiates the SS1 delay time. |
| 3 | - The drive triggers STO once the SS1 delay time has elapsed. - The motor coasts down to a standstill. - STO safely prevents the motor restarting. |
| 4 | - SS1 and STO are deactivated by the drive with (manual or automatic program-controlled) deselection. - The drive is again "ready for switching on". |
| 5 | - You restart the drive with the ON/OFF1 signal. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - SS1 is selected via the control bit of the selected PROFIsafe telegram or via the F-DI. |
| B | - The drive brakes the motor along the OFF3 ramp. - Once the SS1 delay time (p9652) has expired, the drive automatically triggers STO independently of the current speed. |
| C | - The "SS1_active" status is signaled in the status bit of the PROFIsafe telegram. - This value can be applied in the higher-level controller. - When STO becomes active, the "SS1_active" status is also signaled in the status bit of the PROFIsafe telegram. |

###### SS1 with external stop (SS1E-t)

If several drives are connected with one another through a material web, then braking initiated by a single drive at the related OFF3 ramp can damage the machine or system.

When the safety function SS1E-t is used, the drive is shut down using the user program of a higher-level control system. Although the safe delay time is activated when SS1E-t is selected, OFF3 is not activated. Using an appropriate program, the control must then ramp down the drives involved within the delay time to the safe state. After the delay time has elapsed, the drive activates the STO function and safely interrupts the energy feed to the motor (independent of the actual speed).

**Sequence diagram, SS1 with external stop (SS1E-t)**

![Sequence: SS1](images/148125382539_DV_resource.Stream@PNG-en-US.png)

Sequence: SS1

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - SS1 is selected in operation. |
| 2 | - The control system initiates stopping using the setpoint that is entered. - At the same time, the drive initiates the SS1 delay time. |
| 3 | - The drive triggers STO once the SS1 delay time has elapsed. - The motor coasts down to a standstill. - The pulse inhibit safely prevents the motor restarting. |
| 4 | - SS1 and STO are deactivated by the drive with (manual or automatic program-controlled) deselection. - The drive is again "ready for switching on". |
| 5 | - You restart the drive with the ON/OFF1 signal. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - To use SS1E, set the braking response (p9507.3 = 1) to "SS1E external stop". - SS1 is selected via the control bit of the selected PROFIsafe telegram or via the F-DI. |
| B | - The motor is braked by the external setpoint that is entered. - Once the SS1 delay time (p9652) has expired, the drive automatically triggers STO independent of the actual speed. |
| C | - The "SS1_active" status is signaled in the status bit of the PROFIsafe telegram. - This value can be applied in the higher-level controller. - When STO becomes active, the "SS1_active" status is also signaled in the status bit of the PROFIsafe telegram. |

> **Note**
>
> **SS1 cannot be interrupted**
>
> - If SS1 is deselected again during this time, the STO function is selected and deselected again by the drive immediately after the delay time has elapsed or the speed has dropped below the shutdown speed. This terminates the SS1 function normally. It cannot be interrupted.
> - During the delay time, SS1 cannot be deselected by withdrawing the control command, therefore fulfilling the requirements of EN 60204‑1 relating to an Emergency Stop function.

###### Setting the delay time for SS1

Select the SS1 delay time so that the drive can travel the complete OFF3 ramp, and close any motor holding brake before the torque is safely switched off.

The OFF3 ramp-down time must be orientated to the actual braking capacity of the system or machine.

Use the following procedure to select the SS1 delay time:

- SS1 delay time with parameterized motor holding brake

  SS1 delay time (p9652) ≥ OFF3 ramp-down time (p1135) + pulse suppression delay time (p1228) + motor holding brake closing time (p1217)
- SS1 delay time, without parameterized motor holding brake:

  SS1 delay time (p9652) ≥ OFF3 ramp-down time (p1135) + pulse suppression delay time (p1228)

###### SS1 with braking ramp monitoring (SS1-r) mode of operation

###### Flow diagram

![Sequence: SS1-r](images/148125561483_DV_resource.Stream@PNG-en-US.png)

Sequence: SS1-r

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - SS1 is selected in operation. |
| 2 | - The drive immediately initiates braking following the response time via the OFF3 ramp. - At the same time, the drive initiates the SBR delay time. |
| 3 | - The drive monitors the motor to ensure that it does not exceed the set braking ramp when braking. - Upon reaching the SBR speed limit, the drive deactivates monitoring of the braking ramp. Braking continues. |
| 4 | - STO is triggered by the drive when the STO shutdown speed is reached or when the SS1 delay time has elapsed. - The motor coasts down to a standstill. - The drive safely prevents a restart of the motor with the pulse inhibit. |
| 5 | - STO and SS1 are deactivated by the drive with (manual or automatic program-controlled) deselection. - The drive is again "ready for switching on". |
| 6 | - You restart the converter with the ON/OFF1 signal. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - SS1 is selected via the control bit of the selected PROFIsafe telegram or via the F-DI. |
| B | - The drive initiates the SBR delay time (p9582) with selection of SS1. - Monitoring of the braking ramp is initiated by the drive when the delay time has elapsed. |
| C | - You set the braking ramp with the reference speed (p9581) and the SBR monitoring time (p9583). - The drive deactivates monitoring of the braking ramp if speed falls below the SBR speed limit (p9568). |
| D | - In parallel to monitoring the braking ramp, while braking along the OFF3 ramp, you can apply the SS1 delay time (p9556). When this time elapses, the drive automatically triggers STO independently of the current speed. |
| E | - When the SS1 delay time (p9556) elapses OR if the speed falls below the STO shutdown speed (p9560), then the drive triggers STO. |
| F | - The drive signals the "SS1_active" status in the status bit of the PROFIsafe telegram. - You can utilize this status in the higher-level controller. - If STO is active, the drive also signals the "STO_active" status in the corresponding status bit of the PROFIsafe telegram. |

###### SS1 with acceleration monitoring (SS1-a) mode of operation

###### Flow diagram

![Sequence: SS1-a](images/148125648651_DV_resource.Stream@PNG-en-US.png)

Sequence: SS1-a

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - SS1 is selected in operation. |
| 2 | - The drive immediately initiates braking following the response time via the OFF3 ramp. - At the same time, safe acceleration monitoring (SAM) is activated. - The drive monitors the speed of the motor and prevents the motor from re-accelerating by continuously adjusting the monitoring threshold to the decreasing speed. |
| 3 | - STO is triggered upon reaching the STO shutdown speed or once the SS1 delay time has elapsed. - The motor coasts down to a standstill. - STO safely prevents the motor restarting. |
| 4 | - STO and SS1 are deactivated by the drive with (manual or automatic program-controlled) deselection. - The drive is again "ready for switching on". |
| 5 | - You restart the drive with the ON/OFF1 signal. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - SS1 is selected via the control bit of the selected PROFIsafe telegram or via the F-DI. |
| B | - You set the acceleration monitoring with the speed tolerance (p9548). - As long as the speed reduces, the drive continuously adds the speed tolerance to the current speed so that the monitoring tracks the speed. - The monitoring is deactivated when the SAM speed limit is fallen below (p9568). |
| C | - In parallel to monitoring the acceleration, while braking along the OFF3 ramp you can apply the SS1 delay time (p9556). You set this time analogous to the SS1-t delay time of the Basic Functions. Once this time has expired, the drive automatically triggers STO independently of the current speed. |
| D | - When the SS1 delay time (p9556) elapses OR if the speed falls below the STO shutdown speed (p9560), then the drive triggers STO. |
| E | - The "SS1_active" status is signaled in the status bit of the PROFIsafe telegram. - You can utilize this status in the higher-level controller. - If STO is active, the "STO_active" status is also signaled in the corresponding status bit of the PROFIsafe telegram. |

###### Configuring SS1

###### Description

In the "Safe Stop 1" (SS1) screen form you make settings for the motor deceleration. The "SS1" function brakes the motor, monitors the magnitude of the motor deceleration within specified limits, and triggers the STO function after a delay time or violation of a speed threshold.

###### Comparison of settings for motor deceleration

| Settings | Method of operation |
| --- | --- |
| SS1 with SAM and OFF3 | - Braking is monitored with the "Safe Acceleration Monitor" function. - The delay time starts after the function has been selected ([p9556](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9556-si-motion-ss1-to-sto-delay-time)). If SS1 is deselected again within this time, the STO function is selected and deselected again immediately after the delay time has expired or if the shutdown velocity is undershot, i.e. the SS1 function is terminated normally. It cannot be interrupted. - Parameters r9773.4 (SBC active) and r9773.1 (STO selected in the drive) display the current status of the function. |
| SS1 with SAM and OFF3 and STO of the Basic Functions via onboard terminals | - Braking is monitored with the "Safe Acceleration Monitor" function. - The delay time starts after the function has been selected (p9556). If SS1 is deselected again within this time, the STO function is selected and deselected again immediately after the delay time has expired or if the shutdown velocity is undershot, i.e. the SS1 function is terminated normally. It cannot be interrupted. - Parameters r9773.4 (SBC active) and r9773.1 (STO selected in the drive) display the current status of the function. - The drive brakes along the OFF3 ramp ([p1135](SINAMICS%20Parameter%20SINAMICS%20S210.md#p11350-off3-ramp-down-time)) once "Safe Stop 1" is selected and switches to "Safe Torque Off" (STO) once the delay time [p9652](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9652-si-ss1-delay-time) has expired. |
| SS1 with SAM and OFF3 and SS1 of the Basic Functions via onboard terminals | - Braking is monitored with the "Safe Acceleration Monitor" function. - The delay time starts after the function has been selected (p9556). If SS1 is deselected again within this time, the STO function is selected and deselected again immediately after the delay time has expired or if the shutdown velocity is undershot, i.e. the SS1 function is terminated normally. It cannot be interrupted. - Parameters r9773.4 (SBC active) and r9773.1 (STO selected in the drive) display the current status of the function. - The drive brakes along the OFF3 ramp (p1135) once "Safe Stop 1" is selected and switches to "Safe Torque Off" (STO) once the delay time p9652 has expired. |
| SS1 with SBR and OFF3 | - Braking is monitored with the "Safe Brake Ramp" function. - The drive brakes along the OFF3 ramp (p1135) once "Safe Stop 1" is selected and switches to "Safe Torque Off" (STO) once the delay time has expired (p9556) or when the shutdown velocity is undershot ([p9560](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9560-si-motion-sto-shutdown-speed-1)). - Parameters r9773.4 (SBC active) and r9773.1 (STO selected in the drive) display the current status of the function. |
| SS1 with external stop | - With external stop, "Safe Stop 1" functions in principle in just the same way as "Safe Stop 1 with encoder (brake ramp monitoring and acceleration monitoring)". However, note the following differences:   - When SS1 with external stop is selected, the drive is not braked along the OFF3 ramp: You are responsible for applying suitable measures to brake the drive. After the delay time has expired (p9556), only STO/SBC are triggered automatically. After the function has been selected, the delay time expires – even if the function is deselected during this time. In this case, after the delay time has expired, the STO/SBC function is selected and then deselected again immediately.   - The brake ramp (SBR) and the acceleration (SAM) are not monitored and there is no standstill detection.   - With this configuration, STO becomes active after the SS1 timer p9556 has expired; this also applies when SBR has been configured. - Parameters r9773.4 (SBC active) and r9773.1 (STO selected in the drive) display the current status of the function. |

###### Configuring motor deceleration with internal brake response (OFF3)

1. Click the ![Configuring motor deceleration with internal brake response (OFF3)](images/148125432331_DV_resource.Stream@PNG-en-US.png) button (Select SS1) in the "SS1" screen form to configure activation of the "SS1" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Select the "[0] SS1 with OFF 3" setting from the "Braking response" drop-down list.

   The screen form is structured accordingly.
3. Select the monitoring type in the "Monitoring" drop-down list:

   - with SAM
   - with SBR
4. Click "Monitoring" and parameterize the alternative brake monitoring functions "SAM" and "SBR" in the dialog (see "[Configuring SAM/SBR](#configuring-samsbr)").
5. Enter the required delay time in the "Delay time SS1 -&gt; STO active" (p9556) input field.
6. Enter the required delay time in the "Safe Stop 1 delay time" (p9652) input field.

   This field only appears if you have activated the "Basic Functions via onboard terminals" option in the function selection.
7. Should you wish to perform a safe acknowledgment during selection/deselection of STO, activate the "Acknowledge alarm via STO" option ([p9507](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9507-si-motion-function-configuration).0).
8. Click "Save project" in the toolbar to save the changes in the project.

###### Configuring the motor deceleration with external stop

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unplanned axis movements during Safe Stop 1**  During the delay time (p9652), random axis movements are possible for "Safe Stop 1 (time-controlled) with external stop" which could result in severe injuries or death within the hazardous area.  - Take suitable measures to prevent undesirable axis movements, e.g. by using a brake with safe monitoring.    You will find more information in the description of "Safe Brake Control". |  |

1. Click the ![Configuring the motor deceleration with external stop](images/148125432331_DV_resource.Stream@PNG-en-US.png) button (Select SS1) in the "SS1" screen form to configure activation of the "SS1" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Select the "[1] SS1E external stop" setting in the "Brake response" drop-down list.

   The screen form is structured accordingly.
3. Enter the required delay time in the "Delay time SS1 -&gt; STO active" (p9556) input field.
4. Enter the required delay time in the "Safe Stop 1 delay time" (p9652) input field.

   This field only appears if you have activated the "Basic Functions via onboard terminals" option in the function selection.
5. Should you wish to perform a safe acknowledgment during selection/deselection of STO, activate the "Acknowledge alarm via STO" option (p9507.0).
6. Click "Save project" in the toolbar to save the changes in the project.

###### Additional parameters

- p1135
- [p9501](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9501-si-motion-enable-safety-functions)
- [p9506](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9506-si-motion-function-specification)
- p9507
- p9560
- [r9722](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9722028-si-motion-drive-integrated-status-signals)

---

###### Configuring SAM/SBR

###### Description

In the following dialogs you parameterize the alternative brake monitoring functions "Safe Acceleration Monitor" ("SAM") and "Safe Brake Ramp" ("SBR"):

###### Safe Acceleration Monitor (SAM)

The "Safe Acceleration Monitor" (SAM) function is used to safely monitor braking along the OFF3 ramp. The function is active for "SS1" or "SS2".

As long as the speed reduces, the converter continuously adds the adjustable velocity tolerance [p9548](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9548-si-motion-sam-actual-speed-tolerance-1) to the current speed so that the monitoring tracks the speed. If the speed is temporarily higher, the monitoring remains at the last value. The converter reduces the monitoring threshold until the "Shutdown speed" has been reached.

![Example: SAM](images/148125731211_DV_resource.Stream@PNG-en-US.png)

Example: SAM

If the motor accelerates by the velocity tolerance during the OFF3 deceleration ramp, SAM detects the incident and triggers an STO. The monitoring is performed as follows:

- The monitoring by "SAM" is activated for "SS1" and "SS2".
- The SAM limit value is frozen when the velocity falls below the SAM velocity limit in [p9568](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9568-si-motion-samsbr-speed-limit-1).
- SAM monitoring continues until the transition time to SOS/STO expires.

Calculating the SAM tolerance of the actual velocity:

- The following applies when parameterizing the SAM tolerance:

  - The possible velocity increase after SS1 or SS2 is triggered results from the effective acceleration a and the duration of the acceleration phase.
  - The duration of the acceleration phase is equivalent to one monitoring cycle (MC; p9500) (delay from detecting an SS1/SS2 until n<sub>set</sub> = 0)
- Calculating the SAM tolerance:

  Actual velocity for SAM = acceleration x acceleration duration   
  This results in the following setting rule:

  - For a linear axis: SAM tolerance [mm/min] = a [m/s<sup>2</sup>] MC [s] 1000 [mm/m] 60 [s/min]
  - For a rotary axis: SAM tolerance [rpm] = a [rev/s<sup>2</sup>] MC [s] 60 [s/min]
- Recommendation   
  The SAM tolerance value entered should be approx. 20% higher than the calculated value.
- You set the tolerance so that the "undershoot" which inevitably occurs when standstill is reached after braking along the OFF3 ramp is tolerated. However, the size of this cannot be calculated.

**Configuring SAM**

1. Select the setting "with SAM" in the "Monitoring" drop-down list in the "SS1" or "SS2" screen form.

   The "SAM (Safe Acceleration Monitor)" dialog opens.
2. Enter the required values in the input fields.

   - Velocity tolerance (p9548)
   - SAM velocity limit (p9568)
   - STO shutdown velocity ([p9560](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9560-si-motion-sto-shutdown-speed-1))
   - Ramp-down time (OFF3) ([p1135](SINAMICS%20Parameter%20SINAMICS%20S210.md#p11350-off3-ramp-down-time)[0])
   - Maximum speed ([p1082](SINAMICS%20Parameter%20SINAMICS%20S210.md#p10820-maximum-speed)[0])
3. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Safe Brake Ramp (SBR)

The "Safe Brake Ramp" (SBR) function provides a safe method for monitoring the brake ramp. The "Safe Brake Ramp" function is used to monitor braking with the functions "SS1 with encoder" and SS2. For SLS, the setpoint limitation of the Safety Integrated Functions ([r9733](SINAMICS%20Parameter%20SINAMICS%20S210.md#r973302-si-motion-setpoint-speed-limit-effective)) must be connected to the ramp-function generator (p1051/p1052).

![Example: SBR](images/148125736075_DV_resource.Stream@PNG-en-US.png)

Example: SBR

The motor is decelerated with the OFF3 ramp as soon as "SS1", "SS2" or "SLS" is triggered. Monitoring of the brake ramp is activated once the delay time [p9582](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9582-si-motion-brake-ramp-delay-time) has expired. Monitoring ensures that the motor does not exceed the set brake ramp (SBR) when braking.

The gradient of the brake ramp is defined using the reference velocity [p9581](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9581-si-motion-brake-ramp-reference-value-1) and the brake ramp monitoring time [p9583](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9583-si-motion-brake-ramp-monitoring-time). Parameter p9581 defines the reference velocity and parameter p9583 defines the ramp-down time. Parameter p9582 is used to set the time which passes after the triggering of "SS1", selection of "SLS" or SLS level changeover and the start of brake ramp monitoring.

After the end of SBR monitoring, the drive activates the respective subsequent function, depending on the function used:

| Function used | Subsequent function |
| --- | --- |
| SS1 | STO |
| SS2 | SOS |
| SLS | New speed limit value |

> **Note**
>
> **Limitation of the delay time**
>
> The delay time (p9582) is limited to a minimum value of two SI Motion monitoring cycles (2 x p9500), i.e. even if a value less than 2 x p9500 is parameterized for the delay time (p9582), SBR only takes effect two cycles after an active SS1.
>
> If a value greater than 2 x p9500 is parameterized for the delay time (p9582), SBR takes effect after active SS1 after the time p9582. Ensure that you round off the SBR delay time to an integer multiple of the Safety cycle (p9500).

**Configuring SBR**

1. Select the setting "with SBR" in the "Monitoring" drop-down list in the "SS1" or "SS2" screen form.

   The "SBR (Safe Brake Ramp)" dialog opens.
2. Enter the required values in the input fields.

   - Reference velocity (p9581)
   - SAM velocity limit (p9568)
   - STO shutdown velocity (p9560)
   - Delay time (p9582)
   - Brake ramp monitoring time (p9583)
   - Ramp-down time (OFF3) (p1135[0])
   - Maximum speed (p1082[0])
3. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Additional parameters

- [p9516](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9516-si-motion-encoder-configuration-safety-functions)
- [p9546](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9546-si-motion-ssm-velocity-limit-1)
- p9548
- p9560
- p9568
- p9581
- p9582
- p9583

---

##### SS2

This section contains information on the following topics:

- [Safe Stop 2 (SS2) mode of operation](#safe-stop-2-ss2-mode-of-operation)
- [SS2 with braking ramp monitoring (SS2-r) mode of operation](#ss2-with-braking-ramp-monitoring-ss2-r-mode-of-operation)
- [SS2 with acceleration monitoring (SS2-a) mode of operation](#ss2-with-acceleration-monitoring-ss2-a-mode-of-operation)
- [Configuring SS2](#configuring-ss2)
- [Configuring SAM/SBR](#configuring-samsbr-1)

###### Safe Stop 2 (SS2) mode of operation

###### Overview

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/148125783947_DV_resource.Stream@PNG-en-US.png) |  |

The Safety Integrated Function "Safe Stop 2" SS2 causes the motor to come to a standstill with subsequent safe monitoring of the standstill position. When SS2-r is selected, the drive brakes the motor along a braking ramp. In addition to drive-autonomous braking via the OFF3 ramp, you can also stop the drive via the user program of a higher-level controller (SS2E).

SS2 distinguishes the following variants:

- SS2-a with acceleration monitoring (SAM)
- SS2-r with braking ramp monitoring (SBR)
- Additionally, SS2 can be parameterized with a delay time before activation of SOS.

Selection and monitoring of the acceleration (SAM) and the braking ramp (SBR) are realized with two channels. Braking with the OFF3 ramp is realized with one channel.

###### Interruption of the ramp function with OFF2

Activating SS2 can mean that the higher-level controller (PLC, motion controller) which specifies the speed setpoint, interrupts the ramp function (e.g. with OFF2). The device behaves in this way as a result of a fault response triggered by OFF3 activation. This fault reaction must be prevented by way of appropriate parameterization/configuration.

> **Note**
>
> If a higher-level motion controller is used, you should use the Safety Integrated Function SS2E or SOS.
>
> Reason: For the Safety Integrated Function SS2-r/SS2-a, SINAMICS S210 autonomously brakes at the OFF3 ramp. The motion controller detects a deviation between target value and actual value and shifts the drive to pulse cancellation.

###### Applications

Use the SS2 for applications where an axis must be safely stopped and where the standstill position must then be safely monitored. Following deselection of SS2, you can continue traversing the axis without reference point approach.

###### SS2 with braking ramp monitoring (SS2-r) mode of operation

###### Flow diagram

![Sequence: SS2-SBR](images/148125819147_DV_resource.Stream@PNG-en-US.png)

Sequence: SS2-SBR

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - SS2 is selected during operation. |
| 2 | - The drive immediately initiates braking following the response time via the OFF3 ramp. The SBR delay time is initiated at the same time. |
| 3 | - The drive monitors the motor to ensure that it does not exceed the set braking ramp when braking. - Upon reaching the SBR speed limit, monitoring of the braking ramp is deactivated. Braking continues. |
| 4 | - SOS is triggered once the SS2 delay time has elapsed. - The SS2 delay time set must allow the drive to brake to a standstill from every speed of the operating process within this time. - The standstill state of the motor is safely monitored with the Safety Integrated Function SOS. The motor remains in control mode. |
| 5 | - SS2 and SOS are deactivated with (manual or automatic program-controlled) deselection. - You can immediately continue traversing the axis from the standstill position. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - SS2 is selected via the control bit of the selected PROFIsafe telegram. |
| B | - The SBR delay time (p9582) is initiated with selection of SS2. Monitoring of the braking ramp is initiated once the delay time has elapsed. |
| C | - You set the braking ramp with the reference speed (p9581) and the SBR monitoring time (p9583). - The drive deactivates monitoring of the braking ramp if speed falls below the SBR speed limit (p9568). |
| D | - Standstill is safely monitored (SOS becomes active) once the SS2 delay time (p9552) has elapsed. |
| E | - The drive is in control mode and monitors the standstill tolerance (p9530). |
| F | - If the standstill tolerance is violated, the drive executes SS1 as a fault response with subsequent transition to STO. |
| G | - The "SS2_active" status is signaled in the status bit of the PROFIsafe telegram.   This value can be applied in the higher-level controller. - If SOS is active, the "SOS_active" status is also signaled in the corresponding status bit of the PROFIsafe telegram. |

###### SS2 with acceleration monitoring (SS2-a) mode of operation

###### Flow diagram

![Sequence: SS2-SAM](images/148125880715_DV_resource.Stream@PNG-en-US.png)

Sequence: SS2-SAM

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - SS2 is selected during operation. |
| 2 | - The drive immediately initiates braking following the response time via the OFF3 ramp. - At the same time, the drive activates safe acceleration monitoring (SAM).   The drive monitors the speed of the motor and prevents the motor from re-accelerating by continuously adjusting the monitoring threshold to the decreasing speed. |
| 3 | - SOS is triggered once the SS2 delay time has elapsed. The SS2 delay time set must allow the drive to brake to a standstill from every speed of the operating process within this time. - The drive safely monitors the standstill state of the motor with the Safety Integrated Function SOS. The motor remains in control mode. |
| 4 | - SS2 and SOS are deactivated by the drive with (manual or automatic program-controlled) deselection. - You can immediately continue traversing the axis from the standstill position. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - SS2 is selected via the control bit of the selected PROFIsafe telegram. |
| B | - The acceleration monitoring SAM is set with the speed tolerance (p9548). - SINAMICS S210 monitors the change in speed between 2 safety monitoring cycles to ensure that it does not exceed the speed tolerance (p9548). The monitoring is deactivated when the SAM speed limit is fallen below (p9568). |
| C | - Standstill is safely monitored (SOS becomes active) once the SS2 delay time (p9552) has elapsed. |
| D | - The drive is in control mode and monitors the standstill tolerance (p9530). |
| E | - If the standstill tolerance is violated, the drive executes SS1 as a fault response with subsequent transition to STO. |
| F | - The "SS2_active" status is signaled in the status bit of the PROFIsafe telegram. - You can utilize this status in the higher-level controller. - If SOS is active, the drive also signals "SOS_active" in the corresponding status bit of the PROFIsafe telegram. |

###### Configuring SS2

###### Description

The "Safe Stop 2" ("SS2") safety function is used to brake the motor safely along the OFF3 deceleration ramp ([p1135](SINAMICS%20Parameter%20SINAMICS%20S210.md#p11350-off3-ramp-down-time)) with subsequent transition to the "SOS" state (see "[Safe Operating Stop (SOS)](#configuring-sos)") after the delay time expires ([p9552](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9552-si-motion-transition-time-ss2-to-sos)). The delay time set must allow the drive to brake to a standstill from every speed of the operating process within this time. The standstill tolerance ([p9530](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9530-si-motion-standstill-tolerance-1)) must not be violated after this time. After braking, the drives remain in speed control mode with the speed setpoint n = 0. The full torque is available. The default setpoint (e.g. from the setpoint channel, or from a higher-level controller) remains inhibited as long as "SS2" is selected.

> **Note**
>
> **Interruption of the ramp function with OFF3**
>
> Activating SS2 can mean that the higher-level controller (PLC, motion controller) which specifies the speed setpoint, interrupts the ramp function (e.g. with OFF2). The device behaves in this way as a result of a fault response triggered by OFF3 activation. This fault response must be avoided by appropriate parameterization or configuration.

###### Differences between "Safe Stop 2 with OFF3" and "SS2 with external stop (SS2E)"

The following differences exist:

- If SS2 with external stop is selected, the drive does not brake the motor autonomously but follows the defined speed setpoint.
- During the delay time [p9553](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9553-si-motion-transition-time-ss2e-to-sos), the brake ramp (SBR) and the acceleration (SAM) are not monitored and there is no standstill detection.
- SOS becomes active after the delay time p9553 has expired.

  If the SS2E function is active, the higher-level controller must define the speed setpoint in such a way that the motor is stopped no later than after the delay time p9553 has expired.
- To enable "Safe Stop 2 with external stop", set the "SS2E enable" switch to "Connection".
- The PROFIsafe control word S_STW2.28 selects the SS2E function. PROFIsafe S_STW2.28 is included in telegram 901.
- The PROFIsafe status word S_ZSW2.28 indicates whether the SS2E function is active. PROFIsafe status word S_ZSW2.28 is included in telegram 901. The associated diagnostics parameter is [r9722](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9722028-si-motion-drive-integrated-status-signals).28.

  In the "Safety Info Channel," status word S_ZSW3B.11 indicates whether the SS2E function is active. The associated diagnostic parameter is [r10234](SINAMICS%20Parameter%20SINAMICS%20S210.md#r10234015-si-safety-information-channel-status-word-s_zsw3b).11.

  The diagnostic parameters [p9722](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9722028-si-motion-drive-integrated-status-signals).28 and [p10234](SINAMICS%20Parameter%20SINAMICS%20S210.md#r10234015-si-safety-information-channel-status-word-s_zsw3b).11 are also set during internal stop SS2E.

###### Configuring motor deceleration with internal brake response (OFF3)

1. Click the ![Configuring motor deceleration with internal brake response (OFF3)](images/148125432331_DV_resource.Stream@PNG-en-US.png) button (Select SS2) in the "SS2" screen form to configure activation of the "SS2" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Select the monitoring type in the "Monitoring" drop-down list:

   - with SAM
   - with SBR
3. Click "Monitoring" and parameterize the alternative brake monitoring functions "SAM" and "SBR" in the dialog (see "[Configuring SAM/SBR](#configuring-samsbr-1)").
4. Correct the prescribed delay time in the "Delay time SS2 -&gt; SOS active" field (p9552).
5. Correct the value prescribed for the standstill tolerance in the "Standstill monitoring" field (p9530).
6. Click "Save project" in the toolbar to save the changes in the project.

###### Configuring the motor deceleration with external stop (SS2E)

1. Click the ![Configuring the motor deceleration with external stop (SS2E)](images/148125432331_DV_resource.Stream@PNG-en-US.png) button (Select SS2E) in the "SS2" screen form to configure activation of the "SS2" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Set the "SS2E enable" switch to "Connection".
3. Correct the prescribed delay time in the "Delay time SS2E -&gt; SOS active" field (p9553).

   SBR/SAM is not monitored during this delay time. SOS becomes active after this delay time has elapsed.
4. Correct the value prescribed for the standstill tolerance in the "Standstill monitoring" field (p9530).
5. Click "Save project" in the toolbar to save the changes in the project.

###### Additional parameters

- p1135
- [p9501](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9501-si-motion-enable-safety-functions)
- p9530
- [p9548](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9548-si-motion-sam-actual-speed-tolerance-1)
- p9552
- r9722

---

###### Configuring SAM/SBR

###### Description

In the following dialogs you parameterize the alternative brake monitoring functions "Safe Acceleration Monitor" ("SAM") and "Safe Brake Ramp" ("SBR"):

###### Safe Acceleration Monitor (SAM)

The "Safe Acceleration Monitor" (SAM) function is used to safely monitor braking along the OFF3 ramp. The function is active for "SS1" or "SS2".

As long as the speed reduces, the converter continuously adds the adjustable velocity tolerance [p9548](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9548-si-motion-sam-actual-speed-tolerance-1) to the current speed so that the monitoring tracks the speed. If the speed is temporarily higher, the monitoring remains at the last value. The converter reduces the monitoring threshold until the "Shutdown speed" has been reached.

![Example: SAM](images/148125731211_DV_resource.Stream@PNG-en-US.png)

Example: SAM

If the motor accelerates by the velocity tolerance during the OFF3 deceleration ramp, SAM detects the incident and triggers an STO. The monitoring is performed as follows:

- The monitoring by "SAM" is activated for "SS1" and "SS2".
- The SAM limit value is frozen when the velocity falls below the SAM velocity limit in [p9568](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9568-si-motion-samsbr-speed-limit-1).
- SAM monitoring continues until the transition time to SOS/STO expires.

Calculating the SAM tolerance of the actual velocity:

- The following applies when parameterizing the SAM tolerance:

  - The possible velocity increase after SS1 or SS2 is triggered results from the effective acceleration a and the duration of the acceleration phase.
  - The duration of the acceleration phase is equivalent to one monitoring cycle (MC; p9500) (delay from detecting an SS1/SS2 until n<sub>set</sub> = 0)
- Calculating the SAM tolerance:

  Actual velocity for SAM = acceleration x acceleration duration   
  This results in the following setting rule:

  - For a linear axis: SAM tolerance [mm/min] = a [m/s<sup>2</sup>] MC [s] 1000 [mm/m] 60 [s/min]
  - For a rotary axis: SAM tolerance [rpm] = a [rev/s<sup>2</sup>] MC [s] 60 [s/min]
- Recommendation   
  The SAM tolerance value entered should be approx. 20% higher than the calculated value.
- You set the tolerance so that the "undershoot" which inevitably occurs when standstill is reached after braking along the OFF3 ramp is tolerated. However, the size of this cannot be calculated.

**Configuring SAM**

1. Select the setting "with SAM" in the "Monitoring" drop-down list in the "SS1" or "SS2" screen form.

   The "SAM (Safe Acceleration Monitor)" dialog opens.
2. Enter the required values in the input fields.

   - Velocity tolerance (p9548)
   - SAM velocity limit (p9568)
   - STO shutdown velocity ([p9560](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9560-si-motion-sto-shutdown-speed-1))
   - Ramp-down time (OFF3) ([p1135](SINAMICS%20Parameter%20SINAMICS%20S210.md#p11350-off3-ramp-down-time)[0])
   - Maximum speed ([p1082](SINAMICS%20Parameter%20SINAMICS%20S210.md#p10820-maximum-speed)[0])
3. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Safe Brake Ramp (SBR)

The "Safe Brake Ramp" (SBR) function provides a safe method for monitoring the brake ramp. The "Safe Brake Ramp" function is used to monitor braking with the functions "SS1 with encoder" and SS2. For SLS, the setpoint limitation of the Safety Integrated Functions ([r9733](SINAMICS%20Parameter%20SINAMICS%20S210.md#r973302-si-motion-setpoint-speed-limit-effective)) must be connected to the ramp-function generator (p1051/p1052).

![Example: SBR](images/148125736075_DV_resource.Stream@PNG-en-US.png)

Example: SBR

The motor is decelerated with the OFF3 ramp as soon as "SS1", "SS2" or "SLS" is triggered. Monitoring of the brake ramp is activated once the delay time [p9582](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9582-si-motion-brake-ramp-delay-time) has expired. Monitoring ensures that the motor does not exceed the set brake ramp (SBR) when braking.

The gradient of the brake ramp is defined using the reference velocity [p9581](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9581-si-motion-brake-ramp-reference-value-1) and the brake ramp monitoring time [p9583](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9583-si-motion-brake-ramp-monitoring-time). Parameter p9581 defines the reference velocity and parameter p9583 defines the ramp-down time. Parameter p9582 is used to set the time which passes after the triggering of "SS1", selection of "SLS" or SLS level changeover and the start of brake ramp monitoring.

After the end of SBR monitoring, the drive activates the respective subsequent function, depending on the function used:

| Function used | Subsequent function |
| --- | --- |
| SS1 | STO |
| SS2 | SOS |
| SLS | New speed limit value |

> **Note**
>
> **Limitation of the delay time**
>
> The delay time (p9582) is limited to a minimum value of two SI Motion monitoring cycles (2 x p9500), i.e. even if a value less than 2 x p9500 is parameterized for the delay time (p9582), SBR only takes effect two cycles after an active SS1.
>
> If a value greater than 2 x p9500 is parameterized for the delay time (p9582), SBR takes effect after active SS1 after the time p9582. Ensure that you round off the SBR delay time to an integer multiple of the Safety cycle (p9500).

**Configuring SBR**

1. Select the setting "with SBR" in the "Monitoring" drop-down list in the "SS1" or "SS2" screen form.

   The "SBR (Safe Brake Ramp)" dialog opens.
2. Enter the required values in the input fields.

   - Reference velocity (p9581)
   - SAM velocity limit (p9568)
   - STO shutdown velocity (p9560)
   - Delay time (p9582)
   - Brake ramp monitoring time (p9583)
   - Ramp-down time (OFF3) (p1135[0])
   - Maximum speed (p1082[0])
3. Once all necessary settings have been made, click "Close".

   The dialog closes.

###### Additional parameters

- [p9516](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9516-si-motion-encoder-configuration-safety-functions)
- [p9546](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9546-si-motion-ssm-velocity-limit-1)
- p9548
- p9560
- p9568
- p9581
- p9582
- p9583

---

##### SOS

This section contains information on the following topics:

- [Safe Operating Stop (SOS) mode of operation](#safe-operating-stop-sos-mode-of-operation)
- [Configuring SOS](#configuring-sos)

###### Safe Operating Stop (SOS) mode of operation

###### Overview

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/148125977995_DV_resource.Stream@PNG-en-US.png) |  |

When the "Safe Operating Stop" (SOS) safety function is selected, the drive safely monitors the standstill position of the drive. The drive is in control mode, and can therefore withstand external forces.

After SOS has been selected it becomes active after the parameterizable delay time has expired. The drive must be braked to standstill within this delay time, e.g. by the controller.

###### Applications

SOS is suitable for the following applications:

- Machine parts must be safely monitored that they actually are at a standstill.
- A holding torque is required.

###### Flow diagram

![Sequence: SOS](images/148125982091_DV_resource.Stream@PNG-en-US.png)

Sequence: SOS

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - SOS is selected during operation. |
| 2 | - The control system initiates stopping using the setpoint that is entered. - At the same time, the drive initiates the SOS delay time. |
| 3 | - SOS is triggered when the SOS delay time elapses. - The SOS delay time set must allow the drive to brake to a standstill from every speed of the operating process within this time. - The motor is then safely monitored in the standstill position. |
| 4 | - SOS is deactivated by the drive with (manual or automatic program-controlled) deselection. - You can immediately continue traversing the axis from the standstill position. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - SOS is selected via the control bit of the selected PROFIsafe telegram. |
| B | - The drive is braked by external setpoint value specification. - SOS becomes active when the SOS delay time (p9551) has elapsed. |
| C | - The drive is in control mode and monitors the standstill tolerance (p9530). |
| D | - If the standstill tolerance is violated, SS1 is executed as a fault response with subsequent transition to STO. |
| E | - The "SOS active" status is signaled in the status bit of the PROFIsafe telegram. - You can utilize this status in the higher-level controller. |
| F | - Monitoring of the position window is concluded with "Deselect SOS" via the control bit of the selected PROFIsafe telegram. - The drive may be operated freely. |

###### Other functional characteristics

Contrary to SS1 and SS2, SOS does not automatically brake the drive.

The controller still has setpoint control.

Thus, respond to the "Selection SOS" in the user program of the controller in such a way that the controller brings the drive to a standstill within the delay time.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unplanned movement of the drive through mechanical forces**  Mechanical forces that are greater than the maximum torque of the drive can force a drive under closed-loop position control out of the Safe Operating Stop (SOS). Consequently, this process triggers a category 1 stop function according to EN 60204-1 (fault response function SS1). As a result, unexpected axis movements, which can lead to bodily injury or death, are possible.  - If there is a danger of unwanted movement in your application, you must take the appropriate measures to prevent this, e.g. by using a brake with safe monitoring. You will find more information here "[Safe Brake Control](#safe-brake-control-sbc-mode-of-operation-1)". - Note the alarms for SS1 and STO.   Take suitable measures to prevent unwanted axis movements and use, e.g. a brake with safe monitoring. |  |

> **Note**
>
> **Size of the tolerance window**
>
> The size of the tolerance window must be right for the application, otherwise the default monitoring settings will no longer be effective.

###### Configuring SOS

###### Description

The "Safe Operating Stop" (SOS) function is used for safe monitoring of the standstill position of a drive. Positions of a user-defined standstill tolerance are interpreted by the drive as "standstill".

![Standstill monitoring](images/148126019083_DV_resource.Stream@PNG-en-US.png)

Standstill monitoring

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unplanned movement of the drive through mechanical forces**  Mechanical forces that are greater than the maximum torque of the drive can force a drive under closed-loop position control out of the Safe Operating Stop (SOS). Consequently, this process triggers a category 1 stop function according to EN 60204-1. As a result, unexpected axis movements, which can lead to bodily injury or death, are possible.  - Note the alarms for SS1 and STO. - Take suitable measures to prevent unwanted movement, e.g. by using a brake with safe monitoring. |  |

**Effectiveness of the SOS function:**

You can see whether SOS is active by the green "SOS active" LED that illuminates in the "[Function status](#function-status)" screen form.

The "SOS" function takes effect in the following cases:

- After SOS is selected and the delay time (in [p9551](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9551-si-motion-sls-switchoversos-delay-time)) has expired

  The drive must be braked to standstill within this delay time, e.g. by the controller.
- As a consequence of SS2

**Response of the SOS standstill monitoring**

If the standstill tolerance is exceeded (in [p9530](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9530-si-motion-standstill-tolerance-1)), the drive responds as follows with Safety message C01707.

###### Configuring monitoring

1. Enter the required value in the "Delay time SOS -&gt; SOS active" (p9551) field.
2. Enter the required value in the "Standstill tolerance" (p9530) field.

   Alternatively, you can also click on the "Standstill tolerance SOS" button. A dialog with a graphic display of the standstill monitoring opens. You can also enter the standstill tolerance here.
3. Click "Save project" in the toolbar to save the changes in the project.

###### Additional parameters

- [p9501](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9501-si-motion-enable-safety-functions)
- [r9722](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9722028-si-motion-drive-integrated-status-signals)

---

##### SBT

This section contains information on the following topics:

- [Safe Brake Test (SBT) mode of operation](#safe-brake-test-sbt-mode-of-operation)
- [Configuring SBT](#configuring-sbt)

###### Safe Brake Test (SBT) mode of operation

###### Overview

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/148126092043_DV_resource.Stream@PNG-en-US.png) |  |

The diagnostic function "Safe Brake Test" (SBT) checks the required holding torque of a motor holding brake.

This diagnostic function exceeds the scope of EN 61800-5-2.

The drive purposely generates a force/torque against the applied brake. If the brake is operating correctly, the axis movement remains within a parameterized tolerance. If the drive determines a greater axis motion, however, it may be assumed that the braking force or the braking torque has diminished. In this case, maintenance work must be performed.

The "Safe Brake Test" (SBT) diagnostic function meets the requirements for category 2 according to EN ISO 13849‑1.

###### Applications

SBT is suitable for implementing a "safe brake" in conjunction with SBC. This allows errors or wear to be detected in the brake mechanics. Automatic testing of the braking effect reduces maintenance costs and increases safety and availability of the machine or plant.

###### Flow diagram

![Sequence: SBT](images/148126096139_DV_resource.Stream@PNG-en-US.png)

Sequence: SBT

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - SBT is selected during operation. - The drive initiates the brake test. |
| 2 | - The drive generates the test torque against the applied brake.   If the brake is functioning correctly, motion of the axis remains within a defined tolerance. However, if a larger axis movement is identified from the encoder actual values, the brake is not in a position to provide the specified holding torque. - Service or replace the brake. |
| 3 | - SLS is deactivated by the drive with (manual or automatic program-controlled) deselection. - Depending on the result of the brake test, the automation program can initiate the next step. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - Select SBT and Start SBT are implemented via the control bits of the Safety Control Channel (SCC) - in PROFIdrive telegram 701.   The SBT function is thus controlled directly from a higher-level controller. |
| B | - The drive performs the brake test with the following variables:    - Ramp time (p10208[0])   - Holding torque (p10209[0])   - Test torque = Factor (p10210[0])   - Test duration (p10211[0]) |
| C | - Define the maximum permissible axis motion with the position tolerance (p10212[0]). |
| D | - The drive signals the "SBT active" status in the status bit of the SIC/SCC. - You can utilize this status in the higher-level controller. |
| E | - Once SBT is concluded, the drive withdraws the SBT selection. |

###### Configuring SBT

###### Description

The diagnostic function "Safe Brake Test" (SBT) checks the required torque of the motor holding brake for the 1FK2 motor. The drive purposely generates a configurable torque against the applied brake. If the brake is operating correctly, the axis movement remains within a parameterized tolerance. However, if a larger axis movement is identified from the encoder actual values, the brake is not in a position to provide the specified holding torque. The brake must now be serviced or replaced.

###### Requirements

The following requirements must be satisfied when using the "SBT" function:

- Enable the Safety Integrated Extended Functions.
- Safe Brake Control must be enabled when testing a brake controlled by SINAMICS (motor holding brake).
- Speed control (p1300 = 21)

###### Functional characteristics

The "SBT" diagnostic function has the following properties:

- The parameters of the "SBT" function are protected by the Safety password, and can only be changed in the Safety commissioning mode.
- Using this function, brakes can be tested that are directly connected the converter (integrated brake control), but also externally controlled brakes (e.g. via a PLC).
- Test configurations: A maximum of one brake can be tested:

  - One motor holding brake, controlled by the integrated brake control of the SINAMICS.
- The "SBT" function is controlled via Safety Control Channel (SCC) via PROFINET.

  Using "SCC", the "SBT" function can be directly controlled from a higher-level controller.
- The "Safe Brake Test" (SBT) diagnostic function meets the requirements for category 2 according to EN ISO 13849‑1.

###### Configuring the brake test via SCC

The interconnection of the parameters for the telegram extension relevant for SCC/SIC can be performed automatically by setting [p60122](SINAMICS%20Parameter%20SINAMICS%20S210.md#r60122-profidrive-sicscc-telegram-selection) = 701. However, the telegram extension must have been previously created.

1. Record or correct the following information in the entry fields:

   - Test duration ([p10211](SINAMICS%20Parameter%20SINAMICS%20S210.md#p1021101-si-motion-sbt-test-duration-sequence-1)[0])
   - Holding torque ([p10209](SINAMICS%20Parameter%20SINAMICS%20S210.md#p1020901-si-motion-sbt-brake-holding-torque)[0])
   - Position tolerance ([p10212](SINAMICS%20Parameter%20SINAMICS%20S210.md#p1021201-si-motion-sbt-position-tolerance-sequence-1-1)[0])
   - Ramp time (p10209[0])
   - Factor ([p10210](SINAMICS%20Parameter%20SINAMICS%20S210.md#p1021001-si-motion-sbt-test-torque-factor-sequence-1)[0])
2. Click "Save project" in the toolbar to save the changes in the project.

###### Additional parameters

- [p1215](SINAMICS%20Parameter%20SINAMICS%20S210.md#p1215-motor-holding-brake-configuration)
- [p1216](SINAMICS%20Parameter%20SINAMICS%20S210.md#r1216-motor-holding-brake-opening-time)
- [p1217](SINAMICS%20Parameter%20SINAMICS%20S210.md#r1217-motor-holding-brake-closing-time)
- [p9501](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9501-si-motion-enable-safety-functions)
- [p9601](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9601-si-enable-functions-integrated-in-the-drive)
- [p9602](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9602-si-enable-safe-brake-control)
- [p10201](SINAMICS%20Parameter%20SINAMICS%20S210.md#p10201-si-motion-sbt-enable)
- [p10202](SINAMICS%20Parameter%20SINAMICS%20S210.md#p1020201-si-motion-sbt-brake)
- [p10208](SINAMICS%20Parameter%20SINAMICS%20S210.md#p1020801-si-motion-sbt-test-torque-ramp-time)
- p10209
- p10210
- p10211
- p10212
- [p10220](SINAMICS%20Parameter%20SINAMICS%20S210.md#p1022001-si-motion-sbt-test-torque-factor-sequence-2)
- [p10221](SINAMICS%20Parameter%20SINAMICS%20S210.md#p1022101-si-motion-sbt-test-duration-sequence-2)
- [p10222](SINAMICS%20Parameter%20SINAMICS%20S210.md#p1022201-si-motion-sbt-position-tolerance-sequence-2-1)
- [r10231](SINAMICS%20Parameter%20SINAMICS%20S210.md#r10231-si-motion-sbt-control-word-diagnostics)
- [r10234](SINAMICS%20Parameter%20SINAMICS%20S210.md#r10234015-si-safety-information-channel-status-word-s_zsw3b)
- [r10240](SINAMICS%20Parameter%20SINAMICS%20S210.md#r10240-si-motion-sbt-test-torque-diagnostics)
- [r10241](SINAMICS%20Parameter%20SINAMICS%20S210.md#r10241-si-motion-sbt-load-torque-diagnostics)
- [r60122](SINAMICS%20Parameter%20SINAMICS%20S210.md#r60122-profidrive-sicscc-telegram-selection)

---

##### SLS

This section contains information on the following topics:

- [Safely-Limited Speed (SLS) mode of operation](#safely-limited-speed-sls-mode-of-operation)
- [Configuring SLS](#configuring-sls)

###### Safely-Limited Speed (SLS) mode of operation

###### Overview

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/148126176651_DV_resource.Stream@PNG-en-US.png) |  |

The drive with an active "Safely-Limited Speed" (SLS) function monitors the speed/velocity of the motor to ensure that it does not exceed the speed/velocity threshold valid for SLS (SLS monitoring).

The SLS function prevents the parameterized maximum velocity from being exceeded. If the permitted speed is exceeded, then the drive initiates a parameterizable fault response. It is possible to switch between 4 different limit value levels in operation. Additionally, you can specify variable limit values during operation via PROFIsafe.

###### Applications

SLS is suitable for machines susceptible to hazardous situations if a speed is exceeded and wherever work must be performed directly on a machine, for example:

- during operation
- in setup mode
- during maintenance work

###### Sequence diagram: SLS with a speed level

![Sequence: SLS](images/148126193547_DV_resource.Stream@PNG-en-US.png)

Sequence: SLS

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - SLS is selected during operation. The speed exceeds the SLS limit value. - The drive initiates the SLS delay time. |
| 2 | - The actual speed must remain under the SLS limit value until the SLS delay time has elapsed. - After the SLS delay time has elapsed, the monitoring function takes effect (e.g. in "Setup" mode). |
| 3 | - SLS is deactivated by the drive with (manual or automatic program-controlled) deselection. - You can continue to traverse the axis immediately with larger setpoint values (e.g. switchover to "Automatic" mode). |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - SLS is selected via the control bit of the selected PROFIsafe telegram. |
| B | - The drive is braked by external setpoint value specification. - After the SLS delay time (p9551) has elapsed, the monitoring of the SLS limit value takes effect (level 1 = p9531[0]). |
| C | - If the SLS limit value is exceeded, the drive will carry out the set fault response (level 1 = p9563[0]). |
| D | - The drive reports the status "SLS active" in the status bit of the PROFIsafe telegram. - You can utilize this status in the higher-level controller. |
| E | - With deselection of the SLS via the control bit of the selected PROFIsafe telegram, the drive ends the monitoring of the SLS limit value. - The drive may be operated freely. |

###### Sequence diagram: SLS with switchover of the speed levels

![Sequence: SLS_2 levels](images/148126198411_DV_resource.Stream@PNG-en-US.png)

Sequence: SLS_2 levels

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - SLS level 1 is selected during operation. The speed exceeds the SLS limit value. - The drive initiates the SLS delay time. |
| 2 | - The actual speed must remain under the SLS limit value for level 1 until the SLS delay time has elapsed. - After the SLS delay time has elapsed, monitoring of level 1 takes effect. |
| 3 | - With the relative setpoint speed limit, the SLS limit value level 1 can be evaluated and provided as a setpoint limit. |
| 4 | - Switchover to SLS level 2 is initiated subsequently in the process. |
| 5 | - The SLS delay time is (re-)started when there is a switchover to a lower limit value. - The actual speed must remain under the SLS limit value for level 2 until it has elapsed. - The existing limit remains active during the delay time. - After the SLS delay time has elapsed, the lower limit value becomes active and the monitoring of SLS level 2 takes effect. |
| 6 | - SLS is deactivated by the drive with (manual or automatic program-controlled) deselection. - You can continue to traverse the axis immediately with larger setpoint values (e.g. switchover to "Automatic" mode). |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - SLS (level 1) is selected via the control bit of the selected PROFIsafe telegram. |
| B | - The drive is braked by external setpoint value specification. - After the SLS delay time (p9551) has elapsed, the monitoring of the SLS limit value takes effect (level 1 = p9531[0]). |
| C | - If the SLS limit value (level 1) is exceeded, the drive will carry out the set fault response (level 1 = p9563[0]). |
| D | - The drive reports the status "SLS active (level 1)" in the status bit of the PROFIsafe telegram. - You can utilize this status in the higher-level controller. |
| E | - The switchover to SLS (level 2) takes place via the control bits of the selected PROFIsafe telegram. |
| F | - The drive is braked by external setpoint value specification. - After the SLS switchover delay time = SLS delay time (p9551) has elapsed, the monitoring of the SLS limit value takes effect (level 2 = p9531[1]). |
| G | - If the SLS limit value (level 2) is exceeded, the drive will carry out the set fault response (level 2 = p9563[1]). |
| H | - The SLS active statuses (level 1 and level 2) are reported in the status bits of the PROFIsafe telegram. - You can use these values in the higher-level controller. |
| I | - With deselection of the SLS (level 2) via the control bit of the selected PROFIsafe telegram, the drive ends the monitoring of the SLS limit value. - The drive may be operated freely. |

###### SLS with variable speed limit value

SINAMICS offers the option of influencing the first SLS limit value via PROFIsafe:

- Transfer of the first SLS limit value via PROFIsafe is active if speed level 1 in the PROFIsafe telegram is selected and the bit "Enable transfer SLS limit via PROFIsafe" (p9501.24) is set.
- S_SLS_LIMIT_A has the value range 1 ... 32767; the following applies:

  - 32767 ≙ 100% of the 1st SLS level
  - The actually monitored limit value is calculated as follows:

    SLS limit value = (S_SLS_LIMIT_A/32767) · p9531[0]
- Speed levels 2, 3 and 4 can also be parameterized and selected in this case.
- You cannot change the selected delay time during operation. If you require various delay times in your application, you must fulfill this requirement using a time-delayed transfer of the SLS limit value using your controller (F‑CPU).
- If an incorrect SLS limit value is transferred, the drive responds with the fault response of speed level 1 parameterized in p9563 and Safety message A01711.

###### Configuring SLS

###### Description

The "Safely-Limited Speed" ("SLS") Safety Integrated Function is used to protect a drive against unintentionally high speeds in both directions of rotation. This is achieved by monitoring the current drive speed up to a velocity limit.

"SLS" prevents a parameterized speed limit value from being exceeded. Limits must be specified based on results of the risk analysis. Up to four different SLS speed limits can be parameterized; it is possible to switch between them even if the SLS is activated.

A PROFIsafe override can also be added to SLS limit value 1. In operation, this PROFIsafe override can be varied using a PROFIsafe telegram.

###### Functional characteristics

- When SLS is selected, the monitoring only takes effect after the configured delay time has expired ([p9551](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9551-si-motion-sls-switchoversos-delay-time)). Within this time, the actual velocity must be below the (selected) limit. The delay time is not effective when SLS is deselected.
- After switching to a lower limit value ([p9531](SINAMICS%20Parameter%20SINAMICS%20S210.md#p953103-si-motion-sls-limit-values-1)), the actual velocity of the drive must have dropped below the new limit within the delay time (p9551). The existing limit remains active during the delay time. The lower limit value becomes active after the delay time has expired. This also applies to a reduction of the limit value via PROFIsafe.
- If the actual velocity of the drive is higher than the new Safely-Limited Speed limit value after the delay time has expired, a message is generated with the parameterized fault response.
- The fault response is parameterized with [p9563](SINAMICS%20Parameter%20SINAMICS%20S210.md#p956303-si-motion-sls-specific-stop-response). Click on the green arrow next to the SLS level.
- On switchover to a higher limit value, the delay time is not active and the higher limit value becomes active immediately. This also applies to increasing the limit value via PROFIsafe.

###### Setting SLS via PROFIsafe

1. Click the ![Setting SLS via PROFIsafe](images/148125432331_DV_resource.Stream@PNG-en-US.png) button (Select SLS) in the "SLS" screen form to configure control of the "SLS" Safety Integrated Function.

   The "Control" screen form opens. The way the screen form is displayed depends on the basic settings of the Safety Integrated Function "SLS".

   In this screen form, configure the controls via the fail-safe inputs and outputs and/or PROFIsafe (see "[Control](#control)").
2. Call the "SLS" Safety Integrated Function again.
3. Correct the prescribed delay time in the field "Delay time for selection of SLS &gt;&gt; SLS active" (p9551).
4. Enter a suitable value for level 1 of the speed limit (p9531[0]).
5. Select the required fault response for level 1 in the drop-down list (p9563[0]).
6. Click the ![Setting SLS via PROFIsafe](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) icon to open the configuration for level 1.

   Screen form "SS2" opens:

   Set the desired motor deceleration here (see "[Configuring SS2](#configuring-ss2)")
7. If you want to additionally configure levels 2, 3, and/or 4 for the speed limit, repeat steps 4 to 6 for each level.
8. In the "Setpoint velocity limitation SLS level" ([p9533](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9533-si-motion-sls-setpoint-speed-limiting)) field, enter a weighting factor for determining the setpoint limit from the selected actual velocity limit as a percentage.
9. If you want to use a PROFIsafe override for level 1 of the speed limit, select the "Enabled" option in the "PROFIsafe override" ([p9501](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9501-si-motion-enable-safety-functions).24) drop-down list.

**Result**

The velocity limit value of the drive is configured. The current SLS limit value is displayed in the field of the same name ([r9714](SINAMICS%20Parameter%20SINAMICS%20S210.md#r971403-si-motion-diagnostics-velocity-1)[2]). The effective setpoint limit is displayed in the field of the same name ([r9733](SINAMICS%20Parameter%20SINAMICS%20S210.md#r973302-si-motion-setpoint-speed-limit-effective)). It is used, for example, to transmit values to a higher-level control system, which can then, for example, adapt traversing speeds to the SLS levels. The effective setpoint limit is part of the Safety Info Channel (SIC).

###### Additional parameters

- p9501
- p9531
- p9551
- p9563
- p9580
- [p9581](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9581-si-motion-brake-ramp-reference-value-1)
- [p9582](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9582-si-motion-brake-ramp-delay-time)
- [p9583](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9583-si-motion-brake-ramp-monitoring-time)
- [p9601](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9601-si-enable-functions-integrated-in-the-drive)
- r9714
- [r9720](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9720028-si-motion-control-signals-integrated-in-the-drive)
- r9721
- [r9722](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9722028-si-motion-drive-integrated-status-signals)

---

##### SSM

This section contains information on the following topics:

- [Safe Speed Monitor (SSM) mode of operation](#safe-speed-monitor-ssm-mode-of-operation)
- [Configuring SSM](#configuring-ssm)

###### Safe Speed Monitor (SSM) mode of operation

###### Overview

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/148126299019_DV_resource.Stream@PNG-en-US.png) |  |

The "Safe Speed Monitor" (SSM) function provides a reliable method for detecting when the velocity falls below the velocity limit in both directions of rotation, e.g. for standstill detection.

The drive provides a safe output signal for further processing.

###### Applications

SSM is suitable for the realization of enabling access to the machine by way of safe SSM feedback. For example, to ensure that protective doors can only be unlocked when the critical speeds fall below those specified.

###### Flow diagram

![Sequence: SSM](images/148126303243_DV_resource.Stream@PNG-en-US.png)

Sequence: SSM

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - Function SSM is enabled with p9501.16. - If the speed falls below the speed limit, the "Speed below limit value" signal is set. - If the speed is greater than the limit, the "Speed below limit value" is not set. |
| 2 | - The hysteresis ensures that a stable signal characteristic is achieved for speeds close to the monitoring threshold: This ensures that the SSM output signal does not jump between the values "0" and "1" in the limit range. - When hysteresis and filtering is activated with output signal SSM, a time-delayed SSM feedback signal occurs for the axes. This is a characteristic of the filter. |
| 3 | - The signal filter smoothes the speed measured by the drive.   Use the filter if you wish to monitor speeds that lie just below the velocity limit. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - The function becomes active as soon as the Safety Integrated Extended Functions (p9501.0 = 1) are enabled and SSM is activated (p9501.16 = 1). |
| B | - The speed limit (p9546) is effective in both directions of rotation. The SSM function is deactivated with the setting speed limit = 0. |
| C | - The speed hysteresis (p9547) stabilizes the output signal speed below limit value. - The speed hysteresis must be ≤ 0.75 · speed limit. |
| D | - The "Speed below limit value" status is signaled in the status bit of the PROFIsafe telegram. - You can utilize this status in the higher-level controller. |
| E | - You set the response with the filter time (p9545). |

###### SSM is a pure signaling function

Unlike other Safety Integrated Functions, exceeding the SSM limit value does not result in a drive-autonomous fault response.

###### Relationship between SSM and SAM

If 0 is entered for p9568 (SAM shutdown threshold), the velocity limit of the SSM function (p9546) is simultaneously the lower limit for the Safe Acceleration Monitor function (SAM).

In this case, the effects of safe acceleration monitoring are therefore restricted if a relatively high SSM speed limit is set when using the SS1 and SS2 stop functions.

###### Configuring SSM

###### Description

The "Safe Speed Monitor" (SSM) function provides a reliable method for detecting when the velocity falls below the velocity limit ([p9546](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9546-si-motion-ssm-velocity-limit-1)) in both directions of rotation, e.g. for standstill detection. A fail-safe output signal is available for further processing. The hysteresis of the function is enabled automatically for S210.

###### SSM with hysteresis

A velocity hysteresis can be configured for the "SSM" function. In this way, a more stable signal characteristic of SSM can be achieved at velocities close to the velocity limit.

For the hysteresis, the velocity (or speed) determined by the two channels must not differ by more than the difference between the velocity limit and the velocity hysteresis. Otherwise it would be theoretically possible that one channel returns a HIGH signal and the other a LOW signal for "SSM".

The following figure shows the characteristic of the "SSM" safe output signal when hysteresis is active:

![Motion monitoring_SSM.eps](images/147781004171_DV_resource.Stream@PNG-en-US.png)

Motion monitoring_SSM.eps

The output signal for SSM is smoothed by setting a filter time with a PT1 filter ([p9545](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9545-si-motion-ssm-filter-time)).

**Settings:**

1. Enter the required value in mm/min in the "Velocity hysteresis" ([p9547](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9547-si-motion-ssm-velocity-hysteresis-1)) field.
2. Enter the required limit value in mm/min in the "Velocity limit" (p9546) field.
3. Specify a time value for the PT1 filter in the "Filter time" (p9545) field.
4. Click "Save project" in the toolbar to save the changes in the project.

###### Additional parameters

- [p9501](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9501-si-motion-enable-safety-functions)
- [p9506](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9506-si-motion-function-specification)
- p9545
- p9546
- p9547
- [r9722](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9722028-si-motion-drive-integrated-status-signals)

---

##### SDI

This section contains information on the following topics:

- [Safe Direction (SDI) mode of operation](#safe-direction-sdi-mode-of-operation)
- [Configuring SDI](#configuring-sdi)

###### Safe Direction (SDI) mode of operation

###### Overview

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/148126327051_DV_resource.Stream@PNG-en-US.png) |  |

The drive with active function "Safe Direction" (SDI) monitors the direction of rotation of the motor. If the motor rotates in the impermissible direction, the drive stops the motor as quickly as possible.

###### Applications

SDI is suitable for the following cases:

- Machines on which cyclic material must be loaded and removed
- For protection against impermissible direction of rotation

###### Flow diagram

![Sequence: SDI](images/148126331147_DV_resource.Stream@PNG-en-US.png)

Sequence: SDI

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - SDI is selected during operation. - The drive initiates the SDI delay time. |
| 2 | - You must actuate the drive in the enabled safe direction until the SDI delay time has elapsed. - Monitoring of the direction of rotation becomes effective once the SDI delay time has elapsed. |
| 3 | - SDI is deactivated by the drive with (manual or automatic program-controlled) deselection. - You can traverse the axis immediately in both directions of rotation. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - "Select SDI" is performed via the control bits of the selected PROFIsafe telegram. |
| B | - The drive is operated in the enabled direction via external setpoint specification. - Monitoring of the direction of rotation becomes effective once the SDI delay time (p9565) has elapsed. |
| C | - Monitoring takes the tolerance (p9564) into account. |
| D | - The drive reports the status "SDI active" in the status bit of the PROFIsafe telegram. - You can utilize this status in the higher-level controller. |
| E | - The drive ends monitoring of the direction of rotation with "Deselect SDI" via the control bit of the selected PROFIsafe telegram. - You can traverse the axis immediately in both directions of rotation. |

###### Configuring SDI

###### Description

The "Safe Direction" (SDI) function allows reliable monitoring of the direction of motion of the drive. If this function is activated, the drive can only move in the enabled direction. You can check whether SDI is active in the "[Function status](#function-status)" screen form. When active, at least one of the LEDs is green:

- SDI positive active ([r9722](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9722028-si-motion-drive-integrated-status-signals).12)
- SDI negative active (r9722.13)

> **Note**
>
> **No change of direction detected**
>
> If the direction of rotation ([p1821](SINAMICS%20Parameter%20SINAMICS%20S210.md#p18210-direction-of-rotation)) is reversed in the [basic parameterization](#basic-parameter-assignment-1), then safe monitoring is still possible: However, in this case, the setpoint limitation [r9733](SINAMICS%20Parameter%20SINAMICS%20S210.md#r973302-si-motion-setpoint-speed-limit-effective) is calculated with the wrong direction of rotation. A reversal of the direction of rotation therefore does not make sense in this case.

###### Parameterizing SDI

After SDI has been selected via PROFIsafe (see "[Making basic settings](#making-basic-settings)"), delay time [p9565](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9565-si-motion-sdi-delay-time) is started. During this time, you have the option of ensuring that the drive is moving in the enabled direction. After this, the "Safe Direction" function is active and the direction of motion is monitored.

If the drive now moves more than the configured tolerance ([p9564](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9564-si-motion-sdi-tolerance-1)) in the blocked direction, message C01716 is output and the fault response defined in [p9566](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9566-si-motion-sdi-stop-response) is initiated. To acknowledge the messages, you must first deselect SDI, remove the fault cause and then safely acknowledge the messages. Only then can you reselect SDI.

1. Enter a delay time in ms in the "Delay time for selection of SDI -&gt; SDI active" (p9565) field.
2. Enter a monitoring tolerance in mm in the "Monitoring tolerance" (p9564) field.
3. Select the desired fault response in the "Selection" drop-down list (p9566).
4. Click on the icon ![Parameterizing SDI](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) to open an additional configuration screen form for the set fault response.

   Make the necessary configuration here.
5. Click "Save project" in the toolbar to save the changes in the project.

###### Meaning of the display (SDI active)

The "SDI active" icon indicates the following states:

| Symbol | Meaning |
| --- | --- |
| ![Meaning of the display (SDI active)](images/147858416139_DV_resource.Stream@PNG-en-US.png) | SDI not selected |
| ![Meaning of the display (SDI active)](images/147858420107_DV_resource.Stream@PNG-en-US.png) | SDI positive active |
| ![Meaning of the display (SDI active)](images/147858424075_DV_resource.Stream@PNG-en-US.png) | SDI negative active |
| ![Meaning of the display (SDI active)](images/147858428043_DV_resource.Stream@PNG-en-US.png) | SDI positive and SDI negative active |

###### Additional parameters

- p1821
- [p9501](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9501-si-motion-enable-safety-functions)
- [p9506](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9506-si-motion-function-specification)
- p9564
- p9565
- p9566
- p9580
- [r9720](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9720028-si-motion-control-signals-integrated-in-the-drive)
- r9722
- r9733

---

##### SLA

This section contains information on the following topics:

- [Safely-Limited Acceleration (SLA) mode of operation](#safely-limited-acceleration-sla-mode-of-operation)
- [Configuring SLA](#configuring-sla)

###### Safely-Limited Acceleration (SLA) mode of operation

###### Overview

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/148126406155_DV_resource.Stream@PNG-en-US.png) |  |

The Safety Integrated Function "Safely-Limited Acceleration" (SLA) ensures that the drive does not exceed a preset acceleration limit (e.g. in setup mode).

###### Applications

SLA is suitable for machines for which the permissible acceleration may not be exceeded, for example in setup mode.

###### Flow diagram

![Sequence: SLA](images/148126417291_DV_resource.Stream@PNG-en-US.png)

Sequence: SLA

| Symbol | Meaning |
| --- | --- |
| **Behavior** |  |
| 1 | - SLA is selected during operation. - The drive initiates acceleration monitoring. |
| 2 | - The drive monitors the defined acceleration limit during acceleration, as well as for braking, to ensure that it is not exceeded. |
| 3 | - If SLA detects that the acceleration limit has been exceeded, the drive initiates the configured fault response. |
| 4 | - SLA is deactivated with (manual or automatic program-controlled) deselection. - You can traverse the axis immediately in both directions of rotation. |

| Symbol | Meaning |
| --- | --- |
| **Settings** |  |
| A | - Select SLA via a control bit of the PROFIsafe telegram. |
| B | - Define the maximum permissible acceleration with the acceleration limit (p9578). |
| C | - When the SLA limit is violated, the drive executes the fault response (p9579). |
| D | - The drive signals the "SLA active" status in the status bit of the PROFIsafe telegram. - You can utilize this status in the higher-level controller. |
| E | - Once SLA is concluded, the drive withdraws "Select SLA". |

###### Configuring SLA

###### Description

Safety function "Safely-Limited Acceleration" (SLA) ensures that the drive does not exceed a preset acceleration limit (e.g. in setup mode). SLA detects early on whether the drive is accelerating too quickly and initiates the fault response. SLA has no effect with braking.

![SLA overview](images/148126434955_DV_resource.Stream@PNG-en-US.png)

SLA overview

###### Setting Safely-Limited Acceleration

1. Click the ![Setting Safely-Limited Acceleration](images/148125432331_DV_resource.Stream@PNG-en-US.png) button (Select SLA) to configure control of the "SLA" function.

   The "Control" screen form opens. The display of the screen form depends on the basic settings of the Safety Integrated Extended Functions.

   In this screen form, configure the controls via PROFIsafe (see "[Control](#control)").

   You can select the PROFIsafe telegrams in the telegram configuration. This means you also specify the required control word.
2. Call the "SLA" function/screen form once again.
3. Enter a value for the acceleration limit of the Safely-Limited Acceleration in the "Acceleration limit" field ([p9578](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9578-si-motion-sla-acceleration-limit-1)).

   This limit value applies to a positive and negative direction of rotation. The drive in [r9790](SINAMICS%20Parameter%20SINAMICS%20S210.md#r979001-si-motion-sla-acceleration-resolution-1) indicates the possible acceleration resolution.
4. In the "Filter time" ([p9576](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9576-si-motion-sla-filter-time)) field, enter a value for the acceleration monitoring filter time.
5. In the "Fault response" ([p9579](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9579-si-motion-sla-stop-response)) drop-down list, choose the fault response for Safely-Limited Acceleration.

   If SLA later detects that the acceleration limit has been exceeded, the drive initiates the configured fault response.
6. In the "Filter time" (p9576) field, enter the filter time for the acceleration monitoring with fine resolution.
7. Click the ![Setting Safely-Limited Acceleration](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) icon to open the "SS1" screen form.

   Here you correct the settings for the motor deceleration (see "[Safely-Limited Acceleration (SLA) mode of operation](#safely-limited-acceleration-sla-mode-of-operation)").

###### Transmission via PROFIsafe

After SLA has been parameterized and selected, the results of the monitoring are transferred in status words S_ZSW1.8 or S_ZSW2.8.

> **Note**
>
> **Response to bus failure**
>
> If p9580 ≠ 0 and SLA is active, in the event of communication failure, the parameterized ESR reaction is only performed if, as the SLA response, a stop with delayed pulse cancellation when the bus fails has been parameterized (p9579 ≥ 10).

###### Transmission via SIC

After "SLA" has been parameterized and selected, the results of the monitoring are also transferred in the SIC in status word S_ZSW1B.8. You will find this status word in telegrams 700 and 701.

###### Additional parameters

- [p9501](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9501-si-motion-enable-safety-functions)
- p9578
- p9579
- [r9714](SINAMICS%20Parameter%20SINAMICS%20S210.md#r971403-si-motion-diagnostics-velocity-1)
- r9790

---

#### Response to Safety faults

This section contains information on the following topics:

- [Stop responses](#stop-responses)
- [Discrepancy at the inputs of an F-DI](#discrepancy-at-the-inputs-of-an-f-di)
- [Acknowledging Safety Integrated faults](#acknowledging-safety-integrated-faults)

##### Stop responses

###### Overview of stop responses

Safe stops (stop responses of the drive) are used to stop a drive in motion and bring it to a standstill. The type of stop response that occurs in the event of faults/errors can either be permanently specified by the system or configured by the machine manufacturer - for example, if a limit value is violated or an internal fault occurs.

In this way, you can stop the machine optimally adapted to the specific situation.

![Overview of the stop variants](images/148126549003_DV_resource.Stream@PNG-en-US.png)

Overview of the stop variants

###### Explanation of the stop responses

If faults occur in Safety Integrated Functions, the following stop responses can be triggered:

- **Internal event**

  An "internal event" is a serious error for which the drive will bring the motor to a standstill as quickly as possible.

  An "internal event" can be triggered, for example, when the drive detects an error in the monitoring channels during the crosswise data comparison (e.g. F01611 "Defect in a monitoring channel").

  An "internal event" can only be acknowledged with a fail-safe signal.
- **STO stop response**

  For an STO stop response, the drive safely switches off the torque of the connected motor immediately.
- **SS1 stop response**

  The drive is braked (speed-controlled) at the current limit and transitioned to a safe stop (SOS) (corresponds to stop category 1 according to EN 60204‑1, without galvanic isolation).

  Application case

  - e.g. when SOS is addressed
- **SS2 stop response**

  The drive is braked (speed-controlled) at the current limit and transitioned to a Safe Operating Stop (corresponds to stop category 2 according to EN 60204‑1).

  An SS2 stop response followed by an STO is normally selected in the case of an emergency stop because this is the quickest way of stopping a drive.

  Application case:

  - Operator protection
- **SS2E stop response**

  The drives are collectively braked relative to the path (interpolated) on the contour and transitioned into the Safe Operating Stop (SOS).

  Application case:

  - Protection for tools and workpieces (machine protection)
- **KDV stop response**: F01611 ("SI P1: Defect in a monitoring channel") or C01711 ("SI Motion P1: Defect in a monitoring channel")

  - Safety Integrated Basic Functions

    Stop response F01611 is triggered if an error in the data cross-check (KDV) of the monitoring channels is detected. The cause of stop response F01611 is indicated in parameter r9795.

    If a Safety Integrated Function is active, the fault F01611 triggers an STO after the transition time p9658.
  - Safety Integrated Extended Functions

    One of the stop responses F01611 is triggered if an error in the data cross-check (KDV) of the monitoring channels is detected. The cause of stop response F01611 is indicated in parameter r9795. The cause of stop response C01711 is indicated in parameter r9725.

    As a consequence, STO is triggered and fault F01600 is displayed.

    > **Note**
    >
    > The transition time from F01611 to STO (p9658) must be set greater than or equal to the delay time (p9652).

  **Rules for CDC:**

  If a Safety Integrated Function is active, the following applies.

  - The fault F01611 triggers an STO after the transition time p9658.
  - When a Safety Integrated Function is active according to p9555, the message C01711 leads to the SS1 of the Safety Integrated Extended Functions.

  If no Safety Integrated Functions are active, the following applies for C01711:

  - Message C01711 does not trigger an immediate stop response. The message is still pending.
  - When a Safety Integrated Function is selected, the drive responds with a stop as described above.

##### Discrepancy at the inputs of an F-DI

If there is a discrepancy between the two digital inputs of an F-DI, the drive ignores the signals via the Failsafe Digital Input and transitions to the safe STO state.

###### Drive response

The drive sets the bit "Internal event" after the discrepancy time has elapsed. You cannot switch on the motor as long as this signal is active.

> **Note**
>
> **Discrepancy time**
>
> To avoid incorrectly triggered fault messages, the selected discrepancy time in p9650 must always be shorter than the shortest time between 2 switching events at these inputs (ON/OFF, OFF/ON).

The drive indicates the discrepancy error when the RDY-LED flashes quickly red.

- On the numerical display, the drive outputs message Class "10". It signals the fault via the web server and vie PROFIsafe

  - "Discrepancy (fault F01611 or F30611 "Defect in a monitoring channel" with fault values r0949 = 2000 or 2002)"
- The drive sets the error bit of the safety functions (= internal event).

Independent of the voltage levels present, the drive remains in the STO state until you have acknowledged the "Internal event" state.

##### Acknowledging Safety Integrated faults

To acknowledge faults and switch on the motor again, proceed as follows:

###### Acknowledging an internal event

Eliminate the cause of the internal event (e.g. wire break). You have the following options for acknowledging the signal:

1. Acknowledge via PROFIsafe.

   - Selecting and deselecting STO
   - Selecting and deselecting SS1
   - Fail-safe acknowledgement of communication telegrams and bit assignment of the process data
2. Select or deselect the fail-safe digital input F-DI.
3. Turn the supply voltage off and on again.

###### Switching the motor on again

1. Acknowledge the drive faults using one of the following methods:

   - Via the OK switch on the drive
   - Via the web server
   - Via the PLC
2. Switch the motor off and then on again. (bit 0 in STW1: 0 → 1)

#### Actual value acquisition/mechanical system

##### Requirement

- Extended Functions are selected in the function selection of Safety Integrated.

##### Parameterizing actual value acquisition

1. Select the drive axis type in the "Axis type" drop-down list ([p9502](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9502-si-motion-axis-type)):

   - "Linear axis"
   - "Rotary axis"
2. If you are using a "Rotary axis" axis type, enter the modulo value in degrees for the rotary axes in the "Modulo value" field ([p9505](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9505-si-motion-sp-modulo-value)).

   This setting is used exclusively to ensure correct display of the diagnostics information ([r9708](SINAMICS%20Parameter%20SINAMICS%20S210.md#r970805-si-motion-diagnostics-safe-position-1)).

   Set the value so that it lies precisely at 2^n revolutions; this means that when the range that can be represented overflows (+/-2048), the actual position value does not exhibit a step (jump).
3. If using the "Linear axis" axis type, set the transmission ratio between encoder and load in mm (linear axis with rotary encoder) in the "Leadscrew pitch" field ([p9520](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9520-si-motion-spindle-pitch)).
4. If a rotational direction reversal is linked with the gear being used, activate the 'Load rotational direction reversal" ([p9539](SINAMICS%20Parameter%20SINAMICS%20S210.md#p953907-si-motion-gearbox-direction-of-rotation-reversal)) option.
5. Should you wish to use a gear ratio for the gear, record the values for "Load revolutions" ([p9521](SINAMICS%20Parameter%20SINAMICS%20S210.md#p952107-si-motion-gearbox-encoder-motorload-denominator)) and "Encoder revolutions" ([p9522](SINAMICS%20Parameter%20SINAMICS%20S210.md#p952207-si-motion-gearbox-encoder-motorload-numerator)) necessary in this regard.

   A gear ratio is the ratio of encoder revolutions to revolutions of the drive shaft (load revolutions).
6. Should you wish to adopt the encoder data automatically in the Safety parameters, click on the "Adopt encoder data" button.

   The parameter values "Line count" ([p9518](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9518-si-motion-encoder-pulses-per-revolution)), "Fine resolution" ([p9519](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9519-si-motion-fine-resolution-g1_xist1)) and "Sign change of the actual position value" ([p9516](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9516-si-motion-encoder-configuration-safety-functions).1) are imported from the encoder data and displayed in the display fields.
7. Save the project data and perform a POWER ON.

##### Additional parameters

- p9502
- p9505
- p9516
- p9518
- p9519
- p9520
- p9521
- p9522
- p9539

---

#### Control

##### Description

Parameterize the settings of the SINAMICS S210 for the fail-safe inputs and outputs or control via PROFIsafe here.

Only the parameters required for the selected control type (see [Making basic settings](#making-basic-settings)) are displayed in the screen form.

##### F-DI configuration

The signal states of an F-DI are monitored to determine whether they have assumed the same logical state within the discrepancy time.

For example, the unavoidable delay caused by mechanical switching operation can be adapted via parameters. The time within which the selection or deselection must be performed in both monitoring channels in order to qualify as "simultaneous", is specified with [p9650](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9650-si-f-di-discrepancy-time).

For internal errors or limit value violations, the drive-internal Safety Integrated Function issues Safety faults.

1. Enter a discrepancy time [ms] in the "Discrepancy time" (p9650) field.
2. Enter a time [ms] for the input filter (debounce time) in the "F-DI input filter" ([p9651](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9651-si-stosbcss1-t_debounce-time)) field.

   This debounce time applies to F-DIs and the readback input for the forced checking procedure. The debounce time specifies the maximum time an interference pulse can be present at an F-DI before being interpreted as a switching operation.
3. If you also wish to change the digital inputs, click on symbol ![F-DI configuration](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) "Digital inputs".

   Screen form "[Digital inputs](#digital-inputs)" is displayed. If necessary, correct the configuration of the digital inputs.

##### PROFIsafe configuration

The PROFIsafe address is required for control of the Safety Integrated Functions via PROFIsafe.

1. Click the icon ![PROFIsafe configuration](images/147856715147_DV_resource.Stream@PNG-en-US.PNG) "Telegram configuration"

   The properties of the PROFINET interface are displayed in the inspector window. The "Cyclic data traffic" setting range is active. The telegrams for the drive objects can be specified here.
2. Click the &lt;Add telegram&gt; entry in the telegram configuration of "Drive axis_x".
3. Select the "Add Safety telegram" option in the drop-down list of the entry:

   The "Safe actual value" and "Safe setpoint" lines are then inserted. The relevant PROFIsafe telegrams are preassigned.
4. Open the new "Safe setpoint" screen form (for Drive axis_x) in the inspector window.
5. Correct the PROFIsafe address of the drive in the "F-address" field.
6. Switch back to the "Control" screen form of the DRIVE-CLiQ editor.

   The value of the F-address is displayed in the "PROFIsafe address" ([p9610](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9610-si-profisafe-address)) field. A preassigned PROFIsafe telegram is displayed in the "PROFIsafe telegram no." drop-down list.
7. Click "Accept values" to transfer the telegram from the default settings into the Safety programming.
8. Select the desired stop response for a failure of the PROFIsafe communication in the "PROFIsafe failure response" ([p9612](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9612-si-profisafe-failure-response)) drop-down list.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Uncontrollable responses of the drive when PROFIsafe addresses are not unique**  PROFIsafe addresses can be assigned via an automated mechanism. If these automatically generated PROFIsafe addresses are not unique CPU-wide and network-wide, this can lead to uncontrollable responses of the drive. If persons are in the danger zone, accidents causing death or severe injury can occur.  - Take suitable measures to ensure that the fail-safe I/O of PROFIsafe address type 1 is addressed clearly by its fail-safe destination address. - Make sure that the fail-safe destination address of the fail-safe I/O (drive units in this case) is unique for the entire fail-safe I/O network-wide and CPU-wide (system-wide). The fail-safe I/O of PROFIsafe address type 2, e.g. modules of the ET 200SP type, must also be taken into account. - Note also the corresponding documentation in the TIA Portal online help in Section "[SIMATIC Safety - Configuring and programming](SIMATIC%20Safety%20-%20Configuring%20and%20Programming.md#simatic-safety---configuring-and-programming)". |  |

##### Additional parameters

- p9610
- p9650
- p9651

---

#### Test stop

Parameterize the timer settings for the test of the shutdown paths (test stop) in the "Test stop" screen form.

To meet the requirements of the DIN EN ISO 13849‑1 and IEC 61508 standards in terms of timely fault detection, the converter must test its safety-related circuits regularly – at least once a year – for correct functioning. The maximum permissible interval for the test stop for Basic and Extended Functions is 9000 hours.

The converter monitors the regular test of its safety-related circuits that monitor the speed of the motor, and to safely interrupt the torque-generating energy supply to the motor through the safe pulse suppression.

##### Safety devices

When the appropriate safety devices are implemented (e.g. protective doors), it can be assumed that running machinery will not pose any risk to personnel. The user is therefore only informed that the test of the shutdown paths is pending by an alarm, which requests the user to perform the test stop at the next possible opportunity.

Examples for the execution of the tests:

- When the drives are at a standstill after the system has been switched on (POWER ON).
- Before the protective door is opened.
- At defined intervals (e.g. every eight hours).
- In automatic mode (time and event-dependent).

##### Test stop for Basic Functions

To parameterize the test stop for the Basic Functions, proceed as follows:

1. Enter the interval for performing the forced checking procedure and testing the Safety shutdown paths in the "Timer" ([p9659](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9659-si-forced-checking-procedure-timer)) field.

   Within the parameterized time, the "STO" function must be selected and deselected at least once. The monitoring time is reset at every STO deselection.

**Result**

- If the automatically initiated function cannot be correctly completed as a result of a problem (e.g. communication failure), the function will be automatically restarted after the problem has been resolved.
- The automatic test stop for POWER ON does not affect the Safety Integrated Functions.
- After the test stop has been performed successfully, the converter goes into the "Ready" state.
- If there is an automatic test stop, the timer will be reset.

  > **Note**
  >
  > **Reset timer of Basic Functions automatically**
  >
  > If, when simultaneously using the Extended Functions, the associated test stop is performed, the timer of the Basic Functions is also reset.
  >
  > While STO is selected by the Extended Functions, the onboard terminals for the selection of the Basic Functions are not checked for discrepancy. This means that the test stop of the Basic Functions must always be performed without the selection of STO or SS1 by the Extended Functions. Otherwise the correct control by the onboard terminals cannot be checked.

##### Test stop for Extended Functions

> **Note**
>
> If the "Basic Functions via onboard terminals" option is active for the Extended Functions, you must make the test stop settings for the Basic Functions as well as for the Extended Functions.

To parameterize the test stop for the Extended Functions, proceed as follows:

1. Enter the interval for performing the forced checking procedure and testing the Safety shutdown paths in the "Timer" ([p9559](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9559-si-motion-forced-checking-procedure-timer)) field.

   Within the parameterized time, the "STO" function must be selected and deselected at least once. The monitoring time is reset at every STO deselection.

**Result**

- If the automatically initiated function cannot be correctly completed as a result of a problem (e.g. communication failure), the function will be automatically restarted after the problem has been resolved.
- The automatic test stop for POWER ON does not affect the Safety Integrated Functions.
- After the test stop has been performed successfully, the converter goes into the "Ready" state.
- If there is an automatic test stop, the timer will be reset.

##### Status display

The following elements show the current status of the forced checking procedure:

- Remaining time:

  Shows the time remaining until the forced checking procedure and the test of the Safety shutdown paths are performed ([r9660](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9660-si-forced-checking-procedure-remaining-time) for the Basic Functions, [r9765](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9765-si-motion-forced-checking-procedure-remaining-time) for the Extended Functions).

##### Additional parameters

- p9559
- p9659
- r9660
- r9765
- [r9743](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9743813-si-safety-information-channel-status-word-s_zsw2b)

---

#### Function status

##### Status messages

The "Function status" screen form displays a list of all Safety Integrated Functions on the left.

All Safety Integrated Functions activated in Startdrive are identified by a green LED.

In addition, the most important information of the selected Safety Integrated Functions is displayed.

The status information is displayed on the right-hand side of the screen form for:

- Test stop required

  Indicates that a test of the shutdown paths (test stop) is required.

  - Timer test stop ([p9659](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9659-si-forced-checking-procedure-timer)):

    Time interval for performing the forced checking procedure and testing the Safety shutdown paths. Within the parameterized time, the STO must be selected and deselected at least once. The monitoring time is reset at every STO deselection.
  - Remaining time ([r9660](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9660-si-forced-checking-procedure-remaining-time) for the Basic Functions, [r9765](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9765-si-motion-forced-checking-procedure-remaining-time) for the Extended Functions)

    Shows the time remaining until the test of the Safety shutdown paths is performed.
- Internal event

  Set when the first Safety message occurs.

##### Additional parameters

- [p9559](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9559-si-motion-forced-checking-procedure-timer)
- p9659
- [r9781](SINAMICS%20Parameter%20SINAMICS%20S210.md#r978101-si-checksum-to-check-changes)
- [r9782](SINAMICS%20Parameter%20SINAMICS%20S210.md#r978201-si-change-control-time-stamp)
- [r9722](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9722028-si-motion-drive-integrated-status-signals)
- [r9723](SINAMICS%20Parameter%20SINAMICS%20S210.md#r9723016-si-motion-diagnostic-signals-integrated-in-the-drive)

---

#### Acceptance mode

##### Description

The acceptance mode can be activated ([p9570](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9570-si-motion-acceptance-test-mode)) for a parameterized time ([p9558](SINAMICS%20Parameter%20SINAMICS%20S210.md#p9558-si-motion-acceptance-test-mode-time-limit)), and allows intentional limit violations during the acceptance test. For instance, the setpoint velocity limits are no longer active in acceptance mode. To ensure that this state is not accidentally retained, the acceptance mode is automatically exited after the time set in p9558.

It only makes sense to activate the acceptance mode during the acceptance test of the SS2, SOS, SDI and SLS functions. The acceptance mode has no effect on other functions.

Normally, SOS can be selected directly or via SS2. To enable triggering of a violation of the SOS standstill limits while acceptance mode is active (also in the "SS2 active" state), the setpoint is enabled again by the acceptance mode after deceleration and transition to SOS. Movement of the motor is thus possible. When an SOS violation is acknowledged in active acceptance mode, the current position is adopted as the new standstill position so that an SOS violation is not immediately detected again.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unexpected axis movement upon activation of the acceptance test**  If a speed setpoint ≠ 0 is present, the active stop function SS2 is set, and the motor is at a standstill (active SOS), the axis starts to move as soon as the acceptance test is activated. If persons are in the danger zone, accidents causing death or severe injury can occur.  - Take suitable measures to ensure that nobody is in the danger zone during the acceptance test. |  |

##### Activating acceptance mode

1. Correct the specified maximum time for the acceptance mode in the "Acceptance test time limit" (p9558) field.

   If the acceptance mode lasts longer than the set time limit, the mode is exited automatically.
2. Perform a POWER ON to activate the parameters.

   The "Activate acceptance mode" button is then activated.
3. To activate acceptance mode, click the "Activate acceptance mode" button (p9570).

   For activated acceptance mode, you can switch off manually via the "Deactivate acceptance mode" button.

##### Additional parameters

- p9558
- p9570

---

### Inputs/outputs

This section contains information on the following topics:

- [Digital inputs](#digital-inputs)

#### Digital inputs

The S210 converter has the following digital inputs that you can parameterize:

- Failsafe Digital Input (F-DI, DI 2 and DI 3)
- 2 high-speed digital inputs (DI 0 and DI 1) as measuring probes for the evaluation in the controller
- Digital input DI 4 for monitoring the temperature of an optional, external brake resistor

##### Requirements

- The PROFIdrive telegram 105 is set.

  This telegram is preset when an S210 drive is created.
- The following settings must be set in the Safety Integrated basic setting for the parameterization of the F-DI:

  - At least one Safety Integrated Function must be activated.
  - For the control method: "via PROFIsafe", the option "... functions via onboard terminals" must be activated.

##### Configuring digital inputs

1. In the "Activate measuring probe 1" field, select whether you want to use the measuring probe for DI 0.
2. In the "Activate measuring probe 2" field, select whether you want to use the measuring probe for DI 1.
3. In the "Activate equivalent zero mark" drop-down list, select whether you want to use a zero mark replacement and whether this zero mark replacement is to apply to DI 0 or DI 1.
4. In the "Activate overtemperature monitoring for external brake resistor" drop-down list, select whether or not the temperature monitoring of the external brake resistor is to be activated.
5. If you want to configure the Failsafe Digital Inputs, click on the button to the right of "F-DI".

   Then the "Control" Safety interconnection screen opens. Parameterize the Failsafe Digital Inputs for the controller via PROFIsafe here (see [Control](#control)).
6. Then save the project to accept the settings.

## Rotate & optimize

This section contains information on the following topics:

- [Using the control panel](#using-the-control-panel)
- [Traversing the drive with speed specification](#traversing-the-drive-with-speed-specification)
- [Performing One Button Tuning](#performing-one-button-tuning)

### Using the control panel

#### Overview

You can use the control panel to traverse the drive and test the settings that have been made.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Danger to life in the event of non-observance of the safety instructions for the drive control panel**  The safety shutdowns from the higher-level controller have no effect with this function. The **Stop with spacebar** function is not guaranteed in all operating modes. Incorrect operation by untrained personnel and non-observance of the appropriate safety instructions can result in death or serious injury.   - Make sure that this function is only used for commissioning, diagnostic and service purposes. - Make sure that this function is only used by trained and authorized skilled personnel. - Make sure that a hardware device is always available for the EMERGENCY OFF circuit. |  |

> **Note**
>
> **Drive reacts immediately**
>
> Although all enables are removed before returning the master control, the setpoints and commands still come from the original parameterized sources after the control priority is returned.

#### Requirements

- There is an online connection to the drive unit.
- If the project protection is activated: The function rights "Edit hardware configuration" and "Edit software configuration" are activated for your user role.

#### Activating the master control

When an online connection has been established, the bar in the header area is shown in color. The control elements are grayed-out apart from the "Activate" button. The remaining control elements become active only after you have activated the master control and set the enables.

> **Note**
>
> **Project lock not available when master control is active**
>
> As long as the master control of a drive is active, you cannot use the project lock if project protection is activated.
>
> Additionally, the automatic project lock due to inactivity will not take effect while the control panel is active.

When you activate the control panel, you assume master control of the drive. The master control can only be activated for one drive.

| Symbol | Meaning |
| --- | --- |
| 1. Click the "Activate" button under "Master control".    The "Activate master control" message window is opened. 2. Read the warning carefully and check the value for the monitoring time.     The monitoring time specifies the time during which the connection from the PG/PC to the drive is cyclically monitored. The minimum value is 1000 ms. 3. The "Stop with spacebar" option is active by default. When the option is activated the drive is always braked using the shutdown function OFF3 if you press the spacebar or if the focus switches. The focus switches when a dialog is opened (e.g. download dialog) or when switching from TIA Portal to another application.      | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Braking not guaranteed if the "Stop with spacebar" option is deactivated** Stopping by using the buttons on the control panel cannot be guaranteed in extreme operating modes. If the additional braking function "Stop with spacebar" is deactivated, it may no longer be possible to brake the motor via the TIA Portal. This can lead to accidents resulting in death or serious injury. - Only deactivate the "Stop with spacebar" option in absolute exceptional cases and if it has been ensured that you are able to stop the drive safely using suitable hardware solutions. |  |     - Optional: If you do not want to use the "Stop with spacebar" option, deactivate this option in the message window.      This setting requires a safety confirmation. The message window cannot be closed without confirmation.    - Also activate the "Continue without quick stop function via spacebar and focus switch" option. 4. To close the message window and confirm your inputs, click on "OK". The message window closes. The master control is then active. |  |

#### Setting the enable

To set the required enable for the control panel, proceed as follows.

1. Click the "Set" button under "Drive enables".

   Further areas of the control panel are activated.
2. Click the "Acknowledge faults" button to acknowledge the currently pending faults.
3. If you no longer require the enables, click the "Reset" button under "Drive enables".

#### Deactivating the master control

When you deactivate the control panel, you return the master control.

1. Click the "Off" button to stop the drive.

   This is a basic requirement for deactivating the control panel.
2. Click the "Deactivate" button under "Master control".

   The grayed-out user interface of the "Deactivate" button indicates that the master control is deactivated.

#### Result

You can now traverse the drive with the control panel. Enables and faults are displayed at "Drive status". In addition to "Active fault", the currently pending fault is displayed.

### Traversing the drive with speed specification

After you have set the drive enables, switch on the motor in the "Control Panel" screen form. For S210, the mode is permanently set to "Speed setpoint specification" and cannot be changed.

#### Specifying the setpoint and stopping the drive

To specify the setpoint, proceed as follows:

1. Enter a speed setpoint in the "Speed" field with which the motor is to turn.

   Once you have specified the speed setpoint, the drive is switched on as soon as you click one of the buttons "Start backward", "Start forward", "Jog forward" or "Jog backward" for the first time.

   The motor does not accelerate until you click the "Backward" or "Forward" buttons.

   - To rotate the motor backwards, click the "Backward" button.
   - To rotate the motor forward, click the "Forward" button.
   - Click the "Jog forward" button to inch the motor forward.
   - Click the "Jog backward" button to inch the motor backward.
2. Click "Stop" to stop the drive.
3. Click the "Off" button to switch off the drive.

**Note**

**Rotation through clicking**

The motor continues to rotate while you keep the mouse clicked on the button. Traversing stops when you release the mouse button.

#### Viewing actual values of the drive

The current values of various parameters are displayed at "Actual values".

### Performing One Button Tuning

#### Overview

An important part of the basic commissioning is performed using "One Button Tuning" (OBT). With "One Button Tuning", the mechanical drive train is measured with the aid of short test signals. In this way, the controller parameters can be optimally adapted to the existing mechanical system. The optimum controller settings can be determined with a few entries using this tuning.

#### Requirements

- There is an online connection to the drive unit.
- If the project protection is activated: The function rights "Edit hardware configuration" and "Edit software configuration" are activated for your user role.

#### Assuming master control

When an online connection has been established, the bar in the screen form header is highlighted in color. The control elements are grayed-out apart from the "Activate" button. The remaining control elements become active after you have activated the master control and set the enables.

> **Note**
>
> **Project lock not available when master control is active**
>
> As long as the master control of a drive is active, you cannot use the project lock if project protection is activated.
>
> The automatic project lock is also suspended on inactivity.

Proceed as follows to activate the master control:

| Symbol | Meaning |
| --- | --- |
| 1. If the master control is still not active, click on "Activate" under "Master control".    The "Activate master control" message window is opened. 2. Read the warning carefully and check the value for the monitoring time. Adjust the value as required.     The monitoring time specifies the time during which the connection from the PG/PC to the drive is cyclically monitored. The minimum value is 1000 ms. 3. The "Stop with spacebar" option is active by default. When the option is activated the drive is always braked using the shutdown function OFF3 if you press the spacebar or if the focus switches. The focus switches when a dialog is opened (e.g. download dialog) or when switching from TIA Portal to another application.      | Symbol | Meaning |    | --- | --- |    |  | **Warning** |    | **Braking not guaranteed if the "Stop with spacebar" option is deactivated** Stopping by using the buttons on the control panel cannot be guaranteed in extreme operating modes. If the additional braking function "Stop with spacebar" is deactivated, it may no longer be possible to brake the motor via the TIA Portal. This can lead to accidents resulting in death or serious injury. - Only deactivate the "Stop with spacebar" option in absolute exceptional cases and if it has been ensured that you are able to stop the drive safely using suitable hardware solutions. |  |     - Optional: If you do not want to use the "Stop with spacebar" option, deactivate this option in the message window.      This setting requires a safety confirmation. The message window cannot be closed without confirmation.    - Also activate the "Continue without quick stop function via spacebar and focus switch" option. 4. To close the message window and confirm your inputs, click on "OK". The message window closes. The master control is then active. |  |

#### Making settings for tuning

1. Select the desired dynamic response setting for the One Button Tuning corresponding to the mechanical system of your machine.

   One Button Tuning optimizes the drive based on the selected dynamic response setting.

   - Conservative

     Slow control – low mechanical load.
   - Standard

     Best compromise between fast speed control and low mechanical load.
   - Dynamic

     Fast speed control – high mechanical load.
2. Enter the angle in the "Distance limit" field through which the motor and the connected machine are permitted to turn for the required measurements (e.g. 360°) without the mechanical system being damaged.

   The angle should be at least 60° in order to be able to determine useful controller parameters. Generally, longer traversing distances result in better optimization results.
3. Should you wish to perform advanced settings, click on the "Advanced settings" button.

   The "Configuration" dialog opens. The table in the dialog indicates the default settings which you can change for a number of parameters.
4. Correct the default settings in the dialog for each desired parameter. Close the dialog window with "Close".

#### Starting One Button Tuning

When all necessary default settings have been performed, you can initiate One Button Tuning:

1. To measure the drive for tuning, click on the "Start" button in the "Measurement" area.

   The tuning function determines all actual values of the drive necessary for tuning.
2. Optional: If you want to cancel tuning, click the "0" button in the "Switch off" area.
3. If tuning was successful, save the project.

#### Deactivating the master control

Following conclusion of Auto Servo Tuning, the master control can be returned as follows:

1. Click the "Deactivate" button under "Master control".

   The "Deactivate master control" message window opens.
2. If you really want to deactivate the master control, click on "Yes".

   The grayed-out user interface of the "Deactivate" button indicates that the master control is deactivated.

#### Result

The result of the optimization is displayed in the "Status" area. If the optimization was successful, the corresponding LED lights up in green. The "Tuning result" list compares the settings changed by the tuning with the earlier settings prior to tuning.

If tuning was not successful, repeat tuning with modified specifications, if applicable.
