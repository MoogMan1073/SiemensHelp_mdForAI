---
title: "TB30 Option Board"
package: stdrMVui100000enUS
topics: 16
source: Siemens TIA Portal Information System (offline help, en-US)
---


# TB30 Option Board

This section contains information on the following topics:

- [Overview](#overview)
- [Parameterize Inputs/Outputs](#parameterize-inputsoutputs)
- [Control Logic](#control-logic)

## Overview

This section contains information on the following topics:

- [TB30 Description](#tb30-description)
- [TB30 Interfaces](#tb30-interfaces)

### TB30 Description

#### Description

The TB30 option module is a terminal expansion board inserted into the option slot of the Control Unit, see also [TB30 Interfaces](#tb30-interfaces). As it is not connected using DRIVE-CLiQ, no DRIVE-CLiQ interface is occupied. This means it is displayed in the topology as being directly connected with the Control Unit. The TB30 is added in the device view directly from the hardware catalog

For further information, see

- [TB30 Analog Inputs](#tb30-analog-inputs-1)
- [TB30 Analog Outputs](#tb30-analog-outputs-1)
- [Isolated TB30 digital inputs](#isolated-tb30-digital-inputs)
- [Isolated TB30 digital outputs](#isolated-tb30-digital-outputs)

### TB30 Interfaces

#### Description

![TB30 interfaces](images/147863204107_DV_resource.Stream@PNG-en-US.png)

TB30 interfaces

## Parameterize Inputs/Outputs

This section contains information on the following topics:

- [TB30 Inputs/Outputs](#tb30-inputsoutputs)
- [TB30 analog inputs](#tb30-analog-inputs)
- [TB30 Analog Outputs](#tb30-analog-outputs)
- [TB30 Digital Inputs](#tb30-digital-inputs)
- [TB30 Digital Outputs](#tb30-digital-outputs)

### TB30 Inputs/Outputs

#### Description

The TB30 option module has the following input/outputs:

- 2 [Analog inputs](#tb30-analog-inputs-1)
- 2 [Analog outputs](#tb30-analog-outputs-1)
- 4 [Isolated digital inputs](#isolated-tb30-digital-inputs)
- 4 [Digital outputs](#isolated-tb30-digital-outputs)

### TB30 analog inputs

This section contains information on the following topics:

- [TB30 Analog Inputs](#tb30-analog-inputs-1)

#### TB30 Analog Inputs

In the "Analog inputs" screen form, you can change for the TB30 the interconnection of the analog inputs 0 and 1 on the input/output component.

- Analog inputs are used for the acquisition of external analog signals. These signals can be voltages. Analog inputs are used, for example, to specify an analog definition of a speed or torque.
- Analog inputs supply a normalized analog signal (current, voltage or temperature). This analog signal is converted via the scaling in the value range -100%...100%. The scaling serves to adapt to the machine or to the existing components. You can define a scaling characteristic with two points. You must specify an X coordinate and a Y coordinate for each of the two points.
- Analog values are always subject to noise. You can suppress this noise with a filter. You can also smooth the input signal.

##### Parameterizing analog inputs

1. Correct in the "Offset" (p4063) field the specified voltage value of the offset.

   The offset is added to the value of the input signal prior to scaling.
2. If you want to invert the analog signal, interconnect the signal source in the "Inversion" (p4067) field.

   For activated inversion, the LED next to the field illuminates green and the ![Parameterizing analog inputs](images/147822431883_DV_resource.Stream@PNG-en-US.PNG) symbol in the interconnection becomes visible.
3. To define a scaling characteristic via the scaling, click the "Scaling" button.

   The "TM31 analog input AI 0 scaling" dialog opens. Specify here the following values for the X and Y coordinates of the scaling characteristic (each for the value pair 1 and 2):

   - Characteristic value x2 (p4059)
   - Characteristic value y2 (p4060)
   - Characteristic value y1 (p4058)
   - Characteristic value x1 (p4057)

   Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
4. If you want to form the absolute value of the scaled input value, click the ![Parameterizing analog inputs](images/147822448651_DV_resource.Stream@PNG-en-US.PNG) (absolute-value generation) symbol.

   An activated inversion is indicated with the following symbol: ![Parameterizing analog inputs](images/147822452619_DV_resource.Stream@PNG-en-US.PNG)
5. To compensate temporary fluctuations of the measured value at the analog input, enter a time constant in the "Smoothing" (p4053) field.

   The larger the smoothing time constant, the slower the response of the analog input to changes in the measured value.
6. If you require a noise suppression for the input signal, enter a value in the "Noise suppression" (p4068) field. The noise suppression results as follows:

   - |y-x| > noise suppression   
     results in y = x

     The output value is set to the current input value.
   - |y-x| ≤ noise suppression   
     results in y = y<sub>old</sub>

     The output value retains its value.
7. Interconnect the "Activate" (p4069) signal sink for the signal to enable the analog inputs.

   When activated, the LED next to the field illuminates green.
8. Interconnect the "Analog input 0" (p4055) signal sink for the input value of the analog inputs.
9. Repeat steps 1 to 8 for analog input 1 of the terminal board.

##### Function diagrams (FD)

- FD-9104 (51)
- FD-9106 (51)
- FD-9099 (51)

##### Additional parameters

Pxxxx

### TB30 Analog Outputs

This section contains information on the following topics:

- [TB30 Analog Outputs](#tb30-analog-outputs-1)

#### TB30 Analog Outputs

In the "Analog outputs" screen form, you can change the interconnection of the analog outputs 0 and 1 on the input/output component.

- Analog outputs are used for the output of analog variables, e.g. for diagnostic or feedback purposes on a higher-level controller.
- The output setpoint is interconnected by means of BICO technology.
- Absolute-value generation is possible and/or inversion of the output setpoint.
- Smoothing the output setpoint results in a suppression of setpoint peaks.

##### Parameterizing analog outputs

1. Interconnect the "Analog output 0" (p4071) signal source for the analog outputs of the TB30.
2. If you want to invert the analog signal, interconnect the signal source in the "Inversion" (p4082) field.

   For activated inversion, the LED illuminates green and the ![Parameterizing analog outputs](images/147822431883_DV_resource.Stream@PNG-en-US.PNG) symbol becomes visible in the interconnection.
3. If you want to form the absolute value of the scaled input value, click the ![Parameterizing analog outputs](images/147822448651_DV_resource.Stream@PNG-en-US.PNG) (absolute-value generation) symbol.

   An activated inversion is indicated with the following symbol: ![Parameterizing analog outputs](images/147822452619_DV_resource.Stream@PNG-en-US.PNG)
4. To compensate temporary fluctuations of the measured value at the analog input, enter a time constant in the "Smoothing" (p4073) field.

   The larger the smoothing time constant, the slower the response of the analog input to changes in the measured value.
5. To define a scaling characteristic via the scaling, click the "Scaling" button.

   The "TB30 analog input A0 0 scaling" dialog opens. Specify here the following values for the X and Y coordinates of the scaling characteristic (each for the value pair 1 and 2):

   - Characteristic value x2 (p4079)
   - Characteristic value y2 (p4080)
   - Characteristic value y1 (p4078)
   - Characteristic value x1 (p4077)

   Once you have made all the necessary settings, click the "Close" button.

   The dialog closes.
6. Correct in the "Offset" (p4083) field the specified voltage value of the offset.

   The offset is added to the value of the input signal prior to scaling.
7. Repeat steps 1 to 6 for analog output 1 of the terminal board.

##### Function diagrams (FD)

- FD-9100 (51)
- FD-9099 (51)

##### Additional parameters

Pxxxx

### TB30 Digital Inputs

This section contains information on the following topics:

- [Isolated TB30 digital inputs](#isolated-tb30-digital-inputs)

#### Isolated TB30 digital inputs

Digital inputs are used for the acquisition of digital signals. For example, drive enables can be controlled externally. On the "Isolated digital inputs" screen form you can change the interconnection of digital inputs 0...3 on the input/output component. If required, you can also interconnect inverted signals.

**Simulation mode**

The selection box for the terminal evaluation/simulation switchover is only visible online.

##### Parameterizing digital inputs

1. Interconnect the signal sinks for the required digital inputs or the inverted digital inputs.

   You can interconnect up to 4 digital inputs.

##### Function diagrams (FD)

- FD-9100 (51)
- FD-9099 (51)

##### Additional parameters

Pxxxx

### TB30 Digital Outputs

This section contains information on the following topics:

- [Isolated TB30 digital outputs](#isolated-tb30-digital-outputs)

#### Isolated TB30 digital outputs

In the "Isolated digital outputs" screen form, you can change the interconnection of digital outputs 0...3 on the input/output component.

Digital outputs are used for the feedback of signals such as enables.

##### Parameterizing digital outputs

1. Interconnect the signal sinks for the required digital outputs of Terminal Board 30.

   You can interconnect up to 4 digital outputs.
2. If required, you can invert each of the signals of the 4 digital outputs: To do this, click the appropriate ![Parameterizing digital outputs](images/147822448651_DV_resource.Stream@PNG-en-US.PNG) inversion symbol at the right next to the digital input in the screen form.

   An activated inversion is indicated with the following symbol: ![Parameterizing digital outputs](images/147822641803_DV_resource.Stream@PNG-en-US.PNG)

##### Function diagrams (FD)

- FD-9102 (51)
- FD-9099 (51)

##### Additional parameters

Pxxxx

## Control Logic

This section contains information on the following topics:

- [TB30 control logic](#tb30-control-logic)

### TB30 control logic

The interconnections for control/status words of the faults and alarms are displayed and can be edited here.

#### Parameterizing the control logic

1. Select in the drop-down list of the "Control logic" screen form which status words (r2139) or control words (r2138) should be displayed so they can then be interconnected.
2. Then interconnect the individual bits of the status and control words displayed in the screen form.

   A green LED indicates that the corresponding bit of the control or status word is set. If the bit value of the control or status word results from the logical interconnection of several signal sources, the type of the logical interconnection is displayed by the associated logic symbol.

#### Function diagrams (FD)

- FD-2546 (51)
- FD-2548 (51)
