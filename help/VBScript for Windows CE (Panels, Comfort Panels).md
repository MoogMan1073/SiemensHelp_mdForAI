---
title: "VBScript for Windows CE (Panels, Comfort Panels)"
package: VBSWinCEWCCAenUS
topics: 31
devices: [Comfort Panels, Panels]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# VBScript for Windows CE (Panels, Comfort Panels)

This section contains information on the following topics:

- [VBScript for Windows CE (Panels, Comfort Panels)](#vbscript-for-windows-ce-panels-comfort-panels-1)
- [CreateObject (Panels, Comfort Panels)](#createobject-panels-comfort-panels)
- [Control element (Panels, Comfort Panels)](#control-element-panels-comfort-panels)
- [Properties (Panels, Comfort Panels)](#properties-panels-comfort-panels)
- [Methods (Panels, Comfort Panels)](#methods-panels-comfort-panels)

## VBScript for Windows CE (Panels, Comfort Panels)

### VBScript for Windows CE

You can also use the full range of functions of VBScript, except the control elements for access to files, on devices with Windows CE.

On a device with Windows CE the "File" and "FileSystem" control elements and the CreateObject function enable access to files and to the file system.

You will find fundamental information on VBScript language elements on the Microsoft homepage:

<http://msdn.microsoft.com/en-us/library/t0aew7h6.aspx>

### Local ID (LCID)

An overview of all language codes can be found on the Microsoft homepage:

<http://msdn.microsoft.com/en-us/goglobal/bb964664>

---

**See also**

[Principles of Debugging (Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#principles-of-debugging-panels-comfort-panels-rt-advanced-rt-professional)

## CreateObject (Panels, Comfort Panels)

### Function

This function generates a reference to an automation object.

### Syntax

`CreateObject` (object)

### Parameters

**Object**

A string that contains the ProgID of the object to be generated.

### Return value

Outputs a reference to an automation object.

### Notes

Use the CreateObject function to generate invisible ActiveX controls in Runtime. CreateObject cannot be used to generate graphic objects such as TreeView Control or ListView Control. The objects generated with CreateObjekt do not respond to events. To generate objects that respond to events, use the CreateObjectWithEvents function. The following table shows the ProgIDs for ActiveX Controls without events:

| **Control** | **ProgID** |
| --- | --- |
| Microsoft CE File control 6.0 | .file |
| Microsoft CE FileSystem control 6.0 | .filesystem |
| Microsoft CE ImageList control 6.0 | CEimageList.imagelistctrl |

### Example

Dim f, fwModeAppend

Set f = CreateObject("FileCtl.File")

fwModeAppend=8

f.Open "\Storage Card\testfile.txt", fwModeAppend

f.Close

## Control element (Panels, Comfort Panels)

### Control elements for file access

The "File" and "FileSystem" control elements enable access to files and the file system on a device with Windows CE. The control elements can only be used with the Windows CE Toolkit for Visual Basic 6.0.

### Library

FILECTLdtl

### DLL

Mscefile.dll

### File control element

The file control element supports the following properties:

- Attr
- EOF
- Loc
- LOF
- Seek

The File control element supports the following properties:

- Close (File)
- Get
- Input
- Input
- InputFields
- LineInputString
- LinePrint
- Open
- Put
- WriteFields

### FileSystem control element

The FileSystem control element supports the following methods:

- Dir
- FileCopy
- FileDateTime
- FileLen
- GetAttr
- Kill
- MkDir
- MoveFile
- RmDir
- SetAttr

## Properties (Panels, Comfort Panels)

This section contains information on the following topics:

- [Attr (Panels, Comfort Panels)](#attr-panels-comfort-panels)
- [EOF (Panels, Comfort Panels)](#eof-panels-comfort-panels)
- [Loc (Panels, Comfort Panels)](#loc-panels-comfort-panels)
- [LOF (Panels, Comfort Panels)](#lof-panels-comfort-panels)
- [Seek (Panels, Comfort Panels)](#seek-panels-comfort-panels)

### Attr (Panels, Comfort Panels)

#### Function

This property outputs a number that identifies the file mode that was used to open the file.

#### Syntax

File.Attr

#### Parameters

**File**

Reference to a "File" control.

#### Return values

The values shown in the following table indicate the access mode. If the return value is 0, the file is closed.

| Constant | Value |
| --- | --- |
| None | 0 |
| fsModeInput | 1 |
| fsModeOutput | 2 |
| fsModeRandom | 4 |
| fsModeAppend | 8 |
| fsModeBinary | 32 |

#### Notes

"Attr" is a read-only property. Use the Open method of the "File" control to specify the file mode.

### EOF (Panels, Comfort Panels)

#### Function

This property outputs True when the end of a file is reached which was opened for random or sequential input.

#### Syntax

File.EOF

#### Parameters

**File**

Reference to a "File" control.

#### Notes

Use the EOF property to avoid errors that occur due to reading after the end of a file.

The EOF property outputs False until the end of the file is reached. For files which were opened with fsModeRandom or fsModeBinary, False is output until the last executed Get statement returns no complete data record.

For files that were opened in the fsModeBinary mode, an attempt is made to read the file with the input function until EOF outputs True and an error is generated. If you want to read binary data with input, use the properties LOF and LOC instead of EOF or use Get in conjunction with EOF. For files that were opened with fsModeOutput, EOF always outputs True.

### Loc (Panels, Comfort Panels)

#### Function

This property outputs a number that names the current read/write position.

#### Syntax

File.Loc

#### Parameters

**File**

Reference to a "File" control.

#### Notes

For files which were opened with fsModeRandom, Loc outputs the last entry that was read or written as number. For files which were opened in all other modes, Loc outputs the position of the last read or written byte.

### LOF (Panels, Comfort Panels)

#### Function

This property outputs the size of a file, in bytes as number.

#### Syntax

File.LOF

#### Parameters

**File**

Reference to a "File" control.

#### Notes

The LOF property can be used in combination with the Loc property to to ensure that a read operation does not extend beyond the end of a file.

### Seek (Panels, Comfort Panels)

#### Function

This property sets the next position that is to be read or written in a file and outputs this.

#### Syntax

File.Seek [= Position]

#### Parameters

**File**

Reference to a "File" control.

**Position**

Numerical address that describes the position in a file.

#### Notes

The Seek property writes the next file position, by contrast the Loc property describes the current file position. The number output for Seek is always one higher than that for Loc. The only exception to this is when a file was opened new; in this case, both Seek and Loc output one.

An error is output if Seek produces a negative value or zero.

## Methods (Panels, Comfort Panels)

This section contains information on the following topics:

- [Close (Panels, Comfort Panels)](#close-panels-comfort-panels)
- [Dir (Panels, Comfort Panels)](#dir-panels-comfort-panels)
- [FileCopy (Panels, Comfort Panels)](#filecopy-panels-comfort-panels)
- [FileDateTime (Panels, Comfort Panels)](#filedatetime-panels-comfort-panels)
- [FileLen (Panels, Comfort Panels)](#filelen-panels-comfort-panels)
- [Get (Panels, Comfort Panels)](#get-panels-comfort-panels)
- [GetAttr (Panels, Comfort Panels)](#getattr-panels-comfort-panels)
- [Input (Panels, Comfort Panels)](#input-panels-comfort-panels)
- [InputB (Panels, Comfort Panels)](#inputb-panels-comfort-panels)
- [InputFields (Panels, Comfort Panels)](#inputfields-panels-comfort-panels)
- [Kill (Panels, Comfort Panels)](#kill-panels-comfort-panels)
- [LineInputString (Panels, Comfort Panels)](#lineinputstring-panels-comfort-panels)
- [LinePrint (Panels, Comfort Panels)](#lineprint-panels-comfort-panels)
- [MkDir (Panels, Comfort Panels)](#mkdir-panels-comfort-panels)
- [MoveFile (Panels, Comfort Panels)](#movefile-panels-comfort-panels)
- [Open (Panels, Comfort Panels)](#open-panels-comfort-panels)
- [Put (Panels, Comfort Panels)](#put-panels-comfort-panels)
- [RmDir (Panels, Comfort Panels)](#rmdir-panels-comfort-panels)
- [SetAttr (Panels, Comfort Panels)](#setattr-panels-comfort-panels)
- [WriteFields (Panels, Comfort Panels)](#writefields-panels-comfort-panels)

### Close (Panels, Comfort Panels)

#### Function

This method closes an open "File" control.

#### Syntax

File.Close

#### Parameters

**File**

Reference to a "File" control.

#### Output values

None.

#### Notes

Use the Open method to open a file.

### Dir (Panels, Comfort Panels)

#### Function

This method outputs the name of a file or a directory that fits in a specific pattern or contains a specific attribute.

#### Syntax

FileSystem.Dir (Pathname,[Attributs])

#### Parameters

**File**

Reference to a "FileSystem" control.

**Pathname**

Optional: A character string expression that describes the file name or path.

**Attributs**

Optional: A numerical expression whose sum describes the file attribute. If this was omitted, all files that are in the corresponding path are output.

The following table shows the parameter settings of the attribute.

| Constant | Value | Description |
| --- | --- | --- |
| fsAttrNormal | 0 | Normal |
| fsAttrReadOnly | 1 | Read-only |
| fsAttrHidden | 2 | Hidden |
| fsAttrSystem | 4 | System file |
| fsAttrVolume | 8 | Volume Label. If this was defined, all other attributes are ignored. |
| fsAttrDirectory | 16 | Directory |
| fsAttrArchive | 32 | Log |

#### Output values

String. A file name made up of the path name and the attributes. Dir outputs a zero length string ("") if the path name is not found.

#### Notes

Dir supports the use of multi-character wildcards (*) and single-character wildcards (?) for the description of files that exist multiple times. When used for the first time, you must specify the path name of the Dir method. If you specify attributes, the path name must also be included.

The Dir method outputs the first file name that matches the path name. If you want to output additional file names that match the path name, execute Dir again without parameters. If no further matching file names can be found, Dir returns a zero-length string (""). If a zero-length string was output, specify the path name by subsequent calling.

### FileCopy (Panels, Comfort Panels)

#### Function

This method copies the content of a file to another file.

#### Syntax

FileSystem.FileCopy PathName, NewPathName

#### Parameters

**FileSystem**

Reference to a "FileSystem" control.

**PathName**

Character string that contains the path and the file name.

**NewPathName**

Character string that contains the file name and the path of the new file.

#### Output values

None.

#### Notes

FileCopy outputs an error if the new file does not exist.

### FileDateTime (Panels, Comfort Panels)

#### Function

This method outputs a Variant (date) that contains the date and the time at which the file was created or last edited.

#### Syntax

FileSystem.FileDateTime(Pathname)

#### Parameters

**Filesystem**

Reference to a "FileSystem" control.

**Pathname**

Character string expression that names the file name. The path name may contain a directory.

#### Output value

Indicates the date on which the file was last edited.

#### Notes

If a new file does not exist, FileDateTime outputs an error.

### FileLen (Panels, Comfort Panels)

#### Function

This method outputs the value that describes the length of file in bytes.

#### Syntax

FileSystem.FileLen(Pathname)

#### Parameters

**Filesystem**

Reference to a "FileSystem" control.

**Pathname**

Character string that describes the file name. The path name may contain a directory.

#### Output values

Indicates how many bytes a file consists of.

#### Notes

If the specified file is already open when FileLen is called, the value indicates the size of the file before this is opened.

### Get (Panels, Comfort Panels)

#### Function

This method reads data from an open file into a tag.

#### Syntax

File.Get Data, [Recnumber]

#### Parameters

**File**

Reference to a "File" control.

**Data**

Variant tag into which the data is read.

**Recnumber**

Optional: Number at which reading begins. For files that were opened in binary mode, Recnumber defines the byte position.

#### Output values

None.

#### Notes

Data that is read with the Get method is usually written to the file with the Put method. The first data record or the first byte in a file is in position 1, the second in position 2 and so on. If you skip Recnumber, the next data record or the next byte that follows the last Get or Put method (or which was referred to by the Seek method) is read.

The following rules apply to files which were opened in random mode:

- If the length of the read data is shorter than the length defined in length clause of the Open method, Get reads the following data records in the length of the data record limit. The space between the end of a data record and the start of the next data record is filled the content of the file buffer. Because it is not possible to precisely determine the scope of the filled data, it is advisable that the length of the data records matches the length of the data to be read.
- If the data is a numeric type variant, Get reads 2 bytes to determine the VarType of the variant and then reads the data that is written to the tag. If, for example, a variant of type VarType3 reads 6 bytes with Get, 2 bytes identify the variant as VarType 3 (long) and 4 bytes contain long data. The data record length is defined in the length clause. When the open method is used, the data record length must be at least 2 bytes larger than the number of bytes required to save the tag.
- The Get method can be used to read a variant array from the memory. However, it cannot be used to read a scalar variant that contains an array. No objects can be read from the memory with Get.
- If the variant that is to be read is type VarType 8 (string), Get reads 2 bytes and identifies the variant as VarType 8, 2 additional bytes define the length of the string and the data of the string is then read. The data record length of the open method defined by the length clause must be at least 4 bytes greater than the length of the string.
- If the tag to be written is a dynamic array, Get reads the descriptor whose length is 2 plus 8 times the number of dimensions (2 + 8 * NumberOfDimensions). The data record length of the open method defined by the length clause must be greater than or equal to the sum of bytes required to read the array data and the array descriptor.

For files which are opened in binary mode, the length clause of the open method has no effect. Get reads all tags jointly from the memory without filling between the files.

### GetAttr (Panels, Comfort Panels)

#### Function

This method outputs a value that describes the attributes of a file or folder.

#### Syntax

FileSystem.GetAttr(Pfadname)

#### Parameters

**FileSystem**

Reference to a "FileSystem" control.

**Pathname**

Character string that describes the file name or folder name. The path name may contain a directory.

#### Output values

A numerical expression whose sum describes the attributes of a file or folder. The following table shows the possible values.

| Constant | Value | Description |
| --- | --- | --- |
| vbNormal | 0 | Normal |
| vbReadOnly | 1 | Read-only |
| vbHidden | 2 | Hidden |
| VbSystem | 4 | System |
| VbDirectory | 16 | Directory |
| VbArchive | 32 | The file has changed since the last backup. |

#### Notes

To specify the set attributes, use the And operator to execute a bitwise comparison of the values returned by GetAttr and the values of the attribute selected by you.

### Input (Panels, Comfort Panels)

#### Function

This method outputs a string that contains the characters from a file opened in input or binary mode.

#### Syntax

File.Input(Number)

#### Parameters

**File**

Reference to a "File" control.

**Number**

Numerical expression that defines the number of output characters.

#### Output values

A character string that consists of characters read from a file.

#### Notes

Data that is read with the Input method is generally written to the file with LinePrint or Put methods. Use this method only for files which were opened in input or binary mode.

In contrast to the LineInputString method, the Input method outputs all read characters, for example commas, carriage returns, line feeds, quotation marks and leading spaces.

Any attempt to read the file with the Input method before the EOF function returns "True" will cause an error in files that were opened for binary access. To avoid this error, use the LOF and Loc functions instead of the EOF function to read binary files with the Input method or use Get in combination with the EOF function.

### InputB (Panels, Comfort Panels)

#### Function

This method returns bytes from a file opened in input or binary mode.

#### Syntax

File.InputB(Number)

#### Parameters

**File**

Reference to a "File" control.

**Number**

Each valid numerical expression that describes the number of output bytes.

#### Output values

An array that contains the bytes read out from the file.

#### Notes

Files that are read with the InputIB method are usually written with the LinePrint or Put methods. Use this method only for files which were opened in Input or Binary mode.

### InputFields (Panels, Comfort Panels)

#### Function

The method reads data from an open sequential file and outputs a one-dimensional variant data field.

#### Syntax

File.InputFields(Number)

#### Parameters

**File**

Reference to a "FileSystem" control.

**Number**

Number of fields which are delimited by commas and are to be read from a file.

#### Output values

An array that contains fields read from the file.

#### Notes

Data that is read with the InputFields method is usually written with WriteFields. Use this method only in files opened in Binary or Input mode. InputFields reads standard string or numeric data without modifications. The following table shows how InputFields reads other input data:

| Data | Content of the assigned tags |
| --- | --- |
| Comma delimitation or empty line | Empty |
| #NULL# | Null |
| #TRUE# or #FALSE# | True or False |
| #yyyy-mm-dd hh:mm:ss# | The date and/or the time shown as expression |

Double quotation marks ("") with input data are discarded.

If you reach the end of the file while you are adding a data object, the added data is deleted and an error is displayed.

To correctly read data from a file as tags that use InputFields, use the WriteFields method instead of the LinePrint method to write the data to the files. The use of WriteFields ensures that each data field is exactly separated.

### Kill (Panels, Comfort Panels)

#### Function

This method deletes files and folders from the hard disk.

#### Syntax

FileSystem.Kill Pathname

#### Parameters

**FileSystem**

Reference to a "FileSystem" control.

**Pathname**

A character string that names one or more files that are to be deleted. The path name may contain a folder.

#### Output values

None.

#### Notes

The Kill method supports the use of multi-character wildcards (*) and single-character wildcards (?) to identify multiple files.

An error is output if you try to delete an open file using the Kill method.

### LineInputString (Panels, Comfort Panels)

#### Function

This method reads a single line from an open sequential file and links it with a string tag.

#### Syntax

File.LineInputString

#### Parameters

**File**

Reference to a "File" control.

#### Output values

None.

#### Notes

Data that is read with LineInput string is usually written to a file with Line Print.  
The LineInputString method reads a file character by character until a carriage return sequence (Chr(13)) or carriage-return/line-feed (Chr(13) + Chr(10)) is reached. Carriage return and line feed sequences are more often skipped than appended to the character string.

### LinePrint (Panels, Comfort Panels)

#### Function

This method writes a single line to an open sequential file.

#### Syntax

File.LinePrint Output

#### Parameters

**File**

Reference to a "FileSystem" control.

**Output**

A character string that is written to the file.

#### Output values

None

#### Notes

Data that is written to a file with LinePrint is usually read out with LineInput string.  
A carriage return sequence (Chr(13) + Chr(10)) is appended at the end of the string.

### MkDir (Panels, Comfort Panels)

#### Function

This method creates a new folder.

#### Syntax

FileSystem.MkDir Pathname

#### Parameters

**FileSystem**

Reference to a "FileSystem" control.

**Pathname**

A character string that contains the folder name.

#### Output values

None.

#### Notes

MkDir returns an error if the directory already exists.

### MoveFile (Panels, Comfort Panels)

#### Function

The method renames an already existing file or a directory and all subdirectories.

#### Syntax

FileSystem.MoveFile PathName, NewPathName

#### Parameters

**FileSystem**

Reference to a "FileSystem" control.

**PathName**

A character string that contains the file name.

**NewPathName**

A character string that contains the file name to be copied.

#### Output values

None.

### Open (Panels, Comfort Panels)

#### Function

The method opens a file. The following file modes are available: Input (1), Output (2), Random (4), Append (8), or Binary (32).

#### Syntax

File.Open Pathname, Mode, [Access], [Lock], [Reclength]

#### Parameters

**File**

Reference to a "FileSystem" control.

**Pathname**

A character string that contains the file name.

**Mode**

Specifies the file mode: Input (1), Output (2), Random (4), Append (8), or Binary (32).

**Access**

Optional: Not permitted with open file: Read, Write, or ReadWrite [default]. (1, 2, 3)

**Lock**

Optional: Actions on the open file that are blocked by other processes: Shared, LockRead, LockWrite [default] and LockReadWrite. (1, 2, 3, 0).

**Reclength**

Optional: A number in bytes that is lower than 32,767. For files that were opened with random access, this value corresponds to the sentence length. For sequential files, this value is the number of buffered characters.

#### Output values

None.

#### Note

The reclength parameter is ignored in Binary mode. If a file was opened in Random mode, you must define a file size that is greater than zero; otherwise, an error is output.

### Put (Panels, Comfort Panels)

#### Function

This method writes data from a tag to a file.

#### Syntax

File.Put Data, [Recnumber]

#### Parameters

**Data**

A variant tag that contains data that is to be written to the file.

**Recnumber**

Optional. Variant (long). Data record number (random mode files) or byte number (binary mode files) with which the write process starts.

#### Output values

None.

#### Notes

Data that is written with Put is usually read out from a file with Get.

The first data record or the first byte in a file is in position 1, the second in position 2 and so on. If you skip Recnumber, the next data record or the next byte that follows the last Get or Put method, or which was referred to by the Seek method, is read.

The following rules apply to files that were opened in random mode:

- If the length of the data to be written is shorter than the length defined in the length clause of the Mopen method, Put writes the following data records in the length of the data record limit. The space between the end of a data record and the start of the next data record is filled with the content of the file buffer. Because it is not possible to precisely determine the length of the filled data, it is advisable that the length of the data records matches the length of the data to be written. If the length of the data to be written is longer than the length of the Open method defined in the length clause, an error is output.
- If the tag to be written is a numerical type variant, Put first writes 2 bytes to declare the variant as VarType and the tag is then written. If, for example, a VarType 3 variant is written, Put writes 6 bytes, 2 bytes identify the variant as VarType 3 (long) and 4 bytes contain the long data. The data record length of the open method defined in the length clause must be at least 2 bytes greater than the number of bytes required to save the tag.
- The Pet method may be used to write a variant array to the memory. However, it cannot be used to write a scalar variant that contains an array. Objects cannot be written with Put to the hard disk.
- If the version that is to be written is type VarType 8 (string), Put writes 2 Bytes and identifies the variant as VarType 8, 2 additional bytes define the length of the string and the data of the string is then written. The data record length of the open method defined by the length clause must be at least 4 bytes greater than the length of the string.
- If the tag to be written is a dynamic array, Put writes the descriptor whose length is 2 plus 8 times the number of dimensions (2 + 8 * NumberOfDimensions). The data record length of the open method defined by the length clause must be greater than or equal to the sum of bytes required to write the array data and the array descriptor.

For files which are opened in binary mode, the length clause of the open method has no effect. Put writes all tags jointly from the memory with filling between the files.

### RmDir (Panels, Comfort Panels)

#### Function

This method deletes an empty directory.

#### Syntax

FileSystem.RmDir Pathname

#### Parameters

**FileSystem**

Reference to a "FileSystem" control.

**PathName**

A character string that contains the file name.

#### Output values

None.

#### Notes

The directory must be empty in order to be deleted. A complete path must be specified.

### SetAttr (Panels, Comfort Panels)

#### Function

This method set the attribute data of a file.

#### Syntax

FileSystem.SetAttr Pathname, Attributes

#### Parameters

**FileSystem**

Reference to a FileSystem Control

**Pathname**

A character string that contains the file name.

**Attributes**

A numerical expression that contains the sum of the file attributes. The following table shows the possible values.

| Constant | Value | Description |
| --- | --- | --- |
| vbNormal | 0 | Standard (default) |
| vbReadOnly | 1 | Read-only |
| vbHidden | 2 | Hidden |
| VbSystem | 4 | System file |
| VbArchive | 32 | The file has been modified since the last backup |

#### Output values

None.

#### Notes

A runtime error occurs if you try to set the attributes of an open file.

### WriteFields (Panels, Comfort Panels)

#### Function

This method writes data to a sequential file.

#### Syntax

File.WriteFields [Data]

#### Parameters

**File**

Reference to a "File" control.

**Data**

Optional: Variant to be written to a file or variant array of a numerical string or a string expression.

#### Output values

None.

#### Notes

Data that is written with WriteFields is usually read from the file with InputFiles.

If you omit data, a blank line is written to the file.

- The full stop is written as decimal delimiter for numerical data.
- Either #TRUE# or #FALSE# are output for Boolean data. The True and False keywords are not compiled, regardless of location.
- The time data is written to the file in the universal date format. If either the date or the time is missing or null, only the existing information is written to the file.
- If the data is empty, nothing is written to the file.
- If the data is null, #NULL# is written to the file.

The WriteFields method adds commas and quotation marks around the strings that are written to the file. Delimiters do not have to be added to the list. WriteFields inserts a line break in the form of a carriage-return/line-feed (Chr(13) + Chr(10))- after it has written the last character of the data to the file.
