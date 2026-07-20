---
title: "Example libraries (S7-1200, S7-1500)"
package: SampleCodeLib2MenUS
topics: 3
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Example libraries (S7-1200, S7-1500)

This section contains information on the following topics:

- [Sample Library for Instructions (S7-1200, S7-1500)](#sample-library-for-instructions-s7-1200-s7-1500)
- [Library of General Functions (S7-1200, S7-1500)](#library-of-general-functions-s7-1200-s7-1500)

## Sample Library for Instructions (S7-1200, S7-1500)

The "Sample Library for Instructions" is the global library for the program examples using the instructions in STEP 7 (TIA Portal). This library offers you support during programming with its compact, easy to understand program examples in the programming languages LAD or SCL. The precondition for using the library is at least one CPU from the SIMATIC S7-1200 / S7-1500 series.

![Figure](images/94363923211_DV_resource.Stream@PNG-en-US.png)

### Programming examples in the TIA Portal information system

Programming examples in the "Sample Library for Instructions" match the instructions used in the programming examples in the TIA Portal information system. This means that you can call the respective programming example documentation via the help (<F1>) in the TIA Portal.

![Programming examples in the TIA Portal information system](images/104856707851_DV_resource.Stream@PNG-en-US.png)

### Downloading the library

The "Sample Library for Instructions" is available at the [FAQ page](https://support.industry.siemens.com/cs/ww/en/view/109476781).

> **Note**
>
> **Adding program examples to a project correctly**
>
> Due to the differing preconditions and functions, program examples may contain not only program blocks but also other components (e.g. PLC tags, PLC data types, watch tables or the like). There are also program examples that require special hardware (multiple CPUs, distributed I/O, input modules and the like).
>
> Please observe the following rules:
>
> - Never simply add all program examples or the entire "Sample Library for Instructions" folder to a CPU.
> - Make sure that the corresponding program example does not consist of components for multiple CPUs.
> - Always add the individual components of the program examples one at a time to the appropriate project folder. Also make sure that you select the appropriate CPU.

## Library of General Functions (S7-1200, S7-1500)

The "Library of General Functions" is the global library for supplementary functions for the instructions in STEP 7 (TIA Portal). To expand the scope of instructions, this library offers blocks with useful basic functions that are often required in automation projects. All contents of the library can be used with a CPU of the series SIMATIC S7-1200(F) / S7-1500(F).

![Figure](images/86771780235_DV_resource.Stream@PNG-en-US.png)

### General functions

The general functions of the "Library of General Functions" are provided as blocks in the SCL programming language. The library includes the following functions: FIFO, search function, matrix calculations, astro clock. You can immediately use the functions by means of parameter assignment and implement them universally.

### Downloading the library

The "Library of General Functions" is stored on the [FAQ page](https://support.industry.siemens.com/cs/ww/en/view/109479728).
