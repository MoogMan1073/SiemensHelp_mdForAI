---
title: "ET 200S serial interface (S7-1200, S7-1500)"
package: ProgFB1SI1500enUS
topics: 3
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# ET 200S serial interface (S7-1200, S7-1500)

This section contains information on the following topics:

- [Notes on use of an S7-1500 (S7-1200, S7-1500)](#notes-on-use-of-an-s7-1500-s7-1200-s7-1500)
- [Instructions of ET 200S 1SI (S7-1200, S7-1500)](#instructions-of-et-200s-1si-s7-1200-s7-1500)

## Notes on use of an S7-1500 (S7-1200, S7-1500)

### S_SEND / S_RCV / S_USSI / S_MODB on S7‑1500

Note the following when using the S_SEND, S_RCV, S_USSI or S_MODB instructions of the ET 200S 1SI distributed I/O on an S7‑1500:

- **S_SEND**
    
  Data type of the parameter DB_NO: UInt.  
  Only data from non-optimized memory areas can be sent. Keep this in mind during assignment of the DB_NO, DBB_NO and LEN parameters.
- **S_RCV**
    
  Data type of the parameter DB_NO: UInt.  
  Only data from non-optimized memory areas can be received. Keep this in mind during assignment of the DB_NO, DBB_NO and LEN parameters.
- **S_USSI**

  - **Data type of the parameters DBND, DBPA and DBCP: UInt**
      
    Invalid DB numbers for the DBND, DBPA and DBCP parameters: 60000 to 60999
  - **Reaction of CPU to error**
      
    The CPU is not switched to STOP in response to error.   
    If the CPU is to switch to STOP in response to error, the ANZ parameter must be evaluated in the user program   
    (if ANZ is not equal to zero, the STP instruction must be started):
- **S_MODB**

  Data type of the parameter DB_NO: DB_ANY.  
  Only data from non-optimized memory areas can be exchanged. Keep in mind during parameter assignment of the DB_NO parameter and the data block with the Modbus data conversion table.

### Instructions of the "Communication processor &gt; ET200S serial interface" library

Note the following when using the instructions of the ET 200S 1SI distributed I/O on an S7‑1500 (library: "Communication processor &gt; ET200S serial interface"):

- The hardware identifier of the communication module must be configured at the LADDR parameter.
- The send buffer and the receive buffer must both be located outside the optimized memory area.

## Instructions of ET 200S 1SI (S7-1200, S7-1500)

You can find descriptions of the instructions for ET 200S 1SI in the following sections:

- [ET 200S 1SI for 3964(R) and ASCII](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#et-200s-1si-for-3964r-and-ascii-s7-300-s7-400)
- [ET 200S 1SI for Modbus](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#et-200s-1si-for-modbus-s7-300-s7-400)
- [ET 200S 1SI for USS](ET%20200S%20serial%20interface%20%28S7-300%2C%20S7-400%29.md#et-200s-1si-for-uss-s7-300-s7-400)
