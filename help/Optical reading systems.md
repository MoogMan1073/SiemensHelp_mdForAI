---
title: "Optical reading systems"
package: SimIdentMVenUS
topics: 8
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Optical reading systems

This section contains information on the following topics:

- [MV400 optical reader](#mv400-optical-reader)
- [MV500 optical reader](#mv500-optical-reader)

## MV400 optical reader

This section contains information on the following topics:

- [MV400 optical reader](#mv400-optical-reader-1)
- ["Operating mode" parameter group](#operating-mode-parameter-group)

### MV400 optical reader

The MV400 optical readers are specifically designed for the recognition and processing of numerous machine-readable codes, plain text as well as objects in industrial production.

The readers can be operated both in the controllers S7-300, S7-400, S7-1200 and S7-1500 as well as with various third-party controllers. The connection to the controller is via PROFINET IO (FB79/Ident profile), TCP, RS-232 or via communications modules.

The function blocks FB79 and the Ident profile allow simple programming using the SIMATIC S7 tools.

### "Operating mode" parameter group

In this parameter group, you can configure the mode of the MV400 optical readers.

Parameters in the "Operating mode" parameter group

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| Function block | FB79  Ident profile | FB79 | With this parameter, you select the block:   - FB79   Configuration of the optical reader with help of the "FB79" block.   Compatible with the "VS130-2" reader; Compatible controllers: S7-300 and S7-400 - Ident profile    Configuration of the optical reader with help of the Ident blocks.   Compatible with all Ident devices; Compatible controllers: S7-300, S7-400, S7-1200 and S7-1500 |

## MV500 optical reader

This section contains information on the following topics:

- [MV500 optical reader](#mv500-optical-reader-1)
- ["Operating mode" parameter group](#operating-mode-parameter-group-1)
- ["Web Based Management" parameter group](#web-based-management-parameter-group)

### MV500 optical reader

The MV500 optical readers are specifically designed for the recognition and processing of numerous machine-readable codes, plain text as well as objects in industrial production.

The readers can be operated both in the controllers S7-300, S7-400, S7-1200 and S7-1500 as well as with various third-party controllers. The connection to the controller is via PROFINET IO (FB79/Ident profile), TCP, RS-232 or via communications modules.

The function blocks FB79 and the Ident profile allow simple programming using the SIMATIC S7 tools.

### "Operating mode" parameter group

In this parameter group, you can configure the mode of the MV500 optical readers.

Parameters in the "Operating mode" parameter group

| Parameter | Parameter value | Default value | Description |
| --- | --- | --- | --- |
| Function block | FB79  Ident profile | FB79 | With this parameter, you select the block:   - FB79   Configuration of the optical reader with help of the "FB79" block.   Compatible with "VS130-2" and "MV400" readers; Compatible controllers: S7-300 and S7-400 - Ident profile    Configuration of the optical reader with help of the Ident blocks.   Compatible with all Ident devices; Compatible controllers: S7-300, S7-400, S7-1200 and S7-1500 |

### "Web Based Management" parameter group

In this parameter group you can start the Web Based Management.

Parameters in the "Web-based management" parameter group

| Parameter | Description |
| --- | --- |
| Web Based Management | Start Web Based Management of the reader.  Web Based Management (WBM) offers extensive functions for configuring the reader.  Note: WBM can only be started when either the PROFINET connection between CPU and reader has been established or the IP address stored in the project has been assigned to the reader. This means that the device name has been assigned and the TIA configuration must be loaded on the SIMATIC controller. |
