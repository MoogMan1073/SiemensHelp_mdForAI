---
title: "Events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: EventsReferenceWCCPenUS
topics: 105
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Overview (Basic Panels)](#overview-basic-panels)
- [Overview (Panels, Comfort Panels, RT Advanced)](#overview-panels-comfort-panels-rt-advanced)
- [Overview (RT Professional)](#overview-rt-professional)
- [Events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#events-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

## Overview (Basic Panels)

This section contains information on the following topics:

- [Editors (Basic Panels)](#editors-basic-panels)
- [Basic objects (Basic Panels)](#basic-objects-basic-panels)
- [Elements (Basic Panels)](#elements-basic-panels)
- [Controls (Basic Panels)](#controls-basic-panels)

### Editors (Basic Panels)

#### Introduction

The following table shows which events occur in which editor.

Technical data subject to change.

| Icon | Editor |
| --- | --- |
| ![Introduction](images/36121270667_DV_resource.Stream@PNG-de-DE.png) | Screens |
| ![Introduction](images/36121278347_DV_resource.Stream@PNG-de-DE.png) | HMI alarms |
| ![Introduction](images/36121306507_DV_resource.Stream@PNG-de-DE.png) | HMI tags |
| ![Introduction](images/36121298827_DV_resource.Stream@PNG-de-DE.png) | Scheduler |

|  | ![Introduction](images/36121270667_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121278347_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121306507_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121298827_DV_resource.Stream@PNG-de-DE.png) |
| --- | --- | --- | --- | --- |
| [Cleared](#cleared-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | X | -- | -- | -- |
| [Activate](#activate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- |
| [Change](#change-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- |
| [Loaded](#loaded-rt-professional) | X | -- | -- | -- |
| [Execute](#execute-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | X |
| [Selection changed](#selection-changed-rt-professional) | -- | -- | -- | -- |
| [On exceeding](#on-exceeding-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | X | -- |
| [On falling below](#on-falling-below-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | X | -- |
| [When dialog is opened](#when-dialog-is-opened-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | X |
| [When dialog is closed](#when-dialog-is-closed-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | X |
| [User change](#user-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | X |
| [Screen change](#screen-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | X |
| [Deactivate](#deactivate-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | X |
| [Double-click](#double-click-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- |
| [Press](#press-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- |
| [On Finish Input](#on-finish-input-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- |
| [Press ESC twice](#press-esc-twice-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- |
| [Outgoing](#outgoing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- |
| [Incoming](#incoming-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- |
| [Click](#click-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- |
| [Click when flashing](#click-when-flashing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- |
| [Loop-in alarm](#loop-in-alarm-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- |
| [Release](#release-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- |
| [Alarm buffer overflow](#alarm-buffer-overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | X |
| [Acknowledge](#acknowledge-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- |
| [Reach margin](#reach-margin-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- |
| [Runtime Stop](#runtime-stop-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | X |
| [Press key](#press-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- |
| [Release key](#release-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- |
| [Overflow](#overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- |
| [Switch OFF](#switch-off-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- |
| [Switch ON](#switch-on-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- |
| [Low free storage space](#low-free-storage-space-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- |
| [Free space critically low](#free-space-critically-low-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- |
| [Value change](#value-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | X | -- |
| [Time expired](#time-expired-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- |

### Basic objects (Basic Panels)

#### Introduction

The following table shows which events occur on which objects.

Technical data subject to change.

| Icon | Object |
| --- | --- |
| ![Introduction](images/36121380619_DV_resource.Stream@PNG-de-DE.png) | Line |
| ![Introduction](images/36121388299_DV_resource.Stream@PNG-de-DE.png) | Ellipse |
| ![Introduction](images/36121395979_DV_resource.Stream@PNG-de-DE.png) | Circle |
| ![Introduction](images/36121403659_DV_resource.Stream@PNG-de-DE.png) | Rectangle |
| ![Introduction](images/36121411339_DV_resource.Stream@PNG-de-DE.png) | Text field |
| ![Introduction](images/36121419019_DV_resource.Stream@PNG-de-DE.png) | Graphic view |
|  |  |

|  | ![Introduction](images/36121380619_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121388299_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121395979_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121403659_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121411339_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121419019_DV_resource.Stream@PNG-de-DE.png) |
| --- | --- | --- | --- | --- | --- | --- |
| [Cleared](#cleared-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Activate](#activate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Change](#change-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Loaded](#loaded-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Execute](#execute-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Selection changed](#selection-changed-rt-professional) | -- | -- | -- | -- | -- | -- |
| [On exceeding](#on-exceeding-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [On falling below](#on-falling-below-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [When dialog is opened](#when-dialog-is-opened-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [When dialog is closed](#when-dialog-is-closed-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [User change](#user-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Screen change](#screen-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Deactivate](#deactivate-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Double-click](#double-click-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Press](#press-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [On Finish Input](#on-finish-input-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Press ESC twice](#press-esc-twice-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Outgoing](#outgoing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Incoming](#incoming-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Click](#click-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Click when flashing](#click-when-flashing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Loop-in alarm](#loop-in-alarm-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Release](#release-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Alarm buffer overflow](#alarm-buffer-overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Acknowledge](#acknowledge-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Reach margin](#reach-margin-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Runtime Stop](#runtime-stop-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Press key](#press-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Release key](#release-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Overflow](#overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Switch OFF](#switch-off-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Switch ON](#switch-on-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Low free storage space](#low-free-storage-space-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Free space critically low](#free-space-critically-low-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Value change](#value-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Time expired](#time-expired-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |

### Elements (Basic Panels)

#### Introduction

The following table shows which events occur on which objects.

Technical data subject to change.

| Icon | Object |
| --- | --- |
| ![Introduction](images/70601080075_DV_resource.Stream@PNG-de-DE.png) | IO field |
| ![Introduction](images/36121489931_DV_resource.Stream@PNG-de-DE.png) | Button |
| ![Introduction](images/70601087883_DV_resource.Stream@PNG-de-DE.png) | Symbolic IO field |
| ![Introduction](images/70601198091_DV_resource.Stream@PNG-de-DE.png) | Graphic IO field |
| ![Introduction](images/70601349515_DV_resource.Stream@PNG-de-DE.png) | Date/time field |
| ![Introduction](images/70601341707_DV_resource.Stream@PNG-de-DE.png) | Bar |
| ![Introduction](images/70601205899_DV_resource.Stream@PNG-de-DE.png) | Switch |

|  | ![Introduction](images/70601080075_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121489931_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/70601087883_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/70601198091_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/70601349515_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/70601341707_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/70601205899_DV_resource.Stream@PNG-de-DE.png) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Cleared](#cleared-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- |
| [Activate](#activate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | X | X | X | X | -- | -- | X |
| [Change](#change-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | X | -- | -- | -- | X |
| [Loaded](#loaded-rt-professional) | -- | -- | -- | -- | -- | -- | -- |
| [Execute](#execute-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- |
| [Selection changed](#selection-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- |
| [On exceeding](#on-exceeding-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [On falling below](#on-falling-below-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [When dialog is opened](#when-dialog-is-opened-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [When dialog is closed](#when-dialog-is-closed-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [User change](#user-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [Screen change](#screen-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [Deactivate](#deactivate-basic-panels-panels-comfort-panels-rt-advanced) | X | X | X | X | -- | -- | X |
| [Double-click](#double-click-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- |
| [Press](#press-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- | -- | -- | -- |
| [On Finish Input](#on-finish-input-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [Press ESC twice](#press-esc-twice-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [Outgoing](#outgoing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- |
| [Incoming](#incoming-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- |
| [Click](#click-basic-panels-panels-comfort-panels-rt-advanced) | -- | X | -- | -- | -- | -- | -- |
| [Click when flashing](#click-when-flashing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- |
| [Loop-in alarm](#loop-in-alarm-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- |
| [Release](#release-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- | -- | -- | -- |
| [Alarm buffer overflow](#alarm-buffer-overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [Acknowledge](#acknowledge-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- |
| [Reach margin](#reach-margin-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [Runtime Stop](#runtime-stop-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- |
| [Press key](#press-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [Release key](#release-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [Overflow](#overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [Switch OFF](#switch-off-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | X |
| [Switch ON](#switch-on-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | X |
| [Low free storage space](#low-free-storage-space-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [Free space critically low](#free-space-critically-low-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [Value change](#value-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |
| [Time expired](#time-expired-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- |

### Controls (Basic Panels)

#### Introduction

The following table shows which events occur on which objects.

Technical data subject to change.

| Icon | Object |
| --- | --- |
| ![Introduction](images/103788221963_DV_resource.Stream@PNG-de-DE.png) | Alarm view/alarm window |
| ![Introduction](images/36121650443_DV_resource.Stream@PNG-de-DE.png) | Alarm indicator |
| ![Introduction](images/36121627403_DV_resource.Stream@PNG-de-DE.png) | Trend view |
| ![Introduction](images/103788230027_DV_resource.Stream@PNG-de-DE.png) | User view |
| ![Introduction](images/72311964939_DV_resource.Stream@PNG-de-DE.png) | HTML browser (Basic Panel 2nd Generation only) |
| ![Introduction](images/36121642763_DV_resource.Stream@PNG-de-DE.png) | Recipe view |
| ![Introduction](images/36121689483_DV_resource.Stream@PNG-de-DE.png) | System diagnostics view |
| ![Introduction](images/103788353675_DV_resource.Stream@PNG-de-DE.png) | Help indicator |

|  | ![Introduction](images/103788221963_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121650443_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121627403_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/103788230027_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/72311964939_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121642763_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/103788353675_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121689483_DV_resource.Stream@PNG-de-DE.png) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Cleared](#cleared-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Activate](#activate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | X | -- | X | X | X | -- | -- | X |
| [Change](#change-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Loaded](#loaded-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Execute](#execute-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Selection changed](#selection-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [On exceeding](#on-exceeding-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [On falling below](#on-falling-below-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [When dialog is opened](#when-dialog-is-opened-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [When dialog is closed](#when-dialog-is-closed-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [User change](#user-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Screen change](#screen-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Deactivate](#deactivate-basic-panels-panels-comfort-panels-rt-advanced) | X | -- | X | X | X | -- | -- | X |
| [Double-click](#double-click-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press](#press-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [On Finish Input](#on-finish-input-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press ESC twice](#press-esc-twice-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Outgoing](#outgoing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Incoming](#incoming-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) |  |  |  |  |  |  |  |  |
| [Click](#click-basic-panels-panels-comfort-panels-rt-advanced) | -- | X | -- | -- | -- | -- | -- | -- |
| [Click when flashing](#click-when-flashing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- | -- | -- | -- | -- |
| [Loop-in alarm](#loop-in-alarm-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Release](#release-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Alarm buffer overflow](#alarm-buffer-overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Acknowledge](#acknowledge-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Reach margin](#reach-margin-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Runtime Stop](#runtime-stop-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press key](#press-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Release key](#release-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Overflow](#overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Switch OFF](#switch-off-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Switch ON](#switch-on-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Low free storage space](#low-free-storage-space-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Free space critically low](#free-space-critically-low-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Value change](#value-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Time expired](#time-expired-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |

## Overview (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
- [Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
- [Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
- [Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Editors (Panels, Comfort Panels, RT Advanced)

#### Introduction

The following table shows which events occur in which editor.

Technical data subject to change.

| Icon | Editor |
| --- | --- |
| ![Introduction](images/36121270667_DV_resource.Stream@PNG-de-DE.png) | Screens |
| ![Introduction](images/36121278347_DV_resource.Stream@PNG-de-DE.png) | HMI alarms |
| ![Introduction](images/36121306507_DV_resource.Stream@PNG-de-DE.png) | HMI tags |
| ![Introduction](images/36121314187_DV_resource.Stream@PNG-de-DE.png) | Logs |
| ![Introduction](images/36121298827_DV_resource.Stream@PNG-de-DE.png) | Scheduler |
| ![Introduction](images/36121321867_DV_resource.Stream@PNG-de-DE.png) | Audit Trail |

|  | ![Introduction](images/36121270667_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121278347_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121306507_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121314187_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121298827_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121321867_DV_resource.Stream@PNG-de-DE.png) |
| --- | --- | --- | --- | --- | --- | --- |
| [Cleared](#cleared-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | X | -- | -- | -- | -- | -- |
| [Activate](#activate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Change](#change-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Loaded](#loaded-rt-professional) | X | -- | -- | -- | -- | -- |
| [Execute](#execute-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | X | -- |
| [Selection changed](#selection-changed-rt-professional) | -- | -- | -- | -- | -- | -- |
| [On exceeding](#on-exceeding-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | X | -- | -- | -- |
| [On falling below](#on-falling-below-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | X | -- | -- | -- |
| [When dialog is opened](#when-dialog-is-opened-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | X | -- |
| [When dialog is closed](#when-dialog-is-closed-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | X | -- |
| [User change](#user-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | X | -- |
| [Screen change](#screen-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | X | -- |
| [Deactivate](#deactivate-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Double-click](#double-click-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Press](#press-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [On Finish Input](#on-finish-input-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Press ESC twice](#press-esc-twice-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Outgoing](#outgoing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- | -- | -- |
| [Incoming](#incoming-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- | -- | -- |
| [Click](#click-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Click when flashing](#click-when-flashing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Loop-in alarm](#loop-in-alarm-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- | -- | -- |
| [Release](#release-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Alarm buffer overflow](#alarm-buffer-overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | X | -- |
| [Acknowledge](#acknowledge-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- | -- | -- |
| [Reach margin](#reach-margin-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Runtime Stop](#runtime-stop-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | X | -- |
| [Press key](#press-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Release key](#release-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Overflow](#overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | X | -- | -- |
| [Switching](#switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- |
| [Switch OFF](#switch-off-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Switch ON](#switch-on-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |
| [Low free storage space](#low-free-storage-space-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | X | -- | X |
| [Free space critically low](#free-space-critically-low-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | X | -- | X |
| [Value change](#value-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | X | -- | -- | -- |
| [Time expired](#time-expired-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- |

### Basic objects (Panels, Comfort Panels, RT Advanced)

#### Introduction

The following table shows which events occur on which objects.

Technical data subject to change.

| Icon | Object |
| --- | --- |
| ![Introduction](images/36121380619_DV_resource.Stream@PNG-de-DE.png) | Line |
| ![Introduction](images/36121426699_DV_resource.Stream@PNG-de-DE.png) | Polyline |
| ![Introduction](images/36121434379_DV_resource.Stream@PNG-de-DE.png) | Polygon |
| ![Introduction](images/36121388299_DV_resource.Stream@PNG-de-DE.png) | Ellipse |
| ![Introduction](images/36121395979_DV_resource.Stream@PNG-de-DE.png) | Circle |
| ![Introduction](images/36121403659_DV_resource.Stream@PNG-de-DE.png) | Rectangle |
| ![Introduction](images/36121411339_DV_resource.Stream@PNG-de-DE.png) | Text field |
| ![Introduction](images/36121419019_DV_resource.Stream@PNG-de-DE.png) | Graphic view |
|  |  |

|  | ![Introduction](images/36121380619_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121426699_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121434379_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121388299_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121395979_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121403659_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121411339_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121419019_DV_resource.Stream@PNG-de-DE.png) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Cleared](#cleared-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Activate](#activate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change](#change-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Loaded](#loaded-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Execute](#execute-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Selection changed](#selection-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [On exceeding](#on-exceeding-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [On falling below](#on-falling-below-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [When dialog is opened](#when-dialog-is-opened-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [When dialog is closed](#when-dialog-is-closed-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [User change](#user-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Screen change](#screen-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Deactivate](#deactivate-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Double-click](#double-click-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press](#press-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [On Finish Input](#on-finish-input-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press ESC twice](#press-esc-twice-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Outgoing](#outgoing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Incoming](#incoming-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Click](#click-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Click when flashing](#click-when-flashing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Loop-in alarm](#loop-in-alarm-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Release](#release-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Alarm buffer overflow](#alarm-buffer-overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Acknowledge](#acknowledge-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Reach margin](#reach-margin-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Runtime Stop](#runtime-stop-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press key](#press-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Release key](#release-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Overflow](#overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Switching](#switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Switch OFF](#switch-off-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Switch ON](#switch-on-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Low free storage space](#low-free-storage-space-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Free space critically low](#free-space-critically-low-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Value change](#value-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |
| [Time expired](#time-expired-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |

### Elements (Panels, Comfort Panels, RT Advanced)

#### Introduction

The following table shows which events occur on which objects.

Technical data subject to change.

| Icon | Object |
| --- | --- |
| ![Introduction](images/70601080075_DV_resource.Stream@PNG-de-DE.png) | IO field |
| ![Introduction](images/36121489931_DV_resource.Stream@PNG-de-DE.png) | Button |
| ![Introduction](images/70601087883_DV_resource.Stream@PNG-de-DE.png) | Symbolic IO field |
| ![Introduction](images/70601198091_DV_resource.Stream@PNG-de-DE.png) | Graphic IO field |
| ![Introduction](images/70601349515_DV_resource.Stream@PNG-de-DE.png) | Date/time field |
| ![Introduction](images/70601341707_DV_resource.Stream@PNG-de-DE.png) | Bar |
| ![Introduction](images/70601205899_DV_resource.Stream@PNG-de-DE.png) | Switch |
| ![Introduction](images/36121548811_DV_resource.Stream@PNG-de-DE.png) | Symbol library |
| ![Introduction](images/36121556491_DV_resource.Stream@PNG-de-DE.png) | Slider |
| ![Introduction](images/36121564171_DV_resource.Stream@PNG-de-DE.png) | Gauge |
| ![Introduction](images/36121571851_DV_resource.Stream@PNG-de-DE.png) | Clock |

|  | ![Introduction](images/70601080075_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121489931_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/70601087883_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/70601198091_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/70601349515_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/70601341707_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/70601205899_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121548811_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121556491_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121564171_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121571851_DV_resource.Stream@PNG-de-DE.png) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Cleared](#cleared-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Activate](#activate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | X | X | X | X | -- | -- | X | X | X | -- | -- |
| [Change](#change-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | X | -- | -- | -- | X | -- | X | X | -- |
| [Loaded](#loaded-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Execute](#execute-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Selection changed](#selection-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [On exceeding](#on-exceeding-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [On falling below](#on-falling-below-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [When dialog is opened](#when-dialog-is-opened-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [When dialog is closed](#when-dialog-is-closed-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [User change](#user-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Screen change](#screen-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Deactivate](#deactivate-basic-panels-panels-comfort-panels-rt-advanced) | X | X | X | X | -- | -- | X | X | X | -- | -- |
| [Double-click](#double-click-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- |
| [Press](#press-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- | -- | -- | -- | X | -- | -- | -- |
| [On Finish Input](#on-finish-input-basic-panels-panels-comfort-panels-rt-advanced) | X |  | X | X | -- | -- | -- | -- | -- | -- | -- |
| [Press ESC twice](#press-esc-twice-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Outgoing](#outgoing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Incoming](#incoming-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Click](#click-basic-panels-panels-comfort-panels-rt-advanced) | -- | X | -- | -- | -- | -- | -- | X | -- | -- | -- |
| [Click when flashing](#click-when-flashing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Loop-in alarm](#loop-in-alarm-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Release](#release-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- | -- | -- | -- | X | -- | -- | -- |
| [Alarm buffer overflow](#alarm-buffer-overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Acknowledge](#acknowledge-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Reach margin](#reach-margin-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Runtime Stop](#runtime-stop-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press key](#press-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Release key](#release-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Overflow](#overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Switching](#switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Switch OFF](#switch-off-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- |
| [Switch ON](#switch-on-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- |
| [Low free storage space](#low-free-storage-space-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Free space critically low](#free-space-critically-low-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Value change](#value-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Time expired](#time-expired-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |

### Controls (Panels, Comfort Panels, RT Advanced)

#### Introduction

The following table shows which events occur on which objects.

Technical data subject to change.

| Icon | Object |
| --- | --- |
| ![Introduction](images/103788221963_DV_resource.Stream@PNG-de-DE.png) | Alarm view/alarm window |
| ![Introduction](images/36121650443_DV_resource.Stream@PNG-de-DE.png) | Alarm indicator |
| ![Introduction](images/36121627403_DV_resource.Stream@PNG-de-DE.png) | Trend view |
| ![Introduction](images/103788230027_DV_resource.Stream@PNG-de-DE.png) | User view |
| ![Introduction](images/72311964939_DV_resource.Stream@PNG-de-DE.png) | HTML browser |
| ![Introduction](images/36121666443_DV_resource.Stream@PNG-de-DE.png) | Watch table |
| ![Introduction](images/36121674123_DV_resource.Stream@PNG-de-DE.png) | Sm@rtClient view |
| ![Introduction](images/36121642763_DV_resource.Stream@PNG-de-DE.png) | Recipe view |
| ![Introduction](images/36121681803_DV_resource.Stream@PNG-de-DE.png) | f(x) trend view |
| ![Introduction](images/36121689483_DV_resource.Stream@PNG-de-DE.png) | System diagnostics view / system diagnostics window |
| ![Introduction](images/36124743563_DV_resource.Stream@PNG-de-DE.png) | Media Player<sup>1</sup> |
| ![Introduction](images/83769634187_DV_resource.Stream@PNG-de-DE.png) | PLC code view |
| ![Introduction](images/90104798475_DV_resource.Stream@PNG-de-DE.png) | GRAPH overview |
| ![Introduction](images/90104918539_DV_resource.Stream@PNG-de-DE.png) | ProDiag overview |
| ![Introduction](images/103748828171_DV_resource.Stream@PNG-de-DE.png) | Criteria analysis view |
| ![Introduction](images/90077320843_DV_resource.Stream@PNG-de-DE.png) | Camera view<sup>1</sup> |
| ![Introduction](images/90104909707_DV_resource.Stream@PNG-de-DE.png) | PDF view<sup>1</sup> |
| ![Introduction](images/36121697163_DV_resource.Stream@PNG-de-DE.png) | Function key |
| <sup>1</sup> Only with Comfort HMI devices |  |

|  | ![Introduction](images/103788221963_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121650443_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121627403_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/103788230027_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/72311964939_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121666443_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121674123_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121642763_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121681803_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121689483_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124743563_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/83769634187_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/103748823819_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/103748832523_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/103748828171_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/90077320843_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/90104909707_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121697163_DV_resource.Stream@PNG-de-DE.png) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Cleared](#cleared-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Activate](#activate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | X | -- | X | X | X | X | X | X | -- | X | -- | X | X | X | X | X | X | -- |
| [Change](#change-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Loaded](#loaded-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Execute](#execute-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Selection changed](#selection-changed-rt-professional) | X | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [On exceeding](#on-exceeding-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [On falling below](#on-falling-below-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [When dialog is opened](#when-dialog-is-opened-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [When dialog is closed](#when-dialog-is-closed-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [User change](#user-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Screen change](#screen-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Deactivate](#deactivate-basic-panels-panels-comfort-panels-rt-advanced) | X | -- | X | X | X | X | X | X | -- | -- | -- | X | X | X | X | X | X | -- |
| [Double-click](#double-click-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press](#press-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [On Finish Input](#on-finish-input-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- |  | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press ESC twice](#press-esc-twice-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Outgoing](#outgoing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Incoming](#incoming-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Click](#click-basic-panels-panels-comfort-panels-rt-advanced) | -- | X | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Click when flashing](#click-when-flashing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Loop-in alarm](#loop-in-alarm-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Release](#release-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Alarm buffer overflow](#alarm-buffer-overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Acknowledge](#acknowledge-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Reach margin](#reach-margin-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Runtime Stop](#runtime-stop-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Click the Alarm view button](#click-the-alarm-view-button-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | X | -- | -- | -- | -- |
| [Click the PLC code view button](#click-the-plc-code-view-button-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |
| [Press key](#press-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X |
| [Release key](#release-key-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X |
| [Overflow](#overflow-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Switching](#switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Switch OFF](#switch-off-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Switch ON](#switch-on-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Low free storage space](#low-free-storage-space-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Free space critically low](#free-space-critically-low-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Value change](#value-change-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Time expired](#time-expired-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |

## Overview (RT Professional)

This section contains information on the following topics:

- [Editors (RT Professional)](#editors-rt-professional)
- [Basic objects (RT Professional)](#basic-objects-rt-professional)
- [Elements (RT Professional)](#elements-rt-professional)
- [Controls (RT Professional)](#controls-rt-professional)

### Editors (RT Professional)

#### Introduction

The following table shows which events occur in which editor.

Technical data subject to change.

| Icon | Editor |
| --- | --- |
| ![Introduction](images/36121270667_DV_resource.Stream@PNG-de-DE.png) | Screens |
| ![Introduction](images/36121278347_DV_resource.Stream@PNG-de-DE.png) | HMI alarms |
| ![Introduction](images/36121314187_DV_resource.Stream@PNG-de-DE.png) | Logs |
| ![Introduction](images/36121298827_DV_resource.Stream@PNG-de-DE.png) | Scheduler |

|  | ![Introduction](images/36121270667_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121278347_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121314187_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121298827_DV_resource.Stream@PNG-de-DE.png) |
| --- | --- | --- | --- | --- |
| [Play ended](#play-ended-rt-professional) | -- | -- | -- | -- |
| [Activate](#activate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | X | -- | -- | -- |
| [Change](#change-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- |
| [Loaded](#loaded-rt-professional) | X | -- | -- | -- |
| [Execute](#execute-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | X |
| [Selection changed](#selection-changed-rt-professional) | -- | -- | -- | -- |
| [Double-click](#double-click-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- |
| [Press](#press-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- |
| [Operator input alarm property changed](#operator-input-alarm-property-changed-rt-professional) | -- | -- | -- | -- |
| [Block property changed](#block-property-changed-rt-professional) | -- | -- | -- | -- |
| [Property diagram changed](#property-diagram-changed-rt-professional) | -- | -- | -- | -- |
| [Property changed](#property-changed-rt-professional) | -- | -- | -- | -- |
| [Trend property changed](#trend-property-changed-rt-professional) | -- | -- | -- | -- |
| [Column property changed](#column-property-changed-rt-professional) | -- | -- | -- | -- |
| [Alarm statistics column property changed](#alarm-statistics-column-property-changed-rt-professional) | -- | -- | -- | -- |
| [Statistics area column name property changed](#statistics-area-column-name-property-changed-rt-professional) | -- | -- | -- | -- |
| [Change property status bar element](#change-property-status-bar-element-rt-professional) | -- | -- | -- | -- |
| [Change property toolbar button](#change-property-toolbar-button-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- |
| [Change property value axis](#change-property-value-axis-rt-professional) | -- | -- | -- | -- |
| [Change property value column](#change-property-value-column-rt-professional) | -- | -- | -- | -- |
| [X-axis property changed](#x-axis-property-changed-rt-professional) | -- | -- | -- | -- |
| [Y-axis property changed](#y-axis-property-changed-rt-professional) | -- | -- | -- | -- |
| [Change property time axis](#change-property-time-axis-rt-professional) | -- | -- | -- | -- |
| [Change property time column](#change-property-time-column-rt-professional) | -- | -- | -- | -- |
| [Error](#error-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- |
| [Outgoing](#outgoing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- |
| [Incoming](#incoming-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- |
| [In the alarm range](#in-the-alarm-range-rt-professional) | -- | -- | -- | -- |
| [In the tolerance range](#in-the-tolerance-range-rt-professional) | -- | -- | -- | -- |
| [In the warning range](#in-the-warning-range-rt-professional) | -- | -- | -- | -- |
| [Click](#click-basic-panels-panels-comfort-panels-rt-advanced) | X | -- | -- | -- |
| [Shortcut menu](#shortcut-menu-rt-professional) | -- | -- | -- | -- |
| [Volume](#volume-rt-professional) | -- | -- | -- | -- |
| [Change layout](#change-layout-rt-professional) | -- | -- | -- | -- |
| [Change ruler](#change-ruler-rt-professional) | -- | -- | -- | -- |
| [Press left mouse button](#press-left-mouse-button-rt-professional) | X | -- | -- | -- |
| [Release left mouse button](#release-left-mouse-button-rt-professional) | X | -- | -- | -- |
| [Loop-in alarm](#loop-in-alarm-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | X | -- | -- |
| [Release](#release-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- |
| [Move mouse](#move-mouse-rt-professional) | -- | -- | -- | -- |
| [Medium opened](#medium-opened-rt-professional) | -- | -- | -- | -- |
| [Medium closed](#medium-closed-rt-professional) | -- | -- | -- | -- |
| [Object changed](#object-changed-rt-professional) | X | -- | -- | -- |
| [Pause](#pause-rt-professional) | -- | -- | -- | -- |
| [Acknowledge](#acknowledge-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | X | X | -- | -- |
| [Press right mouse button](#press-right-mouse-button-rt-professional) | X | -- | -- | -- |
| [Release right mouse button](#release-right-mouse-button-rt-professional) | X | -- | -- | -- |
| [Runtime Stop](#runtime-stop-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- |
| [Click the Alarm view button](#click-the-alarm-view-button-rt-professional) | -- | -- | -- | -- |
| [Click the PLC code view button](#click-the-plc-code-view-button-rt-professional) | -- | -- | -- | -- |
| [Click toolbar button](#click-toolbar-button-rt-professional) | -- | -- | -- | -- |
| [Change slider](#change-slider-rt-professional) | -- | -- | -- | -- |
| [StepForward](#stepforward-rt-professional) | -- | -- | -- | -- |
| [StepBack](#stepback-rt-professional) | -- | -- | -- | -- |
| [Lock changed](#lock-changed-rt-professional) | -- | -- | X | -- |
| [Status changed](#status-changed-rt-professional) | -- | X | -- | -- |
| [Stop](#stop-rt-professional) | -- | -- | -- | -- |
| [Switch toolbar](#switch-toolbar-rt-professional) | -- | -- | -- | -- |
| [Press key on keyboard](#press-key-on-keyboard-rt-professional) | X | -- | -- | -- |
| [Release key on keyboard](#release-key-on-keyboard-rt-professional) | X | -- | -- | -- |
| [Change video format](#change-video-format-rt-professional) | -- | -- | -- | -- |
| [Full screen](#full-screen-rt-professional) | -- | -- | -- | -- |
| [Exit full screen](#exit-full-screen-rt-professional) | -- | -- | -- | -- |
| [Replay](#replay-rt-professional) | -- | -- | -- | -- |

### Basic objects (RT Professional)

#### Introduction

The following table shows which events occur on which objects.

Technical data subject to change.

| Icon | Object |
| --- | --- |
| ![Introduction](images/36121380619_DV_resource.Stream@PNG-de-DE.png) | Line |
| ![Introduction](images/36121426699_DV_resource.Stream@PNG-de-DE.png) | Polyline |
| ![Introduction](images/36121434379_DV_resource.Stream@PNG-de-DE.png) | Polygon |
| ![Introduction](images/36121388299_DV_resource.Stream@PNG-de-DE.png) | Ellipse |
| ![Introduction](images/36124419979_DV_resource.Stream@PNG-de-DE.png) | Ellipse segment |
| ![Introduction](images/36124427659_DV_resource.Stream@PNG-de-DE.png) | Circle segment |
| ![Introduction](images/36124435339_DV_resource.Stream@PNG-de-DE.png) | Ellipse arc |
| ![Introduction](images/36124443019_DV_resource.Stream@PNG-de-DE.png) | Circular arc |
| ![Introduction](images/36121395979_DV_resource.Stream@PNG-de-DE.png) | Circle |
| ![Introduction](images/36121403659_DV_resource.Stream@PNG-de-DE.png) | Rectangle |
| ![Introduction](images/36124450699_DV_resource.Stream@PNG-de-DE.png) | Connector |
| ![Introduction](images/36121411339_DV_resource.Stream@PNG-de-DE.png) | Text field |
| ![Introduction](images/36121419019_DV_resource.Stream@PNG-de-DE.png) | Graphic view |
| ![Introduction](images/36124458379_DV_resource.Stream@PNG-de-DE.png) | Pipe |
| ![Introduction](images/36124466059_DV_resource.Stream@PNG-de-DE.png) | Double T-piece |
| ![Introduction](images/36124473739_DV_resource.Stream@PNG-de-DE.png) | T piece |
| ![Introduction](images/36124481419_DV_resource.Stream@PNG-de-DE.png) | Pipe bends |

|  | ![Introduction](images/36121380619_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121426699_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121434379_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121388299_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124419979_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124427659_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124435339_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124443019_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121395979_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121403659_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124450699_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121411339_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121419019_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124458379_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124466059_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124473739_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124481419_DV_resource.Stream@PNG-de-DE.png) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Play ended](#play-ended-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Activate](#activate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X |
| [Change](#change-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Loaded](#loaded-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Execute](#execute-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Selection changed](#selection-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Double-click](#double-click-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press](#press-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Operator input alarm property changed](#operator-input-alarm-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Block property changed](#block-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Property diagram changed](#property-diagram-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Property changed](#property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Trend property changed](#trend-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Column property changed](#column-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Alarm statistics column property changed](#alarm-statistics-column-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Statistics area column name property changed](#statistics-area-column-name-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change property status bar element](#change-property-status-bar-element-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change property toolbar button](#change-property-toolbar-button-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change property value axis](#change-property-value-axis-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change property value column](#change-property-value-column-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [X-axis property changed](#x-axis-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Y-axis property changed](#y-axis-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change property time axis](#change-property-time-axis-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change property time column](#change-property-time-column-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Error](#error-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Outgoing](#outgoing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Incoming](#incoming-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [In the alarm range](#in-the-alarm-range-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [In the tolerance range](#in-the-tolerance-range-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [In the warning range](#in-the-warning-range-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Click](#click-basic-panels-panels-comfort-panels-rt-advanced) | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X |
| [Shortcut menu](#shortcut-menu-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Volume](#volume-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change layout](#change-layout-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change ruler](#change-ruler-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press left mouse button](#press-left-mouse-button-rt-professional) | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X |
| [Release left mouse button](#release-left-mouse-button-rt-professional) | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X |
| [Loop-in alarm](#loop-in-alarm-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Release](#release-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Move mouse](#move-mouse-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Medium opened](#medium-opened-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Medium closed](#medium-closed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Object changed](#object-changed-rt-professional) | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X |
| [Pause](#pause-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Acknowledge](#acknowledge-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press right mouse button](#press-right-mouse-button-rt-professional) | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X |
| [Release right mouse button](#release-right-mouse-button-rt-professional) | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X |
| [Runtime Stop](#runtime-stop-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Click the Alarm view button](#click-the-alarm-view-button-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Click the PLC code view button](#click-the-plc-code-view-button-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Click toolbar button](#click-toolbar-button-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change slider](#change-slider-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [StepForward](#stepforward-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [StepBack](#stepback-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Lock changed](#lock-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Status changed](#status-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Stop](#stop-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Switch toolbar](#switch-toolbar-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press key on keyboard](#press-key-on-keyboard-rt-professional) | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X |
| [Release key on keyboard](#release-key-on-keyboard-rt-professional) | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X |
| [Full screen](#full-screen-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Exit full screen](#exit-full-screen-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change video format](#change-video-format-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Replay](#replay-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |

### Elements (RT Professional)

#### Introduction

The following table shows which events occur on which elements.

Technical data subject to change.

| Icon | Object |
| --- | --- |
| ![Introduction](images/70601080075_DV_resource.Stream@PNG-de-DE.png) | IO field |
| ![Introduction](images/36124604811_DV_resource.Stream@PNG-de-DE.png) | Editable text field |
| ![Introduction](images/36124612491_DV_resource.Stream@PNG-de-DE.png) | List box |
| ![Introduction](images/96375319691_DV_resource.Stream@PNG-de-DE.png) | Combo box |
| ![Introduction](images/36121489931_DV_resource.Stream@PNG-de-DE.png) | Button |
| ![Introduction](images/36124574091_DV_resource.Stream@PNG-de-DE.png) | Round button |
| ![Introduction](images/36124627851_DV_resource.Stream@PNG-de-DE.png) | Symbolic IO field |
| ![Introduction](images/70601198091_DV_resource.Stream@PNG-de-DE.png) | Graphic IO field |
| ![Introduction](images/70601341707_DV_resource.Stream@PNG-de-DE.png) | Bar |
| ![Introduction](images/36121548811_DV_resource.Stream@PNG-de-DE.png) | Symbol library |
| ![Introduction](images/36121556491_DV_resource.Stream@PNG-de-DE.png) | Slider |
| ![Introduction](images/36124581771_DV_resource.Stream@PNG-de-DE.png) | Scroll bar |
| ![Introduction](images/36124589451_DV_resource.Stream@PNG-de-DE.png) | Check box |
| ![Introduction](images/36124597131_DV_resource.Stream@PNG-de-DE.png) | Option button |
| ![Introduction](images/36121564171_DV_resource.Stream@PNG-de-DE.png) | Gauge |
| ![Introduction](images/36121571851_DV_resource.Stream@PNG-de-DE.png) | Clock |
| ![Introduction](images/36124620171_DV_resource.Stream@PNG-de-DE.png) | Disk space view |

|  | ![Introduction](images/70601080075_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124604811_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124612491_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/96375319691_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121489931_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124574091_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124627851_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/70601198091_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/70601341707_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121548811_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121556491_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124581771_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124589451_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124597131_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121564171_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121571851_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124620171_DV_resource.Stream@PNG-de-DE.png) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Play ended](#play-ended-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Activate](#activate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X |
| [Change](#change-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | X | -- | -- |
| [Loaded](#loaded-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Execute](#execute-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Selection changed](#selection-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Double-click](#double-click-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- |
| [Press](#press-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- |
| [Operator input alarm property changed](#operator-input-alarm-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Block property changed](#block-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Property diagram changed](#property-diagram-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Property changed](#property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Trend property changed](#trend-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Column property changed](#column-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Alarm statistics column property changed](#alarm-statistics-column-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Statistics area column name property changed](#statistics-area-column-name-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change property status bar element](#change-property-status-bar-element-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change property toolbar button](#change-property-toolbar-button-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change property value axis](#change-property-value-axis-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change property value column](#change-property-value-column-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [X-axis property changed](#x-axis-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Y-axis property changed](#y-axis-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change property time axis](#change-property-time-axis-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change property time column](#change-property-time-column-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Error](#error-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Outgoing](#outgoing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Incoming](#incoming-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [In the alarm range](#in-the-alarm-range-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X |
| [In the tolerance range](#in-the-tolerance-range-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X |
| [In the warning range](#in-the-warning-range-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X |
| [Click](#click-basic-panels-panels-comfort-panels-rt-advanced) | X | X | X | X | X | X | X | X | X | X | -- | X | X | X | -- | -- | -- |
| [Shortcut menu](#shortcut-menu-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Volume](#volume-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change layout](#change-layout-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change ruler](#change-ruler-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press left mouse button](#press-left-mouse-button-rt-professional) | X | X | X | X | X | X | X | X | X | -- | -- | X | X | X | -- | -- | -- |
| [Release left mouse button](#release-left-mouse-button-rt-professional) | X | X | X | X | X | X | X | X | X | -- | -- | X | X | X | -- | -- | -- |
| [Loop-in alarm](#loop-in-alarm-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Release](#release-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- |
| [Move mouse](#move-mouse-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- |
| [Medium opened](#medium-opened-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Medium closed](#medium-closed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Object changed](#object-changed-rt-professional) | X | X | X | X | X | X | X | X | X | -- | -- | X | X | X | -- | -- | -- |
| [Pause](#pause-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Acknowledge](#acknowledge-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press right mouse button](#press-right-mouse-button-rt-professional) | X | X | X | X | X | X | X | X | X | -- | -- | X | X | X | -- | -- | -- |
| [Release right mouse button](#release-right-mouse-button-rt-professional) | X | X | X | X | X | X | X | X | X | -- | -- | X | X | X | -- | -- | -- |
| [Runtime Stop](#runtime-stop-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Click the Alarm view button](#click-the-alarm-view-button-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Click the PLC code view button](#click-the-plc-code-view-button-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Click toolbar button](#click-toolbar-button-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change slider](#change-slider-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [StepForward](#stepforward-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [StepBack](#stepback-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Lock changed](#lock-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Status changed](#status-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Stop](#stop-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Switch toolbar](#switch-toolbar-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press key on keyboard](#press-key-on-keyboard-rt-professional) | X | X | X | X | X | X | X | X | X | -- | -- | X | X | X | -- | -- | -- |
| [Release key on keyboard](#release-key-on-keyboard-rt-professional) | X | X | X | X | X | X | X | X | X | -- | -- | X | X | X | -- | -- | -- |
| [Change video format](#change-video-format-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Full screen](#full-screen-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Exit full screen](#exit-full-screen-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Replay](#replay-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |

### Controls (RT Professional)

#### Introduction

The following table shows which events occur on which controls.

Technical data subject to change.

| Icon | Object |
| --- | --- |
| ![Introduction](images/36124705163_DV_resource.Stream@PNG-de-DE.png) | Screen window |
| ![Introduction](images/103788230027_DV_resource.Stream@PNG-de-DE.png) | User view |
| ![Introduction](images/72311964939_DV_resource.Stream@PNG-de-DE.png) | HTML browser |
| ![Introduction](images/36124751243_DV_resource.Stream@PNG-de-DE.png) | Print job/Script diagnostics |
| ![Introduction](images/36124728203_DV_resource.Stream@PNG-de-DE.png) | Recipe view |
| ![Introduction](images/103788221963_DV_resource.Stream@PNG-de-DE.png) | Alarm view |
| ![Introduction](images/36121681803_DV_resource.Stream@PNG-de-DE.png) | f(x) trend view |
| ![Introduction](images/36121627403_DV_resource.Stream@PNG-de-DE.png) | f(t) trend view |
| ![Introduction](images/36124712843_DV_resource.Stream@PNG-de-DE.png) | Table view |
| ![Introduction](images/103751439627_DV_resource.Stream@PNG-de-DE.png) | Value table |
| ![Introduction](images/103751435275_DV_resource.Stream@PNG-de-DE.png) | System diagnostics view |
| ![Introduction](images/36124743563_DV_resource.Stream@PNG-de-DE.png) | Media Player |
| ![Introduction](images/36124735883_DV_resource.Stream@PNG-de-DE.png) | Channel diagnostics display |
| ![Introduction](images/83769634187_DV_resource.Stream@PNG-de-DE.png) | PLC Code View |
| ![Introduction](images/103748823819_DV_resource.Stream@PNG-de-DE.png) | GRAPH overview |
| ![Introduction](images/103748832523_DV_resource.Stream@PNG-de-DE.png) | ProDiag overview |
| ![Introduction](images/103748828171_DV_resource.Stream@PNG-de-DE.png) | Criteria analysis view |

|  | ![Introduction](images/36124705163_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/103788230027_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/72311964939_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124751243_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124728203_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/103788221963_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121681803_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36121627403_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124712843_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/103751439627_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/103751435275_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124743563_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/36124735883_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/83769634187_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/103748823819_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/103748832523_DV_resource.Stream@PNG-de-DE.png) | ![Introduction](images/103748828171_DV_resource.Stream@PNG-de-DE.png) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Play ended](#play-ended-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |
| [Activate](#activate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X | X |
| [Change](#change-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Loaded](#loaded-rt-professional) | -- | -- | -- | -- | X | X | X | X | X | X | -- | -- | -- | -- | -- | -- | -- |
| [Execute](#execute-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Selection changed](#selection-changed-rt-professional) | -- | -- | -- | -- | X | X | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Double-click](#double-click-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press](#press-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Operator input alarm property changed](#operator-input-alarm-property-changed-rt-professional) | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Block property changed](#block-property-changed-rt-professional) | -- | -- | -- | -- | -- | X | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- |
| [Property diagram changed](#property-diagram-changed-rt-professional) | -- | -- | -- | -- | -- | -- | X | X | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Property changed](#property-changed-rt-professional) | -- | -- | -- | -- | X | X | X | X | X | X | -- | -- | -- | -- | -- | -- | -- |
| [Trend property changed](#trend-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | X | X | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Column property changed](#column-property-changed-rt-professional) | -- | -- | -- | -- | X | X | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- |
| [Alarm statistics column property changed](#alarm-statistics-column-property-changed-rt-professional) | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Statistics area column name property changed](#statistics-area-column-name-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- |
| [Change property status bar element](#change-property-status-bar-element-rt-professional) | -- | -- | -- | -- | X | X | X | X | X | X | -- | -- | -- | -- | -- | -- | -- |
| [Change property toolbar button](#change-property-toolbar-button-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | X | X | X | X | X | X | -- | -- | -- | -- | -- | -- | -- |
| [Change property value axis](#change-property-value-axis-rt-professional) | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change property value column](#change-property-value-column-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- | -- |
| [X-axis property changed](#x-axis-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Y-axis property changed](#y-axis-property-changed-rt-professional) | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change property time axis](#change-property-time-axis-rt-professional) | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change property time column](#change-property-time-column-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- | -- |
| [Error](#error-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | X | X |
| [Outgoing](#outgoing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Incoming](#incoming-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [In the alarm range](#in-the-alarm-range-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [In the tolerance range](#in-the-tolerance-range-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [In the warning range](#in-the-warning-range-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Click](#click-basic-panels-panels-comfort-panels-rt-advanced) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- |
| [Shortcut menu](#shortcut-menu-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |
| [Volume](#volume-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |
| [Change layout](#change-layout-rt-professional) | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change ruler](#change-ruler-rt-professional) | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press left mouse button](#press-left-mouse-button-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Release left mouse button](#release-left-mouse-button-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Loop-in alarm](#loop-in-alarm-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Release](#release-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Move mouse](#move-mouse-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Medium opened](#medium-opened-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |
| [Medium closed](#medium-closed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |
| [Object changed](#object-changed-rt-professional) | X | -- | -- | X | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Pause](#pause-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |
| [Acknowledge](#acknowledge-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Press right mouse button](#press-right-mouse-button-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Release right mouse button](#release-right-mouse-button-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Runtime Stop](#runtime-stop-basic-panels-panels-comfort-panels-rt-advanced-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Click the Alarm view button](#click-the-alarm-view-button-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | X | -- |
| [Click the PLC code view button](#click-the-plc-code-view-button-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- |
| [Click toolbar button](#click-toolbar-button-rt-professional) | -- | -- | -- | -- | X | X | X | X | X | X | -- | -- | -- | -- | -- | -- | -- |
| [Change slider](#change-slider-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |
| [StepForward](#stepforward-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |
| [StepBack](#stepback-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |
| [Lock changed](#lock-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Status changed](#status-changed-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Stop](#stop-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |
| [Switch toolbar](#switch-toolbar-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |
| [Press key on keyboard](#press-key-on-keyboard-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Release key on keyboard](#release-key-on-keyboard-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| [Change video format](#change-video-format-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |
| [Full screen](#full-screen-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |
| [Exit full screen](#exit-full-screen-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |
| [Replay](#replay-rt-professional) | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | X | -- | -- | -- | -- | -- |

## Events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Cleared (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#cleared-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Play ended (RT Professional)](#play-ended-rt-professional)
- [Activate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#activate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Change (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#change-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Loaded (RT Professional)](#loaded-rt-professional)
- [Execute (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#execute-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Selection changed (RT Professional)](#selection-changed-rt-professional)
- [On exceeding (Basic Panels, Panels, Comfort Panels, RT Advanced)](#on-exceeding-basic-panels-panels-comfort-panels-rt-advanced)
- [On falling below (Basic Panels, Panels, Comfort Panels, RT Advanced)](#on-falling-below-basic-panels-panels-comfort-panels-rt-advanced)
- [When dialog is opened (Basic Panels, Panels, Comfort Panels, RT Advanced)](#when-dialog-is-opened-basic-panels-panels-comfort-panels-rt-advanced)
- [When dialog is closed (Basic Panels, Panels, Comfort Panels, RT Advanced)](#when-dialog-is-closed-basic-panels-panels-comfort-panels-rt-advanced)
- [User change (Basic Panels, Panels, Comfort Panels, RT Advanced)](#user-change-basic-panels-panels-comfort-panels-rt-advanced)
- [Screen change (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-change-basic-panels-panels-comfort-panels-rt-advanced)
- [Deactivate (Basic Panels, Panels, Comfort Panels, RT Advanced)](#deactivate-basic-panels-panels-comfort-panels-rt-advanced)
- [Double-click (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#double-click-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Press (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#press-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Operator input alarm property changed (RT Professional)](#operator-input-alarm-property-changed-rt-professional)
- [Block property changed (RT Professional)](#block-property-changed-rt-professional)
- [Property diagram changed (RT Professional)](#property-diagram-changed-rt-professional)
- [Property changed (RT Professional)](#property-changed-rt-professional)
- [Trend property changed (RT Professional)](#trend-property-changed-rt-professional)
- [Column property changed (RT Professional)](#column-property-changed-rt-professional)
- [Alarm statistics column property changed (RT Professional)](#alarm-statistics-column-property-changed-rt-professional)
- [Statistics area column name property changed (RT Professional)](#statistics-area-column-name-property-changed-rt-professional)
- [Change property status bar element (RT Professional)](#change-property-status-bar-element-rt-professional)
- [Change property toolbar button (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#change-property-toolbar-button-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Change property value axis (RT Professional)](#change-property-value-axis-rt-professional)
- [Change property value column (RT Professional)](#change-property-value-column-rt-professional)
- [X-axis property changed (RT Professional)](#x-axis-property-changed-rt-professional)
- [Y-axis property changed (RT Professional)](#y-axis-property-changed-rt-professional)
- [Change property time axis (RT Professional)](#change-property-time-axis-rt-professional)
- [Change property time column (RT Professional)](#change-property-time-column-rt-professional)
- [On Finish Input (Basic Panels, Panels, Comfort Panels, RT Advanced)](#on-finish-input-basic-panels-panels-comfort-panels-rt-advanced)
- [Press ESC twice (Basic Panels, Panels, Comfort Panels, RT Advanced)](#press-esc-twice-basic-panels-panels-comfort-panels-rt-advanced)
- [Error (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#error-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Outgoing (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#outgoing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Incoming (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#incoming-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [In the alarm range (RT Professional)](#in-the-alarm-range-rt-professional)
- [In the tolerance range (RT Professional)](#in-the-tolerance-range-rt-professional)
- [In the warning range (RT Professional)](#in-the-warning-range-rt-professional)
- [Click (Basic Panels, Panels, Comfort Panels, RT Advanced)](#click-basic-panels-panels-comfort-panels-rt-advanced)
- [Click when flashing (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#click-when-flashing-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Shortcut menu (RT Professional)](#shortcut-menu-rt-professional)
- [Volume (RT Professional)](#volume-rt-professional)
- [Change layout (RT Professional)](#change-layout-rt-professional)
- [Change ruler (RT Professional)](#change-ruler-rt-professional)
- [Press left mouse button (RT Professional)](#press-left-mouse-button-rt-professional)
- [Release left mouse button (RT Professional)](#release-left-mouse-button-rt-professional)
- [Loop-in alarm (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#loop-in-alarm-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Release (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#release-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Alarm buffer overflow (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-buffer-overflow-basic-panels-panels-comfort-panels-rt-advanced)
- [Move mouse (RT Professional)](#move-mouse-rt-professional)
- [Medium opened (RT Professional)](#medium-opened-rt-professional)
- [Medium closed (RT Professional)](#medium-closed-rt-professional)
- [Object changed (RT Professional)](#object-changed-rt-professional)
- [Pause (RT Professional)](#pause-rt-professional)
- [Acknowledge (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#acknowledge-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Reach margin (Basic Panels, Panels, Comfort Panels, RT Advanced)](#reach-margin-basic-panels-panels-comfort-panels-rt-advanced)
- [Press right mouse button (RT Professional)](#press-right-mouse-button-rt-professional)
- [Release right mouse button (RT Professional)](#release-right-mouse-button-rt-professional)
- [Runtime Stop (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#runtime-stop-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Click the Alarm view button (RT Professional)](#click-the-alarm-view-button-rt-professional)
- [Click the PLC code view button (RT Professional)](#click-the-plc-code-view-button-rt-professional)
- [Click toolbar button (RT Professional)](#click-toolbar-button-rt-professional)
- [Change slider (RT Professional)](#change-slider-rt-professional)
- [StepForward (RT Professional)](#stepforward-rt-professional)
- [StepBack (RT Professional)](#stepback-rt-professional)
- [Lock changed (RT Professional)](#lock-changed-rt-professional)
- [Status changed (RT Professional)](#status-changed-rt-professional)
- [Stop (RT Professional)](#stop-rt-professional)
- [Switch toolbar (RT Professional)](#switch-toolbar-rt-professional)
- [Press key (Basic Panels, Panels, Comfort Panels, RT Advanced)](#press-key-basic-panels-panels-comfort-panels-rt-advanced)
- [Release key (Basic Panels, Panels, Comfort Panels, RT Advanced)](#release-key-basic-panels-panels-comfort-panels-rt-advanced)
- [Press key on keyboard (RT Professional)](#press-key-on-keyboard-rt-professional)
- [Release key on keyboard (RT Professional)](#release-key-on-keyboard-rt-professional)
- [Overflow (Basic Panels, Panels, Comfort Panels, RT Advanced)](#overflow-basic-panels-panels-comfort-panels-rt-advanced)
- [Switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Switch OFF (Basic Panels, Panels, Comfort Panels, RT Advanced)](#switch-off-basic-panels-panels-comfort-panels-rt-advanced)
- [Switch ON (Basic Panels, Panels, Comfort Panels, RT Advanced)](#switch-on-basic-panels-panels-comfort-panels-rt-advanced)
- [Connected (RT Professional)](#connected-rt-professional)
- [Change video format (RT Professional)](#change-video-format-rt-professional)
- [Full screen (RT Professional)](#full-screen-rt-professional)
- [Exit full screen (RT Professional)](#exit-full-screen-rt-professional)
- [Low free storage space (Basic Panels, Panels, Comfort Panels, RT Advanced)](#low-free-storage-space-basic-panels-panels-comfort-panels-rt-advanced)
- [Free space critically low (Basic Panels, Panels, Comfort Panels, RT Advanced)](#free-space-critically-low-basic-panels-panels-comfort-panels-rt-advanced)
- [Value change (Basic Panels, Panels, Comfort Panels, RT Advanced)](#value-change-basic-panels-panels-comfort-panels-rt-advanced)
- [Replay (RT Professional)](#replay-rt-professional)
- [Time expired (Basic Panels, Panels, Comfort Panels, RT Advanced)](#time-expired-basic-panels-panels-comfort-panels-rt-advanced)

### Cleared (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

Occurs when the active screen on the HMI device is cleared.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Play ended (RT Professional)

#### Description

Occurs when the video or audio file has been played.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Elements (RT Professional)](#elements-rt-professional)

### Activate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

Occurs when the user selects a display or operating object using the configured tab sequence.

If the user e.g. clicks a button with the mouse, the "Click" event is triggered. Users wishing to trigger the "Enable" event must select the button using the tab key.

The "Enable" event is only used to detect whether an object was selected. The event does not trigger a password prompt. For this reason, do not use the "Enable" event if you want to configure access protection on the function call of the object.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Change (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

Occurs if the status of a display and operator control object changes.

The status of an object changes if, for example, the user presses the key.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### Loaded (RT Professional)

#### Description

Occurs if a display or operating object is completely loaded in Runtime.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### Execute (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

Occurs when the scheduled task has been executed.

### Selection changed (RT Professional)

#### Description

Occurs when the selection is changed.

### On exceeding (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs when the high limit of a tag is exceeded.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### On falling below (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs when the low limit of a tag is undershot.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### When dialog is opened (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

The event is triggered when a modal dialog opens.

> **Note**
>
> Please note that the availability of the event depends on the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### When dialog is closed (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

The event is triggered when a modal dialog closes.

> **Note**
>
> Please note that the availability of the event depends on the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### User change (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs when a user logs off at an HMI device or another user logs on at the HMI device.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Screen change (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs when all configured display and operating objects are loaded in the screen after a screen change.

Use the "Loaded" event if you want to perform other system functions during a screen change to a certain screen.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Deactivate (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs when the user takes the focus from a display and operating object. A screen object can be deactivated by using the configured tab sequence or by performing another action with the mouse. System functions or user-defined functions on the "Deactivate" event of a screen are not executed when a screen is being closed.

The "Deactivate" event is only used to detect whether an object was deselected. The event does not trigger a password prompt. For this reason, do not use the "Deactivate" event if you want to configure access protection on the function call of the object.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Double-click (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

Occurs when the user double-clicks on an object from the symbol library.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Press (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

Occurs when the user clicks on a button with the left mouse button, presses <RETURN> or <SPACE>.

Also occurs when the user right-clicks on an object of the symbol library.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Operator input alarm property changed (RT Professional)

#### Description

Occurs when the property of an operator input alarm is changed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Block property changed (RT Professional)

#### Description

Occurs when the property of a block, e.g., alarm text block, is changed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Property diagram changed (RT Professional)

#### Description

Occurs when the property of a trend diagram is changed.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### Property changed (RT Professional)

#### Description

Occurs when a property is changed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Trend property changed (RT Professional)

#### Description

Occurs when the property of the trend is changed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Column property changed (RT Professional)

#### Description

Occurs when the property of a column is changed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Alarm statistics column property changed (RT Professional)

#### Description

Occurs when the property of the alarm statistics column is changed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Statistics area column name property changed (RT Professional)

#### Description

Occurs when the column name of the statistics area is changed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Change property status bar element (RT Professional)

#### Description

Occurs when the property of a status bar element is changed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Change property toolbar button (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

Occurs when the property of a toolbar button is changed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Change property value axis (RT Professional)

#### Description

Occurs when the property of the time axis changes.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Change property value column (RT Professional)

#### Description

Occurs when the property of the value column is changed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### X-axis property changed (RT Professional)

#### Description

Occurs when the property of the X-axis is changed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Y-axis property changed (RT Professional)

#### Description

Occurs when the property of the Y-axis is changed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Change property time axis (RT Professional)

#### Description

Occurs when the property of the time axis changes.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Change property time column (RT Professional)

#### Description

Occurs when the property of the time column is changed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### On Finish Input (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Triggered when you confirm input at an I/O field by pressing ENTER, or by mouse click, or by touch screen operation.

The "On Finish Input" event is also started if the value of a tag does not change, for example, if a value is exceeded, or if a user cancels the dialog to acknowledge a tag (Audit option package) that has to be acknowledged.

The event is not triggered, on the other hand, by user logon or by input fields configured with an authorization.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Press ESC twice (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs when the user presses the <ESC> key twice at the HMI device.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Error (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

Occurs in the event of an error when configuring the view of a program network in the PLC Code View.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### Outgoing (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

Occurs when an alarm is deactivated.

> **Note**
>
> Please note that the availability of the event depends on the HMI device and object type.

### Incoming (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

Occurs when an alarm is triggered and displayed in the alarm view.

> **Note**
>
> Please note that the availability of the event depends on the HMI device and object type.

### In the alarm range (RT Professional)

#### Description

Occurs if the available storage space has reached the configured monitoring limit "alarm". You configure this event in the display and operating object "storage space display".

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### In the tolerance range (RT Professional)

#### Description

Occurs if the available storage space has reached the configured monitoring limit "tolerance". You configure this event in the display and operating object "storage space display".

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### In the warning range (RT Professional)

#### Description

Occurs if the available storage space has reached the configured monitoring limit "warning". You configure this event in the display and operating object "storage space display".

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### Click (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs if the user clicks a display and operating object with the mouse or touches the touch display with a finger.

In case you click the incorrect object, prevent processing of configured function list as follows:

- Move the mouse pointer away from the object while keeping the mouse button pressed. Release the mouse button as soon as the mouse pointer leaves the object. The function list will then not be processed.
- On touch displays, the display must be touched with the finger until a reaction occurs, e.g., a screen change.

  > **Note**
  >
  > Please note that the availability of the event is dependent upon the HMI device and object type.

### Click when flashing (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

Occurs when the user clicks a flashing alarm indicator with the mouse or touches it with a finger.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Shortcut menu (RT Professional)

#### Description

Ocurs when the shortcut menu opens.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Elements (RT Professional)](#elements-rt-professional)

### Volume (RT Professional)

#### Description

Occurs when the volume changes.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Elements (RT Professional)](#elements-rt-professional)

### Change layout (RT Professional)

#### Description

Activated when a property is changed.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### Change ruler (RT Professional)

#### Description

Activated when a property is changed.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### Press left mouse button (RT Professional)

#### Description

Occurs when the operator left-clicks on a display and operating object.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### Release left mouse button (RT Professional)

#### Description

Occurs when the user releases the left mouse button after clicking.

This event does not occur as long as the left button remains pressed.

If the operator releases the button after clicking on a button, this event will also occur even if the mouse pointer is no longer pointing on the button.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### Loop-in alarm (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

The "Loop-In-Alarm" event occurs when the user selects an alarm in the alarm view and clicks on the "Loop-In-Alarm" button or double-clicks on the alarm.

The "Loop-In-Alarm" event is configurable for discrete alarms and for analog alarms. A system function can be configured at the "Loop-In-Alarm" event, for example, switching to a screen in which you provide more information on the alarm that occurred. If a function is configured for the Loop-in-Alarm event and the selected alarm requires acknowledgment, then this alarm is also acknowledged the first time the event occurs.

If no Loop-In-Alarm is configured for the selected alarm, pressing the "Loop-In-Alarm" button has no effect.

You cannot configure local scripts for the "Loop-In-Alarm" event in Runtime Professional.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Release (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

Occurs when the user releases a button.

This even does not occur, as long as the button remains pressed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Alarm buffer overflow (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs when the configured size of the alarm buffer is reached.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Move mouse (RT Professional)

#### Description

Occurs when the user moves the mouse.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### Medium opened (RT Professional)

#### Description

Occurs when the medium is opened.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Elements (RT Professional)](#elements-rt-professional)

### Medium closed (RT Professional)

#### Description

Occurs when the medium is closed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Elements (RT Professional)](#elements-rt-professional)

### Object changed (RT Professional)

#### Description

Occurs if the user changes a property of a display and operating object in Runtime.

> **Note**
>
> Every action triggered by this event is logged on individually and then logged off again when the screen is changed. This behavior puts a burden on the working memory. Use this event only for important changes to properties, e.g., for an I/O field.

> **Note**
>
> The availability of the event is dependent on the HMI device and object type.

### Pause (RT Professional)

#### Description

Occurs when playing of the video or audio file is paused.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Elements (RT Professional)](#elements-rt-professional)

### Acknowledge (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

Occurs when the user acknowledges an alarm.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Reach margin (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs when the user reaches the beginning or the end of a scrollable area.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

> **Note**
>
> A user-defined function must not be configured for the "Boundary reached" event.

#### Configurable objects

The event can only be configured on the <Up> and <Down> keys, or on the keys on which you have configured the "ScreenObjectPageUp" or "ScreenObjectPageDown" system functions.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Press right mouse button (RT Professional)

#### Description

Occurs when the user right-clicks on a display and operating object.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Release right mouse button (RT Professional)

#### Description

Occurs when the user releases the right mouse button after clicking.

This event does not occur as long as the right mouse button remains pressed.

If the operator releases the button after clicking on a button, this event will also occur even if the mouse pointer is no longer pointing on the button.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### Runtime Stop (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

Occurs when the user exits the Runtime software on the HMI device. Since the functions configured at the event are executed when Runtime is being deactivated, not all functionalities can be executed during this period. The server applications are no longer active while Runtime is being terminated. Therefore, you do not have access to tags, alarms and logs, for example.

A user-defined function must not be configured for the "Runtime stop" event.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Click the Alarm view button (RT Professional)

#### Description

Occurs when the user clicks the "Alarm View" button.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### Click the PLC code view button (RT Professional)

#### Description

Occurs when the user clicks the "PLC Code View" button.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### Click toolbar button (RT Professional)

#### Description

Occurs when the user clicks a button in the toolbar.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Change slider (RT Professional)

#### Description

Occurs when the volume slider changes.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Elements (RT Professional)](#elements-rt-professional)

### StepForward (RT Professional)

#### Description

Occurs when the video or audio file goes to the next sequence.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

---

**See also**

[Elements (RT Professional)](#elements-rt-professional)

### StepBack (RT Professional)

#### Description

Occurs when the video or audio file goes to the previous sequence.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Elements (RT Professional)](#elements-rt-professional)

### Lock changed (RT Professional)

#### Description

Occurs when the write access for the log is changed, e.g., from locked to released.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Status changed (RT Professional)

#### Description

Occurs when the status of an alarm is changed, e.g., from incoming to outgoing.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

### Stop (RT Professional)

#### Description

Occurs when playing of the video or audio file is stopped.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

---

**See also**

[Elements (RT Professional)](#elements-rt-professional)

### Switch toolbar (RT Professional)

#### Description

Occurs when the property of the time axis changes.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

---

**See also**

[Elements (RT Professional)](#elements-rt-professional)

### Press key (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs when the user presses a function key.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Release key (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs when the user releases a function key.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Press key on keyboard (RT Professional)

#### Description

Occurs when the user presses a key on the keyboard.

The keys <F10> and <ALT+PRINT> are not used by the operator for process operations.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### Release key on keyboard (RT Professional)

#### Description

Occurs when the user releases a key on the keyboard.

The keys <F10> and <ALT+PRINT> are not used by the operator for process operations.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

### Overflow (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs when the configured size of the log is reached. You use the log type "Trigger event".

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Description

Occurs when the user toggles a display and operating object, e.g. a switch from "ON" to "OFF".

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Switch OFF (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs when the user moves the display and operating object "Switch" to the OFF position.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Switch ON (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs when the user moves the display and operating object "Switch" to the ON position.

> **Note**
>
> Note that the availability of the event depends on the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Connected (RT Professional)

#### Description

Occurs when the user of a Mobile Panel connects to a connection box.

> **Note**
>
> Please note that the availability of the event depends on the HMI device.

### Change video format (RT Professional)

#### Description

Occurs when the video format changes.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Elements (RT Professional)](#elements-rt-professional)

### Full screen (RT Professional)

#### Description

Occurs when the full screen mode is activated.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Elements (RT Professional)](#elements-rt-professional)

### Exit full screen (RT Professional)

#### Description

Occurs when the full screen mode is exited.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Elements (RT Professional)](#elements-rt-professional)

### Low free storage space (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

This event is triggered if the storage space available on the medium to which the Audit Trail is less than the configured minimum.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Free space critically low (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

This event is triggered if the storage medium to which an Audit Trail is saved provides insufficient storage space due to hardware restrictions.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Value change (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs when the value of a tag or the value of an array element changes.

The value change of a tag is triggered by the PLC or by the user, e.g. when a new value is entered. No event is output if a system function changes the value.

> **Note**
>
> Please note that the availability of the event depends on the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)

### Replay (RT Professional)

#### Description

Occurs when the video or audio file has been replayed.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Elements (RT Professional)](#elements-rt-professional)

### Time expired (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Description

Occurs when the time configured in the scheduler expires.

> **Note**
>
> Please note that the availability of the event is dependent upon the HMI device and object type.

---

**See also**

[Editors (Panels, Comfort Panels, RT Advanced)](#editors-panels-comfort-panels-rt-advanced)
  
[Basic objects (Panels, Comfort Panels, RT Advanced)](#basic-objects-panels-comfort-panels-rt-advanced)
  
[Elements (Panels, Comfort Panels, RT Advanced)](#elements-panels-comfort-panels-rt-advanced)
  
[Controls (Panels, Comfort Panels, RT Advanced)](#controls-panels-comfort-panels-rt-advanced)
