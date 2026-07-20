---
title: "Function diagrams for SINAMICS G220"
package: StdrInfSysOptFDSinaG220enUS
topics: 2
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Function diagrams for SINAMICS G220

This section contains information on the following topics:

- [Read function diagrams](#read-function-diagrams)
- [Function diagrams for SINAMICS G220 drives](Function%20diagrams%20for%20SINAMICS%20G220%20drives.md#function-diagrams-for-sinamics-g220-drives)

## Read function diagrams

A block with function diagrams is available for each drive family. Function diagrams are signal flow charts that represent a controller, for example. They can be arranged side-by-side, e.g. to show the structure of the closed-loop control. The screen forms of the program user interface are based on these function diagrams. However, for reasons of clarity they usually do not display all of the parameters.

Function diagrams have the following structure:

![Example: representation of a function block diagram](images/172197993355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| **In the footer:** |  |
| ① | Describes the topic or function area, for which the function diagram is valid. |
| ② | Describes the content of the function diagram, e.g. interface to the power unit |
| ③ | Shows the firmware version. Here as an example FW V6.02.00.  In principle, function diagrams are only available for the current SINAMICS firmware. |
| ④ | Displays the diagram number. |
| **In the diagram:** |  |
| ⑤ | The signal path number is displayed in the footer. The function diagram is divided into 8 (not subdivided) fields. These fields are used for navigation within the diagram. Links to other function diagrams always contain the signal path number in addition to the diagram number so that it is easier to find the link target. |
| ⑥ | The links to other diagrams can also be seen in the diagram. The structure of the links is as follows:  - Function diagram number - Signal path number (separated by a dot) |
| ⑦ | Footnotes are specifically identified in the text:   - square brackets e.g. <1>. - colored bars |
| ⑧ | Signal interconnections of r parameters (signal sources) or c parameters (signal sinks) |
| ⑨ | The signal flow in the function diagram is illustrated using various symbols. |

Example: representation of a function block diagram
