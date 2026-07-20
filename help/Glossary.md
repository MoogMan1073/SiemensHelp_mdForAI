---
title: "Glossary"
package: PEGlossaryenUS
topics: 1
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Glossary

### Access level

The access level is part of a multi-stage concept to protect the functions and data of SIMATIC CPUs (S7-1200/1500). The access levels are "No protection" (all functions are permitted), "Write protection" (data can be read but not changed) and "Write/Read protection" (no access to data permitted).

 

### Access protection

Access protection for projects and libraries is set up by assigning a project password.

 

### Action group (CEM)

All intersections of a column with the same action and number form an action group (e.g. the action group "2N" or "3R"). An action group is active if at least as many causes as indicated by the number are active. When an action group is active, its action is applied to the effect.

 

### Active Infeed

Overall functionality of an infeed with Active Line Module, including the required additional components (filters, switching devices, computing power portion of a Control Unit, voltage detection, etc.).

 

### Active Line Module (ALM)

Controlled, self-commutated infeed/regenerative feedback unit which provides a constant DC link voltage for the Motor Modules. The Active Line Module operates in conjunction with the line reactor to provide a step-up converter function. The control and monitoring functions for the Active Line Module are saved in the drive object under Active Infeed Control.

 

### Actual parameter

A value that replaces the formal parameters when a function block (FB) or function (FC) is called. Example: The formal parameter "Start" is replaced by the actual parameter "I3.6".

 

### Address

An address is the identification of an operand or of an operand area in the user program. Examples: Input I12.1, memory word MW25, data block DB3.

 

### Addressing

Addressing is the assignment of an address to an operand or an operand area. Examples: Input I12.1; memory word MW25.

 

### Addressing, absolute

In absolute addressing, the address of the operand to be processed is specified. Example: Address Q 4.0 designates bit 0 in byte 4 of the process image output.

 

### Addressing, symbolic

Symbolic addressing uses names instead of the absolute address. Example: The input I1.0 is assigned the symbolic name "Start signal".

 

### Alarm

An alarm is event-driven information which allows you to detect errors in process control in the automation system, to localize them, and to eliminate them. We distinguish between program alarms, system diagnostic alarms and user diagnostic alarms.

 

### Alarm (Startdrive)

An alarm is the response to a potential or expected fault condition detected by the drive that does not cause the drive to switch off and does not have to be acknowledged. The alarm mechanism is specified via PROFIdrive. The drive sends a pending alarm to the control system via a bit in the status word.

 

### Alarm configuration

You can use the alarm configuration to create, edit and compile event-driven alarms along with their alarm texts and alarm attributes and display them on display devices.

 

### ARRAY

An ARRAY is a complex data type which consists of data elements of the same type.

 

### Assignment list

The assignment list shows if an address has been allocated by access from an S7 program or if the address has been assigned to a SIMATIC S7 module. The assignment list gives you an overview of which bit in a byte is used for the memory areas input (I), output (Q), and bit memory (M).

 

### Automation system

An automation system is a programmable logic controller (PLC) consisting of a central controller, a CPU, and various input/output modules.

 

### Axis

In the industry, axis is taken to mean a purely mechanical component.   
In SINAMICS, "axis" means the complete system comprising motor, encoder, power unit, drive control (closed-loop current/speed control) as well as any motion control functionality (e.g. positioning, synchronous operation, cam disk).

 

### Backplane bus

The backplane bus of an automation system supplies the inserted modules with the internal operating voltage and allows data exchange between modules.

 

### Base class

Higher-level class from which further similar classes are derived. The base class passes on its tags and methods to the derived classes.

 

### Basic Infeed

Overall functionality of an infeed with Basic Line Module including the required additional components (filters, switching devices, etc.).

 

### Basic Line Module (BLM)

Unregulated line infeed unit (diode bridge or thyristor bridge, without feedback) for rectifying the line voltage of the DC link.

 

### Basic positioner (EPOS)

The basic positioner can be used for "simple" positioning tasks. It can be activated in SINAMICS as function module.

 

### Baud rate

The baud rate (symbol rate) measures the number of states of a transmitted signal per second in the unit baud.

 

### BCD

BCD (binary-coded decimal) refers to a numerical code in computing where each digit of a decimal number is binary-coded individually.

 

### BICO interconnection

See "BICO technology".

 

### BICO technology

Abbreviation for "Binector-Connector-Technology". BICO technology is a method used in drives for freely interconnecting process data via standard drive parameterization. All freely interconnectable word, double word and floating point signals are defined as connectors and all freely connectable binary signals are defined as binectors. A unique monitoring parameter is assigned to each connector and binector.

 

### Bidirectional digital input/output (DI/DO)

Terminal that can be used either as digital input or as digital output depending on the parameterization.

 

### Binector

Freely interconnectable binary signals, e.g. digital input, control bit from PROFIBUS, etc. The signal source is called binector output and the signal sink is called binector input.

 

### Binector input

Signal sink to which a binector output (a freely interconnectable binary signal) can be interconnected using BICO technology.

 

### Binector output

Signal source (freely interconnectable binary signal) that can be interconnected via a binector input using BICO technology.

 

### Bit memory

A bit memory is a memory area in the CPU system memory that is used to save intermediate results. Read/write access is permitted to the bit memory. A bit memory can also be defined as retentive and retains its content after power off and at the STOP to RUN transition after power on.

 

### Block

A block structures the user program into independent sections. There are: organization blocks (OB), function blocks (FB), functions (FC) and data blocks (DB).

 

### Block call

A block call refers to the action in which one block calls another block.

 

### Block comment

The block comment contains optional additional information about a block that is not loaded into the work memory of the CPU.

 

### Block interface

The block interface contains the declaration of the block parameters and local data of a code block.

 

### Block parameters

A block parameter is a placeholder in the block interface which is supplied with current values when the respective block is called.

 

### Block protection

The block protection (know-how protection) gives you the option to assign a password to blocks to protect them from unauthorized access.

 

### Block stack

The block stack is a memory area in the CPU system memory. It saves the start and return addresses of the respective valid data block in the case of block calls.

 

### Blocksize

Volume-optimized, cubic construction of a drive unit. Mostly used for operating a motor.

 

### Booksize

Book-shaped construction of the components of a drive unit, suitable for mounting side-by-side. Usually intended for the operation of multiple motors.

 

### Box

A box is a program element with complex functions. The empty box is an exception. You can use the empty box as a placeholder in which you can select the required operation.

 

### Braking Module

Electronic switch that connects a braking resistor with a specific pulse/pause ratio to the DC-link voltage to convert regenerative (braking) energy to heat energy and finally to restrict the DC-link voltage to permissible values. Limits the DC-link voltage to permissible values. For SINAMICS, no braking resistor is incorporated in the Braking Module. Therefore, an external braking resistor is required.

 

### Broadcast

A broadcast in a computer network is a message in which data packets are transmitted from one point to all devices in a message network.

 

### Broadcast address

The broadcast address is an IP address in the network to which a request is sent that is to be read by all devices.

 

### Bus

A bus is a system for data transmission between multiple devices by means of a shared transmission path.

 

### Bus system

A bus system is a system for data transmission in which all stations of an automation system are physically connected by means of a bus.

 

### Call hierarchy

The call hierarchy is the order and nesting of block calls within an organization block.

 

### Call structure

The call structure describes the call hierarchy of the blocks within an S7 program. It provides an overview of the blocks used, the jumps to the points of use of the blocks, the local data requirement of the blocks and the status of the blocks.

 

### CAPI

CAPI (Common Application Programming Interface) is an ISDN-compliant, standardized programming interface. The CAPI interface enables you to provide software for ISDN use without having to know the manufacturer-specific ISDN card used.

 

### Cause (CEM)

In the cause-effect matrix, a cause represents a process event.

 

### Central processing unit

The user program is stored and executed in the central processing unit (CPU) of an automation system. It contains the operating system, processing unit, and communication interfaces.

 

### Certificate of License (CoL)

The Certificate of License is the licensee's proof that the use of the software has been licensed by Siemens. A Certificate of License is required for each use and must be kept in a safe place.   
See "License Key"

 

### Character delay time

The character delay time monitors the arrival of characters in the data transmission phase.

 

### CIR

CiR (Configuration in RUN) is a configuration change during operation. For systems that are not permitted to be switched off, certain configuration changes can be made while the system is operating, provided that corresponding reserves have been configured.

 

### Class

Classes are classified as program organization units. They form a capsule for tags and methods. Only tags and methods which are assigned the access identifier PUBLIC are visible outside the class. A different class can be derived from a class (base class). This derived class inherits all tags and methods of the base class.

 

### Class instance

Object which is generated when a class is used in the program. The term "instancing" of a class is used in this case. In STEP 7, the class instance is represented by a data block.

 

### Class tag

Tag which can be accessed within a class from all methods. Class tags are declared within the class. In STEP 7, global data blocks perform the role as class tags.

 

### Client

The client is a program or computer which receives data and services from a server.

 

### Clock memory

Clock memory is bit memory that changes its signal state periodically at a fixed frequency.

 

### CM

Communications Module ‑ Module for communications tasks that is used in an automation system as an interface expansion of the CPU. Same interface types of a CPU and a CM are functionally identical.

 

### Code block

A code block is a block which contains part of the user program.

 

### Coil

A coil is used to control binary operands and to set and reset them depending on the signal state of the result of logic operation.

 

### Command data set (CDS)

Parameter data set, in which binector inputs (e.g. for control commands) and connector inputs (e.g. for setpoints) are combined. The individual data sets are represented as indexed parameters. The changeover is performed via input signals. By parameterizing several command data sets and switching between them, the drive can be operated with different pre-configured signal sources.

 

### Communication Board (CB)

Module for external communication (e.g. PROFIBUS, PROFINET). The module is plugged into the option slot of a Control Unit. In SINAMICS S120 drives, a CBE20 (for connection with PROFINET) is used. This supports PROFINET IO with Isochronous Realtime Ethernet (IRT) and PROFINET IO with RT.

 

### Communication connection

A communication connection is established between devices that want to exchange data with each other. A communication connection requires attachment to a common hardware medium (for example, a bus system). Based on this, a logical communication connection (software) is established.

 

### Configuration

Configuration is the selection and combination of individual components of an automation system as well as the installation of required software and customization of the automation system for the specific use.

 

### Connection table

The connection table is a table for defining the communication connections between programmable modules in a network.

 

### Connector

Freely interconnectable analog signal using BICO technology. An analog signal is, for example, the value of an analog input or process data with PROFIBUS.

 

### Connector input

Signal sink to which a connector output, i.e. a freely interconnectable analog signal, can be interconnected using BICO technology.

 

### Connector output

Signal source, e.g. a freely interconnectable analog signal, that can be interconnected via a connector input using BICO technology.

 

### Consistent data

Consistent data is data that belongs together with regard to content and must not be split up during data transmission.

 

### Constant

A constant is a placeholder for constant values in code blocks. Constants are used to improve the readability of a program. Example: instead of specifying a value directly (for example, 10), the placeholder "Max_loop_iterations", for example, is specified in a function block. When this is called, the value of this constant (for example, 10) is specified.

 

### Contact

You can use a contact to create or interrupt a current-carrying connection between two elements. The current is relayed from left to right. You can use contacts to query the signal state or the value of an operand and control it depending on the result of the current flow.

 

### Control Unit (CUxxx)

Central control module in which the closed-loop and open-loop control functions are implemented for one or more SINAMICS Line Modules and/or Motor Modules.

 

### Control Unit Adapter (CUA)

SINAMICS component for DRIVE-CLiQ communication between a Power Module in blocksize format (PM240-2) and a Control Unit for several drives (e.g. CU320). The Control Unit Adapter is connected through the Power Module Interface to the Power Module and through DRIVE-CLiQ to the Control Unit. The two CUAs that can be used are CUA31 and CUA32. They differ with respect to their encoder support.

 

### Control word (STW)

Bit-coded process data word transmitted by PROFIdrive at cyclic intervals to control drive states.

 

### Copy template

A copy template is a library element. Copy templates can be used to create copies of library elements that are independent of each other.

 

### CP

Communications Processor ‑ Module for advanced communications tasks that provides the CPU with additional interface types or communications options.

 

### CPU

The CPU (Central Processing Unit) is the hardware device of the automation system containing the control and arithmetic logic units, memory, operating system and interface for a programming device.

 

### Cross-project data exchange

Cross-project data exchange is made possible by the Inter Project Engineering (IPE) function. Controller data of a CPU is transferred consistently from a source project to a CPU in the target project by an IPE file or a project file.

 

### Cross-reference list

The cross-reference list provides an overview of the use of operands in I, Q, M, P and DB memory areas in the program and an overview of DB, FC, and FB access.

 

### CU320-2/CU310-2

The two most important SINAMICS Control Units. The CU320-2 has 4 DRIVE-CLiQ sockets and 16 digital inputs/outputs. In contrast, the CU310-2 only has 4 DRIVE-CLiQ sockets and 4 digital inputs/outputs. A USP of a CU320-2 is that a Double Motor Module can be connected to it.

 

### Cycle time

The cycle time is the time that the CPU requires to execute the user program once.

 

### Cyclic interrupt

A cyclic interrupt starts a program at constant intervals.

 

### Data block

A data block is used to store user data. There are global data blocks that can be accessed by all code blocks and instance data blocks that are assigned to a specific FB call.

 

### Data flow control

Data flow control controls the data flow and specifies for short-term interruptions of the data flow by means of software or hardware protocols how the data is to be transmitted in such a case.

 

### Data point

Data points are used to identify signals in automation and control technology. A data point is identified by its name. Typical attributes are address, data type and value. Depending on the use of the data point, additional attributes such as time stamp, status, limit values, transmission parameters etc. can be assigned. The data point address of a CP is the reference to an input/output address of the CPU (process value), to a memory (process value or calculation value) or to a variable of the CPU.

 

### Data type

The data type specifies how the value of a tag or constant is to be used in the user program.

 

### Data type, complex

Complex data types result from linking elementary data types. A distinction is made between structures and arrays. Structures consist of different elementary data types; arrays consist of multiple similar elements of a data type.

 

### Data type, elementary

Elementary data types are pre-defined data types according to IEC 1131-3. Example: The "BOOL" data type defines a binary tag ("bit"); the "INT" data type defines a 16-bit fixed-point tag.

 

### Dependency structure

The dependency structure is a display which shows the dependencies for each block in the program to other blocks.

 

### Derived class

Variants of a different class generated by inheritance. A derived class contains the methods and tags of the original base class. New tags and methods in the derived class can also be declared.

 

### Device

A device in TIA Portal refers to different objects, such as controllers (CPU), HMI devices and PC systems. Configuration, parameter assignment and networking of devices takes place in the hardware and network editors.

 

### Device address

The device address is the address by which a device (for example, a PG) or a programmable module (for example, a CPU) is addressed in a network.

 

### Device proxy data

The "Device proxy data" object supports consistent data exchange of CPU controller data across projects between a source project and a target project without redundant configuration.

 

### DHCP

DHCP (Dynamic Host Configuration Protocol) is a communication protocol in computer technology. It is used to assign a network configuration to clients by a server. This means that devices (clients) connected to a network are IP addresses automatically assigned by a DHCP server.

 

### Diagnostic alarm

A diagnostic alarm is, for example, a prepared diagnostic event that is sent by the CPU to a display device.

 

### Diagnostic data

Diagnostic data is the information included in the error message, such as diagnostic events or time stamps.

 

### Diagnostic entry

A diagnostic entry is an entry in the diagnostics buffer by means of a diagnostic event.

 

### Diagnostic interrupt

The diagnostics interrupt is an interrupt by which modules with diagnostics capability signal system errors to the CPU.

 

### Diagnostics

Diagnostics is the detection, signaling and localization of errors and determination of suitable remedial measures. In diagnostics, a distinction is made between system diagnostics, process error diagnostics and user-defined diagnostics.

 

### Diagnostics buffer

The diagnostics buffer represents a backup memory in the CPU used to store a specific number of diagnostics events in the order of their occurrence.

 

### Diagnostics event

A diagnostics event leads to an entry in the diagnostics buffer of a CPU or a CP/FM with diagnostics buffer. Diagnostics events include module faults, process wiring errors, operating mode transition errors and CPU system errors.

 

### Dialing method

The dialing method is the way in which a telephone connection is dialed. There is tone dialing and pulse dialing. On a telephone with pulse dialing, you hear clicking noises when dialing the phone; if the telephone connection uses tone dialing, you hear a series of high-pitched tones.

 

### Direct access

Direct access is access by the CPU to modules over the I/O bus directly without using the process image.

 

### Direct communication

Context: TeleControl. With direct communication, the S7 stations communicate directly with each other without the frames needing to be forwarded by a master station or station.

 

### Direct connection

A direct connection refers to the direct connection established by means of a TS Adapter between the programming device or PC on which TeleService is installed and an automation system. The direct connection is used to assign the parameters of the TS Adapter.

 

### Display device

A display device is a device on which the results of the process are displayed.

 

### Distributed I/O

Distributed I/O refers to analog and digital modules installed away from the central rack.

 

### DNS

The DNS (Domain Name System) is a database distributed across thousands of servers worldwide which manages the name space on the Internet.

 

### DNS server

A DNS server (Domain Name System server) is a server which manages the alphanumeric designations of IP addresses on the Internet.

 

### Document

File that can be edited both in the file system and in the TIA Portal and contains program code in textual format.

 

### Double Motor Module (DMM)

Two motors can be connected to and operated with a Double Motor Module. It is a power unit (inverter) that exchanges setpoint/actual data via DRIVE-CLiQ with the Control Unit and specifies frequencies and voltages for the operation of two motors. In SINAMICS, Double Motor Modules only function together with the CU320-2.

 

### DP master

A DP master is the central controller in a DP master system. The data traffic between the DP master and the DP slaves assigned to it is handled automatically by the master in a defined and recurring order. A DP master behaves in accordance with the Profibus DP standard (EN 50170).

 

### DP slave

A DP slave is a module which is part of a DP master system and communicates with the DP master via PROFIBUS. DP slaves themselves do not have bus access authorization, which means they may only acknowledge received messages or transmit messages to a DP master upon its request.

 

### DP/PA coupler

The DP/PA coupler is a connection module between PROFIBUS DP and PROFIBUS PA.

 

### Drive

The drive encompasses the motor (electrical or hydraulic), the final controlling element (converter, valve), closed-loop control, measuring system and the supply components (infeed, pressure accumulator). For electric drives, a distinction is made between a converter system and an inverter system. In a converter system, the supply, final controlling element, and control unit are grouped together in one device from the user's point of view. In an inverter system (e.g. SINAMICS S), the supply is implemented via Line Modules to make a DC link.

 

### Drive component

Hardware component connected to a Control Unit via DRIVE-CLiQ or otherwise. Drive components include, for example, Motor Modules, Line Modules, motors, Sensor Modules and Terminal Modules. The overall arrangement of a Control Unit including the connected drive components is known as the drive.

 

### Drive Control Block (DCB)

Drive Control Blocks (DCB) are pre-configured function blocks for SINAMICS that are made available in a function block library (DCB library). These Drive Control Blocks can be graphically interconnected and parameterized with the DCC Editor configuration tool.

 

### Drive Control Chart (DCC)

Drive Control Chart (DCC) for SINAMICS allows the additional implementation of continuous drive-level control and calculation functions. A set of function blocks (Drive Control Blocks, DCBs) is available for this in a function block library. These function blocks can be graphically interconnected using a configuration tool (DCC Editor).

 

### Drive data set (DDS)

Parameter data set in which the characteristic parameters of a drive are combined (number of the assigned motor data set, numbers of the assigned encoder data sets, different control parameters). The individual data sets are represented as indexed parameters. The changeover is performed via input signals. With corresponding parameterization of multiple drive data sets, multiple drive variants can be pre-configured between which switchover via control commands can be performed.

 

### Drive object (DO)

A drive object is a self-contained software function with its own parameters and potentially its own faults and alarms. Drive objects can be provided as standard or created individually or multiple times.

 

### Drive parameters

Parameters of a drive that include, for example, the parameters of the corresponding controllers, as well as the motor and encoder data.

 

### Drive software

Software for drive functionalities of a drive system. The drive software in the TIA Portal can be found in the licensed "Startdrive" application.

 

### DRIVE-CLiQ (DQ)

Abbreviation for Drive Component Link with IQ. Communication system for connecting various components of a SINAMICS drive system, e.g. Control Unit, Line Module, Motor Modules, motors, and speed/position encoders. In terms of hardware, DRIVE-CLiQ is based on the Industrial Ethernet standard with twisted-pair lines. The DRIVE-CLiQ line provides the send and receive signals, as well as the +24 V power supply.

 

### DRIVE-CLiQ Hub Module

Generic term for all versions of star couplers for duplication of DRIVE-CLiQ sockets in SINAMICS.

 

### DRIVE-CLiQ motor

Motors with DRIVE-CLiQ comprise a motor, encoder and an integrated encoder evaluation system. A power cable and a DRIVE-CLiQ cable must be connected to the Motor Module to operate these motors.

 

### Duplex

Duplex refers to a data exchange method in communication technology for direction independence of a communication channel. A distinction is made between full-duplex and half-duplex. With full-duplex, data can be transmitted in both directions; with half-duplex, data can be transmitted alternately but not simultaneously in both directions.

 

### Dynamic Servo Control (DSC)

Dynamic Servo Control (DSC) enables the actual position value to be evaluated in a fast speed controller cycle directly in the drive. The position setpoint value is entered in the position controller clock cycle from the higher-level controller via the isochronous PROFIBUS with PROFIdrive telegrams.

 

### Edge

An edge refers to a change in the signal state of digital signals (for example, of an input). A positive edge is present when the signal changes from state "0" to state "1". In the case of a negative edge, the signal changes from state "1" to state "0".

 

### Edge evaluation

An edge evaluation is needed to detect and evaluate the change of a signal state.

 

### Effect (CEM)

An effect represents the reaction of the cause-effect matrix to the process event.

 

### EMC

EMC (Electromagnetic Compatibility) is the status in which electrical and/or electronic devices do not interfere with each other.

 

### EN

EN (Enable) is an input which exists in each STEP 7 block and which can be set when the block is called. With EN = TRUE, the block is called; with EN = FALSE, the block is not called.

 

### Encoder

An encoder is a measuring system that measures actual values for speed and/or angles/positions and makes them available for electronic processing. Depending on their mechanical design, encoders can be incorporated in the motor (motor encoder) or mounted on the external mechanics (external encoder). Depending on the type of movement, a distinction is made between rotary encoders and translational encoders. In terms of measured value provision, a distinction is made between absolute encoders and incremental encoders.

 

### Encoder data set (EDS)

Parameter data set that can be selected by a parameter within the active drive data set and that contains the speed/position encoder parameters with which the drive control works. In this way, a common switchover of all encoder parameters is possible. The individual data sets are represented as indexed parameter.

 

### Encoderless vector control

A variant of vector control (field-oriented control) for induction motors without speed feedback (encoders) that allows a high degree of accuracy and dynamic performance to be achieved in a speed control range of approx. 1:10.

 

### ENO

ENO (Enable output) is an output which exists in each STEP 7 block. You can use the ENO to check directly after the call of a block whether all operations in the block were completed correctly or whether errors occurred.

 

### Error OB

The error OB is an organization block with which the user can program the reaction to an error.

 

### Error reaction

An error reaction is the reaction of the operating system to a runtime error. Possible error reactions include: Changing the automation system to STOP mode, calling an organization block in which the user can program a reaction, or displaying the error.

 

### Ethernet

Ethernet is a technology for data exchange in the form of data packets between connected devices in a local network.

 

### Exclusive Engineering

With Exclusive Engineering you are working with a copy of a server project in an exclusive local session. Project management is located either on a local or external server, the TIA project server. Working in the local session is exclusive, which means you are the only user working on this server project. You transfer the changes from the exclusive local session to the server project. During each check-in, a new, commentable revision of the server project is created to which you can revert, if necessary. The project history is therefore available to you at any time.

 

### Fault

Unwanted status that is identified and displayed by the drive controller or can be sent to a higher-level controller. A fault normally causes the drive to shut down. In certain cases, an alternative reaction can be parameterized. Faults must always be acknowledged and the correct procedure for clearing them is specified by PROFIdrive.

 

### FBD

The function block diagram (FBD) is a language defined in EN 61131-3 (IEC 61131-3) for programming of programmable logic controllers (PLC). The function block diagram uses the logic boxes familiar from Boolean algebra to represent the logic and is especially suitable for logic controllers.

 

### Field device

A field device is a sensor or actuator which is connected to an automation system or an I/O device.

 

### Firmware

Firmware is software embedded in electronic devices. It is usually saved in a flash memory, such as EPROM, EEPROM or ROM, and can only be replaced by the user with special tools or functions. The term is derived from the fact that firmware is permanently connected to the hardware, which means that one cannot be used without the other.

 

### Firmware update

A firmware update is an update of the module firmware. The update resolves existing errors and can add new functions.

 

### Flying restart

After the converter has been switched on, the "flying restart" function allows it to be automatically connected to a motor that is possibly coasting down. An induction motor first has to be magnetized when the converter is switched to it while it is still running. For drives not equipped with an encoder, a search for the current speed is carried out. The current speed setpoint in the ramp-function generator is then set to the current actual speed value. The ramp-up to the final speed setpoint takes place from this value.   
After the converter has been switched on, the "flying restart" function can help to shorten the ramp-up procedure if the load is still coasting down. It can usually only be used with single drives because, in the case of group drives (multiple motors at the converter in parallel), the motors can take on different speeds with the converter being switched off.

 

### Force

Forcing is used to permanently assign fixed values to individual peripheral outputs of a CPU. The tags and values that are to be forced must be entered in the force table.

 

### Force table

The force table allows you to monitor and force tags in the user program. Forcing is used to permanently assign fixed values to individual peripheral outputs of a CPU.

 

### Formal parameter

A formal parameter is a parameter of a code block. It is used as a placeholder for an actual parameter that is transferred to the code block when it is called.

 

### Free function blocks (FBLOCKS)

Logical operations (e.g. AND, OR) can be realized via function blocks using the FBLOCKS technology extension. In addition, for example, calculation functions (e.g. adder), time functions (e.g. on delay), memory functions, switch functions (e.g. binary switch) and control functions (e.g. limiter) are available.

 

### FTP

FTP (File Transfer Protocol) is a network protocol for transferring files between two computers over the Internet. One computer must be an FTP server and the other computer an FTP client.

 

### Full-duplex

Full-duplex refers to a data exchange method in communication technology in which data can be transmitted in both directions simultaneously.

 

### Function

A function (FC) is a code block without memory according to IEC 1131-3. A function gives you the option to transfer parameters in the user program. Functions are therefore particularly suitable for frequently recurring complex constructs, such as calculations.

 

### Function block

According to IEC 1131-3, a function block is a code block with static data. A function block gives you the option to transfer parameters in the user program and has a memory (instance data block).

 

### Function Block Diagram

The function block diagram (FBD) is a language defined in EN 61131-3 (IEC 61131-3) for programming of programmable logic controllers (PLC). The function block diagram uses the logic boxes familiar from Boolean algebra to represent the logic and is especially suitable for logic controllers.

 

### Function module

A function module is a functional expansion of a SINAMICS drive object that can be activated during commissioning.   
A function module generally has separate parameters and, in some cases, separate faults and alarms too. These parameters and messages are only displayed when the function module is active. An active function module also generally requires additional processing time. This must be taken into consideration when designing the Control Unit.

 

### GPRS

GPRS (General Packet Radio Service) is a packet-oriented service for IP-based data transmission in GSM networks. GPRS data packets can also be transmitted via the Internet.

 

### GRAPH

GRAPH is a graphical programming language for the creation of sequential control systems, configured and programmed according to IEC 61131-3, DIN EN 61131. Sequences can be programmed in a fast and straightforward manner using sequencers. The process is broken down into individual steps, each with a clear scope of functions, and organized into sequencers. The actions to be executed are defined within the individual steps. There are transitions between the steps. These contain conditions for advancing to the next step.

 

### GSM

GSM (Global System for Mobile Communication) is a standard for fully digital mobile communication networks that are used mainly for telephony but also for line- and packet-switching data transmission as well as for short messages.

 

### Half-duplex

Half-duplex refers to a data exchange method in communication technology in which data can be transmitted alternately but not simultaneously in both directions.

 

### Hardware

Hardware (HW) is the collective term for mechanical and electronic equipment of a system, for example, a computer system.

 

### Hardware limit switch

The hardware limit switch is a mechanical limit switch that limits, for example, the maximum permissible traversing range of an axis.

 

### HMI

HMI (Human Machine Interface) is a device for visualization and control of automation processes.

 

### HOLD mode

In "HOLD" operating mode, execution of the user program is halted. The "HOLD" operating mode is used only when using the programming device for testing.

 

### HTTP

HTTP (Hypertext Transfer Protocol) is the transfer protocol for web pages on the Internet.

 

### HTTPS

HTTPS (Secure Hypertext Transfer Protocol) is the transfer protocol for encrypted data on the Internet. HTTPS extends the HTTP protocol for secure transmission of confidential data using SSL.

 

### I/O

I/O refers to analog and digital modules installed away from the central rack.

 

### I/O access, direct

Direct I/O access is an instruction for direct access to the I/O without using the process image.

 

### Identification data

Identification data is information that is saved in modules and that supports the user in checking the plant configuration and locating hardware changes or errors. Modules can be clearly identified online using the identification data.

 

### In/out parameter

In/out parameters are used to pass data to the called block as well as to return results to the calling block.

 

### Incremental encoder

The incremental encoder is a position encoder that outputs the change of position incrementally in the form of a digital numerical value.

 

### Induction motor (ASM)

The asynchronous motor is a 3-phase motor whose speed lags somewhat behind the synchronous speed. Induction motors can be connected to the AC line both directly in a star or delta circuit and via a frequency converter. In combination with a frequency converter, the induction motor becomes a variable-speed drive system.

 

### Industrial Ethernet

Industrial Ethernet (IE) is a guideline for installing an Ethernet network in an industrial environment. The main difference to the standard Ethernet is the mechanical current carrying capacity and interference immunity of the individual components.

 

### Infeed

Input component of a converter system for generating a DC-link voltage to supply one or more Motor Modules, including all the required components such as Line Modules, fuses, reactors, line filters and firmware, as well as proportional computing power (if required) in a Control Unit.

 

### Inheritance

Creation of a new class on the basis of an existing class. The relationship between the original class and the derived class is retained. The new class can be an extension of the original class.

 

### Initialization string

The initialization string is a string composed of AT commands (standard commands for modems) used to initialize the modem connected to the TS Adapter.

 

### Input

An input is a memory area in the system memory of the CPU (process image input) or a connection to an input module.

 

### Input parameter

Input parameters are used to pass data to a called block for processing.

 

### Instance

An instance is the call of a function block to which an instance data block is assigned.

 

### Instance data block

An instance data block stores the formal parameters and static data of function blocks. An instance data block can be assigned to a function block call or to a call hierarchy of function blocks.

 

### Instruction

An instruction is the smallest independent unit of a user program. It represents an instruction for the processor, formulated in the respective programming language, which is to be executed during processing of the user program.

 

### Inter Project Engineering

Inter Project Engineering (IPE) supports data exchange across a project. The controller data in a source project can be copied with the "Device proxy data" object and exported to a target project.

 

### Interface module

The interface module connects the distributed I/O system via a fieldbus to the CPU and prepares the data for the I/O modules.

 

### Interlock

An interlock is a condition that can be programmed within a step. The interlock influences the execution of individual actions.

 

### Interrupt

An interrupt is an event that causes the operating system of an S7-CPU to call an assigned organization block (interrupt OB) in which the user can program the desired reaction.

 

### Intersection (CEM)

An intersection specifies how a cause affects an assigned effect.

 

### Inter-station communication

Context: TeleControl. Communication between two stations that is forwarded by a master station. For dial-up networks, a direct connection between the two stations is established in ST7 networks.

 

### IO controller

An IO controller is a central device in a PROFINET system, such as a CPU or a PC. The IO controller sets up connections to the IO devices, exchanges data with them and controls and monitors the PROFINET system.

 

### IO device

An IO device is a device in the distributed I/O of a PROFINET system that is monitored and controlled by an IO controller.

 

### IPE

IPE (Inter Project Engineering) supports data exchange across a project. The controller data in a source project can be copied with the "Device proxy data" object and exported to a target project.

 

### IPE file

The IPE (Inter Project Engineering) file includes CPU controller data from a source project which is exported with the "Device proxy data" object and transferred to the CPU in the target project.

 

### ISDN

ISDN (Integrated Services Digital Network) is an international standard for a digital telecommunication network used for digital data and voice transmission.

 

### ISDN adapter

An ISDN adapter (or ISDN terminal adapter, ISDN-TA) is an ISDN device that is connected to a serial PG/PC interface for the purpose of transmitting data over the digital network.

 

### ISDN modem

An ISDN modem (modulator/demodulator) is an ISDN adapter with integrated analog modem functionality.

 

### Know-how protection

The know-how protection (block protection) gives you the option to assign a password to blocks to protect them from unauthorized access.

 

### LAD

LAD (ladder logic) is one of the graphical programming languages standardized in IEC norm EN 61131-3 which is particularly suitable for logic controllers. The ladder logic corresponds to the representation of a circuit diagram.

 

### Ladder Logic

The ladder logic (LAD) is one of the graphical programming languages standardized in IEC norm EN 61131-3 which is particularly suitable for logic controllers. The ladder logic corresponds to the representation of a circuit diagram.

 

### Library

A library is used for storage of reusable program components. These can be, for example, stations, blocks, PLC tag tables, process pictures or picture elements. You have the choice of a project library and global libraries.

 

### License Key

The license key is an electronic license stamp that indicates that one or more licenses for the software used are owned. It enables unimpaired operation. Actual customer verification of the license for the software used that is subject to license is called a "Certificate of License". This term is generally used instead of "license key".

 

### Line Module

A Line Module is a power unit that generates the DC-link voltage for one or more Motor Modules from a three-phase line voltage. In SINAMICS, there are three types of Line Modules:   
‑ Basic Line Module  
‑ Smart Line Module  
‑ Active Line Module  
The overall function of an infeed, including the required additional components, such as line reactors, proportional computing power in a Control Unit, switching devices, etc., is called:  
‑Basic Infeed  
‑Smart Infeed   
‑Active Infeed

 

### Linear motor

This motor type consists of primary section and secondary section and is installed directly in the drive. Any motor forces and traversing distances can be achieved by connecting primary and secondary sections are mounted side-by-side. Siemens offers linear motors of the 1FN3 series. These motors are permanent-magnet, linear synchronous motors with a modular cooling concept.

 

### Load memory

The load memory is a component of a programmable module. It contains objects created on the programming device (load objects). It is implemented either as an insertable memory card or as a permanently integrated memory.

 

### Local data

Local data is data assigned to a code block which is declared in its interface. It includes formal parameters, static data, and temporary data.

 

### Local project server

The local project server is a server that manages the server projects for working with Multiuser Engineering, Multiuser Commissioning and Exclusive Engineering . The local project server has only limited functionality. To use the full server functionality, a dedicated project server must be installed. Prior to TIA Portal V16, the "Local project server" was referred to as "Local Multiuser server".

 

### Local session

The local session is a copy of the server project that is created while working with Multiuser Engineering or with Exclusive Engineering .

 

### MAC address

A MAC address (Media Across Control address) is the unique device identification for Ethernet devices worldwide. The MAC address is assigned by the manufacturer and has a 3-byte vendor ID and 3-byte device ID as a consecutive number.

 

### Maintenance request

The maintenance request is a maintenance information with the following meaning: The hardware involved must be replaced within a brief time period.

 

### Maintenance required

Maintenance required is maintenance information with the following meaning: The hardware involved must be replaced within a foreseeable time period.

 

### Manufacturer-specific telegram

In Siemens drives, manufacturer-specific PROFIBUS telegrams are the telegrams from telegram number 101. The telegram numbers are defined via PROFIdrive.

 

### Master project

The master project is a basic project for joint commissioning. It is a project structured according to the specified rules which already contains the fully configured hardware configuration with all required tags and blocks. This project is loaded into the jointly used CPU and then distributed as "master project" by means of project copies to the participating engineering systems. Each engineering system only processes the parts it was assigned within the specific project copy. The project copies are then integrated into the master project once again.

 

### Maximum cycle time

The maximum cycle time monitors the permitted execution time for the user program. If the execution time of the user program exceeds the specified maximum cycle time, the operating system generates an error alarm and the CPU changes to STOP.

 

### Method

Code sequence which is assigned to a class. It defines the behavior of the instances which are generated from the class.

 

### Method tag

Tag which is used to provide a method with a value or tag which is used to return a value from a method.

 

### Minimum cycle time

The minimum cycle time is the time that is required for the runtime of the cyclic program, including the runtime of all nested program parts in higher-priority organization blocks.

 

### Modem

A modem (modulator/demodulator) is a communication device that enables a computer to send and receive data over telephone lines. It converts the digital pulses of the computer into analog signals, and vice versa.

 

### Modem connection

The modem connection is a connection that is established over a modem line. This connection exists between the programming device or PC on which TeleService is installed and the automation system in which the TS Adapter is inserted in the MPI/DP or Ethernet interface. The modem connection is the usual configuration for working with TeleService.

 

### Modify tags

Using the "modify tags" function, you can modify the tags of a user program and assign permanent values to individual tags at a specified point during execution of the user program.

 

### Module parameter

The module parameter is a parameter with which the behavior of the module can be set.

 

### Monitor tags

Using the "monitor tags" function, you can monitor the tags of a user program and read out the current values of individual tags on the programming device at a specified point during execution of the user program.

 

### Motor

For the electric motors that can be driven by SINAMICS, a basic distinction is made between rotary and linear motors in terms of direction of motion, and between synchronous and induction motors in terms of electromagnetic operating principle. For SINAMICS, the motors are connected to a Motor Module. In the TIA application "Startdrive", the following motor types can be integrated (and parameterized) in a SINAMICS drive:  
‑ DRIVE-CLiQ motor  
‑ Reluctance motor  
‑ Induction motor  
‑ Synchronous motor

 

### Motor data set (MDS)

The parameters belonging to a motor data set are responsible for configuration of a motor. There are multiple motor data sets which can be switched between using control commands. In this way, a common switchover of all parameters defining the motor configuration is possible. A typical application is the operation of multiple motors on one Motor Module.

 

### Motor Module

A Motor Module is a power unit (DC-AC inverter) that supplies the power for the connected motor(s). Power is supplied by means of the DC link of the drive unit. A Motor Module must be connected to a Control Unit via DRIVE-CLiQ. The open-loop and closed-loop control functions for the Motor Module are stored in the Control Unit. There are "Single Motor Modules" and "Double Motor Modules".

 

### Motor temperature sensor

Motor temperature sensors are elements that are mounted in the motor winding and/or in the motor bearings to acquire the relevant temperatures and protect the motor against overtemperature. The most common sensors are:   
- PTC (thermistors), which respond at a specific temperature (thermistor motor protection)   
- KTY84 as (linear) thermistor   
- PT100 for (linear) temperature measurement, primarily with high outputs  
- PT1000 for (linear) temperature measurement, for precise measuring results through higher rated resistances

 

### MRP

MRP (Media Redundancy Protocol) supports the creation of redundant networks. Within these networks, redundant transmission paths in a ring topology ensure that, if one transmission path fails, an alternative communication path is available. The PROFINET devices that are part of this redundant network form an MRP domain.

 

### Multi-instance

A multi-instance is a block call in which the called block stores its data in the instance data block of the calling function block.

 

### Multiuser Commissioning

After you have created and edited multiuser projects with multiple users in Multiuser Engineering , commissioning can be executed just as conveniently and also in the team with Multiuser Commissioning . The changes from the local sessions are first downloaded to the shared CPU with Multiuser Commissioning and then, after successful download, transferred to the server project. Downloaded changes from other users are displayed and can be conveniently applied. The server project is already synchronized on the project server. This means consistent versions of the server project are always downloaded to the CPU. Time-consuming synchronization of different project versions on the CPU therefore becomes unnecessary. This approach significantly reduces the commissioning times for your projects. You can use your plant faster and start productive operation sooner.

 

### Multiuser Engineering

Multiuser Engineering enables simultaneous and parallel working in a team. The advantage of this is that you can work with multiple users simultaneously in projects. Project management is located either on a local or external server. Different users work in local sessions, based on the projects managed by the server. Users work independently from each other in local sessions. The changes from the local sessions are transferred to the server project on check-in. Checked-in changes from other users are displayed and can be conveniently applied. This approach significantly reduces the configuration times for your projects. You can commission your plant faster and start production sooner.

 

### Named value

Value that has a unique name assigned to it.

 

### Named value data type

Data structure that assigns a unique set of names to a set of values.

 

### Namespace

A namespace declares an area within the PLC program in which program elements, such as blocks, can be grouped semantically. All elements within a namespace are identified by a unique name. However, the same name can be used in a different namespace to designate another element. The uniqueness is achieved by prefixing the namespace to the name of the element as an additional identifier. This creates a fully qualified name that is unique within the entire PLC program. Namespaces can be structured hierarchically.

 

### Network

Networks divide the user program within code blocks. For a code block to be programmed in STL, LAD or FBD, it must contain at least one network.

 

### Network data

Network data is exchanged between a central processing unit and a signal module, a function module and communications modules via the process image or using direct access. Network data can include: Digital and analog input/output signals of signal modules and control and status information of function modules.

 

### NTP

NTP (Network Time Protocol ) is a standard for synchronizing clocks in automation systems via Industrial Ethernet.

 

### Offline (status)

A drive in a Startdrive project of the TIA Portal is in "Offline" status when it does not communicate with any Control Unit of a real drive (hardware). The header of the work area in the "Startdrive" application is dark blue.

 

### Online (status)

A drive in a Startdrive project of the TIA Portal is in "Online" status when it communicates with a Control Unit of a real drive (hardware). The header of the work area in the "Startdrive" application is orange.

 

### OPC / OPC UA

Short for "Open Platform Communications" (formerly "OLE for Process Control"), a standardized software interface used in the field of automation technology. With OPC, data communication between applications from different manufacturers is possible as long as their interfaces have drivers written according to the OPC specification. The previous link to the Windows operating system has been omitted with the successor OPC UA ( "OPC Unified Architecture"). Security functions and functional expandability are other important features of OPC UA.

 

### OPC- / OPC UA server

Device with server functionality for data communication with an OPC or OPC UA client according to the OPC/OPC UA standard.

 

### Operand

An operand is part of a program statement and indicates what the processor will do something with.

 

### Operating mode

The operating mode describes the respective status of the CPU. A CPU can have the following operating states: RUN, STOP, Startup, ERROR and Maintenance (MAINT).

 

### Operating system

The operating system organizes all functions and sequences of the CPU that are not associated with a specific control task.

 

### Operation

An operation is part of a program statement and indicates what the processor will do.

 

### Option Board

Board for insertion in the Control Unit of a drive. A typical Option Board would be a Terminal Board 30 (TB30), for example.

 

### Option Slot

Slot for an optional component (e.g. in the Control Unit).

 

### Organization block

Organization blocks form the interface between the operating system of the CPU and the user program. The order in which the user program executes is specified in organization blocks.

 

### Output

An output is a memory area in the CPU system memory.

 

### Output parameter

The output parameter is a parameter that transfers the data and calculation results from a block in the program to the calling block.

 

### Parameter instance

A parameter instance is a block call with which the instance of the block being called is transferred as an in/out parameter to the calling block.

 

### PLC data type

A PLC data type is a data structure defined by the user that can be used more than once in the program. A PLC data type can consist of multiple elements which each can have different data types.

 

### PLC synchronization

In PLC synchronization, multiple engineering systems work together and in parallel on one CPU as part of team engineering. Prior to TIA Portal V15, the "PLC synchronization" functionality was referred to as "Shared commissioning".

 

### PLC tag table

The PLC tag table is a table for the definition of tags that are valid throughout the CPU.

 

### Position controller

Generally, the position controller is a P controller (less frequently a PI controller), which cyclically compares the internal digital position setpoint and the digital actual value of the measuring system. The result of this setpoint/actual value comparison is a signed differential value. The proportional gain of the position controller is known as the position loop gain or Kv factor. The output signal of the position controller acts on the speed controller in order to correct the position error.

 

### Power Module

In relation to SINAMICS, a Power Module is an AC-AC converter without an integrated Control Unit.

 

### POWER ON

A POWER ON on the Control Unit of a drive resets the entire system and forces another ramp-up. A POWER ON can be triggered, for example, by switching the power supply off/on for all components of the drive system.

 

### Power unit

In SINAMICS, power unit is the generic term for Motor Modules, Line Modules and Power Modules.

 

### Priority

The priority defines the interruptibility of the user program that is currently running, as higher-priority events interrupt lower-priority events.

 

### Private

If tags and methods are declared with the keyword "Private", access is only possible within the object in which they were declared. Such an object may be a class or block, for example.

 

### Process data (PZD)

Process data controls an automation process and provides information about its state.

 

### Process image

The process image is a memory area of the CPU system memory that includes the signal states of the digital input and output modules. A distinction is made between the process image input (PII) and the process image output (PIQ).

 

### Process image input

The process image input (PII) is read from the input modules by the operating system before the user program is started.

 

### Process image output

The process image output (PIQ) is transferred by the operating system to the output modules before the execution of the user program and before the reading of the process image input.

 

### Process interrupt

A process interrupt is an interrupt triggered due to an event in the process.

 

### PROFIBUS

PROFIBUS (Process Field Bus) is a standard for fieldbus communication in automation technology.

 

### PROFIBUS DP

PROFIBUS DP is a PROFIBUS (Process Field Bus) with DP protocol (Decentralized Peripherals) that complies with EN 50170. It is used to address sensors and actuators by means of a central controller as well as for networking of multiple controllers. From the perspective of the user program, the distributed I/O is addressed in exactly the same way as the central I/O.

 

### PROFIdrive

PROFIdrive is the modular, cross-vendor device profile for drive units from "Profibus & Profinet International (PI)". PROFIdrive was developed jointly by automation technology vendors and users in the 1990s and, in conjunction with the PROFIBUS field bus and PROFINET industrial Ethernet, covers the entire range from very simple to extremely complex drive solutions.

 

### PROFINET

PROFINET (Process Field Network) is an Ethernet-based communication system for distributed automation systems.

 

### PROFINET device

A PROFINET device is a device with a PROFINET interface (electrical, optical, wireless).

 

### PROFINET port

A PROFINET port is a physical connection option for devices that are PROFINET nodes.

 

### PROFIsafe

PROFIsafe (or, more precisely: PROFIBUS safety profile) specifies communication between fail-safe I/O devices and fail-safe controllers. It is based on the standards for safety-related applications as well as on the experience of PLC users and manufacturers who are members of PROFIBUS International (PI). PROFIsafe is certified by TÜV and BIA (Institute for Occupational Safety and Health of the German Social Accident Insurance).

 

### Program alarm

Program alarms are used to report program-synchronous events and are each assigned to a block. They are created in the program editor and edited in the alarm editor.

 

### Programmable logic controllers

Programmable logic controllers (PLCs) are electronic controllers whose functionality is stored as a program on the control device. The installation and wiring of the device do not therefore depend on the function of the controller.

 

### Programmable module

Programmable modules is a collective term for central processing units (CPUs), function modules (FMs) and communication modules (CPs).

 

### Programming device

A programming device (PG) is a personal computer with a compact and industry-compatible design. A programming device is completely equipped for programming SIMATIC automation systems.

 

### Programming language

A programming language is used to create user programs and provides a defined language subset for this purpose in the form of graphical or textual instructions. These instructions are entered by the user with an editor and then compiled into an executable user program.

 

### Project copy

A project copy is the copy of a project which is created from structured master projects when working with team engineering; it is distributed to the participating engineering systems for editing. Each engineering system only processes the parts it was assigned within the specific project copy as part of joint commissioning. The individual project copies are once again integrated into the master project at the end of joint commissioning.

 

### Project server

The project server is the server that manages the server projects for working with Multiuser-Engineering, Multiuser Commissioning and Exclusive Engineering . Various server configurations and network profiles are available for working with the project server. Prior to TIA Portal V16, the "Project server" was referred to as "Multiuser server".

 

### Project texts

Project texts are all the texts within a project (for example, alarm texts or comments). They can be translated into the respective project languages.

 

### Protected

Tags and methods which were declared with the keyword "protected" can be accessed within the class in which they were declared. The access right is also passed on to all derived classes of the class.

 

### Protection level

The protection level is part of a multi-stage concept to protect the functions and data of SIMATIC CPUs (S7-300/400). The protection levels are "No protection" (all functions are permitted), "Write protection" (data can be read but not changed) and "Write/Read protection" (no access to data permitted).

 

### Protocol

A protocol is a synchronization method used by transmission systems for efficient data exchange, for example, MRP.

 

### Public

Tags and methods which were declared with the keyword "protected" can be accessed from everywhere.

 

### Publisher

Sender in a Publisher-Subscriber system

 

### Publisher-Subscriber system

Communication model in which the sender (Publisher) does not send directly to a receiver (Subscriber), but publishes its data classified. One or more subscribers can register to read published data or data classes; they subscribe to this data. Depending on the protocol used, communication between publishers and subscribers can take place directly or via intermediate instances.

 

### Pulse enable

Signal or terminal to activate or deactivate a SINAMICS drive. Without controlling the signal, the control pulses for power transistors in the Motor Module and the motor are switched torque-free. This signal has top priority for the drive. When the pulse enable for the drives is removed during operation, the drives "coast down" unbraked.

 

### Ramp-function generator (RFG)

A ramp-function generator is used to limit the rate-of-rise of setpoints (e.g. speed setpoints) for closed-loop drives. In the event of a step change of the setpoint at the input, it supplies a running output signal with configured slope. In this way, ramp-up of the motor adapted to technological conditions is possible.

 

### Reference

A tag which itself contains no value but includes the storage location (address) of a tag. When the reference is declared, the programmer species from which data type the referenced tag must be.

 

### Relation

Link that allows data access from a software unit to an object outside the software unit.

 

### Reluctance motor (REL)

A synchronous motor with three-phase stator winding, without rotor winding and without permanent magnets in the rotor. The rotor, which is normally laminated, is designed in such a way that small and large air gaps (pole and pole gap, so to speak) occur alternately. This results in a simple construction but a much lower power density than with a comparable permanent-magnet "synchronous motor". Use only with small outputs < approx. 1 kW.

 

### Remote communication

Remote communication, also referred to as remote connection, is an asynchronous connection setup from a plant to a programming device or PC. Using the specified telephone number, a TS Adapter establishes a remote link/remote connection to a programming device/PC.

 

### Remote connection

A remote connection is established when you use TeleService to dial in to a remote plant via a telephone network. A remote connection enables a remote plant to be operated as usual.

 

### RESET

A RESET of the Control Unit of a drive resets the entire system and forces another ramp-up. A RESET can be triggered by pressing the RESET button or by switching the power supply off/on.

 

### Resources

Resources in the program information displays the CPU hardware resources for each utilized programming object, the allocation of memory areas within the CPU, and the inputs and outputs used on the existing I/O modules.

 

### Restart

Restart is a startup type of the CPU. When a CPU starts up, all non-retentive system and user data is initialized.

 

### Result of logic operation

The result of logic operation is the current signal state in the processor that is used for subsequent binary signal processing. Certain operations are executed depending on the previous result of logic operation.

 

### Retentive data

Retentive data includes tags, data or blocks which are stored in the retentive memory area of a CPU and which are therefore retained even when the supply voltage is switched off.

 

### Retentive memory

The retentive memory is a memory area within a CPU whose content is retained after power off and at the STOP to RUN transition after power on. The retentive memory is also referred to as retentive memory area.

 

### RUN mode

In "RUN" operating mode the CPU executes the user program, updates the inputs and outputs and processes interrupts and error messages.

 

### Runtime error

A runtime error is an error that occurs during execution of the user program in the automation system.

 

### Safety Integrated

Safety Integrated designates all safety functions integrated into the products for efficient personal and machine protection in accordance with the EC Machinery Directive 98/37/EC. In SINAMICS, these safety functions fulfill the following requirements:   
‑ SIL2 - Safety Integrity Level according to IEC 61508 and EN 61800-5-2   
‑ Performance Level (PL) d according to DIN EN ISO 13849-1  
‑ Category 3 according to DIN EN ISO 13849-1

 

### SCL

SCL (Structured Control Language) is a high-level programming language based on PASCAL. The language is based on DIN EN 61131-3 (international IEC 1131-3). The standard standardizes programming languages for programmable logic controllers. The SCL programming language fulfills the PLCopen Basis Level of ST language (Structured Text) defined in this standard.

 

### Sensor Module (SMCxx/SMExx)

The Sensor Module is used for evaluating speed/position encoder signals and providing detected actual values as numerical values at a DRIVE-CLiQ socket. Two variants of these modules can be used:   
SMCxx = Sensor Module Cabinet Mounted = Sensor Module for snap-on mounting in the control cabinet   
SME = Sensor Module Externally Mounted = Sensor Module with a high degree of protection for mounting outside the cabinet.

 

### Sequencer

Sequencers are used in the GRAPH programming language for programming of the user program. The program can be separated into individual steps within the sequencers, whereby the conditions for advancing to the next step are specified in the transitions.

 

### Sequential control system

The sequential control system is a control system that executes a program step-by-step using sequential commands or conditions.

 

### Servo control

Particularly suitable for highly dynamic drives.   
This type of closed-loop control enables operation with a high dynamic response and precision for a motor with a motor encoder. In addition to speed control, position control can be included.

 

### Shared commissioning

In shared commissioning, multiple engineering systems work together and in parallel on one CPU as part of team engineering. The "Shared commissioning" functionality is referred to as "PLC synchronization" as of TIA Portal V15.1.

 

### Signal module

Signal modules (SMs) form the interface between the process and the automation system. They include input modules, output modules and in/out modules (both digital and analog).

 

### SINAMICS

Brand name of Siemens AG for a drive system.

 

### SINAMICS Link

Cyclic, isochronous PZD communication between multiple SINAMICS Control Units (CU320-2). Based on the PROFINET controller-controller communication. The requirement is a Communication Board Ethernet 20.

 

### Single instance

A single instance is a block call in which the called block stores its data in its own instance data block.

 

### Single Motor Module (SMM)

A Single Motor Module is a Motor Module to which 1 single motor can be connected and operated.

 

### Smart Infeed

Overall functionality of an infeed with Smart Line Module, including the required additional components (filters, switching devices, etc.).

 

### Smart Line Module (SLM)

Unregulated infeed/feedback unit with a diode bridge for feeding and stall-protected, line-commutated feedback via IGBTs. The Smart Line Module provides the DC-link voltage for the Motor Modules.

 

### SMS

An SMS (Short Message Service) is a message of limited length (maximum of 160 characters) that can be sent to a GSM receiver via the mobile network.

 

### SNMP

SNMP (Simple Network Management Protocol) is the standardized protocol for diagnostics and parameter assignment of the Ethernet network infrastructure.

 

### Software unit

Program unit that can be individually compiled and loaded independent of other program units

 

### Speed control

Speed control constantly compares the actual value of the motor speed with the specified setpoint. These two signals are processed by a speed controller that specifies a torque or a motor current at its output as manipulated variable that controls the setpoint/actual difference to zero with the greatest possible accuracy.   
Even with fast changes of the speed setpoint and sudden load surges, the actual speed value should follow the speed setpoint as congruently as possible, i.e. the speed control should have the best possible control and disturbance behavior as well as a high dynamic response.   
The actual speed value is either measured using an encoder or calculated from other measured and calculation values by means of a software motor model. SINAMICS has a very precise and highly dynamic speed control. Various filters arranged in the speed setpoint and actual value branch and in the speed controller output enable precise, dynamic and yet stable speed control even in mechanical systems that tend to oscillate.

 

### SSL

SSL (Secure Sockets Layer) is an encryption protocol for secure data transmission on the Internet.

 

### Standard telegram

The standard telegrams (telegram numbers up to 100) are cross-vendor telegrams. These telegrams are specified via PROFIdrive.

 

### Start event

A start event is a defined event, such as a fault/error or interrupt, that causes the operating system to start a corresponding organization block.

 

### Start information

The start information is information that is made available by the operating system when certain organization blocks start; it can be evaluated in the user program.

 

### Start value

The start value is the value assigned to a tag when the system starts up.

 

### Start-up mode

The CPU runs through start-up mode on a transition from STOP mode to RUN mode. A distinction is made between a cold restart, restart, and warm restart.

 

### Startup OB

The startup OB is an organization block with is called once by the CPU operating system when the CPU goes from STOP to RUN. The startup OB can, for example, contain the default settings for a defined system startup following a power outage. If multiple startup OBs exist, they are called in the order of their OB numbers.

 

### Statement List (STL)

The Statement List (STL) is a textual programming language, similar to machine code. If a program is written in STL, the individual statements represent the steps in which the CPU executes the program.

 

### Static data

Static data is local data of a function block that is stored in the instance data block and is therefore only retained until the next time the function block is processed.

 

### Station

Any device that can be operated without additional modules is referred to as a station. For example, a simple DP slave is not designated as a station because it cannot be operated without an associated DP master. An intelligent DP slave (with CPU) is a station because it can be operated alone.

 

### Status word (ZSW)

Bit-coded process data word transmitted by PROFIdrive at cyclic intervals for acquisition of drive states.

 

### STL

The Statement List (STL) is a textual programming language, similar to machine code. If a program is written in STL, the individual statements represent the steps in which the CPU executes the program.

 

### STOP mode

The user program does not execute in STOP mode. All outputs are set to substitute values to bring the controlled process to a safe operating mode.

 

### Stop response

With Safety Integrated, the set "Stop response" (e.g. STOP A, B, C) of a safety function determines the response to triggering of monitoring.  
The term "Error response" is used almost equally. Error response is used exclusively with SINAMICS S210 drives.

 

### Structure

A structure (STRUCT) is a complex data type made up of data elements of different types.

 

### Subnet

A subnet includes all the network devices interconnected without gateways. It can include repeaters.

 

### Subscriber

Receiver in a Publisher-Subscriber system

 

### Synchronous motor

A synchronous motor is a single-phase or three-phase synchronous machine operated as motor, where a permanently magnetized rotor is moved synchronously by the rotating magnetic field in the stator. The operational synchronous motor moves synchronously with the AC voltage. This means that the motor speed is linked to the AC voltage frequency through the pole pair number.  
The "Synchronous motor" motor type can be divided into further subtypes:   
‑ Permanent-magnet synchronous motor (PMSM)  
‑ Synchronous reluctance motor (RESM)  
‑ Separately excited synchronous motor (SESM)

 

### System control point

System control points (SCP) are defined points in cyclic program execution at which no block is processed and operating system functions are performed instead.

 

### System diagnostic alarm

System diagnostic alarms are alarms triggered by configuration-dependent module events. System diagnostic alarms are activated or deactivated in the hardware configuration. They can only be viewed, not edited, in the alarm editor.

 

### System diagnostics

System diagnostics is the detection and evaluation of diagnostic information which is initiated by the operating system when a system error occurs.

 

### System error

System errors are errors that can occur in an automation system, for example, program errors in the CPU or module defects.

 

### System memory

The system memory is integrated on the S7-CPU and is implemented as RAM. The system memory contains operand areas (for example bit memory) and data areas required internally by the operating system (for example, buffers for communication).

 

### Target system

The target system is an automation system on which the user program runs.

 

### Team Engineering

Team Engineering supports access of several editors in parallel and at the same time with multiple engineering systems (ES) to one shared CPU.

 

### Telegram

The number, type and order of the process data to be transferred in send and receive direction are defined in a telegram. A distinction is made between manufacturer-specific telegrams and standard telegrams. The individual signals of a telegram can also be freely interconnected using BICO technology.

 

### TeleService

TeleService supports central management, control and monitoring of distributed plants by means of remote connections. A TS Adapter or a Telecontrol CP must be used in order to establish a remote connection using TeleService.

 

### Temporary local data

Temporary local data is local data of a block that is stored temporarily during the processing of the block and is no longer available following processing.

 

### Terminal Board (TB)

Terminal expansion module for plugging into the option slot of a SINAMICS Control Unit.

 

### Terminal Module (TM)

Terminal expansion module of SINAMICS drives for snapping onto the installation rail, for installation in the control cabinet.

 

### Third-party motor

A motor is designated as a third-party motor if its motor data is not known to the drive (or the corresponding drive software) and it cannot be identified by means of its order number. When a third-party motor is commissioned, its motor data therefore needs to be entered manually in the corresponding parameters (motor data input).

 

### Time stamp

The time stamp is an entry made in a block about the last change made.

 

### Time-delay interrupt

The time-delay interrupt is an interrupt that is generated after the expiry of a time delay started in the user program.

 

### Token

A token is a time-limited access authorization to the bus.

 

### Trace and logic analyzer function

You can use the trace and logic analyzer function to record tags of a device and evaluate these recordings.

 

### Trigger

A trigger initiates a test function and is defined by the trigger point and trigger condition.

 

### Trigger condition

The trigger condition determines whether or not selected tags are to be monitored or modified once or permanently.

 

### Trigger point

The trigger point is a defined point during the user program, for example, at the beginning of the cycle, at the end of the cycle, at a RUN --> STOP transition. The trigger point determines when selected tags are to be monitored or modified during the user program.

 

### TS Adapter MPI

TS Adapter MPI is a collective term for all TS Adapters with an MPI/DP interface.

 

### TS Adapter

A TS Adapter is used to connect an automation system to a telephone network via a modem for the purpose of preparing the telephone network for the use of TeleService. The TS Adapter is available in two versions, for example, as TS Adapter MPI and as TS Adapter IE.

 

### TS Adapter IE

TS Adapter IE is a collective term for all TS Adapters with an Ethernet interface.

 

### Types

Types are a kind of library element. You can use types to derive and use instances of the respective library element. These instances are tied to their respective type, and changes to one instance also change all other existing instances.

 

### User diagnostics alarm

User diagnostics alarms are used to write a user entry into the diagnostic buffer of a CPU. User diagnostics alarms are created and edited by the user in the alarm editor.

 

### User program

The user program solves a self-contained control task. It is assigned to a programmable module and can be structured with the help of individual blocks.

 

### V/f control

Control technique for three-phase motors where the voltage amplitude U is specified as a function of the actual motor frequency f.   
To this end, a rugged motor model is used, in which the quotient V/f is proportional to the achievable torque. ‑Servo control: The servo drive has a simple V/f control that is used for diagnostic purposes.   
‑Vector control: In a vector drive, the V/f control can be used for induction motors to control single and group drives (multiple motors on a converter) with low to medium demands on the dynamic response, speed setting range and accuracy. The V/f characteristic can be adjusted. The most usual characteristic types are those with a constant torque or a square-law characteristic for pumps and fans.

 

### Vector control

Particularly suitable for universal drives.  
Vector control (field-oriented control) is a high-performance control type for induction machines. It is based on an exact model calculation of the motor and two current components, which simulate the flux and torque by means of software algorithms so that they can be easily controlled. This means that speed and torque setpoints can be precisely maintained and limited with a good dynamic response. There are two versions of vector control: The frequency control ("Encoderless vector control") and the speed-torque control with speed feedback ("Encoder").

 

### Voltage Sensing Module (VSM)

A Voltage Sensing Module is used in conjunction with an Active Line Module for feeding back the actual line voltage value. It detects the current values of the line voltage and makes these available via DRIVE-CLiQ. The VSM can be mounted on a mounting rail and features two analog inputs and a connection for a temperature sensor.

 

### Watch table

The watch table allows you to monitor and modify tags in the user program. Within the watch table, it is also possible to assign fixed values to individual peripheral outputs of the CPU in STOP mode.

 

### Webserver

Web application that allows you to access the data of a drive directly via a browser. The drive must be accessible via the network for this purpose. In addition to checking and correcting the drive data, it is also possible to download projects and update firmware via the web server. Activation and password settings for the web server are possible with SINAMICS drives via the "Startdrive" TIA application also.

 

### Work memory

The work memory is a RAM on the CPU accessed by the processor while the user program is executed.
