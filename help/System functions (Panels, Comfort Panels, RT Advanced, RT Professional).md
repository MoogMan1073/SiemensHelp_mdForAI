---
title: "System functions (Panels, Comfort Panels, RT Advanced, RT Professional)"
package: VBSReferenceWCCPenUS
topics: 33
devices: [Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# System functions (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [ActivateScreen (Panels, Comfort Panels, RT Advanced, RT Professional)](#activatescreen-panels-comfort-panels-rt-advanced-rt-professional)
- [ActivateScreenInScreenWindow (Panels, Comfort Panels, RT Advanced, RT Professional)](#activatescreeninscreenwindow-panels-comfort-panels-rt-advanced-rt-professional)
- [DecreaseTag (Panels, Comfort Panels, RT Advanced, RT Professional)](#decreasetag-panels-comfort-panels-rt-advanced-rt-professional)
- [ExportImportUserAdministration (Panels, Comfort Panels, RT Advanced, RT Professional)](#exportimportuseradministration-panels-comfort-panels-rt-advanced-rt-professional)
- [GetParentScreen (Panels, Comfort Panels, RT Advanced, RT Professional)](#getparentscreen-panels-comfort-panels-rt-advanced-rt-professional)
- [GetParentScreenWindow (Panels, Comfort Panels, RT Advanced, RT Professional)](#getparentscreenwindow-panels-comfort-panels-rt-advanced-rt-professional)
- [IncreaseTag (Panels, Comfort Panels, RT Advanced, RT Professional)](#increasetag-panels-comfort-panels-rt-advanced-rt-professional)
- [InverseLinearScaling (Panels, Comfort Panels, RT Advanced, RT Professional)](#inverselinearscaling-panels-comfort-panels-rt-advanced-rt-professional)
- [InvertBit (Panels, Comfort Panels, RT Advanced, RT Professional)](#invertbit-panels-comfort-panels-rt-advanced-rt-professional)
- [InvertBitInTag (Panels, Comfort Panels, RT Advanced, RT Professional)](#invertbitintag-panels-comfort-panels-rt-advanced-rt-professional)
- [LinearScaling (Panels, Comfort Panels, RT Advanced, RT Professional)](#linearscaling-panels-comfort-panels-rt-advanced-rt-professional)
- [LookupText (Panels, Comfort Panels, RT Advanced, RT Professional)](#lookuptext-panels-comfort-panels-rt-advanced-rt-professional)
- [ResetBit (Panels, Comfort Panels, RT Advanced, RT Professional)](#resetbit-panels-comfort-panels-rt-advanced-rt-professional)
- [ResetBitInTag (Panels, Comfort Panels, RT Advanced, RT Professional)](#resetbitintag-panels-comfort-panels-rt-advanced-rt-professional)
- [SetBit (Panels, Comfort Panels, RT Advanced, RT Professional)](#setbit-panels-comfort-panels-rt-advanced-rt-professional)
- [SetBitInTag (Panels, Comfort Panels, RT Advanced, RT Professional)](#setbitintag-panels-comfort-panels-rt-advanced-rt-professional)
- [SetLanguage (Panels, Comfort Panels, RT Advanced, RT Professional)](#setlanguage-panels-comfort-panels-rt-advanced-rt-professional)
- [SetPropertyByConstant (Panels, Comfort Panels, RT Advanced, RT Professional)](#setpropertybyconstant-panels-comfort-panels-rt-advanced-rt-professional)
- [SetPropertyByProperty (Panels, Comfort Panels, RT Advanced, RT Professional)](#setpropertybyproperty-panels-comfort-panels-rt-advanced-rt-professional)
- [SetPropertyByTag (Panels, Comfort Panels, RT Advanced, RT Professional)](#setpropertybytag-panels-comfort-panels-rt-advanced-rt-professional)
- [SetPropertyByTagIndirect (Panels, Comfort Panels, RT Advanced, RT Professional)](#setpropertybytagindirect-panels-comfort-panels-rt-advanced-rt-professional)
- [SetTag (Panels, Comfort Panels, RT Advanced, RT Professional)](#settag-panels-comfort-panels-rt-advanced-rt-professional)
- [SetTagByProperty (Panels, Comfort Panels, RT Advanced, RT Professional)](#settagbyproperty-panels-comfort-panels-rt-advanced-rt-professional)
- [SetTagByTagIndirect (Panels, Comfort Panels, RT Advanced, RT Professional)](#settagbytagindirect-panels-comfort-panels-rt-advanced-rt-professional)
- [SetTagIndirect (Panels, Comfort Panels, RT Advanced, RT Professional)](#settagindirect-panels-comfort-panels-rt-advanced-rt-professional)
- [SetTagIndirectByProperty (Panels, Comfort Panels, RT Advanced, RT Professional)](#settagindirectbyproperty-panels-comfort-panels-rt-advanced-rt-professional)
- [SetTagIndirectByTagIndirect (Panels, Comfort Panels, RT Advanced, RT Professional)](#settagindirectbytagindirect-panels-comfort-panels-rt-advanced-rt-professional)
- [SetTagWithOperatorEvent (Panels, Comfort Panels, RT Advanced, RT Professional)](#settagwithoperatorevent-panels-comfort-panels-rt-advanced-rt-professional)
- [ShowBlockInTIAPortalFromAlarm (Panels, Comfort Panels, RT Advanced, RT Professional)](#showblockintiaportalfromalarm-panels-comfort-panels-rt-advanced-rt-professional)
- [ShowLogonDialog (Panels, Comfort Panels, RT Advanced, RT Professional)](#showlogondialog-panels-comfort-panels-rt-advanced-rt-professional)
- [ShowPLCCodeViewFromAlarm (Panels, Comfort Panels, RT Advanced, RT Professional)](#showplccodeviewfromalarm-panels-comfort-panels-rt-advanced-rt-professional)
- [StopRuntime (Panels, Comfort Panels, RT Advanced, RT Professional)](#stopruntime-panels-comfort-panels-rt-advanced-rt-professional)

## ActivateScreen (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Performs a screen change to the given screen.

Use the "ActivateScreenByNumber" system function to change from the root screen to the permanent area or vice versa.

### Use in the function list

ActivateScreen (Screen name, Object number)

### Use in user-defined functions

ActivateScreen Screen_name, Object_number

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Screen name**

Name of the screen to which you change.

**Object number**

The operator control element which receives the focus in the given screen after the screen change. The number of the operator control element is to be determined using the tabulator sequence during configuration.

When "0" is specified:

- If the focus is in the permanent area when the system function is called up, the permanent area maintains the focus.
- If the focus is in the root screen when the system function is called up, the first operator control element in the given screen receives the focus.

  > **Note**
  >
  > If the "Reach margin" event is assigned to the "ActivateScreen" system function, only the value "0" is valid for the "Object number" parameter. The active object is not defined by the object number, but rather by the X position it had prior to the screen change.

### Example

The following program code activates "Screen_2" with the ActivateScreen function, for example, when you click a button.

`Sub ActivateScreen_2()`

`'User-defined code`

`'' i. e. when pressing a button`

`ActivateScreen "Screen_2",0`

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## ActivateScreenInScreenWindow (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Performs a screen change to the specified screen in a specified screen window.

### Use in the function list

ActivateScreenInScreenWindow (Screen name, Screen window, New screen name)

### Use in user-defined functions

ActivateScreenInScreenWindow Screen_name, Screen_window, New_screen_name

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

### Parameters

**Screen name**

Name of the screen to be displayed in the screen window.

**Screen window**

Name of the screen window in which the new screen is to be displayed.

**New screen name**

Name of the new screen to be displayed in the screen window.

### Example

The ActivateScreenInScreenWindow function is used in the following program code to activate the "Screen_2" screen when you click a button.

{

// User defined code

// i.e. when pressing a button

ActivateScreenInScreenWindow (GetParentScreen(screenName), GetParentScreenWindow(screenName), "Screen_2");

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## DecreaseTag (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Subtracts the given value from the tag value.

X = X - a

> **Note**
>
> The system function uses the same tag as input and output values. When this system function is used to convert a value, auxiliary tags must be used. You can use the "SetTag" system function to assign the tag value to the auxiliary tags.

If you configure the system function for events of an alarm and the tag is not being used in the current screen, it is not ensured that the actual tag value is being used in the PLC. You can improve the situation by setting the "Cyclic continuous" acquisition mode.

### Use in the function list

DecreaseTag (Tag, Value)

### Use in user-defined functions

DecreaseTag Tag, Value

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

### Parameters

**Tag**

The tag from which the given value is subtracted.

**Value**

The value which is subtracted.

### Example

The following program code decrements the value at the varX tag by the value at the value tag. The value entered is saved to the old_value tag and output along with the new varX value.

{

BYTE varX;

BYTE value;

//user input

...

BYTE old_value = varX;

//Decrease tag

DecreaseTag(varX, value);

//print original value and function result

printf ("User input: %i\r\n, Result of function DecreaseTag: %i\r\n", old_value, varX);

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## ExportImportUserAdministration (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Exports all users of the user administration of the currently active project to the specified file or imports the users from the specified file to the currently active project.

Users, their passwords and rights are saved in the user administration.

The export/import of the user administration configuration encompasses all the settings. Existing objects (users, groups, logon settings, authorization levels) are overwritten during the import.

The imported users are valid immediately.

### Use in the function list

ExportImportUserAdministration (File name, Direction)

### Use in user-defined functions

ExportImportUserAdministration File_name, Direction

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**File name**

Name of the file which contains the passwords or to which the passwords are written. Enter the file location and the file extension (*.txt), for example, "C:\TEMP\Passwords.txt".

> **Note**
>
> If a storage card is used as file location, specify the file location as follows: "\StorageCard\&lt;FileName".

**Direction**

Specifies whether passwords are exported or imported:

0 (hmiExport) = Export: Passwords are exported.

1 (hmiImport) = Import: Passwords are imported.

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## GetParentScreen (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

The function determines the name of the parent screen from a specified screen path.

### Use in the function list

GetParentScreen (screen)

### Use in user-defined functions

GetParentScreen Screen

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Screen**

The structure of the transferred "Screen" parameter must correspond to that formed by the graphics system for screen paths:

&lt;Screen_name&gt;.&lt;Screen_window_name&gt;:&lt;Screen_name&gt;.&lt;Screen_window_name&gt;:&lt;Screen_name&gt;...

If you use the object list in the function list to specify the parameter, the screen name is entered instead of the screen path.

> **Note**
>
> The "." character is used to distinguish between screen and screen object names. The ":" character is used for the hierarchy structuring. Therefore, use only the "-" or "_" as a delimiter in the name designations.

### Return value

Name of the parent screen.

### Principle

A "Screenwindow_1" screen window is in a "Screen_1" screen. In the screen window, the screen becomes "Screen_2" with the "Screenwindow_2" screen window, etc.

Screen path: Screen_1.Screenwindow_1:Screen_2.Screenwindow_2:Screen_3

GetParentScreen returns:

- "Screen_2", if the system function is called in the "Screen_3" screen.
- "Screen_1", if the system function is called in the "Screen_2" screen.

GetParentScreenwindow returns:

- "Screenwindow_2", if the system function is called in the "Screen_3" screen.
- "Screenwindow_1", if the system function is called in the "Screen_2" screen.

## GetParentScreenWindow (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

The function determines the name of the parent screen window from a transferred screen path.

### Use in the function list

GetParentScreenWindow (Screen)

### Use in user-defined functions

GetParentScreenWindow Screen

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Screen**

The structure of the transferred "Screen" parameter must correspond to that formed by the graphics system for screen paths:

&lt;Screen_name&gt;.&lt;Screen_window_name&gt;:&lt;Screen_name&gt;.&lt;Screen_window_name&gt;:&lt;Screen_name&gt;...

If you use the object list in the function list to specify the parameter, the screen name is entered instead of the screen path.

> **Note**
>
> The "." character is used to distinguish between screen and screen object names. The ":" character is used for the hierarchy structuring. Therefore, use only the "-" or "_" as a delimiter in the name designations.

### Return value

Name of the parent screen window.

### Principle

A "Screenwindow_1" screen window is in a "Screen_1" screen. In the screen window, the screen becomes "Screen_2" with the "Screenwindow_2" screen window, etc.

Screen path: Screen_1.Screenwindow_1:Screen_2.Screenwindow_2:Screen_3

GetParentScreen returns:

- "Screen_2", if the system function is called in the "Screen_3" screen.
- "Screen_1", if the system function is called in the "Screen_2" screen.

GetParentScreenwindow returns:

- "Screenwindow_2", if the system function is called in the "Screen_3" screen.
- "Screenwindow_1", if the system function is called in the "Screen_2" screen.

## IncreaseTag (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Adds the given value to the value of the tags.

X = X + a

> **Note**
>
> The system function uses the same tag as input and output values. When this system function is used to convert a value, auxiliary tags must be used. You can use the "SetTag" system function to assign the tag value to the auxiliary tags.

If you configure the system function for events of an alarm and the tag is not being used in the current screen, it is not ensured that the actual tag value is being used in the PLC. You can improve the situation by setting the "Cyclic continuous" acquisition mode.

### Use in the function list

IncreaseTag (Tag, Value)

### Use in user-defined functions

IncreaseTag Tag, Value

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

### Parameters

**Tag**

The tag to which the given value is added.

**Value**

The value that is added.

### Example

The following program code increments the value of the varX tag by the value in the value tag. The value entered is saved to the old_value tag and output along with the new varX value.

{

BYTE varX;

BYTE value;

//user input

...

BYTE old_value = varX;

//Increase tag

IncreaseTag(varX, value);

//print original value and function result

printf ("User input: %i\r\n, Result of function IncreaseTag: %i\r\n", old_value, varX);

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## InverseLinearScaling (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Assigns a value to the tag X, which is calculated from the value of the given tag Y using the linear function X = (Y - b) / a.

The tags X and Y must not be identical. This system function is the inverse of the "LinearScaling" system function.

> **Note**
>
> The tags X and Y must not be identical. If a tag is to be converted into itself, a auxiliary tag must be used.
>
> The "SetTag" system function can be used to assign the value of the tags to be converted to the auxiliary tags.

### Use in the function list

InvertLinearScaling (X, Y, b, a)

### Use in user-defined functions

InverseLinearScaling X, Y, b, a

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**X**

The tag which is assigned the value calculated from the linear equation.

**Y**

The tag that contains the value used for calculation.

**b**

The value which is subtracted.

**a**

The value through which is divided.

### Example

The following program code assigns a value to the varX tag by means of the InverseLinearScaling function.

{

BYTE varX;

BYTE Yvalue = 10;

BYTE bvalue = 3;

BYTE avalue = 4;

//Inverse linear scaling

InverseLinearScaling (varX, Yvalue, bvalue, avalue);

printf ("varX = %d\r\n, varX);

...

}

The saved return value can be processed in the following code.

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## InvertBit (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Inverts the value of the given tag of the "Bool" type:

- If the tag has the value of 1 (TRUE), it will be set to 0 (FALSE).
- If the tag has the value of 0 (FALSE), it will be set to 1 (TRUE).

### Use in the function list

InvertBit (Tag)

### Use in user-defined functions

InvertBit Tag

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Tag**

The tag whose bit is set.

### Example

The following program code inverts the value of the Boolean tag bStatus and outputs the result along with the original bSaved value.

'Programming language: VB

Dim myTag

Dim myOutputField

Dim bValue, bSaved, strResult

Set myTag = SmartTags("bStatus")

Set myOutputField=HMIRuntime.Screens("MyScreen").ScreenItems("objTextField")

'Get current value

bValue=myTag.Value

'Save current value

bSaved=bValue

'Invert Bit

InvertBit myTag

bValue=myTag.Value

'Output result old and new value:

strResult="Old Value: "&amp;bSaved &amp;Chr(13)&amp;"New Value: "&amp;bValue

myOutputField.Text=strResult

//Programming language: C

{

BOOL bStatus = 0;

BOOL bSaved = bStatus;

//Invert variable

invertBit(bStatus);

//print current and saved value

printf ("Current value: %d\r\n, Saved value: %d\r\n",bStatus, bSaved);

  ...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## InvertBitInTag (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Inverts a bit in the given tag:

- If the bit in the tag has the value of 1 (TRUE), it will be set to 0 (FALSE).
- If the bit in the tag has the value of 0 (FALSE), it will be set to 1 (TRUE).

After changing the given bit, the system function transfers the entire tag back to the PLC. It is not checked whether other bits in the tags have changed in the meantime. Operator and PLC have read-only access to the indicated tag until it is transferred back to the PLC.

> **Note**
>
> If the PLC supports BOOL tags, do not use this system function. Use the "InvertBit" system function instead.

### Use in the function list

InvertBitInTag (Tag, Bit)

### Use in user-defined functions

InvertBitInTag Tag, Bit

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Tag**

The tag in which the given bit is set.

**Bit**

The number of the bit that is set.

When this system function is used in a user-defined function, the bits in a tag are counted from right to left. The counting begins with 0.

### Example

The following program code inverts a bit at the specified bitposition in the bStatusWord tag and outputs the result along with the original bSaved value.

'Programming language: VB

Dim myTag

Dim myOutputField

Dim bValue, bSaved, bitposition, strResult

Set myTag = SmartTags("bStatusWord")

Set myOutputField=HMIRuntime.Screens("MyScreen").ScreenItems("objTextField")

'Get current value

bValue=myTag.Value

'Save current value

bSaved=bValue

'Invert Bit in position

bitposition=2

InvertBit myTag, bitposition

bValue=myTag.Value

'Output result old and new value:

strResult="Old Value: "&amp;bSaved &amp;Chr(13)&amp;"New Value: "&amp;bValue

myOutputField.Text=strResult

//Programming language: C

{

BYTE bStatusWord;

BYTE bsaved = bStatusWord;

BYTE bitposition = 2;

//Invert bit in bitposition

InvertBitInTag (bStatusWord, bitposition);

//print current and saved value

printf ("Current value: %d\r\n, Saved value: %d\r\n",bStatusWord, bsaved);

  ...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## LinearScaling (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Assigns a value to the tag Y, which is calculated from the value of the given tag X using the linear function Y= (a *X) + b.

The inverse of this function is the "InvertLinearScaling" system function.

> **Note**
>
> The tags X and Y must not be identical. If a tag is to be converted into itself, a auxiliary tag must be used.
>
> The "SetTag" system function can be used to assign the value of the tags to be converted to the auxiliary tags.

### Use in the function list

LinearScaling (Y, a, X, b)

### Use in user-defined functions

LinearScaling Y, a, X, b

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Y**

The tag which is assigned the value calculated from the linear equation.

**a**

The value with which is multiplied.

**X**

The tag that contains the value used for calculation.

**b**

The value that is added.

### Example

The following program code uses the LinearScaling function to assign a value to the Yvar tag.

{

BYTE Yvar;

BYTE Xvalue = 10;

BYTE bvalue = 3;

BYTE avalue = 4;

// linear scaling

LinearScaling ( Yvar, avalue, Xvalue, bvalue);

printf ("Yvar = %d\r\n, Yvar);

...

}

The saved return value can be processed in the following code.

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## LookupText (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Identifies an entry from a text list. The result depends on the value and on the selected runtime language. The result is saved to a tag of data type "String".

### Use in the function list

LookupText (Output text, Index, Language, Text list)

### Use in user-defined functions

LookupText Output_text, Index, Language, Text_list

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Output text**

The tag to which the result is written.

**Index**

The tag that defines the value of the list entry.

**Language**

Defines the runtime language in which the list entry is identified.

- Runtime language

  Language code as per VBScript reference, for example, "de-DE" for German (Germany) or "en-US" for English (United States of America). The selection depends on the activated runtime languages.
- Tag

  The tag that contains the language. Enter the runtime language as decimal value of the country ID, for example, 1031 for German - Standard, 1033 for English - USA. Details are available in the VBScript basics, "Locale identifier (LCID) diagram".
- Integer

  The number that corresponds to the order of runtime languages for language switching.   
  The selection depends on the activated runtime languages, for example, "0" for the language that appears when you first start runtime. You can find more information under the topic of "Languages in Runtime".

**Text list**

Defines the text list. The list entry is read from the text list.

---

**See also**

[Device dependency (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#device-dependency-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## ResetBit (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Sets the value of a "Bool" type tag to 0 (FALSE).

### Use in the function list

ResetBit (Tag)

### Use in user-defined functions

ResetBit Tag

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Tag**

The BOOL type tag which is set to 0 (FALSE).

### Example

The following program code sets the value of the Boolean tag bStatus to 0 by means of the ResetBit function and outputs the result along with the original bSaved value.

'Programming language: VB

Dim myTag

Dim myOutputField

Dim bValue, bSaved, strResult

Set myTag = SmartTags("bStatus")

Set myOutputField=HMIRuntime.Screens("MyScreen").ScreenItems("objTextField")

'Set value

bValue=1

myTag.Value=bValue

'Save current value

bSaved=bValue

'Reset Bit

ResetBit myTag

bValue=myTag.Value

'Output result old and new value:

strResult="Old Value: "&amp;bSaved &amp;Chr(13)&amp;"New Value: "&amp;bValue

myOutputField.Text=strResult

//Programming language: C

{

BOOL bStatus = 1;

BOOL bSaved = bStatus;

//Reset bit

ResetBit (bStatus);

//print current and saved value

printf ("Current value: %d\r\n, Saved value: %d\r\n",bStatus, bSaved);

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## ResetBitInTag (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Sets a bit in the specified tag to 0 (FALSE).

After changing the given bit, the system function transfers the entire tag back to the PLC. It is not checked whether other bits in the tags have changed in the meantime. Operator and PLC have read-only access to the indicated tag until it is transferred back to the PLC.

> **Note**
>
> If the PLC supports BOOL tags, do not use this system function. Use the "ResetBit" system function instead.

### Use in the function list

ResetBitInTag (Tag, Bit)

### Use in user-defined functions

ResetBitInTag Tag, Bit

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Tag**

The tag in which a bit is set to 0 (FALSE).

**Bit**

The number of the bit that is set to 0 (FALSE).

When this system function is used in a user-defined function, the bits in the specified tag will be counted from right to left independent of the PLC used. The counting begins with 0.

### Example

The following program code sets a bit to 0 at the specified bitposition in the bStatusWord tag and outputs the result along with the original bSaved value.

'Programming language: VB

Dim myTag

Dim myOutputField

Dim bValue, bSaved, bitposition, strResult

Set myTag = SmartTags("bStatusWord")

Set myOutputField=HMIRuntime.Screens("MyScreen").ScreenItems("objTextField")

'Save current value

bValue=myTag.Value

bSaved=bValue

'Reset Bit

bitposition=2

ResetBitInTag myTag, bitposition

bValue=myTag.Value

'Output result old and new value:

strResult="Old Value: "&amp;bSaved &amp;Chr(13)&amp;"New Value: "&amp;bValue

myOutputField.Text=strResult

//Programming language: C

{

BYTE bSaved;

BYTE bitposition = 2;

bSaved = GetTagByte("bStatusWord");

//Reset bit in bitposition

ResetBitInTag ("bStatusWord", bitposition);

//print current and saved value

printf ("Current value: %d\r\n, Saved value: %d\r\n",GetTagByte("bStatusWord"), bSaved);

  ...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## SetBit  (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Sets the value of a "Bool" type tag to 1 (TRUE).

### Use in the function list

SetBit (Tag)

### Use in user-defined functions

SetBit Tag

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Tag**

The BOOL type tag which is set to 1 (TRUE).

### Example

The following program code sets the value of the Boolean tag bStatus to 1 by means of the SetBit function and outputs the result along with the original bSaved value.

'Programming language: VB

Dim myTag

Dim myOutputField

Dim bValue, bSaved, strResult

Set myTag = SmartTags("bStatus")

Set myOutputField=HMIRuntime.Screens("MyScreen").ScreenItems("objTextField")

'Set value

bValue=0

myTag.Value=bValue

'Save current value

bSaved=bValue

'Set Bit

SetBit myTag

bValue=myTag.Value

'Output result old and new value:

strResult="Old Value: "&amp;bSaved &amp;Chr(13)&amp;"New Value: "&amp;bValue

myOutputField.Text=strResult

//Programming language: C

{

BOOL bStatus = 0;

BOOL bSaved = bStatus;

//Set bit

SetBit (bStatus);

//print current and saved value

printf ("Current value: %d\r\n, Saved value: %d\r\n",bStatus, bSaved);

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## SetBitInTag (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Sets a bit in the given tag to 1 (TRUE).

After changing the given bit, the system function transfers the entire tag back to the PLC. It is not checked whether other bits in the tags have changed in the meantime. Operator and PLC have read-only access to the indicated tag until it is transferred back to the PLC.

> **Note**
>
> If the PLC supports BOOL tags, do not use this system function. Use the "SetBit" system function instead.

### Use in the function list

SetBitInTag (Tag, Bit)

### Use in user-defined functions

SetBitInTag Tag, Bit

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Tag**

The tag in which a bit is set to 1 (TRUE).

**Bit**

The number of the bit that is set to 1 (TRUE).

When this system function is used in a user-defined function, the bits in the specified tag will be counted from right to left independent of the PLC used. The counting begins with 0.

> **Note**
>
> The guaranteed update of the tags used with actual process values is absolutely conditional in terms of reliable functionality. You should therefore configure the tag in an I/O field or assign the system function to a screen object, such as a button.
>
> If you have configured a short event such as the activation of an alarm for the system function you can only access the actual process values by setting the tag for continuous reading.

### Example

The following program code sets a bit to 1 at the specified bitposition in the bStatusWord tag and outputs the result along with the original bSaved value.

'Programming language: VB

Dim myTag

Dim myOutputField

Dim bValue, bSaved, bitposition, strResult

Set myTag = SmartTags("bStatusWord")

Set myOutputField=HMIRuntime.Screens("MyScreen").ScreenItems("objTextField")

'Save current value

bValue=myTag.Value

bSaved=bValue

'Set Bit in tag

bitposition=1

SetBitInTag "bStatusWord", bitposition

bValue=myTag.Value

'Output result old and new value:

strResult="Old Value: "&amp; bSaved &amp; "New Value: " &amp; bValue

myOutputField.Text=strResult

//Programming language: C

{

BYTE bSaved;

BYTE bitposition = 1;

bSaved = GetTagByte("bStatusWord");

//Reset bit in bitposition

SetBitInTag ("bStatusWord", bitposition);

//print current and saved value

printf ("Current value: %d\r\n, Saved value: %d\r\n",GetTagByte("bStatusWord"), bSaved);

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## SetLanguage (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Toggles the language on the HMI device. All configured text and system events are displayed on the HMI device in the newly set language.

### Use in the function list

SetLanguage (Language)

### Use in user-defined functions

SetLanguage Language

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameter

**Language**

Determines which language is set on the HMI device. The following specifications are possible:

- -1 (hmiToggle) = Toggle: Changes to the next language. The sequence is determined during configuration in the "Project languages" editor.
- Number you have defined under "Languages and fonts" in the "Runtime Settings" editor. Changes to the language with the given number.
- Language you have defined under "Languages and fonts" in the "Runtime Settings" editor.
- Language abbreviation in accordance with the VBScript5 reference: This changes to the language corresponding to the specified language code, e.g. "de-DE" for German (Germany) or "en-US" for English (United States).

  An overview of the language abbreviations is available in the basic information of VBScript under the topic "Area diagram-ID (LCID) Diagram".

## SetPropertyByConstant (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Specifies the value of an object property as a string.

### Use in the function list

SetPropertyByConstant (Screen name, screen object, name of the property, value)

### Use in user-defined functions

SetPropertyByConstant Screen_name, Screen_object, Property_name, Value

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

If you want to change the property of a screen, the parameter "Object" must be empty. For this purpose, use the following syntax, for example:

SetPropertyByConstant Screen_name, Property_name, Value

### Parameters

**Screen name**

Name of the screen that contains the object.

**Screen object**

Name of the object whose property is changed.

**Name of the property**

Name of the property that will be changed.

**Value**

The value assigned to the property.

### Example

The SetPropertyByConstant function is used in the following program code to change an object property: In the "Trends" screen, the "ToolbarButtonClick" property of the "Control_1" object is set to the value 26.

'Programming language: VBS

'Name of the picture: Trends

'Name of the f(t) trend view control: Control_1

SetPropertyByConstant "Trends", "Control_1", "ToolbarButtonClick", "26"

'User defined code

...

{

//Programming language: C

//Name of the picture: Trends

//Name of the f(t) trend view control: Control_1

SetPropertyByConstant ("Trends", "Control_1", "ToolbarButtonClick", "26");

// User defined code

...

}

### Example: Changing a screen property

The SetPropertyByConstant function is used in the following program code to change a screen property: In the "Trends" screen, the "Backcolor" property is set to the value 255.

'Programming language: VBS

'Name of the picture: Trends

SetPropertyByConstant "Trends", "Trends", "Backcolor", "255"

'User defined code

...

{

//Programming language: C

//Name of the picture: Trends

SetPropertyByConstant ("Trends", "Trends", "Backcolor", "255");

// User defined code

...

}

Alternatively, use the password ZERO or a space string instead of the second parameter (object).

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## SetPropertyByProperty (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Specifies the value of an object property with another object property.

### Use in the function list

SetPropertyByProperty (screen name, object, property name, target screen name, target screen object, target property name)

### Use in user-defined functions

SetPropertyByProperty Screen_name, Screen_object, Property_name, Source_screen_name, Source_screen_object, Source_property_name

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

If you want to specify the property of a screen with another screen property, the parameters "Object" and "Destination object" must be empty. For this purpose, use the following syntax, for example:

SetPropertyByProperty Screen_name, Property_name, Source_screen_name, Source_property_name

### Parameters

**Screen name**

Name of the screen that contains the object.

**Object**

Name of the object whose property value is transferred to the target object.

**Property name**

Name of the property whose value is transferred to the target object.

**Target screen name**

Name of the screen that contains the target object.

**Target screen object**

Name of the target object for which a property is changed.

**Target property name**

Name of the property that will be changed.

### Example

The following program code uses the SetPropertyByProperty function to set the property "ToolbarButtonClick" of the object "Control_1" in the original screen Trend_1": on the corresponding property in the destination screen "Trend_2".

'Programming language: VBS

'Name of source picture: Trend_1

'Name of target picture: Trend_2​

'Name of the f(t) trend view control: Control_1

SetPropertyByProperty "Trend_1", "Control_1", "ToolbarButtonClick", "Trend_2", "Control_2", "ToolbarButtonClick"

'User defined code

...

{

//Programming language: C

//Name of source picture: Trend_1

//Name of target picture: Trend_2​

//Name of the f(t) trend view control: Control_1

SetPropertyByProperty ("Trend_1", "Control_1", "ToolbarButtonClick", "Trend_2", "Control_2", "ToolbarButtonClick");

// User defined code

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## SetPropertyByTag (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Specifies the value of an object property with a tag value.

### Use in the function list

SetPropertyByTag (Screen name, screen object, name of the property, tag name)

### Use in user-defined functions

SetPropertyByTag Screen_name, Screen_object, Property_name, Tag_name

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

If you want to specify the property of a screen by means of a tag value, the "Object" parameter must be empty. For this purpose, use the following syntax, for example:

SetPropertyByTag Screen_name, Property_name, Tag_name

### Parameters

**Screen name**

Name of the screen that contains the object.

**Screen object**

Name of the object containing the property to be set with the tag value.

**Name of the property**

Name of the property that is set with the tag value.

**Tag name**

Name of the tag that contains the value of the property.

### Example

The SetPropertyByTag function is used in the following program code to change an object property: When you click on the object, the object name and the screen in which the object is located are transferred. The CaptionText in the screen window contains the value of the HMI_value_1 tag.

'Programming language: VBS

SetPropertyByTag screenName, objectName, "CaptionText", "HMI_value_1"

'User defined code

...

{

//Programming language: C

SetPropertyByTag (screenName, objectName, "CaptionText", "HMI_value_1");

// User defined code

...

}

### Example

The SetPropertyByTag function is used in the following program code to change an object property: In the "Trends" screen, the "ToolbarButtonClick" property of the "Control_1" object is set to the value 26.

'Programming language: VBS

'Name of the picture: Trends

'Name of the f(t) trend view control: Control_1

SetPropertyByConstant "Trends", "Control_1", "ToolbarButtonClick", "26"

'User defined code

...

{

//Programming language: C

//Name of the picture: Trends

//Name of the f(t) trend view control: Control_1

SetPropertyByConstant ("Trends", "Control_1", "ToolbarButtonClick", "26");

// User defined code

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## SetPropertyByTagIndirect (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Writes the value of an indirect addressed tag to an object property. The tag transferred as parameter contains the name of a second tag the value of which is read.

### Use in the function list

SetPropertyByTagIndirect (Screen name, screen object, name of the property, , tag name)

### Use in user-defined functions

SetPropertyByTagIndirect Screen_name, Screen_object, Property_name, Tag_name

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

If you want to specify the property of a screen by means of a tag, the "Object" parameter must be empty. For this purpose, use the following syntax, for example:

SetPropertyByTagIndirect Screen_name, Property_name, Tag_name

### Parameters

**Screen name**

Name of the screen that contains the object.

**Screen object**

Name of the object whose property you want to change.

**Name of the property**

Name of the property to be changed.

**Tag name**

Name of the tag which, in turn, contains the name of the tag whose value is read.

### Example

The SetPropertyByTagIndirect function is used in the following program code to change an object property: .

'Programming language: VBS

SetPropertyByTagIndirect GetParentScreen(screenName), GetParentScreenWindow(screenName), "ScreenName", "HMI_value_1"

'User defined code

...

{

//Programming language: C

SetPropertyByTagIndirect (GetParentScreen(screenName), GetParentScreenWindow(screenName), "ScreenName", "HMI_value_1");

// User defined code

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## SetTag (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Assigns a new value to the given tag.

> **Note**
>
> This system function can be used to assign strings and numbers, depending on the type of tag.

### Use in the function list

SetTag (Tag, Value)

### Use in user-defined functions

SetTag Tag, Value

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Tag**

The tag to which the given value is assigned.

**Value**

The value which the given tag is assigned.

> **Note**
>
> The "SetTag" system function is only executed after a connection has been established.

### Example

The following program code uses the SetTag function to set the value of the gs_tag_bit tag to TRUE and saves the return value to the ok tag.

{

BOOL ok;

BOOL bvalue;

//Set the tag to true

ok = SetTag("gs_tag_bit", TRUE);

//error handling

if(ok)

{

  // succeeded

  printf ( "Function has run through.\r\n" );

bvalue = GetTagBit("gs_tag_bit");

printf ("Value of gs_tag_bit: %d\r\n", bvalue);

}

else

{

  // failed

  printf ( "Error - function failed." );

}

...

}

The saved return value can be processed in the following code.

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## SetTagByProperty (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Specifies a tag value with the value of an object property. The change is also logged in the alarm system.

### Use in the function list

SetTagIndirectByProperty (tag name, screen name, screen object, name of the property, with or without operator event)

### Use in user-defined functions

SetTagByProperty Tag_name, Screen_name, Screen_object, Property_name, With_or_without_operator_event

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

### Parameters

**Tag name**

Name of the tag whose value is specified by the object property.

**Screen name**

Name of the screen that contains the object.

**Screen object**

Name of the object whose property supplies the tag value.

**Name of the property**

Name of the property that supplies the tag value.

**With or without operator event**

0 (hmiWithoutOperatorEvent) = Without operator event

1 (hmiWithOperatorEvent) = With operator event

### Example

The following program code returns the value of the selected text when you click in a combo box.

{

char* rt_value;

SetTagByProperty (rt_value, screenName, objectName, "SelectedText", hmiWithoutOperatorEvent);

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## SetTagByTagIndirect (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Writes the value of an indirect addressed tag to a tag. The tag transferred as parameter contains the name of a second tag the value of which is read. The change in the alarm system is logged via an operator input alarm.

### Use in the function list

SetTagIndirectByTagIndirect (name of the tag, tag name, with or without operator input alarm)

### Use in user-defined functions

SetTagByTagIndirect Tag_name, Source_tag_name, With_or_without_operator_event

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

### Parameters

**Name of the tag**

Name of the tag whose value is to be set.

**Tag name**

Name of a string tag which contains the name of a tag which supplies the tag value.

**With or without operator event**

0 (hmiWithoutOperatorEvent) = Without operator input alarm

1 (hmiWithOperatorEvent) = With operator input alarm

### Example

The following program code writes the value of the tag Tag4 to the tag Tag1.

{

SetTag ("IndirectRead", "Tag4");

SetTagByTagIndirect ("Tag1", "IndirectRead", hmiWithoutOperatorEvent);

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## SetTagIndirect (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Writes a value to an indirect addressed tag. The tag transferred as output parameter contains the name of a second tag the value of which is changed by the function. The change in the alarm system is logged via an operator input alarm.

### Use in the function list

SetTagIndirect (tag name, , value, with or without operator event)

### Use in user-defined functions

SetTagIndirect Tag_name, Value, With_or_without_operator_event

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

### Parameters

**Tag name**

Name of a string tag which contains the name of a tag whose value is to be changed.

**Value**

Value which is to be written.

**With or without operator event**

0 (hmiWithoutOperatorEvent) = Without operator event

1 (hmiWithOperatorEvent) = With operator event

### Example

The following program code writes the value "value" to the tag Tag3.

{

int value;

SetTag ("IndirectWrite", "Tag3");

SetTagIndirect ("IndirectWrite", "value", hmiWithoutOperatorEvent);

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## SetTagIndirectByProperty (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Writes the value of an object property to an indirectly addressed tag. The tag transferred as output parameter contains the name of a second tag the value of which is changed by the function. The change in the alarm system is logged via an operator input alarm.

### Use in the function list

SetTagIndirectByProperty (Tag name, Screen name, Screen object, Name of the property, With or without operator event)

### Use in user-defined functions

SetTagIndirectByProperty Tag_name, Screen_name, Screen_object, Property_name, With_or_without_operator_event

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

### Parameters

**Tag name**

Name of a string tag which contains the name of a tag whose value is to be changed.

**Screen name**

Name of the screen that contains the object.

**Screen object**

Name of the object whose property supplies the value.

**Name of the property**

Name of the property which supplies the value.

**With or without operator event**

0 (hmiWithoutOperatorEvent) = Without input alarm

1 (hmiWithOperatorEvent) = With operator input alarm

### Example

The following program code writes the value of the object property "Background color" to the tag Tag2.

{

SetTag ("IndirectWrite", "Tag2");

SetTagIndirectByProperty ("IndirectWrite", screenName, objectName, "BackColor", hmiWithoutOperatorEvent);

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## SetTagIndirectByTagIndirect (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Writes the value of an indirectly addressed tag to an indirectly addressed tag. The tag transferred as output parameter contains the name of a second tag the value of which is changed by the function. The tag transferred as parameter contains the name of a second tag the value of which is read. The change in the alarm system is logged via an operator input alarm.

### Use in the function list

SetTagIndirectByTagIndirect (Tag name, Tag name, With or without operator input alarm)

### Use in user-defined functions

SetTagIndirectByTagIndirect Tag_name, Source_tag_name, With_or_without_operator_event

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

### Parameters

**Tag name**

Name of a string tag which contains the name of a tag whose value is to be changed.

**Tag name**

Name of the indirect tag that returns the tag value.

**With or without operator event**

0 (hmiWithoutOperatorEvent) = Without operator event

1 (hmiWithOperatorEvent) = With operator event

### Example

The following program code writes the value of the tag "Tag4" to the tag "Tag2".

{

SetTag ("IndirectWrite", "Tag2");

SetTag ("IndirectRead", "Tag4");

SetTagIndirectByTagIndirect ("IndirectWrite", "IndirectRead");

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## SetTagWithOperatorEvent (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Specifies the value for a tag. The change is also logged in the alarm system.

### Use in the function list

SetTagWithOperatorEvent (name of the tag, value)

### Use in user-defined functions

SetTagWithOperatorEvent Tag_name, Value

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

### Parameters

**Name of the tag**

Name of the tag whose value is to be set.

**Value**

Value written to the tag.

### Example

The following program code transfers the value from the "value" tag to the "result" tag when you click the corresponding button.

'Programming language: VBS

SetTagWithOperatorEvent result, value

...

//Programming language: C

{

SetTagWithOperatorEvent ("result", "value");

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## ShowBlockInTIAPortalFromAlarm (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Switches from the alarm view to the affected program code of the selected project in the engineering system. Changing from the alarm view to the project in the TIA Portal enables further analysis of the program code, for example, search for a missing contact in the interlock.

You configure this system function at a screen object, for example, a button or a button of the toolbar in an alarm view. When you click the button, the necessary context is stored by the system and the corresponding location is automatically displayed in the program code after switching to the engineering system. You use the Write protection parameter to specify which authorization is required to enable the switch to the engineering system.

If you have configured the system function to a button, the TIA Portal is started in the mode that was specified with the write protection parameter. To enable different levels of security when accessing the system function, configure the buttons with two different authorizations:

- For the first button, configure the authorization for unlimited access by setting the write protection parameter to FALSE.
- For the second button, configure the authorization so that data cannot be changed by setting the write protection parameter to TRUE.

### Use in the function list

ShowBlockInTiaPortalFromAlarm (write protection, offline mode, TIA Portal project path, screen name of alarm view, name of alarm view, error tag)

### Use in user-defined functions

ShowBlockInTIAPortalFromAlarm ReadOnly, Offline_mode, TiaPortalProject_path, AlarmScreen_name, AlarmView_name, Error_tag

Can be used if the configured device supports user-defined functions. For more information, refer to "System functions for Runtime Professional".

### Parameters

****Write protection****

Specifies whether the project is opened in read-only mode.

TRUE (default): TIA Portal is opened in read mode, the user cannot make any changes.

FALSE: TIA Portal is opened with read and right authorization.

****Offline mode****

Specifies whether the project is opened in offline mode.

TRUE: The TIA Portal does not go to online mode after the block is opened.

FALSE (default): Online mode is started after the block is opened.

****TIA Portal project path****

Path and file name of the project in the TIA Portal to which you change from the alarm view.

****Screen name of the alarm view****

Name of the screen that contains the alarm view.

****Alarm view name****

Object name of the alarm view to which you change from the TIA Portal.

**Error tag**

If an error occurs, information about the error is provided by the error tag.

## ShowLogonDialog (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Opens a dialog on the HMI device with which the user can log on to the HMI device.

### Use in the function list

ShowLogonDialog

### Use in user-defined functions

ShowLogonDialog

Can be used if the configured device supports user-defined functions. Additional information is available under "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

### Parameters

--

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

## ShowPLCCodeViewFromAlarm (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Switches from the alarm view with the selected ProDiag alarm or selected GRAPH alarm to the PLC code view with the respective network. The screen that contains the PLC code view is either opened in a root screen or in a screen window. No commas are permitted in the name of the PLC from which the alarm originates.

### Use in the function list

ShowPLCCodeViewFromAlarm (alarm screen name, alarm view name, basic screen name, screen window name, screen name of the PLC code view, name of the PLC code view, error tag)

### Use in user-defined functions

ShowPLCCodeViewFromAlarm Screen_name, Alarmview_name, Screen_name, Screen_window_name, Screen_name, PLCCodeView_name, Error_tag

Can be used if the configured device supports user-defined functions. For more information, refer to "System functions for Runtime Professional".

### Parameters

****Alarm screen name****

Name of the screen that contains the alarm view.

****Alarm view name****

Object name of the alarm view from which the selected alarm is transferred.

****Basic screen name****

Name of the screen which includes a screen window in which the screen can be displayed.

****Screen window name****

Name of the screen window in which the screen with the PLC code view can be displayed.

****Screen name of the PLC code view****

Name of the screen that contains the PLC code view.

****Name of the PLC code view****

Object name of the PLC code view.

****Error tag****

If an error occurs, information about the error is provided by the error tag.

### Error messages

The following errors can be reported back using the error tag:

| Symbol | Meaning |
| --- | --- |
| KOPAPI_E_TPSF_ALGCTRL_NOTSELECTED | Exactly one alarm must be selected |
| KOPAPI_E_TPSF_ONLYONLINELISTALLOWED | Only select alarms from the alarm list of the alarm view |
| KOPAPI_E_TPSF_ONALARMWRONGPRODUCERID | No GRAPH/ProDiag alarm selected |
| KOPAPI_E_TPSF_ONALARMNOSD0JUMPFLAG | It is not possible to jump over this GRAPH/ProDiag alarm.  The jump from an alarm in the alarm view to the PLC code view is made possible for the following supervision alarms:  - With global supervisions, only for interlock supervisions (Interlock) - With local supervisions, for all basic supervisions at input parameters |

## StopRuntime (Panels, Comfort Panels, RT Advanced, RT Professional)

### Description

Exits the runtime software and thereby the project running on the HMI device.

### Use in the function list

StopRuntime (Mode)

### Use in user-defined functions

StopRuntime Mode

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

### Parameters

**Mode**

Determines whether the operating system is shut down after exiting runtime.

0 (hmiStopRuntime) = Runtime: Operating system is not shut down

1 (hmiStopRuntimeAndOperatingSystem) = Runtime and operating system: The operating system is shut down (not possible with WinCE)

### Example

The following program code shuts down Runtime and the operating system.

{

//Stop runtime and shutdown

StopRuntime (hmiStopRuntimeAndOperationSystem);

}

The saved return value can be processed in the following code.

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)
