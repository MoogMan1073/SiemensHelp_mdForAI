---
title: "C scripting (RT Professional)"
package: CReferenceWCCPenUS
topics: 157
devices: [RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# C scripting (RT Professional)

This section contains information on the following topics:

- [System functions (RT Professional)](#system-functions-rt-professional)
- [C-bib (RT Professional)](#c-bib-rt-professional)
- [Structure definition (RT Professional)](#structure-definition-rt-professional)

## System functions (RT Professional)

This section contains information on the following topics:

- [ActivateNextScreen (RT Professional)](#activatenextscreen-rt-professional)
- [ActivatePreviousScreen (RT Professional)](#activatepreviousscreen-rt-professional)
- [ActivateScreen (RT Professional)](#activatescreen-rt-professional)
- [ActivateScreenInScreenWindow (RT Professional)](#activatescreeninscreenwindow-rt-professional)
- [ActivateStartScreen (RT Professional)](#activatestartscreen-rt-professional)
- [ActivateStoredScreen (RT Professional)](#activatestoredscreen-rt-professional)
- [DateToSystemTime (RT Professional)](#datetosystemtime-rt-professional)
- [DecreaseTag (RT Professional)](#decreasetag-rt-professional)
- [GetLink (RT Professional)](#getlink-rt-professional)
- [GetLinkedTag (RT Professional)](#getlinkedtag-rt-professional)
- [GetLocalScreen (RT Professional)](#getlocalscreen-rt-professional)
- [GetLanguageByLocaleID (RT Professional)](#getlanguagebylocaleid-rt-professional)
- [GetParentScreen (RT Professional)](#getparentscreen-rt-professional)
- [GetParentScreenWindow (RT Professional)](#getparentscreenwindow-rt-professional)
- [GetProp (RT Professional)](#getprop-rt-professional)
- [GetServerTagPrefix (RT Professional)](#getservertagprefix-rt-professional)
- [GetTag (RT Professional)](#gettag-rt-professional)
- [IncreaseTag (RT Professional)](#increasetag-rt-professional)
- [InquireLanguage (RT Professional)](#inquirelanguage-rt-professional)
- [InverseLinearScaling (RT Professional)](#inverselinearscaling-rt-professional)
- [InvertBit (RT Professional)](#invertbit-rt-professional)
- [InvertBitInTag (RT Professional)](#invertbitintag-rt-professional)
- [IsUserAuthorized (RT Professional)](#isuserauthorized-rt-professional)
- [LinearScaling (RT Professional)](#linearscaling-rt-professional)
- [ReportJob (RT Professional)](#reportjob-rt-professional)
- [ResetBit (RT Professional)](#resetbit-rt-professional)
- [ResetBitInTag (RT Professional)](#resetbitintag-rt-professional)
- [Set_Focus (RT Professional)](#set_focus-rt-professional)
- [SetBit (RT Professional)](#setbit-rt-professional)
- [SetBitInTag (RT Professional)](#setbitintag-rt-professional)
- [SetLanguageByLocaleID (RT Professional)](#setlanguagebylocaleid-rt-professional)
- [SetLanguageByName (RT Professional)](#setlanguagebyname-rt-professional)
- [SetLink (RT Professional)](#setlink-rt-professional)
- [SetProp (RT Professional)](#setprop-rt-professional)
- [SetPropertyByConstant (RT Professional)](#setpropertybyconstant-rt-professional)
- [SetPropertyByProperty (RT Professional)](#setpropertybyproperty-rt-professional)
- [SetPropertyByTag (RT Professional)](#setpropertybytag-rt-professional)
- [SetPropertyByTagIndirect (RT Professional)](#setpropertybytagindirect-rt-professional)
- [SetTag (RT Professional)](#settag-rt-professional)
- [StartProgram (RT Professional)](#startprogram-rt-professional)
- [StopRuntime (RT Professional)](#stopruntime-rt-professional)
- [StoreScreen (RT Professional)](#storescreen-rt-professional)
- [SystemTimeToDate (RT Professional)](#systemtimetodate-rt-professional)
- [TriggerOperatorEvent (RT Professional)](#triggeroperatorevent-rt-professional)
- [UA (Recipe) (RT Professional)](#ua-recipe-rt-professional)

### ActivateNextScreen (RT Professional)

#### Description

WinCC saves the names of the screens opened by the user during runtime as well as the sequence in which these screens were opened.

Can only be used in C scripting.

The maximum size of the screen buffer is specified in the "Runtime settings > Screens > Screen buffer" editor.

The ActivateNextScreen system function now opens the screen that was opened before the last call of ActivatePreviousScreen.

#### Syntax

BOOL ActivateNextScreen();

#### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

#### Example

The ActivateNextScreen function is used in the following program code to call the next screen and to save the return value to the b_error tag.

The saved return value can be processed in the following code.

{

BOOL b_error;

//Open next screen

b_error = ActivateNextScreen();

if(b_error)

{

// User defined code if

// function succeeds without error

...

}

else

{

// User defined code in case of error

...

}

...

}

### ActivatePreviousScreen (RT Professional)

#### Description

WinCC saves the names of the screens opened by the user during runtime as well as the sequence in which these screens were opened.

The system function can be used in C scripting only.

The maximum size of the screen buffer is specified in the "Runtime settings > Screens > Screen buffer" editor.

The ActivatePreviousScreen system function now opens the screen which was open before the currently open screen.

#### Syntax

BOOL ActivatePreviousScreen();

#### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

#### Example

The ActivatePreviousScreen function is used in the following program code to call the previous screen and to save the return value to the b_error tag.

The saved return value can be processed in the following code.

{

BOOL b_error;

//Open previous screen

b_error = ActivatePreviousScreen();

if(b_error)

{

// User defined code if

// function succeeds without error

...

}

else

{

// User defined code in case of error

...

}

...

}

### ActivateScreen (RT Professional)

#### Description

Performs a screen change to the given screen.

Use the "ActivateScreenByNumber" system function to change from the root screen to the permanent area or vice versa.

#### Use in the function list

ActivateScreen (Screen name, Object number)

#### Use in user-defined functions

ActivateScreen Screen_name, Object_number

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

#### Parameters

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

#### Example

The following program code activates "Screen_2" with the ActivateScreen function, for example, when you click a button.

`Sub ActivateScreen_2()`

`'User-defined code`

`'' i. e. when pressing a button`

`ActivateScreen "Screen_2",0`

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

### ActivateScreenInScreenWindow (RT Professional)

#### Description

Performs a screen change to the specified screen in a specified screen window.

#### Use in the function list

ActivateScreenInScreenWindow (Screen name, Screen window, New screen name)

#### Use in user-defined functions

ActivateScreenInScreenWindow Screen_name, Screen_window, New_screen_name

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

#### Parameters

**Screen name**

Name of the screen to be displayed in the screen window.

**Screen window**

Name of the screen window in which the new screen is to be displayed.

**New screen name**

Name of the new screen to be displayed in the screen window.

#### Example

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
  
[Example of configuring a screen change via a property (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#example-of-configuring-a-screen-change-via-a-property-rt-professional-1)

### ActivateStartScreen (RT Professional)

#### Description

Opens the configured start screen.

Can only be used in C scripting.

#### Syntax

BOOL ActivateStartScreen();

#### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

#### Example

The ActivateStartScreen function is used in the following program code to call the configured start screen and to save the return value to the b_error tag.

The saved return value can be processed in the following code.

{

BOOL b_error;

//Open start screen

b_error = ActivateStartScreen();

if(b_error)

{

// User defined code if

// function succeeds without error

...

}

else

{

// User defined code in case of error

...

}

...

}

### ActivateStoredScreen (RT Professional)

#### Description

Opens the screen saved with the StoreScreen system function.

Can only be used in C scripting.

#### Syntax

BOOL ActivateStoredScreen();

#### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

#### Example

The ActivateStoredScreen function is used in the following program code to call the stored screen and to save the return value to the b_error tag.

The saved return value can be processed in the following code.

{

BOOL b_error;

//Open stored screen

b_error = ActivateStoredScreen();

if(b_error)

{

// User defined code if

// function succeeds without error

...

}

else

{

// User defined code in case of error

...

}

...

}

---

**See also**

[StoreScreen (RT Professional)](#storescreen-rt-professional)

### DateToSystemTime (RT Professional)

#### Description

Converts a date-clock time specification in DATE format into the SYSTEMTIME data format.

Can only be used in C scripting.

#### Use in the function list

DateToSystemTime (Value, Pointer to Date/Time)

#### Syntax

DateToSystemTime(Value, PointerToTime);

#### Parameters

**Value**

Value in DATE data format

**PointerToTime**

Pointer to the result in the SYSTEMTIME format

#### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

#### Example

BOOL BRet;

SYSTEMTIME st_1, st_2;

DATE       d_1, d_2;   // wtypes.h.  DATE type. Visual Studio documnetation.

GetSystemTime( &st_1 );

printf( "st_1.wYear = %d \r\n", st_1.wYear );

printf( "st_1.wMonth = %d \r\n", st_1.wMonth );

printf( "st_1.wDayOfWeek = %d \r\n", st_1.wDayOfWeek );

printf( "st_1.wDay = %d \r\n", st_1.wDay );printf( "st_1.wHour = %d \r\n", st_1.wHour );

printf( "st_1.wMinute = %d \r\n", st_1.wMinute );

printf( "st_1.wSecond = %d \r\n", st_1.wSecond );

printf( "st_1.wMilliseconds = %d \r\n", st_1.wMilliseconds );

BRet = SystemTimeToDate( st_1, &d_1 );

printf( "DATE d = %ld \r\n \r\n", d_1 );

printf( "DATE d = %lf \r\n \r\n", d_1 );

printf( "DATE d = %f \r\n \r\n", d_1 );

BRet = DateToSystemTime( d_1, &st_2 );

printf( "st_2.wYear = %d \r\n", st_2.wYear );

printf( "st_2.wMonth = %d \r\n", st_2.wMonth );

printf( "st_2.wDayOfWeek = %d \r\n", st_2.wDayOfWeek );

printf( "st_2.wDay = %d \r\n", st_2.wDay );

printf( "st_2.wHour = %d \r\n", st_2.wHour );

printf( "st_2.wMinute = %d \r\n", st_2.wMinute );

printf( "st_2.wSecond = %d \r\n", st_2.wSecond );

printf( "st_2.wMilliseconds = %d \r\n \r\n \r\n", st_2.wMilliseconds );

### DecreaseTag (RT Professional)

#### Description

Subtracts the given value from the tag value.

X = X - a

> **Note**
>
> The system function uses the same tag as input and output values. When this system function is used to convert a value, auxiliary tags must be used. You can use the "SetTag" system function to assign the tag value to the auxiliary tags.

If you configure the system function for events of an alarm and the tag is not being used in the current screen, it is not ensured that the actual tag value is being used in the PLC. You can improve the situation by setting the "Cyclic continuous" acquisition mode.

#### Use in the function list

DecreaseTag (Tag, Value)

#### Use in user-defined functions

DecreaseTag Tag, Value

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

#### Parameters

**Tag**

The tag from which the given value is subtracted.

**Value**

The value which is subtracted.

#### Example

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

### GetLink (RT Professional)

#### Function

Indicates the current tag connection of object properties.

#### Syntax

BOOL GetLink(LPCTSTR lpszPictureName, LPCTSTR lpszObjectName, LPCTSTR lpszPropertyName, LPLINKINFO *pLink);

#### Parameter

**lpszPictureName**

Screen name

**lpszObjectName**

Object name

**lpszPropertyName**

Object property

**pLink**

Pointer to a structure of the type: LINKINFO

#### Return value

**TRUE**

The function has been completed without any errors.

**FALSE**

An error has occurred.

---

**See also**

[Structure definition LINKINFO (RT Professional)](#structure-definition-linkinfo-rt-professional)

### GetLinkedTag (RT Professional)

#### Description

Returns the name of the tag which is logically linked to the specified object property.

Can only be used in C scripting.

#### Syntax

char* GetLinkedTag(ScreenName, Object, NameOfProperty);

#### Parameters

**ScreenName**

Pointer to the name of the screen.

**Object**

Pointer to the name of the object.

**NameOfProperty**

Pointer to the name of the object property.

#### Return value

Pointer to the name of the tag which is logically linked to the specified object property.

> **Note**
>
> **Return value for user data types on the faceplate**
>
> If a user data type is directly interconnected on the faceplate, no tag name is returned. A tag name is only returned if the structure elements of the user data type are interconnected individually on the faceplate.

#### Example

The following program code saves the return value of function "GetLinkedTag" to the "pszVarName" tag. If the return value is valid, it is saved with the maximum path length to the szVAarName tag. The saved return value can be processed in a following code.

char CFunktion()

{

char* pszVarName = NULL;

char szVarName[_MAX_PATH+1]; //Get the TagName

pszVarName = GetLinkedVariable("gs_stand_graph_00","Textfield6","Visible"); //Copy the string

if (strcmp (pszVarName,"")!= 0)

{

strncpy(szVarName,pszVarName,_MAX_PATH);

}

else printf("The property 'visible' is not dynamized\r\n");

//User defined code where the

//user can do something with the returnvalue

...

}

---

**See also**

[Configuring a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)

### GetLocalScreen (RT Professional)

#### Description

Returns a pointer to the screen name.

Can only be used in C scripting.

#### Syntax

char* GetLocalScreen(ScreenName);

#### Parameters

**ScreenName**

Pointer to the name of the screen.

#### Return value

Pointer to the name of the screen.

> **Note**
>
> The syntax of the transferred call parameter "ScreenName" must correspond to that formed by the graphics system for the screen paths:
>
> <Screen_name>.<Screen_window_name>:<Screen_name>.<Screen_window_name>:<Screen_name>...

#### Principle

A "Screen_A" contains a "Screen_window_B". Another screen is called in the screen window and visualized as minimized image, etc.

**Calling screens in the screen windows**

1. "Screen_window_B" displays "Screen_C".

   "Screen_C" contains "Screen_window_D".
2. "Screen_window_D" displays "Screen_E".

**Pointer to the screen name**

Returns the system function `GetLocalScreen(ScreenName)` in the next step with the following values:

- "Screen_E", if the system function is called in "Screen_E"
- "Screen_C", if the system function is called in "Screen_C"
- "Screen_A", if the system function is called in "Screen_A"

#### Example

The following program code saves the return value of the function GetLocalScreen to the pszScrName tag. If the return value is valid (not NULL), it is saved with maximum_MAX_PATH characters to the szScrName tag.

{

char* pszScrName = NULL;

char szScrName[_MAX_PATH+1];

//Get the Local Screen

pszScrName = GetLocalScreen(lpszScreenName);

//Copy the string

if (pszScrName != NULL)

{

  strncpy(szScrName,pszScrName,_MAX_PATH);

// print local screen name

printf ("Local screen name: %s\r\n", szScrName);

}

...

}

### GetLanguageByLocaleID (RT Professional)

#### Description

Determines the current Runtime language.

Can only be used in C scripting.

#### Syntax

DWORD GetLanguageByLocaleID ();

#### Return value

Language ID.

The following assignments apply (hexadecimal language code):

| Symbolic name | Value(hexadecimal) | Abbreviation |
| --- | --- | --- |
| LANG_ARABIC | 0x0401 |  |
| LANG_AFRIKAANS | 0x0436 |  |
| LANG_ALBANIAN | 0x041C |  |
| LANG_BASQUE | 0x042D |  |
| LANG_BULGARIAN | 0x0402 |  |
| LANG_BYELORUSSIAN | 0x0423 |  |
| LANG_CATALAN | 0x0403 |  |
| LANG_CHINESE | 0x0804 |  |
| LANG_CROATIAN | 0x041A |  |
| LANG_CZECH | 0x0405 | CSY |
| LANG_DANISH | 0x0406 | DAN |
| LANG_DUTCH | 0x0413 | NLD |
| LANG_ENGLISH | 0x0409 | ENU |
| LANG_ESTONIAN | 0x0425 |  |
| LANG_FAEROESE | 0x0438 |  |
| LANG_FARSI | 0x0429 |  |
| LANG_FINNISH | 0x040B | FIN |
| LANG_FRENCH | 0x040C | FRA |
| LANG_GERMAN | 0x0407 | DEU |
| LANG_GREEK | 0x0408 |  |
| LANG_HEBREW | 0x040D |  |
| LANG_HUNGARIAN | 0x040E | HUN |
| LANG_ICELANDIC | 0x040F | ISL |
| LANG_INDONESIAN | 0x0421 |  |
| LANG_ITALIAN | 0x0410 | ITA |
| LANG_JAPANESE | 0x0411 |  |
| LANG_KOREAN | 0x0412 |  |
| LANG_LATVIAN | 0x0426 |  |
| LANG_LITHUANIAN | 0x0427 |  |
| LANG_NORWEGIAN | 0x0414 | NOR |
| LANG_POLISH | 0x0415 | PLK |
| LANG_PORTUGUESE | 0x0416 | PTB |
| LANG_ROMANIAN | 0x0418 |  |
| LANG_RUSSIAN | 0x0419 | RUS |
| LANG_SLOVAK | 0x041B | SKY |
| LANG_SLOVENIAN | 0x0424 |  |
| LANG_SORBIAN | 0x042E |  |
| LANG_SPANISH | 0x040A | ESP |
| LANG_SWEDISH | 0x041D | SVE |
| LANG_THAI | 0x041E |  |
| LANG_TURKISH | 0x041F | TRK |
| LANG_UKRAINIAN | 0x0422 |  |

#### Example

The following program code reads out the current Runtime language and saves the return value in the rt_language tag.

The saved return value can be processed in the following code (in this case, with printf output).

{

DWORD rt_language;

//Get the current language

rt_language = GetLanguageByLocaleID ();

//print language code

printf ("Language code: %d\r\n", rt_language);

...

}

### GetParentScreen (RT Professional)

#### Description

The function determines the name of the parent screen from a specified screen path.

Can only be used in C scripting.

#### Syntax

char* GetParentScreen(ScreenName);

#### Parameters

**ScreenName**

Pointer to the name of the screen. The syntax of the transferred call parameter Screen name must correspond to that formed by the graphics system for the screen paths:

<Screen_name>.<Screen_window_name>:<Screen_name>.<Screen_window_name>:<Screen_name>...

> **Note**
>
> The "." character is used to distinguish between screen and screen object names. The ":" character is used for the hierarchy structuring. Therefore, use only the "-" or "_" as a delimiter in the name designations.

#### Return value

Name of the parent screen.

#### Principle

A "Screenwindow_1" screen window is in a "Screen_1" screen. In the screen window, the screen becomes "Screen_2" with the "Screenwindow_2" screen window, etc.

Screen path: Screen_1.Screenwindow_1:Screen_2.Screenwindow_2:Screen_3

GetParentScreen returns:

- "Screen_2", if the system function is called in the "Screen_3" screen.
- "Screen_1", if the system function is called in the "Screen_2" screen.

GetParentScreenwindow returns:

- "Screenwindow_2", if the system function is called in the "Screen_3" screen.
- "Screenwindow_1", if the system function is called in the "Screen_2" screen.

#### Example

The following program code saves the return value of function GetParentScreen to the pszScrName tag. If the return value is valid (not NULL), it is saved with maximum_MAX_PATH characters to the szScrName tag.

{

char* pszScrName = NULL;

char szScrName[_MAX_PATH+1];

//Get the Parent Screen

pszScrName = GetParentScreen(lpszScreenName);

//Copy the string

if (pszScrName != NULL)

{

  strncpy(szScrName,pszScrName,_MAX_PATH);

// print Screen name

printf ("Screen name: %s\r\n", szScrName);

}

...

}

### GetParentScreenWindow (RT Professional)

#### Description

The function determines the name of the parent screen window from a transferred screen path.

Can only be used in C scripting.

#### Syntax

char* GetParentScreenWindow(ScreenName);

#### Parameters

**ScreenName**

Pointer to the name of the screen. The syntax of the transferred Screen name call parameter must correspond to that formed by the graphics system for the screen paths:

<Screen name>.<screen window name>:<screen name>.<screen window name>:<screen name>...The "." character is used to distinguish between screen and screen object names. The ":" character is used for the hierarchy structuring. Therefore, use only the "-" or "_" as a delimiter in the name designations.

> **Note**
>
> The "." character is used to distinguish between screen and screen object names. The ":" character is used for the hierarchy structuring. Therefore, use only the "-" or "_" as a delimiter in the name designations.

#### Return value

Name of the parent screen window.

#### Principle

A "Screenwindow_1" screen window is in a "Screen_1" screen. In the screen window, the screen becomes "Screen_2" with the "Screenwindow_2" screen window, etc.

Screen path: Screen_1.Screenwindow_1:Screen_2.Screenwindow_2:Screen_3

GetParentScreen returns:

- "Screen_2", if the system function is called in the "Screen_3" screen.
- "Screen_1", if the system function is called in the "Screen_2" screen.

GetParentScreenwindow returns:

- "Screenwindow_2", if the system function is called in the "Screen_3" screen.
- "Screenwindow_1", if the system function is called in the "Screen_2" screen.

#### Example

The following program code saves the return value of the function GetParentScreenWindow to the pszScrName tag. If the return value is valid (not NULL), it is saved with maximum_MAX_PATH characters to the szScrName tag.

{

char* pszScrName = NULL;

char szScrName[_MAX_PATH+1];

//Get the Parent Screen Window

pszScrName = GetParentScreenWindow(lpszScreenName);

//Copy the string

if (pszScrName != NULL)

{

  strncpy(szScrName,pszScrName,_MAX_PATH);

// print name of the parent screen window

printf ("Parent screen window: %s\r\n", szScrName);

}

...

}

### GetProp (RT Professional)

This section contains information on the following topics:

- [GetPropBOOL (RT Professional)](#getpropbool-rt-professional)
- [GetPropChar (RT Professional)](#getpropchar-rt-professional)
- [GetPropDouble (RT Professional)](#getpropdouble-rt-professional)
- [GetPropLong (RT Professional)](#getproplong-rt-professional)

#### GetPropBOOL  (RT Professional)

##### Description

Returns the current status of a property of data type "BOOL".

Can only be used in C scripting.

##### Syntax

BOOL GetPropBOOL(ScreenName, Object, NameOfTheProperty)

##### Parameters

**ScreenName**

Screen name

**Object**

Object name You must set the parameter Object = NULL if the function call relates to a screen object property.

**NameOfTheProperty**

Name of the object property

##### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

##### Example

The following program code reads out whether the object is visible or not. The value is saved to the b_error tag.

{

BOOL b_error;

//Get the property Visible of object IOField1 in screen gs_graph_iofield

b_error = GetPropBOOL("gs_graph_iofield","IOField1","Visible");

if(b_error)

{

  // User defined code if the

  // object is visible

  ...

}

else

{

  // User defined code if the

  // object is not visible

  ...

}

}

A specific code is processed, depending on the return value.

#### GetPropChar (RT Professional)

##### Description

Returns the value of a property of data type "Char".

Can only be used in C scripting.

##### Syntax

Char* GetPropChar(ScreenName, Object, NameOfTheProperty)

##### Parameters

**ScreenName**

Screen name

**Object**

Object name You must set the parameter Object = NULL if the function call relates to a screen object property.

**NameOfTheProperty**

Name of the object property

##### Return value

Value of the property in data type "Char".

##### Example

The following program code reads the tooltip text from the object using the GetPropChar function and processes it as follows:

1. Saving the return value to the pszProp tag
2. Validation of the return value: Step 3 follows if the value is valid (not NULL).
3. The first 13 characters of the character sequence are saved in the szProp tag.

{

char* pszProp = NULL;

char szProp[14];

//Get the property Tooltiptext of object IOField1 in screen Screen_1

pszProp = GetPropChar("Screen_1","IOField1","Tooltiptext");

if(pszProp != NULL)

{

//Copy the string and trim

strncpy(szProp,pszProp,13);

// print trimmed string

printf ("Short description of tooltip: %s\r\n", szProp);

}

...

}

The saved return value can be processed in the following code.

#### GetPropDouble (RT Professional)

##### Description

Returns the value of a property of data type "Double".

Can only be used in C scripting.

##### Syntax

double GetPropDouble(ScreenName, Object, NameOfTheProperty)

##### Parameters

**ScreenName**

Screen name

**Object**

Object name You must set the parameter Object = NULL if the function call relates to a screen object property.

**NameOfTheProperty**

Name of the object property

##### Return value

Value of the property in data type "Double".

##### Example

The following program code reads the "BackColor" property (background color of the "Button_1" object) by means of GetPropDouble function and processes the return value as follows:

1. Saving the return value to the szprop tag
2. Validation of the return value: Step 3 follows if the value is valid (not NULL).
3. Output of the background color

{

double szProp = NULL;

//Get the property Backcolor of object Button_1 in screen Screen_1

szProp = GetPropDouble("Screen_1","Button_1","BackColor");

if(szProp != NULL)

{

// print output value

printf ("Background color: %s\r\n", szProp);}

}

...

}

#### GetPropLong (RT Professional)

##### Description

Returns the value of a property of data type "long".

Can only be used in C scripting.

##### Syntax

long GetPropLong(ScreenName, Object, NameOfTheProperty)

##### Parameters

**ScreenName**

Screen name

**Object**

Object name You must set the parameter Object = NULL if the function call relates to a screen object property.

**NameOfTheProperty**

Name of the object property

##### Return value

Value of the property in data type "long".

##### Example

The following program code reads the CaptionBackColor property (background color of the TemperatureField object) by means of GetPropLong function and processes the return value as follows:

1. Saving the return value to the szProp tag
2. Validation of the return value: Step 3 follows if the value is valid (not NULL).
3. Output

{

long szProp = NULL;

//Get the property CaptionBackColor of object TemperatureField in screen Screen_1

szProp = GetPropLong("Screen_1","TemperatureField","CaptionBackColor");

if(szProp != NULL)

{

// print caption

printf ("Caption of window: %d\r\n", szProp);

}

...

}

The saved return value can be processed in the following code.

### GetServerTagPrefix (RT Professional)

#### Description

In order for a WinCC client in a distributed system to access tags of the associated server, the tag names must be expanded to include the server prefix.

> **Note**
>
> This system function is not supported at present.

A pointer of type "char" to server prefix, tag prefix, and window prefix is returned in each case.

The user is not permitted to change the memory (including no strcat) or release it.

Can only be used in C scripting.

#### Syntax

void GetServerTagPrefix(ppszServerPrefix, ppszTagPrefix, ppszWindowPrefix);

#### Return value

**ppszServerPrefix**

Pointer to a pointer that references the server prefix

**ppszTagPrefix**

Pointer to a pointer that references the tag prefix

**ppszWindowPrefix**

Pointer to a pointer that references the window prefix

#### Example

The following program code retrieves the **server prefix**, **tag prefix** and **window prefix** checks their validity. If an error occurs, a text is output and the function is exited. If the check is successful a tag name is created and returned. Processing is executed as follows:

1. Declaration of pointer pszServerPrefix, pszTagPrefix and pszWindowPrefix for the three prefixes
2. Initialization of the nServerPrefixLen, nTagPrefixLen and nTagLen tags

   They serve as a buffer for the string length of the prefixes to be read out.
3. Initialization of the myTagName tag
4. Reading out of server prefix, tag prefix and window prefix
5. **Case distinction**: Server prefix

   - **No** server prefix returned: a text is output and the function is exited.
   - Server prefix returned: Its length is determined and saved in the nServerPrefixLen tag.
6. If a tag prefix is returned, its length is determined and saved in the nTagPrefixLen tag.
7. Determines the length of the tag name and saves it in the nTagLen tag.
8. **Case distinction**: Permissible length for tag name

   - Permissible length exceeded: a text is output and the function is exited.
   - Permissible length **not** exceeded: The tag name required for a client environment is compiled.

{

char* pszServerPrefix;

char* pszTagPrefix;

char* pszWindowPrefix;

int nServerPrefixLen = 0;

int nTagPrefixLen = 0;

int nTagLen = 0;

char myTagName[MAX_DM_VAR_NAME+1];

//Initialize the return value

memset(myTagName,0,MAX_DM_VAR_NAME + 1);

//Get the serverprefix the tagprefix and the windowprefix

GetServerTagPrefix(&pszServerPrefix, &pszTagPrefix, &pszWindowPrefix);

//If a serverprefix exists

if (pszServerPrefix)

{

  //Get the length of the string

  nServerPrefixLen = strlen(pszServerPrefix);

}

Else

{

  printf("No server prefix was returned.");

  return;

}

//If a tagprefix exists

if (pszTagPrefix)

{

  //Get the length of the string

  nTagPrefixLen = strlen(pszTagPrefix);

}

//Get the length of the tag

nTagLen = strlen("TagName");

//Check if the lenght of the  
//ServerPrefix+TagPrefix+VarName + the double points < MAX_DM_VAR_NAME)

if (nServerPrefixLen + nTagPrefixLen + nTagLen+2 < MAX_DM_VAR_NAME)

{

  sprintf(myTagName,"%s::%s%s",pszServerPrefix,pszTagPrefix,"TagName");

  //User defined code where the

  //user can do something with the returnvalue

  ...

}

Else

{

  printf("The resulting string is too long.");

  return;

}

}

### GetTag (RT Professional)

This section contains information on the following topics:

- [GetTag functions (RT Professional)](#gettag-functions-rt-professional)
- [GetTagDateTime function (RT Professional)](#gettagdatetime-function-rt-professional)
- [GetTagMultiStateQCWait functions (RT Professional)](#gettagmultistateqcwait-functions-rt-professional)
- [GetTagMultiStateWait functions (RT Professional)](#gettagmultistatewait-functions-rt-professional)
- [GetTagMultiWait functions (RT Professional)](#gettagmultiwait-functions-rt-professional)
- [GetTagState functions (RT Professional)](#gettagstate-functions-rt-professional)
- [GetTagStateQC functions (RT Professional)](#gettagstateqc-functions-rt-professional)
- [GetTagStateQCWait functions (RT Professional)](#gettagstateqcwait-functions-rt-professional)
- [GetTagStateWait functions (RT Professional)](#gettagstatewait-functions-rt-professional)
- [GetTagValue functions (RT Professional)](#gettagvalue-functions-rt-professional)
- [GetTagValueStateQC functions (RT Professional)](#gettagvaluestateqc-functions-rt-professional)
- [GetTagValueStateQCWait functions (RT Professional)](#gettagvaluestateqcwait-functions-rt-professional)
- [GetTagValueWait functions (RT Professional)](#gettagvaluewait-functions-rt-professional)
- [GetTagWait functions (RT Professional)](#gettagwait-functions-rt-professional)

#### GetTag functions (RT Professional)

##### Description

The GetTagXXX function calculates the value of a tag of the specified data type.

Can only be used in C scripting:

The following table shows the different GetTag functions for reading the tag value:

| Type | Function name | Parameter | PLC data type | HMI data type |
| --- | --- | --- | --- | --- |
| BOOL | GetTagBit | Tag Tag_Name | Binary tag | Bool |
| BYTE | GetTagByte | Tag Tag_Name | Unsigned 8-bit | USInt |
| char* | GetTagChar | Tag Tag_Name | Text tag 8-bit or  text tag 16-bit | String or WString |
| SYSTEMTIME | GetTagDateTime | Tag Tag_Name | DTL | DateTime |
| double | GetTagDouble | Tag Tag_Name | Floating point 64-bit | LReal |
| DWORD | GetTagDWord | Tag Tag_Name | Unsigned 32-bit | UDInt |
| float | GetTagFloat | Tag Tag_Name | Floating point 32-bit | Real |
| BOOL | GetTagRaw | Tag Tag_Name, BYTE* pValue, DWORD size | Raw data type | Raw |
| signed char | GetTagSByte | Tag Tag_Name | Signed 8-bit | SInt |
| long int | GetTagSDWord | Tag Tag_Name | Signed 32-bit | DInt |
| short int | GetTagSWord | Tag Tag_Name | Signed 16-bit | Int |
| WORD | GetTagWord | Tag Tag_Name | Unsigned 16-bit | UInt |

##### Syntax

<Type><FunctionName><(Parameter)>;

Example: BYTE GetTagByte(Tag_Name);

##### Parameter

**Tag_Name**

Tag name

**pValue**

Pointer to a byte field containing the value of the raw data tags.

**size**

Length of the byte field in bytes

##### Return value

Value of the tags in the specified type.

System function "GetTagChar" returns a pointer to a string that contains the tag value.

System function "GetTagRaw" returns TRUE or FALSE:

**TRUE**: System function completed without errors.

**FALSE**: An error has occurred.

##### Example

The following program code uses the GetTagByte function to read out the value of the gs_tag_byte tag and saves it to the bvalue tag.

{

BYTE bvalue;

//Get the current value of the tag

bvalue = GetTagByte("gs_tag_byte");

// print value

printf ("Value of gs_tag_byte: %d\r\n", bvalue);

...

}

The saved return value can be processed in the following code.

---

**See also**

[Access to HMI tags (Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#access-to-hmi-tags-panels-comfort-panels-rt-advanced-rt-professional)
  
[Data types (RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-types-rt-professional)

#### GetTagDateTime function (RT Professional)

##### Function

Determines the value of a tag of data type "Date/Time".

##### Syntax

SYSTEMTIME GetTagDateTime(Tag_Name);

##### Parameter

**Tag_Name**

Name of the tag

##### Return value

Value of the tag in the data type "Date/Time".

#### GetTagMultiStateQCWait functions (RT Professional)

##### Description

The values, status, and quality code of several tags are established and saved in the repsective addresses in the specified format . The values are read explicitly from the AS.

Two DWORD arrays are transferred, in the member of which the status and quality codes of the individual tags will be located after the system function has been called. The size of the arrays must be large enough to provide sufficient storage space for the status and quality codes.

Can only be used in C scripting.

##### Syntax

BOOL GetTagMultiStateQCWait(pdwState, pdwQualityCode, pFormat);

##### Parameters

**pdwState**

Field in which the status of the individual tags is created after the system function cycle.

**pdwQualityCode**

Field in which the quality code of the individual tag is created after the system function cycle.

**pFormat**

Format description (type) for all requested tags, followed by the name and address of the value for each tag.

##### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

##### Example

The following program code uses the GetTagMultiStateQCWait function to read the value from the "gs_tag_XXX" tag and saves these values to the Ivalue1, Ivalue2 tags, etc.

1. Preprocessor definition for "DATA_SIZE" (in this case for 5 tags)
2. Creating the DWord fields

   - dwState Tag status field
   - dwQc Field for quality codes
3. Tag definition for buffering
4. Execution of the function GetTagMultiStateQCWait

   The value read is written to the addresses of the tags.

{

#define DATA_SIZE 5

DWORD dwState[DATA_SIZE];

DWORD dwQC[DATA_SIZE];

//define all Datas

BOOL lValue1;

long lValue2 ;

char* szValue3;

double dblValue4 ;

WORD lValue5 ;

//Set the tags

GetTagMultiStateQCWait(dwState,dwQC,"%d%d%s%f%d",

  "gs_tag_bit",&lValue1,

  "gs_tag_SByte",&lValue2,

  "gs_tag_char",&szValue3,

  "gs_tag_float",&dblValue4,

  "gs_tag_word",&lValue5);

//User defined code where the

//user can do something with the returnvalue

...

}

The saved return value can be processed in the following code.

---

**See also**

[Constants (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#constants-rt-professional)

#### GetTagMultiStateWait functions (RT Professional)

##### Description

The values and status of several tags are determined and saved in the respective addresses in the specified format. The values are read explicitly from the AS.

The system function must be given a DWORD array, in the member of which the status of the individual tags will be located after the system function has been called. The size of the array must be large enough to provide sufficient storage space for the status.

Can only be used in C scripting.

##### Syntax

BOOL GetTagMultiStateWait(pdwState, pFormat);

##### Parameters

**pdwState**

Field in which the tag status is saved.

**pFormat**

Format description (type) for all requested tags, followed by the name and address of the value for each tag.

##### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

##### Example

The following program code uses the GetTagMultiStateWait function to read the value from the "gs_tag_XXX" tag and saves these values to the Ivalue1, Ivalue2 tags, etc.

1. Preprocessor definition for "DATA_SIZE" (in this case for 5 tags)
2. Creating DWord field dwState for the tag status
3. Tag definition for buffering
4. Execution of the function GetTagMultiStateWait

   The value read is written to the addresses of the tags.

{

#define DATA_SIZE 5

DWORD dwState[DATA_SIZE];

//define all Datas

BOOL lValue1;

long lValue2 ;

char* szValue3;

double dblValue4 ;

WORD lValue5 ;

//Set the tags

GetTagMultiStateWait(dwState,"%d%d%s%f%d",

  "gs_tag_bit",&lValue1,

  "gs_tag_SByte",&lValue2,

  "gs_tag_char",&szValue3,

  "gs_tag_float",&dblValue4,

  "gs_tag_word",&lValue5);

//User defined code where the

//user can do something with the returnvalue

...

}

The saved return value can be processed in the following code.

---

**See also**

[Constants (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#constants-rt-professional)

#### GetTagMultiWait functions (RT Professional)

##### Description

The values of several tags are determined and saved in the respective addresses in the specified format. The value is read explicitly from the AS. The system function uses SysMalloc to allocate memory to the tag value.

Can only be used in C scripting.

##### Syntax

BOOL GetTagMultiWait(pFormat,...);

##### Parameters

**pFormat**

Format description for all requested tags along with name and address of the value for each tag.

##### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

##### Example

The GetTagMultiWait function is used in the following program code to read several tags of different types:

1. Declaration of three tags as memory for three different tag types
2. Declaration of the boolean tag ok for buffering the return value (TRUE/FALSE)
3. Reading the three tags and saving the values to the corresponding addresses.

   The return value of the function is saved to the ok tag.
4. Output of the three tags with tag type prefix

DWORD dwVar1Value;

char* szVar2Value;

//memory for values allocated via SysMalloc

double dbVar3Value;

BOOL ok;

ok=GetTagMultiWait("%d%s%f", "Ernie_word", &dwVar1Value,

  "Ernie_char", &szVar2Value,

  "Ernie_double", &dbVar3Value);

printf("Word %d, String %s, Double %f\r\n",

  dwVar1Value, szVar2Value, dbVar3Value);

#### GetTagState functions (RT Professional)

##### Description

The GetTagStateXXX function calculates the value of a tag of the specified data type. It also returns the status of the tags.

Can only be used in C scripting.

The following table lists the different GetTagStateXXX functions for reading the tag value:

| Type | Function name | Parameters | PLC data type | HMI data type |
| --- | --- | --- | --- | --- |
| BOOL | GetTagBitState | Tag Tag_Name, PDWORD lp_dwstate | Binary tag | Bool |
| BYTE | GetTagByteState | Tag Tag_Name, PDWORD lp_dwstate | Unsigned 8-bit | Byte |
| char* | GetTagCharState | Tag Tag_Name, PDWORD lp_dwstate | Text tag 8-bit or text tag 16-bit | String |
| double | GetTagDoubleState | Tag Tag_Name, PDWORD lp_dwstate | Floating point 64-bit | Double |
| DWORD | GetTagDWordState | Tag Tag_Name, PDWORD lp_dwstate | Unsigned 32-bit | UInteger |
| float | GetTagFloatState | Tag Tag_Name, PDWORD lp_dwstate | Floating point 32-bit | Float |
| BOOL | GetTagRawState | Tag Tag_Name, BYTE* pValue, DWORD size, PDWORD lp_dwstate | Raw data type | Raw |
| signed char | GetTagSByteState | Tag Tag_Name, PDWORD lp_dwstate | Signed 8-bit | Byte |
| long int | GetTagSDWordState | Tag Tag_Name, PDWORD lp_dwstate | Signed 32-bit | Integer |
| short int | GetTagSWordState | Tag Tag_Name, PDWORD lp_dwstate | Signed 16-bit | Short |
| WORD | GetTagWordState | Tag Tag_Name, PDWORD lp_dwstate | Unsigned 16-bit | UShort |

##### Syntax

<Type><FunctionName><(Parameter)>;

Example: BOOL GetTagBitState(Tag_Name, lp_dwstate);

##### Parameters

**Tag_Name**

Tag name

**lp_dwstate**

Pointer to a DWORD to which the tag status is saved on completion of the system function cycle.

**pValue**

Pointer to a byte field containing the value of the raw data tags.

**size**

Length of the byte field in bytes

##### Return value

Value of the tags in the specified type.

The system function "GetTagCharState" returns a pointer to a value of the tag of data type "char".

System function "GetTagRawState" returns TRUE or FALSE:

**TRUE**: System function completed without errors.

**FALSE**: An error has occurred.

##### Example

The following program code uses the GetTagBitState function to read out the value of the gs_tag_bit tag and saves it to the bValue tag.

The status is stored in the address of the dwState tag.

A specific code will be executed, depending on the return value in bValue (TRUE/FALSE).

{

DWORD dwState;

BOOL bValue;

dwState = 0xFFFFFFFF;

//Get the tag value

//dwstate is the tag state

bValue = GetTagBitState("gs_tag_bit",&dwState);

//Create a string which includes the tag value

if (bValue)

{

  // User defined code if the

  // value of the tag is true

  ...

}

else

{

  // User defined code if the

  // value of the tag is false

  ...

}

}

---

**See also**

[Constants (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#constants-rt-professional)
  
[Data types (RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-types-rt-professional)

#### GetTagStateQC functions (RT Professional)

##### Description

The GetTagStateQC function calculates the value of a tag of the specified data type. It also returns the status and quality code of the tags.

Can only be used in C scripting.

The following table shows the different GetTagStateQC functions for reading the tag value:

| Type | Function name | Parameters | PLC data type | HMI data type |
| --- | --- | --- | --- | --- |
| BOOL | GetTagBitStateQC | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Binary tag | Bool |
| BYTE | GetTagByteStateQC | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Unsigned 8-bit | UByte |
| char* | GetTagCharStateQC | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Text tag 8-bit or text tag 16-bit | String |
| double | GetTagDoubleStateQC | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Floating point 64-bit | Double |
| DWORD | GetTagDWordStateQC | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Unsigned 32-bit | UInteger |
| float | GetTagFloatStateQC | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Floating point 32-bit | Float |
| BOOL | GetTagRawStateQC | Tag Tag_Name, BYTE pValue[], DWORD size, PDWORD lp_dwstate, PDWORD pdwQualityCode | Raw data type | Raw |
| signed char | GetTagSByteStateQC | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Signed 8-bit | Byte |
| long int | GetTagSDWordStateQC | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Signed 32-bit | Integer |
| short int | GetTagSWordStateQC | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Signed 16-bit | Short |
| WORD | GetTagWordStateQC | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Unsigned 16-bit | UShort |

##### Syntax

<Type><FunctionName><(Parameter)>;

Example: BOOL GetTagBitStateQC(Tag_Name, lp_dwstate, pdwQualityCode);

##### Parameters

**Tag_Name**

Tag name

**lp_dwstate**

Pointer to a DWORD to which the tag status is saved on completion of the system function cycle.

**pdwQualityCode**

Pointer on a DWORD in which the quality code of the tag is created after the system function cycle.

**pValue**

Pointer to a byte field containing the value of the raw data tags.

**size**

Length of the byte field in bytes

##### Return value

Value of the tags in the specified type.

The system function "GetTagCharStateQC" returns a pointer to a value of the tag of data type "char".

The system function "GetTagRawStateQC" returns TRUE or FALSE:

**TRUE**: System function completed without errors.

**FALSE**: An error has occurred.

##### Example

The following program code uses the GetTagBitStateQC function to read the value from the gs_tag_bit tag and saves it to the ok tag.

The status and quality code is saved to the dwState and dwQC addresses of the tag.

A specific code will be executed, depending on the return value in the tag (TRUE/FALSE).

{

DWORD dwState;

DWORD dwQC;

BOOL ok;

dwState = 0xFFFFFFFF;

//Get the tag value

//dwstate is the tag state

ok = GetTagBitStateQC("gs_tag_bit",&dwState,&dwQC);

//Create a string which includes the tag value

if (ok)

{

  // succeeded, print tag value

printf ("Value at dwState: %x\r\n", dwState);

printf ("Value at dwQC: %x\r\n", dwQC);

  ...

}

else

{

  // failed

  printf ( "Error - function failed." );

}

}

---

**See also**

[Constants (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#constants-rt-professional)
  
[Data types (RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-types-rt-professional)

#### GetTagStateQCWait functions (RT Professional)

##### Description

The GetTagStateQCWait function calculates the value of a tag of the specified data type. The value is read explicitly from the AS. It also returns the status and quality code of the tags.

Can only be used in C scripting.

The following table lists the different GetTagStateQCWait functions for reading the tag value:

| Type | Function name | Parameters | PLC data type | HMI data type |
| --- | --- | --- | --- | --- |
| BOOL | GetTagBitStateQCWait | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Binary tag | Bool |
| BYTE | GetTagByteStateQCWait | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Unsigned 8-bit | UByte |
| char* | GetTagCharStateQCWait | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Text tag 8-bit or text tag 16-bit | String |
| double | GetTagDoubleStateQCWait | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Floating point 64-bit | Double |
| DWORD | GetTagDWordStateQCWait | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Unsigned 32-bit | UInteger |
| float | GetTagFloatStateQCWait | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Floating point 32-bit | Float |
| BOOL | GetTagRawStateQCWait | Tag Tag_Name, BYTE pValue[], DWORD size, PDWORD lp_dwstate, PDWORD pdwQualityCode | Raw data type | Raw |
| signed char | GetTagSByteStateQCWait | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Signed 8-bit | Byte |
| long int | GetTagSDWordStateQCWait | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Signed 32-bit | Integer |
| short int | GetTagSWordStateQCWait | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Signed 16-bit | Short |
| WORD | GetTagWordStateQCWait | Tag Tag_Name, PDWORD lp_dwstate, PDWORD pdwQualityCode | Unsigned 16-bit | UShort |

##### Syntax

<Type><FunctionName><(Parameter)>;

Example: BOOL GetTagBitStateQC(Tag_Name, lp_dwstate, pdwQualityCode);

##### Parameters

**Tag_Name**

Tag name

**lp_dwstate**

Pointer to a DWORD to which the tag status is saved on completion of the system function cycle.

**pdwQualityCode**

Pointer on a DWORD in which the quality code of the tag is created after the system function cycle.

**pValue**

Pointer to a byte field containing the value of the raw data tags.

**size**

Length of the byte field in bytes

##### Return value

Value of the tags in the specified type.

The system function "GetTagCharStateQCWait" returns a pointer to a value of the tag of data type "char".

The system function "GetTagRawStateQCWait" returns TRUE or FALSE:

**TRUE**: System function completed without errors.

**FALSE**: An error has occurred.

##### Example

The following program code uses the GetTagBitStateQCWait function to read the value from the gs_tag_bit tag and saves it to the bValue tag.

The status and quality code is saved to the dwState and dwQC addresses of the tag.

A specific code will be executed, depending on the return value in bValue (TRUE/FALSE).

{

DWORD dwState;

DWORD dwQC;

BOOL bValue;

dwState = 0xFFFFFFFF;

//Get the tag value

//dwstate is the tag state

bValue = GetTagBitStateQCWait("gs_tag_bit",&dwState,&dwQC);

//Create a string which includes the tag value

if (bValue)

{

  // User defined code if the

  // value of the tag is true

  ...

}

else

{

  // User defined code if the

  // value of the tag is false

  ...

}

}

---

**See also**

[Constants (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#constants-rt-professional)
  
[Data types (RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-types-rt-professional)

#### GetTagStateWait functions (RT Professional)

##### Description

The GetTagStateWait function calculates the value of a tag of the specified data type. The value is read explicitly from the AS. It also returns the status of the tags.

Can only be used in C scripting.

The following table lists the different GetTagStateWait functions for reading the tag value:

| Type | Function name | Parameters | PLC data type | HMI data type |
| --- | --- | --- | --- | --- |
| BOOL | GetTagBitStateWait | Tag Tag_Name, PDWORD lp_dwstate | Binary tag | Bool |
| BYTE | GetTagByteStateWait | Tag Tag_Name, PDWORD lp_dwstate | Unsigned 8-bit | UByte |
| char* | GetTagCharStateWait | Tag Tag_Name, PDWORD lp_dwstate | Text tag 8-bit or text tag 16-bit | String |
| double | GetTagDoubleStateWait | Tag Tag_Name, PDWORD lp_dwstate | Floating point 64-bit | Double |
| DWORD | GetTagDWordStateWait | Tag Tag_Name, PDWORD lp_dwstate | Unsigned 32-bit | UInteger |
| float | GetTagFloatStateWait | Tag Tag_Name, PDWORD lp_dwstate | Floating point 32-bit | Float |
| BOOL | GetTagRawStateWait | Tag Tag_Name, BYTE* pValue, DWORD size, PDWORD lp_dwstate | Raw data type | Raw |
| signed char | GetTagSByteStateWait | Tag Tag_Name, PDWORD lp_dwstate | Signed 8-bit | Byte |
| long int | GetTagSDWordStateWait | Tag Tag_Name, PDWORD lp_dwstate | Signed 32-bit | Integer |
| short int | GetTagSWordStateWait | Tag Tag_Name, PDWORD lp_dwstate | Signed 16-bit | Short |
| WORD | GetTagWordStateWait | Tag Tag_Name, PDWORD lp_dwstate | Unsigned 16-bit | UShort |

##### Syntax

<Type><FunctionName><(Parameter)>

Example: BOOL GetTagBitStateWait(Tag_Name, lp_dwstate)

##### Parameters

**Tag_Name**

Tag name

**lp_dwstate**

Pointer to a DWORD to which the tag status is saved on completion of the system function cycle.

**pValue**

Pointer to a byte field containing the value of the raw data tags.

**size**

Length of the byte field in bytes

##### Return value

Value of the tags in the specified type.

The system function "GetTagCharStateWait" returns a pointer to a value of the tag of data type "char".

The system function "GetTagRawState" returns TRUE or FALSE:

**TRUE**: System function completed without errors.

**FALSE**: An error has occurred.

##### Example

The following program code uses the GetTagBitStateWait function to read the value from the gs_tag_bit tag and saves it to the bValue tag.

The status is stored in the address of the dwState tag.

A specific code will be executed, depending on the return value in bValue (TRUE/FALSE).

{

DWORD dwState;

BOOL bValue;

dwState = 0xFFFFFFFF;

//Get the tag value

//dwstate is the tag state

bValue = GetTagBitStateWait("gs_tag_bit",&dwState);

//Create a string which includes the tag value

if (bValue)

{

  // User defined code if the

  // value of the tag is true

  ...

}

else

{

  // User defined code if the

  // value of the tag is false

  ...

}

}

---

**See also**

[Constants (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#constants-rt-professional)
  
[Data types (RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-types-rt-professional)

#### GetTagValue functions (RT Professional)

##### Description

Enables the transfer of a value in the form of a variant. Determines the pointer on the results structure that contains the value.

Can only be used in C scripting.

##### Syntax

BOOL GetTagValue(lpdmVarKey, lpdmresult, lpdmError);

##### Parameters

**lpdmVarKey**

Pointer to a structure of data type "DM_VARKEY"

**lpdmresult**

Pointer to a structure of data type "DM_VAR_UPDATE_STRUCT"

**lpdmError**

Pointer on the structure that contains the error description.

##### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

##### Example

The GetTagValue function is used in the following program code to calculate the value in varKey.

A specific code will be executed, depending on the return value in keyFound (TRUE/FALSE).

{

DM_VARKEY varKey;

DM_VAR_UPDATE_STRUCT result;

CMN_ERROR error:

BOOL keyFound;

//Get the tag value

keyFound = GetTagValue(&varKey, &result, &error);

if (keyFound)

{

  // print tag value

printf ("Value of varKey: %d\r\n", &varKey);

  ...

}

else

{

  // failed

  printf ( "Error - function failed." );

  ...

}

}

#### GetTagValueStateQC functions (RT Professional)

##### Description

Enables the transfer of a value in the form of a variant. Determines the pointer on the results structure that contains the value. It also returns the status and quality code of the tags.

The system function can be used in C scripting only.

##### Syntax

BOOL GetTagValueStateQC(lpdmVarKey, lpdmresult, lpdmError);

##### Parameters

**lpdmVarKey**

Pointer to a structure of data type "DM_VARKEY"

**lpdmresult**

Pointer to a structure of data type "DM_VAR_UPDATE_STRUCTEX"

**lpdmError**

Pointer on the structure that contains the error description.

##### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

##### Example

The GetTagValueStateQC function is used in the following program code to calculate the value in varKey.

The status and quality code is saved to the dwState and dwQC addresses of the tag.

A specific code will be executed, depending on the return value in keyFound (TRUE/FALSE).

{

DM_VARKEY varKey;

DM_VAR_UPDATE_STRUCTEX result;

CMN_ERROR error:

// clarify (DM_VAR_UPDATE_STRUCTEX already contains QualityCode)

DWORD dwState;

DWORD dwQC;

BOOL keyFound;

//Get the tag value

keyFound = GetTagValueStateQC(&varKey, &result, &error,&dwState,&dwQC);

if (keyFound)

{

  // User defined code if the

  // value of the tag is true

  ...

}

else

{

  // User defined code if the

  // value of the tag is false

  ...

}

}

#### GetTagValueStateQCWait functions (RT Professional)

##### Description

Enables the transfer of a value in the form of a variant. Determines the pointer on the results structure that contains the value. The value is read explicitly from the AS. It also returns the status and quality code of the tags.

Can only be used in C scripting.

##### Syntax

BOOL GetTagValueStateQCWait(lpdmVarKey, lpdmresult, lpdmError);

##### Parameters

**lpdmVarKey**

Pointer to a structure of data type "DM_VARKEY"

**lpdmresult**

Pointer to a structure of data type "DM_VAR_UPDATE_STRUCTEX"

**lpdmError**

Pointer on the structure that contains the error description.

##### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

##### Example

The following program code uses the function GetTagValueStateQCWait for reading

The status and quality code is saved to the dwState and dwQC addresses of the tag.

A specific code will be executed, depending on the return value in keyFound (TRUE/FALSE).

{

DM_VARKEY varKey;

DM_VAR_UPDATE_STRUCTEX result;

CMN_ERROR error:

// clarify (DM_VAR_UPDATE_STRUCTEX already contains QualityCode)

DWORD dwState;

DWORD dwQC;

BOOL keyFound;

//Get the tag value

keyFound = GetTagValueStateQC(&varKey, &result, &error,&dwState,&dwQC);

if (keyFound)

{

  // User defined code if the

  // value of the tag is true

  ...

}

else

{

  // User defined code if the

  // value of the tag is false

  ...

}

}

#### GetTagValueWait functions (RT Professional)

##### Description

Enables the transfer of a value in the form of a variant. Determines the pointer on the results structure that contains the value. The value is read directly from the AS.

Can only be used in C scripting.

##### Syntax

BOOL GetTagValueWait(lpdmVarKey, lpdmresult, lpdmError);

##### Parameters

**lpdmVarKey**

Pointer to a structure of data type "DM_VARKEY"

**lpdmresult**

Pointer to a structure of data type "DM_VAR_UPDATE_STRUCT"

**lpdmError**

Pointer on the structure that contains the error description

##### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

##### Example

The GetTagValueWait function is used in the following program code to calculate the value in varKey.

A specific code will be executed, depending on the return value in keyFound (TRUE/FALSE).

{

DM_VARKEY varKey;

DM_VAR_UPDATE_STRUCT result;

CMN_ERROR error:

BOOL keyFound;

//Get the tag value

keyFound = GetTagValueWait(&varKey, &result, &error);

if (keyFound)

{

  // succeeded, key found

  // print tag value

printf ("Value of varKey: %d\r\n", &varKey);

  ...

}

else

{

  // failed

  printf ( "Error - function failed." );

}

  ...

}

#### GetTagWait functions (RT Professional)

##### Description

The GetTagWaitXXX function calculates the value of a tag of the specified data type. The value is read explicitly from the AS.

Can only be used in C scripting.

The following table shows the different GetTagWait functions for reading the tag value:

| Type | Function name | Parameters | PLC data type | HMI data type |
| --- | --- | --- | --- | --- |
| BOOL | GetTagBitWait | Tag Tag_Name | Binary tag | Bool |
| BYTE | GetTagByteWait | Tag Tag_Name | Unsigned 8-bit | UByte |
| char* | GetTagCharWait | Tag Tag_Name | Text tag 8-bit or text tag 16-bit | String |
| double | GetTagDoubleWait | Tag Tag_Name | Floating point 64-bit | Double |
| DWORD | GetTagDWordWait | Tag Tag_Name | Unsigned 32-bit | UInteger |
| float | GetTagFloatWait | Tag Tag_Name | Floating point 32-bit | Float |
| BOOL | GetTagRawWait | Tag Tag_Name, BYTE* pValue, DWORD size | Raw data type | Raw |
| char | GetTagSByteWait | Tag Tag_Name | Signed 8-bit | Byte |
| long int | GetTagSDWordWait | Tag Tag_Name | Signed 32-bit | Integer |
| short int | GetTagSWordWait | Tag Tag_Name | Signed 16-bit | Short |
| WORD | GetTagWordWait | Tag Tag_Name | Unsigned 16-bit | UShort |

##### Syntax

<Type><FunctionName><(Parameter)>;

Example: BYTE GetTagByteWait(Tag_Name);

##### Parameters

**Tag_Name**

Tag name

**pValue**

Pointer to a byte field containing the value of the raw data tags.

##### Return value

Value of the tags in the specified type.

System function "GetTagCharWait" returns a pointer to a string that contains the tag value.

System function "GetTagRawWait" returns TRUE or FALSE:

**TRUE**: System function completed without errors.

**FALSE**: An error has occurred.

##### Example

The following program code uses the GetTagByteWait function to read the value from the gs_tag_byte tag and saves it to the bvalue tag.

{

BYTE bvalue;

//Get the current value of the tag

bvalue = GetTagByteWait("gs_tag_byte");

// print value

printf ("Value of gs_tag_byte: %d\r\n", bvalue);

...

}

The saved return value can be processed in the following code.

---

**See also**

[Data types (RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-types-rt-professional)

### IncreaseTag (RT Professional)

#### Description

Adds the given value to the value of the tags.

X = X + a

> **Note**
>
> The system function uses the same tag as input and output values. When this system function is used to convert a value, auxiliary tags must be used. You can use the "SetTag" system function to assign the tag value to the auxiliary tags.

If you configure the system function for events of an alarm and the tag is not being used in the current screen, it is not ensured that the actual tag value is being used in the PLC. You can improve the situation by setting the "Cyclic continuous" acquisition mode.

#### Use in the function list

IncreaseTag (Tag, Value)

#### Use in user-defined functions

IncreaseTag Tag, Value

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

#### Parameters

**Tag**

The tag to which the given value is added.

**Value**

The value that is added.

#### Example

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

### InquireLanguage (RT Professional)

#### Description

Determines all languages configured in the text library for the runtime.

Use Pointer to a counter to specify the storage location for language IDs.

The system function can be used in C scripting only.

#### Syntax

DWORD* InquireLanguage(PointerToACounter);

#### Parameters

**PointerToACounter**

Pointer to the number of language IDs found

#### Return value

Pointer to a field containing the established language IDs.

The following assignments apply (hexadecimal language code):

| Symbolic name | Value(hexadecimal) | Abbreviation |
| --- | --- | --- |
| LANG_ARABIC | 0x0401 |  |
| LANG_AFRIKAANS | 0x0436 |  |
| LANG_ALBANIAN | 0x041C |  |
| LANG_BASQUE | 0x042D |  |
| LANG_BULGARIAN | 0x0402 |  |
| LANG_BYELORUSSIAN | 0x0423 |  |
| LANG_CATALAN | 0x0403 |  |
| LANG_CHINESE | 0x0404 |  |
| LANG_CROATIAN | 0x041A |  |
| LANG_CZECH | 0x0405 | CSY |
| LANG_DANISH | 0x0406 | DAN |
| LANG_DUTCH | 0x0413 | NLD |
| LANG_ENGLISH | 0x0409 | ENU |
| LANG_ESTONIAN | 0x0425 |  |
| LANG_FAEROESE | 0x0438 |  |
| LANG_FARSI | 0x0429 |  |
| LANG_FINNISH | 0x040B | FIN |
| LANG_FRENCH | 0x040C | FRA |
| LANG_GERMAN | 0x0407 | DEU |
| LANG_GREEK | 0x0408 |  |
| LANG_HEBREW | 0x040D |  |
| LANG_HUNGARIAN | 0x040E | HUN |
| LANG_ICELANDIC | 0x040F | ISL |
| LANG_INDONESIAN | 0x0421 |  |
| LANG_ITALIAN | 0x0410 | ITA |
| LANG_JAPANESE | 0x0411 |  |
| LANG_KOREAN | 0x0412 |  |
| LANG_LATVIAN | 0x0426 |  |
| LANG_LITHUANIAN | 0x0427 |  |
| LANG_NORWEGIAN | 0x0414 | NOR |
| LANG_POLISH | 0x0415 | PLK |
| LANG_PORTUGUESE | 0x0416 | PTB |
| LANG_ROMANIAN | 0x0418 |  |
| LANG_RUSSIAN | 0x0419 | RUS |
| LANG_SLOVAK | 0x041B | SKY |
| LANG_SLOVENIAN | 0x0424 |  |
| LANG_SORBIAN | 0x042E |  |
| LANG_SPANISH | 0x040A | ESP |
| LANG_SWEDISH | 0x041D | SVE |
| LANG_THAI | 0x041E |  |
| LANG_TURKISH | 0x041F | TRK |
| LANG_UKRAINIAN | 0x0422 |  |

#### Example

The following program code uses the InquireLanguage function to query the language configured at runtime and processes these as follows:

1. Saving the queried language ID to the tag language
2. Saving the number of languages to the tag count
3. Formatted output of the ID and number of languages

{

DWORD count;

DWORD* language;

int i;

//Count the installed languages

language = InquireLanguage(&count);

printf("##################### INQUIRE LANGUAGE ####################");

//Print out the count of languages

printf ( "\r\nCount Languages=%d\r\n", count );

//print out which languages are installed

for (i=1;i<=count; i++)

{

printf ("\r\n%d.language=%x", i,*language++);

}

}

The saved return value can be processed in the following code.

### InverseLinearScaling (RT Professional)

#### Description

Assigns a value to the tag X, which is calculated from the value of the given tag Y using the linear function X = (Y - b) / a.

The tags X and Y must not be identical. This system function is the inverse of the "LinearScaling" system function.

> **Note**
>
> The tags X and Y must not be identical. If a tag is to be converted into itself, a auxiliary tag must be used.
>
> The "SetTag" system function can be used to assign the value of the tags to be converted to the auxiliary tags.

#### Use in the function list

InvertLinearScaling (X, Y, b, a)

#### Use in user-defined functions

InverseLinearScaling X, Y, b, a

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

#### Parameters

**X**

The tag which is assigned the value calculated from the linear equation.

**Y**

The tag that contains the value used for calculation.

**b**

The value which is subtracted.

**a**

The value through which is divided.

#### Example

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

### InvertBit (RT Professional)

#### Description

Inverts the value of the given tag of the "Bool" type:

- If the tag has the value of 1 (TRUE), it will be set to 0 (FALSE).
- If the tag has the value of 0 (FALSE), it will be set to 1 (TRUE).

#### Use in the function list

InvertBit (Tag)

#### Use in user-defined functions

InvertBit Tag

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

#### Parameters

**Tag**

The tag whose bit is set.

#### Example

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

strResult="Old Value: "&bSaved &Chr(13)&"New Value: "&bValue

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

### InvertBitInTag (RT Professional)

#### Description

Inverts a bit in the given tag:

- If the bit in the tag has the value of 1 (TRUE), it will be set to 0 (FALSE).
- If the bit in the tag has the value of 0 (FALSE), it will be set to 1 (TRUE).

After changing the given bit, the system function transfers the entire tag back to the PLC. It is not checked whether other bits in the tags have changed in the meantime. Operator and PLC have read-only access to the indicated tag until it is transferred back to the PLC.

> **Note**
>
> If the PLC supports BOOL tags, do not use this system function. Use the "InvertBit" system function instead.

#### Use in the function list

InvertBitInTag (Tag, Bit)

#### Use in user-defined functions

InvertBitInTag Tag, Bit

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

#### Parameters

**Tag**

The tag in which the given bit is set.

**Bit**

The number of the bit that is set.

When this system function is used in a user-defined function, the bits in a tag are counted from right to left. The counting begins with 0.

#### Example

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

strResult="Old Value: "&bSaved &Chr(13)&"New Value: "&bValue

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

### IsUserAuthorized (RT Professional)

#### Description

Authentication of users.

Can only be used in C scripting.

#### Syntax

BOOL IsUserAuthorized(AuthorizationNumber);

#### Parameters

**AuthorizationNumber**

Authorization (numerical) to be verified.

#### Return value

**TRUE**

The user has the specified authorization.

**FALSE**

The user does not have the specified authorization.

#### Example

The following program code authenticates users by means of IsUserAuthorized function and writes the value to the boolean tag ok.

{

BOOL ok;

DWORD authnumber;

//Check authorization and return value

ok = IsUserAuthorized (authnumber);

//error handling

if(ok)

{

  // user authorized

  printf ( "User is authorized." );

}

else

{

  // user not authorized

  printf ( "Authorization failed." );

}

...

}

The return value is output.

### LinearScaling (RT Professional)

#### Description

Assigns a value to the tag Y, which is calculated from the value of the given tag X using the linear function Y= (a *X) + b.

The inverse of this function is the "InvertLinearScaling" system function.

> **Note**
>
> The tags X and Y must not be identical. If a tag is to be converted into itself, a auxiliary tag must be used.
>
> The "SetTag" system function can be used to assign the value of the tags to be converted to the auxiliary tags.

#### Use in the function list

LinearScaling (Y, a, X, b)

#### Use in user-defined functions

LinearScaling Y, a, X, b

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

#### Parameters

**Y**

The tag which is assigned the value calculated from the linear equation.

**a**

The value with which is multiplied.

**X**

The tag that contains the value used for calculation.

**b**

The value that is added.

#### Example

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

### ReportJob (RT Professional)

#### Description

A print job or the preview for a print job is started depending on the value of the NameOfMethod parameter.

Can only be used in C scripting.

#### Syntax

void ReportJob(PrintJobName, NameOfMethod)

#### Parameters

**PrintJobName**

Pointer to the name of the print job

**NameOfMethod**

Defines whether to start the print job or a print job preview:

- PRINTJOB: Print job is started.
- PREVIEW: Preview of the print job is started.

#### Example

The following program code executes a preview or print job for each content of the printmethod tag. The printmethod tag is read by an I/O field that is connected to the strPrintJobMethod tag.

{

char* pszPrintjobName;

char* printmethod;

//Get the print method

printf("Input PRINTJOB for printing or PREVIEW for a quick view");

printmethod = GetTagChar("strPrintJobMethod")

//Print job or show preview

ReportJob(&PrintjobName, printmethod);

//error handling

if(printmethod=="PRINTJOB")

{

  // message for printing completed

printf("printing done");

  ...

}

else

{

  // User defined code if the

  // job is a preview or failed

  ...

}

}

### ResetBit (RT Professional)

#### Description

Sets the value of a "Bool" type tag to 0 (FALSE).

#### Use in the function list

ResetBit (Tag)

#### Use in user-defined functions

ResetBit Tag

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

#### Parameters

**Tag**

The BOOL type tag which is set to 0 (FALSE).

#### Example

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

strResult="Old Value: "&bSaved &Chr(13)&"New Value: "&bValue

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

### ResetBitInTag (RT Professional)

#### Description

Sets a bit in the specified tag to 0 (FALSE).

After changing the given bit, the system function transfers the entire tag back to the PLC. It is not checked whether other bits in the tags have changed in the meantime. Operator and PLC have read-only access to the indicated tag until it is transferred back to the PLC.

> **Note**
>
> If the PLC supports BOOL tags, do not use this system function. Use the "ResetBit" system function instead.

#### Use in the function list

ResetBitInTag (Tag, Bit)

#### Use in user-defined functions

ResetBitInTag Tag, Bit

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

#### Parameters

**Tag**

The tag in which a bit is set to 0 (FALSE).

**Bit**

The number of the bit that is set to 0 (FALSE).

When this system function is used in a user-defined function, the bits in the specified tag will be counted from right to left independent of the PLC used. The counting begins with 0.

#### Example

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

strResult="Old Value: "&bSaved &Chr(13)&"New Value: "&bValue

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

### Set_Focus (RT Professional)

#### Function

Sets the focus on the specified object.

#### Syntax

BOOL Set_Focus(lpszPictureName, lpszObjectName)

#### Parameters

**lpszPictureName**

Screen name

**lpszObjectName**

Object name

#### Return value

**TRUE**

The function has been completed without any errors.

**FALSE**

An error has occurred.

### SetBit (RT Professional)

#### Description

Sets the value of a "Bool" type tag to 1 (TRUE).

#### Use in the function list

SetBit (Tag)

#### Use in user-defined functions

SetBit Tag

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

#### Parameters

**Tag**

The BOOL type tag which is set to 1 (TRUE).

#### Example

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

strResult="Old Value: "&bSaved &Chr(13)&"New Value: "&bValue

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

### SetBitInTag (RT Professional)

#### Description

Sets a bit in the given tag to 1 (TRUE).

After changing the given bit, the system function transfers the entire tag back to the PLC. It is not checked whether other bits in the tags have changed in the meantime. Operator and PLC have read-only access to the indicated tag until it is transferred back to the PLC.

> **Note**
>
> If the PLC supports BOOL tags, do not use this system function. Use the "SetBit" system function instead.

#### Use in the function list

SetBitInTag (Tag, Bit)

#### Use in user-defined functions

SetBitInTag Tag, Bit

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

#### Parameters

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

#### Example

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

strResult="Old Value: "& bSaved & "New Value: " & bValue

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

### SetLanguageByLocaleID (RT Professional)

#### Description

Changes the language setting in Runtime.

Can only be used in C scripting.

#### Syntax

BOOL SetLanguageByLocaleID(dwLocaleID);

#### Parameters

**dwLocaleID**

Language ID of the language to be set

#### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

#### Example

The following program code uses the SetLanguage function to set the current runtime language to German and saves the return value to the ok tag.

{

BOOL ok;

DWORD old_language;

DWORD new_language;

//Get the current language and save it

old_language = GetLanguageByLocaleID ();

//Set the current language to German

ok = SetLanguageByLocaleID (0x0407);

//Get the current language and save it

new_language = GetLanguageByLocaleID ();

//error handling

if(ok)

{

  // succeeded

  printf ( "RT language is now German." );

}

else

{

  // failed

  printf ( "RT language was not updated." );

}

//print language code

printf ("Former language code: %d\r\n", old_language);

printf ("Current language code: %d\r\n", new_language);

}

The saved return value can be processed in the following code.

---

**See also**

[GetLanguageByLocaleID (RT Professional)](#getlanguagebylocaleid-rt-professional)
  
[Example of configuring a language switch (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#example-of-configuring-a-language-switch-rt-professional-1)

### SetLanguageByName (RT Professional)

#### Description

Changes the language setting in Runtime by the country name of the language to be set.

Can only be used in C scripting.

#### Use in the function list

SetLanguageByName (Language))

#### Syntax

Bool SetLanguageByName(lpszLanguage);

#### Parameters

**lpszLanguage**

Pointer to the language abbreviation according to "RFC 1766" format.

#### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

### SetLink (RT Professional)

#### Function

Creating a tag connection of object properties

#### Syntax

BOOL SetLink(LPCTSTR lpszPictureName, LPCTSTR lpszObjectName, LPCTSTR lpszPropertyName, LPLINKINFO *pLink);

#### Parameter

**lpszPictureName**

Screen name

**lpszObjectName**

Object name

**lpszPropertyName**

Name of the object property

**pLink**

Pointer to a structure of the type: LINKINFO

#### Return value

**TRUE**

The function has been completed without any errors.

**FALSE**

An error has occurred.

---

**See also**

[Structure definition LINKINFO (RT Professional)](#structure-definition-linkinfo-rt-professional)

### SetProp (RT Professional)

This section contains information on the following topics:

- [SetPropBOOL (RT Professional)](#setpropbool-rt-professional)
- [SetPropChar (RT Professional)](#setpropchar-rt-professional)
- [SetPropDouble (RT Professional)](#setpropdouble-rt-professional)
- [SetPropLong (RT Professional)](#setproplong-rt-professional)

#### SetPropBOOL (RT Professional)

##### Description

Sets an object property of data type "BOOL".

Can only be used in C scripting.

##### Syntax

BOOL SetPropBOOL(ScreenName, Object, NameOfTheProperty, Value)

##### Parameters

**ScreenName**

Screen name

**Object**

Object name You must set the parameter Object = NULL if the function call relates to a screen object property.

**NameOfTheProperty**

Name of the object property

**Value**

Value assigned to the object property of data type "BOOL".

##### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

##### Example

The following program code uses the SetPropBool function to set the property of the gs_graph_iofield object to "Visible". The return value is saved to the ok tag.

{

BOOL ok;

//Set the visibility TRUE

ok = SetPropBOOL("gs_graph_iofield","IOField1","Visible",TRUE);

//error handling

if(ok)

{

  // succeeded

  printf ( "IO field is visible." );

}

else

{

  // failed

  printf ( "Error - visibility not set" );

}

...

}

The saved return value can be processed in the following code.

#### SetPropChar (RT Professional)

##### Description

Sets an object property of data type "char".

Can only be used in C scripting.

##### Syntax

BOOL SetPropChar(ScreenName, Object, NameOfTheProperty, Value)

##### Parameters

**ScreenName**

Screen name

**Object**

Object name You must set the parameter Object = NULL if the function call relates to a screen object property.

**NameOfTheProperty**

Name of the object property

**Value**

Value assigned to the object property of data type "char".

##### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

##### Example

The following program code uses the SetPropChar function to set the Tooltiptext property of the gs_graph_iofield object to the "Tooltiptext 1" value. The return value is saved to the ok tag.

{

BOOL ok;

//Set the property Tooltiptext

ok = SetPropChar("Screen_1","gs_graph_iofield","ToolTipText","Tooltiptext 1");

//error handling

if(ok)

{

  // succeeded

  printf ( "Property of Tooltiptext is now Tooltiptext 1." );

}

else

{

  // failed

  printf ( "Error - property not set" );

}

...

}

The saved return value can be processed in the following code.

#### SetPropDouble (RT Professional)

##### Description

Sets an object property of data type "Double".

Can only be used in C scripting.

##### Syntax

BOOL SetPropDouble(ScreenName, Object, NameOfTheProperty, Value)

##### Parameters

**ScreenName**

Screen name

**Object**

Object name You must set the parameter Object = NULL if the function call relates to a screen object property.

**NameOfTheProperty**

Name of the object property

**Value**

Value assigned to the object property of data type "double".

##### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

##### Example

The following program code accesses an object property in the screenName screen. In this example, the SetPropDouble function sets the property (radius) of "Circle_1" to the value 10. The return value is saved to the ok tag.

{

BOOL ok;

//Set the property of circle

ok = SetPropDouble(screenName,"Circle_1","Radius",10);

//error handling

if(ok)

{

  // succeeded

  printf ( "Radius was set." );

}

else

{

  // failed

  printf ( "Error - radius not set" );

}

...

}

The saved return value can be processed in the following code.

---

**See also**

[Example of accessing objects in the Screens editor (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#example-of-accessing-objects-in-the-screens-editor-rt-professional-1)

#### SetPropLong (RT Professional)

##### Description

Sets an object property of data type "long".

Can only be used in C scripting.

##### Syntax

BOOL SetPropLong(ScreenName, Object, NameOfTheProperty, Value)

##### Parameters

**ScreenName**

Screen name

**Object**

Object name You must set the parameter Object = NULL if the function call relates to a screen object property.

**NameOfTheProperty**

Name of the object property

**Value**

Value assigned to the object property of data type "long".

##### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

##### Example

The following program code uses the SetPropLong function to change the foreground color of an object: In "Screen_1", the "ForeColor property of the "Button1" object is set to the value 65333 (red). The return value is saved to the ok tag.

{

BOOL ok;

//Set the property Tooltiptext

ok = SetPropLong("Screen_1","Button1","ForeColor",65333);

//error handling

if(ok)

{

  // succeeded

  printf ( "Color was set." );

}

else

{

  // failed

  printf ( "Error - color not set" );

}

...

}

The saved return value can be processed in the following code.

---

**See also**

[Accessing objects with C (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#accessing-objects-with-c-rt-professional)
  
[Example of writing object properties (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#example-of-writing-object-properties-rt-professional-1)

### SetPropertyByConstant (RT Professional)

#### Description

Specifies the value of an object property as a string.

#### Use in the function list

SetPropertyByConstant (Screen name, screen object, name of the property, value)

#### Use in user-defined functions

SetPropertyByConstant Screen_name, Screen_object, Property_name, Value

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

If you want to change the property of a screen, the parameter "Object" must be empty. For this purpose, use the following syntax, for example:

SetPropertyByConstant Screen_name, Property_name, Value

#### Parameters

**Screen name**

Name of the screen that contains the object.

**Screen object**

Name of the object whose property is changed.

**Name of the property**

Name of the property that will be changed.

**Value**

The value assigned to the property.

#### Example

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

#### Example: Changing a screen property

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
  
[Example of defining object colors (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#example-of-defining-object-colors-rt-professional-1)

### SetPropertyByProperty (RT Professional)

#### Description

Specifies the value of an object property with another object property.

#### Use in the function list

SetPropertyByProperty (screen name, object, property name, target screen name, target screen object, target property name)

#### Use in user-defined functions

SetPropertyByProperty Screen_name, Screen_object, Property_name, Source_screen_name, Source_screen_object, Source_property_name

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

If you want to specify the property of a screen with another screen property, the parameters "Object" and "Destination object" must be empty. For this purpose, use the following syntax, for example:

SetPropertyByProperty Screen_name, Property_name, Source_screen_name, Source_property_name

#### Parameters

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

#### Example

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

### SetPropertyByTag (RT Professional)

#### Description

Specifies the value of an object property with a tag value.

#### Use in the function list

SetPropertyByTag (Screen name, screen object, name of the property, tag name)

#### Use in user-defined functions

SetPropertyByTag Screen_name, Screen_object, Property_name, Tag_name

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

If you want to specify the property of a screen by means of a tag value, the "Object" parameter must be empty. For this purpose, use the following syntax, for example:

SetPropertyByTag Screen_name, Property_name, Tag_name

#### Parameters

**Screen name**

Name of the screen that contains the object.

**Screen object**

Name of the object containing the property to be set with the tag value.

**Name of the property**

Name of the property that is set with the tag value.

**Tag name**

Name of the tag that contains the value of the property.

#### Example

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

#### Example

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

### SetPropertyByTagIndirect (RT Professional)

#### Description

Writes the value of an indirect addressed tag to an object property. The tag transferred as parameter contains the name of a second tag the value of which is read.

#### Use in the function list

SetPropertyByTagIndirect (Screen name, screen object, name of the property, , tag name)

#### Use in user-defined functions

SetPropertyByTagIndirect Screen_name, Screen_object, Property_name, Tag_name

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

If you want to specify the property of a screen by means of a tag, the "Object" parameter must be empty. For this purpose, use the following syntax, for example:

SetPropertyByTagIndirect Screen_name, Property_name, Tag_name

#### Parameters

**Screen name**

Name of the screen that contains the object.

**Screen object**

Name of the object whose property you want to change.

**Name of the property**

Name of the property to be changed.

**Tag name**

Name of the tag which, in turn, contains the name of the tag whose value is read.

#### Example

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

### SetTag (RT Professional)

This section contains information on the following topics:

- [SetTag functions (RT Professional)](#settag-functions-rt-professional)
- [SetTagDateTime (RT Professional)](#settagdatetime-rt-professional)
- [SetTagMultiStateWait functions (RT Professional)](#settagmultistatewait-functions-rt-professional)
- [SetTagMultiWait functions (RT Professional)](#settagmultiwait-functions-rt-professional)
- [SetTagState functions (RT Professional)](#settagstate-functions-rt-professional)
- [SetTagStateWait functions (RT Professional)](#settagstatewait-functions-rt-professional)
- [SetTagValue functions (RT Professional)](#settagvalue-functions-rt-professional)
- [SetTagValueWait functions (RT Professional)](#settagvaluewait-functions-rt-professional)
- [SetTagWait functions (RT Professional)](#settagwait-functions-rt-professional)
- [SetTag (RT Professional)](#settag-rt-professional-1)
- [SetTagByProperty (RT Professional)](#settagbyproperty-rt-professional)
- [SetTagByTagIndirect (RT Professional)](#settagbytagindirect-rt-professional)
- [SetTagIndirect (RT Professional)](#settagindirect-rt-professional)
- [SetTagIndirectByProperty (RT Professional)](#settagindirectbyproperty-rt-professional)
- [SetTagIndirectByTagIndirect (RT Professional)](#settagindirectbytagindirect-rt-professional)
- [SetTagIndirectWithOperatorEvent (RT Professional)](#settagindirectwithoperatorevent-rt-professional)
- [SetTagWithOperatorEvent (RT Professional)](#settagwithoperatorevent-rt-professional)

#### SetTag functions (RT Professional)

##### Description

The SetTagXXX function calculates the value of a tag of the specified data type.

Can only be used in C scripting.

The following table shows the different SetTag functions for setting the tag value:

| Function name | Parameter | PLC data type | HMI data type |
| --- | --- | --- | --- |
| SetTagBit | Tag Tag_Name, short int value | Binary tag | Bool |
| SetTagByte | Tag Tag_Name, BYTE value | Unsigned 8-bit | USInt |
| SetTagDateTime | Tag Tag_Name, SYSTEMTIME value | DTL | DateTime |
| SetTagChar | Tag Tag_Name, LPSTR value | Text tag 8-bit or text tag 16-bit | String or WString |
| SetTagDouble | Tag Tag_Name, double value | Floating point 64-bit | LReal |
| SetTagDWord | Tag Tag_Name, DWORD value | Unsigned 32-bit | UDInt |
| SetTagFloat | Tag Tag_Name, float value | Floating point 32-bit | Real |
| SetTagRaw | Tag Tag_Name, BYTE* pValue, DWORD size | Raw data type | Raw |
| SetTagSByte | Tag Tag_Name, char value | Signed 8-bit | SInt |
| SetTagSDWord | Tag Tag_Name, long int value | Signed 32-bit | DInt |
| SetTagSWord | Tag Tag_Name, short int value | Signed 16-bit | Int |
| SetTagWord | Tag Tag_Name, WORD value | Unsigned 16-bit | UInt |

> **Note**
>
> **Error message when using a tag of WString type**
>
> If you use a WString type tag in a SetTag system function that was converted into a C script, an error message is generated in the Global Script diagnostics window when the function is executed. The function is correctly executed despite the error message.
>
> The following SetTag functions are affected:
>
> - SetTagWithOperatorEvent
> - SetTagIndirect
> - SetTagByTagIndirect
> - SetTagIndirectByTagIndirect
> - SetTagByProperty
> - SetTagIndirectByProperty

##### Syntax

BOOL<FunctionName><(Parameter)>;

Example: BOOL SetTagBit(Tag_Name, value);

##### Parameter

**Tag_Name**

Tag name

**value**

Value of the tags in the specified data type.

**pValue**

Pointer to a byte field containing the value of the raw data tags.

**size**

Length of the byte field in bytes

##### Return value

**TRUE**

System function completed without errors.

However, no check is made to verify that the tag was written without any errors.

**FALSE**

An error has occurred.

##### Example

The following program code uses the SetTagBit function to set the value of the gs_tag_bit tag to TRUE and saves the return value to the ok tag.

{

BOOL ok;

BOOL bvalue;

//Set the tag to true

ok = SetTagBit("gs_tag_bit", TRUE);

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

[Access to HMI tags (Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#access-to-hmi-tags-panels-comfort-panels-rt-advanced-rt-professional)
  
[VariableStateType property (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#variablestatetype-property-rt-professional)
  
[Data types (RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-types-rt-professional)

#### SetTagDateTime (RT Professional)

##### Function

Sets the value of a tag of data type "Date/Time".

##### Syntax

BOOL SetTagDateTime(Tag_Name, value);

##### Parameter

**Tag_Name**

Tag name

**value**

Value of the tag in the data type "Date/Time".

##### Return value

**TRUE**

The function itself has been completed without any errors.

However, no check is made to verify that the tag was written without any errors.

**FALSE**

An error has occurred.

#### SetTagMultiStateWait functions (RT Professional)

##### Description

Sets the values of several tags. The system function will end only after the AS has reported the acceptance of the value.

The system function can be used in C scripting only.

The system function must be given a DWORD array, in the member of which the status of the individual tags will be located after the system function has been called. The size of the array must be large enough to provide sufficient storage space for the status.

For more information, refer to the FAQs on the Internet, [entry ID 26712371](https://support.industry.siemens.com/cs/us/en/view/26712371).

##### Syntax

BOOL SetTagMultiStateWait(pdwState, pFormat,...);

##### Parameters

**pdwState**

Field in which the tag status is saved.

**pFormat**

Format description for all the requested tags along with the name and value for each tag.

##### Return value

**TRUE**

System function completed without errors.

However, no check is made to verify that the tag was written without any errors.

**FALSE**

An error has occurred.

##### Example

The following program code uses the SetTagMultiStateWait function to set the value of several tags.

1. Creation of a DWord arrays of the necessary size (number of tags)
2. Creation of the tags that will contain the values to be transferred to the WinCC tags by means of the SetTagMultiStateWait function
3. Writing the values of the recently declared tags to the WinCC tags:

   - gs_tag_bit including the tag value "lValue1"
   - gs_tag_SByte including the tag value in the address "&lValue2"
   - etc.

{

#define DATA_SIZE 5

DWORD dwData[DATA_SIZE];

//define all tags

BOOL lValue1;

long lValue2;

char szValue3[_MAX_PATH];

float lValue4;

char lValue5;

// Fill the tags with the values

// you want to set into the WinCC tags

...

//Set the WinCC tags

SetTagMultiStateWait(dwData,"%d%d%s%f%d","gs_tag_bit",lValue1,

"gs_tag_SByte",lValue2,

"gs_tag_char",szValue3,

"gs_tag_float",lValue4,

"gs_tag_word",lValue5);

...

}

The saved return value can be processed in the following code.

---

**See also**

[Constants (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#constants-rt-professional)
  
[Entry 26712371](https://support.industry.siemens.com/cs/us/en/view/26712371)

#### SetTagMultiWait functions (RT Professional)

##### Description

The values of several tags are set in the specified format. The system function will end only after the AS has reported the acceptance of the value.

Can only be used in C scripting.

For more information, refer to the FAQs on the Internet, [entry ID 26712371](https://support.industry.siemens.com/cs/us/en/view/26712371).

##### Syntax

BOOL SetTagMultiWait(pFormat,...);

##### Parameters

**pFormat**

Format description for all the requested tags along with the name and value for each tag.

##### Return value

**TRUE**

System function completed without errors.

However, no check is made to verify that the tag was written without any errors.

**FALSE**

An error has occurred.

##### Example

The following program code uses the SetTagMultiWait function to change the value of several tags. The return value is saved to the ok tag.

{

BOOL ok;

//memory for values allocated via SysMalloc

DWORD dwVar1Value;

char* szVar2Value;

double dbVar3Value;

//settings

ok=SetTagMultiWait("%d%s%f", "Ernie_word", 16,

"Ernie_char", "Hallo Welt",

"Ernie_double", 55.4711);

//error handling

if(ok)

{

  // succeeded

  printf ( "Function has run through.\r\n" );

// Get values and print

GetTagMultiWait("%d%s%f", "Ernie_word", &dwVar1Value,

  "Ernie_char", &szVar2Value,

  "Ernie_double", &dbVar3Value);

printf("Word %d, String %s, Double %f\r\n",

  dwVar1Value, szVar2Value, dbVar3Value);

}

else

{

  // failed

  printf ( "Error - function failed." );

}

...

}

##### Example

The GetTagMultiWait function is used in the following program code to read several tags of different types:

1. Declaration of three tags as memory for three different tag types
2. Declaration of the boolean tag ok for buffering the return value (TRUE/FALSE)
3. Reading the three tags and saving the values to the corresponding addresses.

   The return value of the function is saved to the ok tag.
4. Output of the three tags with tag type prefix

DWORD dwVar1Value;

char* szVar2Value;

//Memory for the tag value is allocated by the function SysMalloc

double dbVar3Value;

BOOL ok;

ok=GetTagMultiWait("%d%s%f", "Ernie_word", &dwVar1Value,

  "Ernie_char", &szVar2Value,

  "Ernie_double", &dbVar3Value);

printf("Word %d, String %s, Double %f\r\n",

  dwVar1Value, szVar2Value, dbVar3Value);

---

**See also**

[Entry 26712371](https://support.industry.siemens.com/cs/us/en/view/26712371)

#### SetTagState functions (RT Professional)

##### Description

Sets the value of a tag of a specified data type. It also returns the status of the tags.

Can only be used in C scripting.

The following table lists the different SetTagStateXXX functions for reading the tag value:

| Function name | Parameters | PLC data type | HMI data type |
| --- | --- | --- | --- |
| SetTagBitState | Tag Tag_Name, short int value, PDWORD lp_dwstate | Binary tag | Bool |
| SetTagByteState | Tag Tag_Name, BYTE value, PDWORD lp_dwstate | Unsigned 8-bit | UByte |
| SetTagCharState | Tag Tag_Name, LPSTR value, PDWORD lp_dwstate | Text tag 8-bit or text tag 16-bit | String |
| SetTagDoubleState | Tag Tag_Name, double value, PDWORD lp_dwstate | Floating point 64-bit | Double |
| SetTagDWordState | Tag Tag_Name, DWORD value, PDWORD lp_dwstate | Unsigned 32-bit | UInteger |
| SetTagFloatState | Tag Tag_Name, float value, PDWORD lp_dwstate | Floating point 32-bit | Float |
| SetTagRawState | Tag Tag_Name, BYTE* pValue, DWORD size, PDWORD lp_dwstate | Raw data type | Raw |
| SetTagSByteState | Tag Tag_Name, signed char value, PDWORD lp_dwstate | Signed 8-bit | Byte |
| SetTagSDWordState | Tag Tag_Name, long int value, PDWORD lp_dwstate | Signed 32-bit | Integer |
| SetTagSWordState | Tag Tag_Name, short int value, PDWORD lp_dwstate | Signed 16-bit | Short |
| SetTagWordState | Tag Tag_Name, WORD value, PDWORD lp_dwstate | Unsigned 16-bit | UShort |

##### Syntax

BOOL <FunctionName><(Parameter)>;

Example: BOOL SetTagBitState(Tag_Name, value, lp_dwstate);

##### Parameters

**Tag_Name**

Tag name

**value**

Value of the tags of a specified type.

**lp_dwstate**

Pointer to a DWORD to which the tag status is saved on completion of the system function cycle.

**pFormat**

Format description for all the requested tags along with name and value for each tag.

**pValue**

Pointer to a byte field containing the value of the raw data tags.

**size**

Length of the byte field in bytes

##### Return value

**TRUE**

System function completed without errors.

However, no check is made to verify that the tag was written without any errors.

**FALSE**

An error has occurred.

##### Example

The following program code uses the SetTagBitState function to set the value of the gs_tag_bit tag to TRUE and saves the return value to the ok tag. ""&dwstate" is the address of the tag in which the tag status is stored.

The saved return value can be processed in the following code.

{

DWORD dwstate;

BOOL ok;

//Load dwState with default values

dwstate = 0xFFFFFFFF;

//Set the value of the tag to TRUE

//dwstate is the tag state

ok = SetTagBitState("gs_tag_bit",TRUE,&dwstate);

//error handling

if(ok)

{

  // succeeded

  printf ( "Function has run through.\r\n" );

printf ("Status of gs_tag_bit: %d\r\n", dwstate);

}

else

{

  // failed

  printf ( "Error - function failed." );

}

...

}

---

**See also**

[Constants (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#constants-rt-professional)
  
[Data types (RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-types-rt-professional)

#### SetTagStateWait functions (RT Professional)

##### Description

Sets the value of a tag of a specified data type. The system function will end only after the AS has reported the acceptance of the value. It also returns the status of the tags.

Can only be used in C scripting.

The following table lists the different SetTagStateWait functions for setting the tag value:

| Function name | Parameters | PLC data type | HMI data type |
| --- | --- | --- | --- |
| SetTagBitStateWait | Tag Tag_Name, short int value, PDWORD lp_dwstate | Binary tag | Bool |
| SetTagByteStateWait | Tag Tag_Name, BYTE value, PDWORD lp_dwstate | Unsigned 8-bit | UByte |
| SetTagCharStateWait | Tag Tag_Name, LPSTR value, PDWORD lp_dwstate | Text tag 8-bit or text tag 16-bit | String |
| SetTagDoubleStateWait | Tag Tag_Name, double value, PDWORD lp_dwstate | Floating point 64-bit | Double |
| SetTagDWordStateWait | Tag Tag_Name, DWORD value, PDWORD lp_dwstate | Unsigned 32-bit | UInteger |
| SetTagFloatStateWait | Tag Tag_Name, float value, PDWORD lp_dwstate | Floating point 32-bit | Float |
| SetTagRawStateWait | Tag Tag_Name, BYTE* pValue, DWORD size, PDWORD lp_dwstate | Raw data type | Raw |
| SetTagSByteStateWait | Tag Tag_Name, char value, PDWORD lp_dwstate | Signed 8-bit | Byte |
| SetTagSDWordStateWait | Tag Tag_Name, long int value, PDWORD lp_dwstate | Signed 32-bit | Integer |
| SetTagSWordStateWait | Tag Tag_Name, short int value, PDWORD lp_dwstate | Signed 16-bit | Short |
| SetTagWordStateWait | Tag Tag_Name, WORD value, PDWORD lp_dwstate | Unsigned 16-bit | UShort |

##### Syntax

BOOL<FunctionName><(Parameter)>;

Example: BOOL SetTagBitStateWait(Tag_Name, value, lp_dwstate);

##### Parameters

**Tag_Name**

Tag name

**value**

Value of the tags of a specified type.

**lp_dwstate**

Pointer to a DWORD to which the tag status is saved on completion of the system function cycle.

**pValue**

Pointer to a byte field containing the value of the raw data tags.

**size**

Length of the byte field in bytes

##### Return value

**TRUE**

System function completed without errors.

However, no check is made to verify that the tag was written without any errors.

**FALSE**

An error has occurred.

##### Example

The following program code uses the SetTagBitStateWait function to set the value of the gs_tag_bit tag to TRUE and saves the return value to the ok tag. ""&dwstate" is the address of the tag in which the tag status is stored.

The saved return value can be processed in the following code.

{

DWORD dwstate;

BOOL ok;

//Load dwState with default values

dwstate = 0xFFFFFFFF;

//Set the value of the tag to TRUE

//dwstate is the tag state

ok = SetTagBitStateWait("gs_tag_bit",TRUE,&dwstate);

//error handling

if(ok)

{

  // succeeded

  printf ( "Function has run through.\r\n" );

printf ("Status of gs_tag_bit: %d\r\n", dwstate);

}

else

{

  // failed

  printf ( "Error - function failed." );

}

...

}

---

**See also**

[Constants (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#constants-rt-professional)
  
[Data types (RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-types-rt-professional)

#### SetTagValue functions (RT Professional)

##### Description

Enables the transfer of a value in the form of a variant and sets the pointer to the value of data type "Variant".

Can only be used in C scripting.

##### Syntax

BOOL SetTagValue(lpdmVarKey, lpdmValue, dwState, lpdmError);

##### Parameters

**lpdmVarKey**

Pointer to a structure of data type "DM_VARKEY"

**lpdmValue**

Pointer to a structure of data type "Variant". Refer to relevant technical references for the description of data type VARIANT.

**lpdmError**

Pointer on the structure that contains the error description.

##### Return value

**TRUE**

System function completed without errors.

However, no check is made to verify that the tag was written without any errors.

**FALSE**

An error has occurred.

##### Example

The SetTagValue function is used in the following program code to transfer the value in varKey.

A specific code will be executed, depending on the return value in keyFound (TRUE/FALSE).

{

// tags for setting the value

DM_VARKEY varKey;

LPVARIANT value;

LPCMN_ERROR error1:

// tags for getting the value

DM_VAR_UPDATE_STRUCT result;

CMN_ERROR error:

BOOL keyFound;

ok = SetTagValue(&varKey, &value, &error1);

if (keyFound)

{

  // succeeded, get the new value

GetTagValue(&varKey, &result, &error);

  // print tag value

printf ("Value of varKey: %d\r\n", &varKey);

  ...

}

else

{

  // failed

  printf ( "Error - function failed." );

  ...

}

}

#### SetTagValueWait functions (RT Professional)

##### Description

Enables the transfer of a value in the form of a variant and sets the pointer to the value of data type "Variant". The system function will end only after the AS has reported the acceptance of the value.

Can only be used in C scripting.

##### Syntax

BOOL SetTagValueWait(lpdmVarKey, lpdmValue, dwState, lpdmError);

##### Parameters

**lpdmVarKey**

Pointer to a structure of data type "DM_VARKEY"

**lpdmValue**

Pointer to a structure of data type "Variant". Refer to relevant technical references for the description of data type VARIANT.

**dwState**

Status of the tags that is returned after the system function cycle.

**lpdmError**

Pointer on the structure that contains the error description.

##### Return value

**TRUE**

System function completed without errors.

There is no check to see if the tag was written without any errors.

**FALSE**

An error has occurred.

##### Example

The SetTagValueWait function is used in the following program code to transfer the value in varKey.

A specific code will be executed, depending on the return value in keyFound (TRUE/FALSE).

{

// tags for setting the value

DM_VARKEY varKey;

LPVARIANT value;

LPCMN_ERROR error1:

// tags for getting the value

DM_VAR_UPDATE_STRUCT result;

CMN_ERROR error:

BOOL keyFound;

ok = SetTagValueWait(&varKey, &value, &error1);

if (keyFound)

{

  // succeeded, get the new value

GetTagValueWait(&varKey, &result, &error);

  // print tag value

printf ("Value of varKey: %d\r\n", &varKey);

  ...

}

else

{

  // failed

  printf ( "Error - function failed." );

  ...

}

}

#### SetTagWait functions (RT Professional)

##### Description

Sets the value of a tag of a specified data type. The system function will end only after the AS has reported the acceptance of the value.

Can only be used in C scripting.

The following table lists the different SetTagWait functions for setting the tag value:

| Function name | Parameters | PLC data type | HMI data type |
| --- | --- | --- | --- |
| SetTagBitWait | Tag Tag_Name, short int value | Binary tag | Bool |
| SetTagByteWait | Tag Tag_Name, BYTE value | Unsigned 8-bit | UByte |
| SetTagCharWait | Tag Tag_Name, char* value | Text tag 8-bit or text tag 16-bit | String |
| SetTagDoubleWait | Tag Tag_Name, double value | Floating point 64-bit | Double |
| SetTagDWordWait | Tag Tag_Name, DWORD value | Unsigned 32-bit | UInteger |
| SetTagFloatWait | Tag Tag_Name, float value | Floating point 32-bit | Float |
| SetTagRawWait | Tag Tag_Name, BYTE* pValue, DWORD size | Raw data type | Raw |
| SetTagSByteWait | Tag Tag_Name, char value | Signed 8-bit | Byte |
| SetTagSDWordWait | Tag Tag_Name, long int value | Signed 32-bit | Integer |
| SetTagSWordWait | Tag Tag_Name, short int value | Signed 16-bit | Short |
| SetTagWordWait | Tag Tag_Name, WORD value | Unsigned 16-bit | UShort |

##### Syntax

BOOL <FunctionName><(Parameter)>;

Example: BOOL SetTagBitWait(Tag_Name, value);

##### Parameters

**Tag_Name**

Tag name

**value**

Value of the tags of a specified type.

**pValue**

Pointer to a byte field containing the value of the raw data tags.

**size**

Length of the byte field in bytes

##### Return value

**TRUE**

System function completed without errors.

However, no check is made to verify that the tag was written without any errors.

**FALSE**

An error has occurred.

##### Example

The following program code uses the SetTagBitWait function to set the value of the gs_tag_bit tag to TRUE and saves the return value to the ok tag.

{

BOOL ok;

BOOL bvalue;

//Set the tag to true

ok = SetTagBitWait("gs_tag_bit", TRUE);

//error handling

if(ok)

{

  // succeeded

  printf ( "Function has run through.\r\n" );

bvalue = GetTagBitWait("gs_tag_bit");

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

[Data types (RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#data-types-rt-professional)

#### SetTag (RT Professional)

##### Description

Assigns a new value to the given tag.

> **Note**
>
> This system function can be used to assign strings and numbers, depending on the type of tag.

##### Use in the function list

SetTag (Tag, Value)

##### Use in user-defined functions

SetTag Tag, Value

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

##### Parameters

**Tag**

The tag to which the given value is assigned.

**Value**

The value which the given tag is assigned.

> **Note**
>
> The "SetTag" system function is only executed after a connection has been established.

##### Example

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

#### SetTagByProperty (RT Professional)

##### Description

Specifies a tag value with the value of an object property. The change is also logged in the alarm system.

##### Use in the function list

SetTagIndirectByProperty (tag name, screen name, screen object, name of the property, with or without operator event)

##### Use in user-defined functions

SetTagByProperty Tag_name, Screen_name, Screen_object, Property_name, With_or_without_operator_event

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

##### Parameters

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

##### Example

The following program code returns the value of the selected text when you click in a combo box.

{

char* rt_value;

SetTagByProperty (rt_value, screenName, objectName, "SelectedText", hmiWithoutOperatorEvent);

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

#### SetTagByTagIndirect (RT Professional)

##### Description

Writes the value of an indirect addressed tag to a tag. The tag transferred as parameter contains the name of a second tag the value of which is read. The change in the alarm system is logged via an operator input alarm.

##### Use in the function list

SetTagIndirectByTagIndirect (name of the tag, tag name, with or without operator input alarm)

##### Use in user-defined functions

SetTagByTagIndirect Tag_name, Source_tag_name, With_or_without_operator_event

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

##### Parameters

**Name of the tag**

Name of the tag whose value is to be set.

**Tag name**

Name of a string tag which contains the name of a tag which supplies the tag value.

**With or without operator event**

0 (hmiWithoutOperatorEvent) = Without operator input alarm

1 (hmiWithOperatorEvent) = With operator input alarm

##### Example

The following program code writes the value of the tag Tag4 to the tag Tag1.

{

SetTag ("IndirectRead", "Tag4");

SetTagByTagIndirect ("Tag1", "IndirectRead", hmiWithoutOperatorEvent);

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

#### SetTagIndirect  (RT Professional)

##### Description

Writes a value to an indirect addressed tag. The tag transferred as output parameter contains the name of a second tag the value of which is changed by the function. The change in the alarm system is logged via an operator input alarm.

##### Use in the function list

SetTagIndirect (tag name, , value, with or without operator event)

##### Use in user-defined functions

SetTagIndirect Tag_name, Value, With_or_without_operator_event

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

##### Parameters

**Tag name**

Name of a string tag which contains the name of a tag whose value is to be changed.

**Value**

Value which is to be written.

**With or without operator event**

0 (hmiWithoutOperatorEvent) = Without operator event

1 (hmiWithOperatorEvent) = With operator event

##### Example

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

#### SetTagIndirectByProperty (RT Professional)

##### Description

Writes the value of an object property to an indirectly addressed tag. The tag transferred as output parameter contains the name of a second tag the value of which is changed by the function. The change in the alarm system is logged via an operator input alarm.

##### Use in the function list

SetTagIndirectByProperty (Tag name, Screen name, Screen object, Name of the property, With or without operator event)

##### Use in user-defined functions

SetTagIndirectByProperty Tag_name, Screen_name, Screen_object, Property_name, With_or_without_operator_event

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

##### Parameters

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

##### Example

The following program code writes the value of the object property "Background color" to the tag Tag2.

{

SetTag ("IndirectWrite", "Tag2");

SetTagIndirectByProperty ("IndirectWrite", screenName, objectName, "BackColor", hmiWithoutOperatorEvent);

...

}

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

#### SetTagIndirectByTagIndirect (RT Professional)

##### Description

Writes the value of an indirectly addressed tag to an indirectly addressed tag. The tag transferred as output parameter contains the name of a second tag the value of which is changed by the function. The tag transferred as parameter contains the name of a second tag the value of which is read. The change in the alarm system is logged via an operator input alarm.

##### Use in the function list

SetTagIndirectByTagIndirect (Tag name, Tag name, With or without operator input alarm)

##### Use in user-defined functions

SetTagIndirectByTagIndirect Tag_name, Source_tag_name, With_or_without_operator_event

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

##### Parameters

**Tag name**

Name of a string tag which contains the name of a tag whose value is to be changed.

**Tag name**

Name of the indirect tag that returns the tag value.

**With or without operator event**

0 (hmiWithoutOperatorEvent) = Without operator event

1 (hmiWithOperatorEvent) = With operator event

##### Example

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

#### SetTagIndirectWithOperatorEvent (RT Professional)

##### Description

Specifies the indirect name for a tag. The change is also logged in the alarm system.

##### Use in the function list

SetTagIndirectWithOperatorInputAlarm (Tag name (output), LpValue)

##### Use in user-defined functions

SetTagIndirectWithOperatorEvent

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

##### Parameters

**Tag name (output)**

Name of the tag to which the tag name is written.

**LpValue**

Name of the tag written to the tag.

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)

#### SetTagWithOperatorEvent (RT Professional)

##### Description

Specifies the value for a tag. The change is also logged in the alarm system.

##### Use in the function list

SetTagWithOperatorEvent (name of the tag, value)

##### Use in user-defined functions

SetTagWithOperatorEvent Tag_name, Value

Can be used if the configured device supports user-defined functions. For more information, refer to "[System functions for Runtime Professional](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)".

##### Parameters

**Name of the tag**

Name of the tag whose value is to be set.

**Value**

Value written to the tag.

##### Example

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

### StartProgram (RT Professional)

#### Description

Starts the specified program with the specified parameters.

The system function can be used in C scripting only

#### Syntax

void StartProgram(Program_name, Program_parameters, Display_mode, Wait_for_program_end);

#### Parameters

**Program_name**

Path and name of the program to be started.

**Program_parameters**

Parameters to be used for start-up. Information on the possible parameters can be found in the description of the program to be started.

**Display_mode**

Defines the display mode in which the program is started:

0 (hmiShowNormal) = Display in window

1 (hmiShowMinimized) = Display in minimized window

2 (hmiShowMaximized) = Display in maximized window

3 (hmiShowMinimizedAndInactive) = Display in inactive and minimized window

**Wait_for_program_end**

The parameter is not evaluated by WinCC Runtime Professional.

#### Example

The following program code starts the calc.exe program in the minimized window.

{

BOOL Wait_for_program_end;

char* number;

//start the program calc.exe

StartProgram("C:\\Winnt\\system32\\calc.exe",number,hmiShowMinimized, Wait_for_program_end);

...

}

### StopRuntime (RT Professional)

#### Description

Exits the runtime software and thereby the project running on the HMI device.

#### Use in the function list

StopRuntime (Mode)

#### Use in user-defined functions

StopRuntime Mode

Can be used if the configured device supports user-defined functions. For additional information, refer to "Device dependency".

#### Parameters

**Mode**

Determines whether the operating system is shut down after exiting runtime.

0 (hmiStopRuntime) = Runtime: Operating system is not shut down

1 (hmiStopRuntimeAndOperatingSystem) = Runtime and operating system: The operating system is shut down (not possible with WinCE)

#### Example

The following program code shuts down Runtime and the operating system.

{

//Stop runtime and shutdown

StopRuntime (hmiStopRuntimeAndOperationSystem);

}

The saved return value can be processed in the following code.

---

**See also**

[System functions for Runtime Professional (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-functions-for-runtime-professional-rt-professional)
  
[Example of deactivating Runtime (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#example-of-deactivating-runtime-rt-professional-1)

### StoreScreen  (RT Professional)

#### Description

Saves the current screen. This screen can be opened with the ActivateStoredScreen system function.

Can only be used in C scripting.

#### Syntax

BOOL StoreScreen();

#### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

#### Example

The following program code writes the return value of the StoreScreen function to the screen_stored tag and calls the stored screen, provided that this was saved without errors.

{

BOOL screen_stored;

screen_stored = StoreScreen();

//user defined code

...

//error handling

if(screen_stored)

{

  // succeeded

ActivateStoredScreen();

  printf ( "Stored screen is now activated.\r\n" );

}

else

{

  // failed

  printf ( "Error - no screen stored." );

}

...

}

---

**See also**

[ActivateStoredScreen (RT Professional)](#activatestoredscreen-rt-professional)

### SystemTimeToDate (RT Professional)

#### Description

Converts a date-clock time specification in SYSTEMTIME format into the DATE data format.

Can only be used in C scripting.

#### Use in the function list

SystemTimeToDate (value, pointer to time)

#### Syntax

SystemTimeToDate(Value, PointerToTime);

#### Parameters

**Value**

Value in SYSTEMTIME data format

**Pointer to time**

Pointer to the result in the DATE format

#### Return value

**TRUE**

System function completed without errors.

**FALSE**

An error has occurred.

#### Example

BOOL BRet;

SYSTEMTIME st_1, st_2;

DATE       d_1, d_2;   // wtypes.h.  DATE type. Visual Studio documnetation.

GetSystemTime( &st_1 );

printf( "st_1.wYear = %d \r\n", st_1.wYear );

printf( "st_1.wMonth = %d \r\n", st_1.wMonth );

printf( "st_1.wDayOfWeek = %d \r\n", st_1.wDayOfWeek );

printf( "st_1.wDay = %d \r\n", st_1.wDay );printf( "st_1.wHour = %d \r\n", st_1.wHour );

printf( "st_1.wMinute = %d \r\n", st_1.wMinute );

printf( "st_1.wSecond = %d \r\n", st_1.wSecond );

printf( "st_1.wMilliseconds = %d \r\n", st_1.wMilliseconds );

BRet = SystemTimeToDate( st_1, &d_1 );

printf( "DATE d = %ld \r\n \r\n", d_1 );

printf( "DATE d = %lf \r\n \r\n", d_1 );

printf( "DATE d = %f \r\n \r\n", d_1 );

BRet = DateToSystemTime( d_1, &st_2 );

printf( "st_2.wYear = %d \r\n", st_2.wYear );

printf( "st_2.wMonth = %d \r\n", st_2.wMonth );

printf( "st_2.wDayOfWeek = %d \r\n", st_2.wDayOfWeek );

printf( "st_2.wDay = %d \r\n", st_2.wDay );

printf( "st_2.wHour = %d \r\n", st_2.wHour );

printf( "st_2.wMinute = %d \r\n", st_2.wMinute );

printf( "st_2.wSecond = %d \r\n", st_2.wSecond );

printf( "st_2.wMilliseconds = %d \r\n \r\n \r\n", st_2.wMilliseconds );

### TriggerOperatorEvent (RT Professional)

#### Description

The TriggerOperatorEvent system function triggers an operator input alarm.

#### Syntax

int TriggerOperatorEvent(dwFlags, dwMsgNum, lpszObjectName, dwMyTextID, doValueOld, doValueNew, pszComment);

#### Parameters

**dwFlags**

FLAG_COMMENT_PARAMETER (0x001): Specifies that the comment is input by means of the parameter.

FLAG_COMMENT_DIALOG (0x003): Specifies that the comment is input by means of a dialog.

FLAG_TEXTID_PARAMETER (0x100): Specifies that the comment is specified by means of a Text ID. To do so, configure a text list entry in the "C text list" tab of the "Text and graphics list" editor.

**dwMsgNum**

Number of the operator input alarm that is triggered.

**lpszObjectName**

Pointer to the name of the tag with the old value and the new value.

**dwMyTextID**

ID of the text to be used as comment.

If you are using "FLAG_COMMENT_PARAMETER" (0x001) or "FLAG_COMMENT_DIALOG" (0x003) for the parameter "dwFlags", enter the value 0 for the parameter "dwMyTextID".

If you are using "FLAG_TEXTID_PARAMETER" (0x100) for the parameter "dwFlags", enter the ID of the text list entry for the parameter "dwMyTextID". You can configure the text list entry in the "C text list" tab of the "Text and graphics list" editor.

**doValueOld**

Old value.

**doValueNew**

New value.

**pszComment**

Pointer to the text to be used as comment.

#### Return value

**0**

System function completed without errors.

**-101**

Editing of the operator input alarm could not be started.

**-201**

An error has occurred when calling "MSRTGetComment()".

**-301**

An error has occurred when calling "MSRTCreateMsgInstanceWithComment()".

### UA (Recipe) (RT Professional)

This section contains information on the following topics:

- [uaArchiveClose (RT Professional)](#uaarchiveclose-rt-professional)
- [uaArchiveDelete (RT Professional)](#uaarchivedelete-rt-professional)
- [uaArchiveExport (RT Professional)](#uaarchiveexport-rt-professional)
- [uaArchiveGetCount (RT Professional)](#uaarchivegetcount-rt-professional)
- [uaArchiveGetFieldLength (RT Professional)](#uaarchivegetfieldlength-rt-professional)
- [uaArchiveGetFieldName (RT Professional)](#uaarchivegetfieldname-rt-professional)
- [uaArchiveGetFields (RT Professional)](#uaarchivegetfields-rt-professional)
- [uaArchiveGetFieldType (RT Professional)](#uaarchivegetfieldtype-rt-professional)
- [uaArchiveGetFieldValueDate (RT Professional)](#uaarchivegetfieldvaluedate-rt-professional)
- [uaArchiveGetFieldValueDouble (RT Professional)](#uaarchivegetfieldvaluedouble-rt-professional)
- [uaArchiveGetFieldValueFloat (RT Professional)](#uaarchivegetfieldvaluefloat-rt-professional)
- [uaArchiveGetFieldValueLong (RT Professional)](#uaarchivegetfieldvaluelong-rt-professional)
- [uaArchiveGetFieldValueString (RT Professional)](#uaarchivegetfieldvaluestring-rt-professional)
- [uaArchiveGetFilter (RT Professional)](#uaarchivegetfilter-rt-professional)
- [uaArchiveGetID (RT Professional)](#uaarchivegetid-rt-professional)
- [uaArchiveGetName (RT Professional)](#uaarchivegetname-rt-professional)
- [uaArchiveGetSor (RT Professional)](#uaarchivegetsor-rt-professional)
- [uaArchiveImport (RT Professional)](#uaarchiveimport-rt-professional)
- [uaArchiveInsert (RT Professional)](#uaarchiveinsert-rt-professional)
- [uaArchiveMoveFirst (RT Professional)](#uaarchivemovefirst-rt-professional)
- [uaArchiveMoveLast (RT Professional)](#uaarchivemovelast-rt-professional)
- [uaArchiveMoveNext (RT Professional)](#uaarchivemovenext-rt-professional)
- [uaArchiveMovePrevious (RT Professional)](#uaarchivemoveprevious-rt-professional)
- [uaArchiveOpen (RT Professional)](#uaarchiveopen-rt-professional)
- [uaArchiveReadTagValues (RT Professional)](#uaarchivereadtagvalues-rt-professional)
- [uaArchiveReadTagValuesByName (RT Professional)](#uaarchivereadtagvaluesbyname-rt-professional)
- [uaArchiveRequery (RT Professional)](#uaarchiverequery-rt-professional)
- [uaArchiveSetFieldValueDate (RT Professional)](#uaarchivesetfieldvaluedate-rt-professional)
- [uaArchiveSetFieldValueDouble (RT Professional)](#uaarchivesetfieldvaluedouble-rt-professional)
- [uaArchiveSetFieldValueFloat (RT Professional)](#uaarchivesetfieldvaluefloat-rt-professional)
- [uaArchiveSetFieldValueLong (RT Professional)](#uaarchivesetfieldvaluelong-rt-professional)
- [uaArchiveSetFieldValueString (RT Professional)](#uaarchivesetfieldvaluestring-rt-professional)
- [uaArchiveSetFilter (RT Professional)](#uaarchivesetfilter-rt-professional)
- [uaArchiveSetSort (RT Professional)](#uaarchivesetsort-rt-professional)
- [uaArchiveUpdate (RT Professional)](#uaarchiveupdate-rt-professional)
- [uaArchiveWriteTagValues (RT Professional)](#uaarchivewritetagvalues-rt-professional)
- [uaArchiveWriteTagValuesByName (RT Professional)](#uaarchivewritetagvaluesbyname-rt-professional)
- [uaConnect (RT Professional)](#uaconnect-rt-professional)
- [uaDisconnect (RT Professional)](#uadisconnect-rt-professional)
- [uaGetArchive (RT Professional)](#uagetarchive-rt-professional)
- [uaGetField (RT Professional)](#uagetfield-rt-professional)
- [uaGetLastError (RT Professional)](#uagetlasterror-rt-professional)
- [uaGetLastHResult (RT Professional)](#uagetlasthresult-rt-professional)
- [uaGetNumArchives (RT Professional)](#uagetnumarchives-rt-professional)
- [uaGetNumFields (RT Professional)](#uagetnumfields-rt-professional)
- [uaQueryArchive (RT Professional)](#uaqueryarchive-rt-professional)
- [uaQueryArchiveByName (RT Professional)](#uaqueryarchivebyname-rt-professional)
- [UaQueryConfiguration (RT Professional)](#uaqueryconfiguration-rt-professional)
- [uaReleaseArchive (RT Professional)](#uareleasearchive-rt-professional)
- [uaReleaseConfiguration (RT Professional)](#uareleaseconfiguration-rt-professional)

#### uaArchiveClose (RT Professional)

##### Description

Terminates the connection to the current recipe.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveClose (`

`UAHARCHIVE hArchive )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

##### Return value

**TRUE**

Successful closing of the recipe

**FALSE**

Error

#### uaArchiveDelete (RT Professional)

##### Description

Deletes the data from a recipe. The configured recipe, however, is retained.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveDelete (`

`UAHARCHIVE hArchive,`

`LPCSTR pszWhere )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LPCSTR pszWhere`**

This string contains the SQL selection expression. It defines which data records are to be deleted. The expression is equivalent to the SQL instruction "DELETE FROM <archive> WHERE pszWhere".

`Warning!` If this string is empty, the entire recipe will be deleted.

##### Return value

**TRUE**

Successful deletion of the recipe

**FALSE**

Error

#### uaArchiveExport (RT Professional)

##### Description:

Exports the current recipe to a log in CSV format.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveExport (`

`UAHARCHIVE hArchive,`

`LPCSTR pszDestination,`

`LONG lType,`

`LONG lOptions )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using UaQueryArchive or UaQueryArchiveByName.

**`LPCSTR pszDestination`**

File name of the target archive. When calling the function on a client, the path specified refers to the server.

**`LONG lType`**

Data format of the target archive. Two formats are available:

- UA_FILETYPE_DEFAULT = 0: Default file format = CSV
- UA_FILETYPE_CSV = 1: CSV file format

**`LONG lOptions`**

Reserved for future expansions. Must be 0.

##### Return value

**TRUE**

Successful export of the recipe

**FALSE**

Error

#### uaArchiveGetCount (RT Professional)

##### Description

Reads the number of data records.

Can only be used in C scripting.

##### Syntax

`LONG uaArchiveGetCount(`

`UAHARCHIVE hArchive,`

`LONG * plCount )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName .

**`LONG plCount`**

Pointer to a tag in which the number of data records should be stored.

##### Return value

Number of data records.

0 = Log is empty or error has occurred. Must be queried by means of uaGetLastError() .

#### uaArchiveGetFieldLength (RT Professional)

##### Description

Reads the length of a field in the current data record.

Can only be used in C scripting.

##### Syntax

`LONG uaArchiveGetFieldLength(`

`UAHARCHIVE hArchive,`

`LONG lField )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LONG lField`**

Field number, with lField = 1 addressing the first field.

##### Return value

Length of the current field.

#### uaArchiveGetFieldName (RT Professional)

##### Description

Reads the name of a field in the current data record.

Can only be used in C scripting.

##### Syntax

`VOID uaArchiveGetFieldName (`

`UAHARCHIVE hArchive,`

`LONG lField,`

`LPCSTR pszName,`

`LONG cMaxLen )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LONG lField`**

Field number, with lField = 1 addressing the first field.

**`LPCSTR pszName`**

Field Name

**`LONG cMaxLen`**

Maximum length

#### uaArchiveGetFields (RT Professional)

##### Description

Reads the number of configured data fields, which also includes the "ID", "Last User", and "Last Access" fields. In the Runtime calls, the indexes of the configured fields are indicated 1 to N. The field ID has the index 0. The fields "Last User" and "Last Access" are appended to the end of the configured fields.

Can only be used in C scripting.

##### Syntax

`LONG uaArchiveGetFields (`

`UAHARCHIVE hArchive )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

##### Return value

Number of configured fields.

#### uaArchiveGetFieldType  (RT Professional)

##### Description

Reads the type of a field in the current data record.

Can only be used in C scripting.

##### Syntax

`LONG uaArchiveGetFieldType (`

`UAHARCHIVE hArchive,`

`LONG lField )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LONG lField`**

Field number, with lField = 1 addressing the first field.

##### Return value

Type of the current field.

The symbolic definitions of the field types are:

UA_FIELDTYPE_INTEGER

UA_FIELDTYPE_DOUBLE

UA_FIELDTYPE_STRING

UA_FIELDTYPE_DATETIME

#### uaArchiveGetFieldValueDate (RT Professional)

##### Description

Reads the date and time of a field in the current data record.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveGetFieldValueDate (`

`UAHARCHIVE hArchive,`

`LONG lField,`

`LPSYSTEMTIME pstDateTime )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName .

**`LONG lField`**

Field number, with lField = 1 addressing the first field.

**`LPSYSTEMTIME pstDateTime`**

Pointer to a tag of the type SYSTEMTIME

##### Return value

**TRUE**

Successful reading of date and time

**FALSE**

Error

#### uaArchiveGetFieldValueDouble (RT Professional)

##### Description

Reads the Double value of a field in the current data record.

The system function can be used in C scripting only.

`BOOL uaArchiveGetFieldValueDouble (`

`UAHARCHIVE hArchive,`

`LONG lField,`

`double* pdValue )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LONG lField`**

Field number, with lField = 1 addressing the first field.

**`double* pdValue`**

Pointer to tag for the current field content.

##### Return value

**TRUE**

Successful reading of field value

**FALSE**

Error

#### uaArchiveGetFieldValueFloat (RT Professional)

##### Description

Reads Float value of a field in the current data record.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveGetFieldValueFloat (`

`UAHARCHIVE hArchive,`

`LONG lField,`

`FLOAT* pfValue )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LONG lField`**

Field number, with lField = 1 addressing the first field.

**`FLOAT* pfValue`**

Pointer to Float tag for the current field content.

##### Return value

**TRUE**

Successful reading of field value

**FALSE**

Error

#### uaArchiveGetFieldValueLong (RT Professional)

##### Description

Reads the Long Integer value of a field in the current data record.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveGetFieldValueLong (`

`UAHARCHIVE hArchive,`

`LONG lField,`

`LONG* pdValue )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LONG lField`**

Field number, with lField = 1 addressing the first field.

**`LONG* pdValue`**

Pointer to Long tag for the current field content.

##### Return value

**TRUE**

Successful reading of field value

**FALSE**

Error

#### uaArchiveGetFieldValueString (RT Professional)

##### Description

Reads the string of a field in the current data record.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveGetFieldValueString (`

`UAHARCHIVE hArchive,`

`LONG lField,`

`LPSTR pszString,`

`LONG cMaxLen )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LONG lField`**

Field number, with lField = 1 addressing the first field.

**`LPCSTR pszString`**

Field value as string.

**`LONG cMaxLen`**

Maximum length of the string.

##### Return value

**TRUE**

Successful reading of field value

**FALSE**

Error

#### uaArchiveGetFilter (RT Professional)

##### Description

Reads the filter of the current data record. Additional information can be found in the appendix under "SQL Statements".

Can only be used in C scripting.

##### Syntax

`VOID uaArchiveGetFilter (`

`UAHARCHIVE hArchive,`

`LPSTR pszFilter,`

`LONG cMaxLen )`

The system function can be used in C scripting only.

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LPSTR pszFilter`**

Read filter.

**`LONG cMaxLen`**

Maximum length

#### uaArchiveGetID (RT Professional)

##### Description

uaArchiveGetID reads the ID of the recipe.

The recipe ID serves internal purposes and may differ from the number given in the recipe.

Can only be used in C scripting.

##### Syntax

`LONG uaArchiveGetID (`

`UAHARCHIVE hArchive )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

##### Return value

ID of the recipe.

#### uaArchiveGetName (RT Professional)

##### Description

Reads the name of the recipe.

Can only be used in C scripting.

##### Syntax

`VOID uaArchiveGetName (`

`UAHARCHIVE hArchive,`

`LPSTR pszName,`

`LONG cMaxLen )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LPSTR pszName`**

Pointer to buffer for recipe name.

**`LONG cMaxLen`**

Maximum length

##### Example

char Filling [40];

uaArchiveGetName( hArchive, bottling, 39 );

#### uaArchiveGetSor (RT Professional)

##### Description

uaArchiveGetSort reads the sorting of the recipe.

Can only be used in C scripting.

##### Syntax

`VOID uaArchiveGetSort (`

`UAHARCHIVE hArchive,`

`LPSTR pszSort,`

`LONG cMaxLen )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LPCSTR pszSort`**

Sorting

**`LONG cMaxLen`**

Maximum length

#### uaArchiveImport (RT Professional)

##### Description

uaArchivImport imports a recipe with CSV data format. The structure of the destination recipe must be identical to that of the imported recipe.

##### Syntax

`BOOL uaArchiveImport (`

`UAHARCHIVE hArchive,`

`LPCSTR pszSource,`

`LONG lType,`

`LONG lOptions )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LPCSTR pszSource`**

File name of the source archive.

**`LONG lType`**

Data format of the source archive. Two formats are available:

UA_FILETYPE_DEFAULT = 0: Default file format = CSV

UA_FILETYPE_CSV = 1: CSV file format

**`LONG lOptions`**

Reserved for future expansions. Must be 0.

##### Return value

**TRUE**

Successful import of the recipe.

**FALSE**

Error

#### uaArchiveInsert (RT Professional)

##### Description

Inserts the local data record buffer into the current database. Before you call uaArchiveInsert, use the "uaArchiveSetFieldValue..." system functions to enter the data in the fields of the local data buffer so that the new data record contains useful data.  
Use system function "uaArchiveSetFieldValueLong" to enter the internal column "ID" in the current data record. Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveInsert (`

`UAHARCHIVE hArchive )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

##### Return value

**TRUE**

Successful insertion of the data record.

#### uaArchiveMoveFirst (RT Professional)

##### Description

Goes to the first data record.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveMoveFirst (`

`UAHARCHIVE hArchive )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

##### Return value

**TRUE**

Successful jumping in the recipe

**FALSE**

Error

#### uaArchiveMoveLast  (RT Professional)

##### Description

Goes to the last data record.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveMoveLast (`

`UAHARCHIVE hArchive )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName .

##### Return value

**TRUE**

Successful jumping in the recipe

**FALSE**

Error

#### uaArchiveMoveNext (RT Professional)

##### Description

Goes to the next data record.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveMoveNext (`

`UAHARCHIVE hArchive )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

##### Return value

**TRUE**

Successful jumping in the recipe

**FALSE**

Error

#### uaArchiveMovePrevious (RT Professional)

##### Description

Goes to the previous data record.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveMovePrevious (`

`UAHARCHIVE hArchive )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

##### Return value

**TRUE**

Successful jumping in the recipe

**FALSE**

Error

#### uaArchiveOpen (RT Professional)

##### Description

uaArchiveOpen must be called before all RT functions (e.g. uaArchiveMoveFirst, uaArchiveMoveLast, uaArchiveMoveNext, uaArchiveMovePrevious, uaArchiveDelete, uaArchiveUpdate, uaArchiveInsert, uaArchiveGetID, uaArchiveGetFields, uaArchiveGetFieldType, uaArchiveGetFieldValueDate, uaArchiveGetFieldValueDouble, uaArchiveGetFieldValueFloat, uaArchiveGetFieldValueLong, uaArchiveGetFieldValueString, uaArchiveSetFieldValueDate, uaArchiveSetFieldValueDouble, uaArchiveSetFieldValueFloat, uaArchiveSetFieldValueLong and uaArchiveSetFieldValueString).

> **Note**
>
> **Sort and filter recipes**
>
> You may apply the "uaArchiveSetSort" and "uaArchiveSetFilter" system functions to a recipe without having to open this recipe by means of "uaArchiveOpen".

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveOpen (`

`UAHARCHIVE hArchive )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

##### Return value

**TRUE**

Successful opening of the recipe

**FALSE**

Error

#### uaArchiveReadTagValues (RT Professional)

##### Description

Reads the current value from the field tag.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveReadTagValues (`

`UAHARCHIVE hArchive,`

`LONG* pnFields,`

`LONG cFields,`

`LONG lOptions )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LONG* pnFields`**

Reserved for future applications (NULL)

**`LONG cFields`**

Number of field indices transferred (size of array pnFields).

Reserved for future applications (0)

**`LONG lOptions`**

Reserved for future applications (0)

In the case of all other values of lOptions, the data is inserted at the position of the pointer.

##### Return value

**TRUE**

Successful reading in the recipe

**FALSE**

Error

#### uaArchiveReadTagValuesByName (RT Professional)

##### Description

Reads the tag values in the current data.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveReadTagValuesByName (`

`UAHARCHIVE hArchive,`

`LPCSTR pszFields,`

`LONG lOptions )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LPCSTR pszFields`**

Reserved for future applications (NULL)

**`LONG lOptions`**

Reserved for future applications (0)

##### Return value

**TRUE**

Successful reading in the recipe

**FALSE**

Error

#### uaArchiveRequery (RT Professional)

##### Description

On completion of the call of uaArchiveSetFilter and uaArchiveSetSort, reload the recipe by means of uaArchiveRequery.

> **Note**
>
> **Sort and filter recipes**
>
> You may apply the "uaArchiveSetSort" and "uaArchiveSetFilter" system functions to a recipe without having to open this recipe by means of "uaArchiveOpen". In this case you do no have to call the system function "uaArchiveRequery".

Call uaArchiveRequery in the following situations as well:

- If you have made inputs in the recipe view.
- If you have made inputs in the "Recipes" editor that are to be transferred to the table cell.

##### Syntax

`BOOL uaArchiveRequery(`

`UAHARCHIVE hArchive )`

Can only be used in C scripting.

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

##### Return value

**TRUE**

Successful requery

**FALSE**

Error

#### uaArchiveSetFieldValueDate (RT Professional)

##### Description

Writes the date and time into a field of the current data record.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveSetFieldValueDate (`

`UAHARCHIVE hArchive,`

`LONG lField,`

`LPSYSTEMTIME pstDateTime )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LONG lField`**

Field number, with lField = 1 addressing the first configured field. The ID field is addressed with lField = 0.

**`LPSYSTEMTIME pstDateTime`**

Date and Time

##### Return value

**TRUE**

Successful writing of date and time

**FALSE**

Error

#### uaArchiveSetFieldValueDouble (RT Professional)

##### Description

Writes a Double value into a field of the current data record.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveSetFieldValueDouble (`

`UAHARCHIVE hArchive,`

`LONG lField,`

`double dValue )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LONG lField`**

The field number, where lField = 1 is addressing the first configured field. The ID field is addressed with lField = 0.

**`double dValue`**

Field value

##### Return value

**TRUE**

Successful writing of field value

**FALSE**

Error

#### uaArchiveSetFieldValueFloat (RT Professional)

##### Description:

Writes a Float value into a field of the current data record.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveSetFieldValueFloat (`

`UAHARCHIVE hArchive,`

`LONG lField,`

`float fValue )`

##### Parameters:

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LONG lField`**

Field number, with lField = 1 addressing the first configured field. The ID field is addressed with lField = 0.

**`float fValue`**

Field value

##### Return value:

**TRUE**

Successful writing of field value

**FALSE**

Error

#### uaArchiveSetFieldValueLong (RT Professional)

##### Description

Writes a Long Integer value into a field of the current data record.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveSetFieldValueLong (`

`UAHARCHIVE hArchive,`

`LONG lField,`

`LONG dValue )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LONG lField`**

The field number, where lField = 1 is addressing the first configured field. The ID field is addressed with lField = 0.

**`LONG dValue`**

Field value

##### Return value

**TRUE**

Successful writing of field value

**FALSE**

Error

#### uaArchiveSetFieldValueString  (RT Professional)

##### Description

Writes a String into a field of the current data record.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveSetFieldValueString (`

`UAHARCHIVE hArchive,`

`LONG lField,`

`LPCSTR pszString )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LONG lField`**

The field number, where lField = 1 is addressing the first configured field. The ID field is addressed with lField = 0 .

**`LPCSTR pszString`**

Field value

##### Return value

**TRUE**

Successful writing of field value

**FALSE**

Error

#### uaArchiveSetFilter (RT Professional)

##### Description

Sets the filter. You can call the system function without having opened the recipe with "uaArchiveOpen".

> **Note**
>
> If you have opened the recipe with "uaArchiveOpen", reload the recipe after filtering by means of "uaArchiveRequery".

Can only be used in C scripting.

##### Syntax

`VOID uaArchiveSetFilter (`

`UAHARCHIVE hArchive,`

`LPSTR pszFilter )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LPSTR pszFilter`**

Filter to be set.

#### uaArchiveSetSort (RT Professional)

##### Description

Sets the sorting of the recipe. You can call the system function without having opened the recipe with "uaArchiveOpen".

> **Note**
>
> If you have opened the recipe with "uaArchiveOpen", reload the recipe after sorting by means of "uaArchiveRequery".

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveSetSort (`

`UAHARCHIVE hArchive,`

`LPSTR pszSort )`

The system function can be used in C scripting only.

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LPCSTR pszSort`**

Sorting

##### Return value

**TRUE**

Successful setting of the sorting

**FALSE**

Error

#### uaArchiveUpdate (RT Professional)

##### Description

Updates the open recipe. All data changes of a recipe are transferred to the database. The configuration of the recipe remains unchanged.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveUpdate (`

`UAHARCHIVE hArchive )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

##### Return value

**TRUE**

Successful update of the recipe

**FALSE**

"Update_failed" error = 106

This error occurs when there is a consistency violation. Example: The "Field requires a value" flag is set in a field, but no value has been entered there.

#### uaArchiveWriteTagValues (RT Professional)

##### Description

Writes the values of the current data record into the tags.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveWriteTagValues (`

`UAHARCHIVE hArchive,`

`LONG* pnFields,`

`LONG cFields,`

`LONG lOptions )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LONG* pnFields`**

Reserved for future applications (NULL)

**`LONG cFields`**

Reserved for future applications (0)

**`LONG lOptions`**

Reserved for future applications (0)

##### Return value

**TRUE**

Successful reading in the recipe

**FALSE**

Error

#### uaArchiveWriteTagValuesByName (RT Professional)

##### Description

Writes the values of the current data record into the tags. The access is based on the names of the recipe and field.

Can only be used in C scripting.

##### Syntax

`BOOL uaArchiveWriteTagValuesByName (`

`UAHARCHIVE hArchive,`

`LPCSTR pszFields,`

`LONG lOptions )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

**`LPCSTR pszFields`**

Reserved for future applications (NULL)

**`LONG lOptions`**

Reserved for future applications (0)

##### Return value

**TRUE**

Successful reading in the recipe

**FALSE**

Error

#### uaConnect (RT Professional)

##### Description

Establishes connection to recipes (Runtime).

Can only be used in C scripting.

##### Syntax

`BOOL uaConnect (`

`UAHCONNECT* phConnect )`

##### Parameters

**`UAHCONNECT* phConnect`**

Pointer to handle for newly connected recipe.

##### Return value

**TRUE**

Successful connection of a recipe

**FALSE**

Error

#### uaDisconnect (RT Professional)

##### Description

If a connection to recipes (Runtime) exists, it will be disconnected.

Can only be used in C scripting.

##### Syntax

`BOOL uaDisconnect (`

`UAHCONNECT hConnect )`

##### Parameters

**`UAHCONNECT hConnect`**

Handle for the connected recipe (Runtime). The handle is generated using uaConnect.

##### Return value

**TRUE**

Successful disconnection of a recipe

**FALSE**

Error

#### uaGetArchive (RT Professional)

##### Description

Reads the recipe configuration.

Can only be used in C scripting.

##### Syntax

`BOOL uaGetArchive (`

`UAHCONFIG hConfig,`

`long lArchive,`

`UACONFIGARCHIVE* pArchive )`

##### Parameters

**`UAHCONFIG hConfig,`**

Configuration handle of the recipe. This handle is generated using uaQueryConfiguration.

**`long lArchive,`**

Archive index (0 to (uaGetNumArchives()-1))

**`UACONFIGARCHIVE* pArchive`**

Pointer to buffer for receiving the recipe configuration

##### Return value

**TRUE**

Successful access to the recipe

**FALSE**

Error

#### uaGetField (RT Professional)

##### Description:

Reads the field configuration.

Can only be used in C scripting.

##### Syntax

`BOOL uaGetField (`

`UAHCONFIG hConfig,`

`long lArchive,`

`long lField,`

`UACONFIGFIELD* pField )`

##### Parameters:

**`UAHCONFIG hConfig,`**

Configuration handle of the recipe. This handle is generated using uaQueryConfiguration.

**`long lArchive,`**

Archive index (0 to (uaGetNumArchives()-1))

**`long lField,`**

The field number; if lField = 0 the first field is addressed.

**`UACONFIGFIELD* pArchive`**

Pointer to buffer for receiving the field configuration.

##### Return value

**TRUE**

Successful access to the recipe

**FALSE**

Error

#### uaGetLastError  (RT Professional)

##### Description

The system functions of the WinCC script language return a BOOL value; TRUE corresponds to error-free processing. If FALSE is returned, you can use "uaGetLastError()" and "uaGetLastHResult()" to read the error of the last system function.

Can only be used in C scripting.

If you do not call uaGetLastError() until several system functions have been processed, uaGetLastError() will return the most recent error. You should call a "uaGetLastError()" and "uaGetLastHResult()" system function whenever FALSE is returned to identify the system function that triggered the error.

Example:

`if ( uaArchiveGetFieldValueLong ( hArchive, Index, &IntValue ) == TRUE )`

`printf( "Field Value = %u\n", IntValue );`

`else`

`printf("Error calling uaArchiveGetFieldValueLong: %d / %08lx\n", uaGetLastError(), uaGetLastHResult());`

You should always query system functions that do not return a value (VOID) by calling uaGetLastError() .

Example:

`uaArchiveGetFilter(hArchive, pszFilter, cMaxLen);`

`INT nUAError = uaGetLastError (  );`

`if ( UA_ERROR_SUCCESS != nUAError)`

`{`

`printf( "Filter = [%s]\n", pszFilter );`

`}`

`else`

`{`

`printf("Error calling uaArchiveGetFilter: %d, hr=0x%08lX\n", nUAError, uaGetLastHResult());`

`}`

`INT uaGetLastError()`

##### Return value

Error status of the last system function executed. uaGetLastError() can return the following errors:

UA_ERROR_SUCCESS

UA_ERROR_GENERIC

UA_ERROR_CONNECT_FAILED

UA_ERROR_OPEN_FAILED

UA_ERROR_CLOSE_FAILED

UA_ERROR_REQUERY_FAILED

UA_ERROR_MOVE_FAILED

UA_ERROR_INSERT_FAILED

UA_ERROR_UPDATE_FAILED

UA_ERROR_DELETE_FAILED

UA_ERROR_IMPORT_FAILED

UA_ERROR_EXPORT_FAILED

UA_ERROR_READ_FAILED

UA_ERROR_WRITE_FAILED

UA_ERROR_GET_FAILED

UA_ERROR_SET_FAILED

UA_ERROR_INVALID_NAME

UA_ERROR_INVALID_TYPE

UA_ERROR_INVALID_NUMRECS

UA_ERROR_INVALID_COMMTYPE

UA_ERROR_INVALID_LENGTH

UA_ERROR_INVALID_PRECISION

UA_ERROR_NULL_POINTER

UA_ERROR_INVALID_POINTER

UA_ERROR_INVALID_HANDLE

UA_ERROR_INVALID_INDEX

UA_ERROR_SERVER_UNKNOWN

These error constants as well as the predefines of the user archive routines are located in CCUACAPI.H.

#### uaGetLastHResult  (RT Professional)

##### Description

Reads the last occurred COM error. This system function is used primarily to analyze incompatibility in the COM implementation or to identify registry errors and communication errors.  
This system function must always be called in addition to UAGetLastError if one of the user archive system functions (e.g uaConnect) returns the value "FALSE" to signal an error.

Can only be used in C scripting.

##### Syntax

`LONG uaGetLastHResult()`

##### Return value

Last occurred COM error

#### uaGetNumArchives (RT Professional)

##### Description

Reads the number of recipes currently configured.

Can only be used in C scripting.

##### Syntax

`LONG uaGetNumArchives (`

`UAHCONFIG hConfig )`

##### Parameters

**`UAHCONFIG hConfig`**

Configuration handle of the recipe. This handle is generated using uaQueryConfiguration.

##### Return value

Number of recipes currently configured. In case of an error, -1 will be returned.

#### uaGetNumFields (RT Professional)

##### Description

Supplies the number of the configured fields. The "ID", "Last User" and "Last Access" fields are not included. Indexes are specified from 0 to uaGetNumFields() -1 in the configuration calls.

Can only be used in C scripting.

##### Syntax

`LONG uaGetNumFields (`

`UAHCONFIG hConfig,`

`long lArchive )`

##### Parameters

**`UAHCONFIG hConfig,`**

Configuration handle of the recipe. This handle is generated using uaQueryConfiguration.

**`long lArchive,`**

Archive index (0 to (uaGetNumArchives()-1))

##### Return value

Number of configured fields. In case of an error, -1 will be returned.

#### uaQueryArchive  (RT Professional)

##### Description

Establishes a connection to the recipe for Runtime operation. UaQueryArchive creates the handle UAHARCHIVE.

Can only be used in C scripting.

##### Syntax

`BOOL uaQueryArchive (`

`UAHCONNECT hConnect,`

`LONG lArchive,`

`UAHARCHIVE* phArchive )`

##### Parameters

**`UAHCONNECT hConnect`**

Handle of the connected recipe (Runtime). The handle is generated using uaConnect.

**`LONG lArchive`**

ID of the archive to be connected

**`UAHARCHIVE* phArchive`**

Pointer to handle of the recipe

##### Return value

**TRUE**

Successful generation of the handle to the recipe.

**FALSE**

Error

##### Comment

If you use User Archives functions in a client project that works with redundant server pairs, the user archives connection cannot be switched automatically to the new master when switching masters. In this case, all user archives calls return the LastError UA_ERROR_SERVER_UNKNOWN = 1004, which means that the user programs must execute a new uaQueryArchive() or uaQueryArchiveByName() and uaArchiveOpen().

#### uaQueryArchiveByName  (RT Professional)

##### Description

Establishes a connection to the recipe for Runtime operation using the recipe name. UaQueryArchiveByName creates the UAHARCHIVE handle for the recipe.

Can only be used in C scripting.

##### Syntax

`BOOL uaQueryArchiveByName (`

`UAHCONNECT hConnect,`

`LPCSTR pszName,`

`UAHARCHIVE* phArchive )`

##### Parameters

**`UAHCONNECT hConnect`**

Handle of the connected recipe (Runtime). The handle is generated using uaConnect.

**`LPCSTR pszName`**

Name of the recipe. With a client project, you can add a server prefix with ‘::‘ to the recipe name as a separator, if a server other than the default server is used.

**`UAHARCHIVE* phArchive`**

Pointer to handle of the recipe

##### Return value

**TRUE**

Successful generation of the handle to the recipe.

**FALSE**

Error

##### Comment

If you use User Archives functions in a client project that works with redundant server pairs, the user archives connection cannot be switched automatically to the new master when switching masters. In this case, all user archives calls return the LastError UA_ERROR_SERVER_UNKNOWN = 1004, which means that the user programs must execute a new uaQueryArchive() or uaQueryArchiveByName() and uaArchiveOpen().

#### UaQueryConfiguration (RT Professional)

##### Description

Establishes a connection to the recipe for the configuration.

Can only be used in C scripting.

##### Syntax

`BOOL uaQueryConfiguration (`

`UAHCONFIG* phConfig )`

##### Parameters

**`UAHCONFIG* phConfig,`**

Pointer to handle of the recipe.

##### Return value

**TRUE**

Successful access to recipe

**FALSE**

Error

#### uaReleaseArchive (RT Professional)

##### Description

Releases the connection to the current recipe.

Can only be used in C scripting.

##### Syntax

`BOOL uaReleaseArchive (`

`UAHARCHIVE hArchive )`

##### Parameters

**`UAHARCHIVE hArchive`**

Handle of the recipe. This handle is generated using uaQueryArchive or uaQueryArchiveByName.

##### Return value

**TRUE**

Successful release of connection to the recipe.

**FALSE**

Error

##### Comment

The "hArchive" handle must be set to "NULL" on successful release to make absolutely sure that the "UA_ERROR_INVALID_HANDLE" error is triggered on further use of the invalid handle and without the respective function dwelling at the COM interface for a longer period of time.

#### uaReleaseConfiguration  (RT Professional)

##### Description

Releases connection to recipes (configuration).

Can only be used in C scripting.

##### Syntax

`BOOL uaReleaseConfiguration (`

`UAHCONFIG hConfig,`

`BOOL bSave )`

##### Parameters

**`UAHCONFIG hConfig`**

Configuration handle of the recipe. This handle is generated using uaQueryConfiguration.

**`BOOL bSave`**

Saves changes made to the configuration before releasing the connection to recipes for the configuration.

TRUE = Save Changes, FALSE = Discard Changes

`Warning: Save changes (bSave = TRUE) may only be used when Runtime is not active!` You can check whether Runtime is active by requesting uaIsActive().

##### Return value

**TRUE**

Successful connection release

**FALSE**

Error

## C-bib (RT Professional)

This section contains information on the following topics:

- [ctype functions (RT Professional)](#ctype-functions-rt-professional)
- [Function group c_bib (RT Professional)](#function-group-c_bib-rt-professional)
- [math functions (RT Professional)](#math-functions-rt-professional)
- [memory functions (RT Professional)](#memory-functions-rt-professional)
- [multibyte functions (RT Professional)](#multibyte-functions-rt-professional)
- [stdio functions (RT Professional)](#stdio-functions-rt-professional)
- [stdlib functions (RT Professional)](#stdlib-functions-rt-professional)
- [string functions (RT Professional)](#string-functions-rt-professional)
- [time functions (RT Professional)](#time-functions-rt-professional)

### ctype functions (RT Professional)

#### Function overview

The following ctype functions are available:

- long int isalnum (long int x);
- long int isalpha (long int x);
- long int isdigit (long int x);
- long int isgraph (long int x);
- long int islower (long int x);
- long int isprint (long int x);
- long int ispunct (long int x);
- long int isspace (long int x);
- long int isupper (long int x);
- long int isxdigit (long int x);
- long int tolower (long int x);
- long int toupper (long int x);

For a description of the ctype functions see the specialist literature on programming language C.

The functions can be used in C scripts only.

### Function group c_bib (RT Professional)

#### Introduction

The c_bib function group contains C functions from the C library and is divided into:

- ctype
- math
- memory
- stdio
- stdlib
- string
- time

stdio itself is again divided into:

- char_io
- directio
- error
- file
- file_pos
- output

For a description of these functions see the relevant specialist literature.

#### Specific features of WinCC functions

The localtime function behaves as follows when the date is issued:

- The counting of the months begins with 0.
- The years are counted as of 1990, starting with 0.

Only 360 characters of the functions of the C library printf(), sprintf(), fprintf() can be edited in WinCC.

### math functions  (RT Professional)

#### Function overview

The following math functions are available:

- double acos (double x);
- double asin (double x);
- double atan (double x);
- double atan2 (double x, double y);
- double ceil (double x);
- double cos (double x);
- double cosh (double x);
- double exp (double x);
- double fabs (double x);
- double floor (double x);
- double fmod (double x, double y);
- double frexp (double x, long int* y);
- double ldexp (double x, long int y);
- double log (double x);
- double log10 (double x);
- double modf (double x, double* y);
- double pow (double x, double y);
- double sin (double x);
- double sinh (double x);
- double sqrt (double x);
- double tan (double x);
- double tanh (double x);

For a description of the math functions see the specialist literature on programming language C.

The functions can be used in C scripts only.

### memory functions (RT Professional)

#### Function overview

The following memory functions are available:

- long int memcmp (const void* cs, const void* ct, size_t n);
- void* memchr (const void* cs, long int c, size_t n);
- void* memcpy (void* s, const void* ct, size_t n);
- void* memmove (void* s, const void* ct, size_t n);
- void* memset (void* s, long int c, size_t n);

For a description of the memory functions see the specialist literature on programming language C.

The functions can be used in C scripts only.

### multibyte functions (RT Professional)

#### Function overview

The following multibyte functions are available:

- int _ismbcalnum( unsigned int c )
- int _ismbcalpha( unsigned int c )
- int _ismbcdigit( unsigned int c )
- int _ismbcgraph( unsigned int c )
- int _ismbclower( unsigned int c )
- int _ismbcprint( unsigned int c )
- int _ismbcpunct( unsigned int c )
- int _ismbcspace( unsigned int c )
- int _ismbcupper( unsigned int c )
- int _mbscmp(const unsigned char *string1, const unsigned char *string2 )
- int _mbsncmp( const unsigned char *string1, const unsigned char *string2, size_t count )
- int _mbsrchr( const unsigned char *string, unsigned int c )
- size_t _mbscspn( const unsigned char *string, const unsigned char *strCharSet )
- size_t _mbsspn( const unsigned char *string, const unsigned char *strCharSet )
- size_t _mbstrlen( const char *string )
- size_t _mbslen( const unsigned char *string )
- unsigned char *_mbscat( unsigned char *strDestination, const unsigned char *strSource)
- unsigned char *_mbschr( const unsigned char *string, unsigned int c )
- unsigned char *_mbscpy( unsigned char *strDestination, const unsigned char *strSource )
- unsigned char *_mbsdec( const unsigned char *start, const unsigned char *current )
- unsigned char *_mbsinc( const unsigned char *current ) size_t _mbclen( const unsigned char *c );
- unsigned char *_mbsncat( unsigned char *strDest, const unsigned char *strSource, size_t count)
- unsigned char *_mbsncpy( unsigned char *strDest, const unsigned char *strSource, size_t count)
- unsigned char *_mbspbrk( const unsigned char*string, const unsigned char *strCharSet )
- unsigned char *_mbsstr( const unsigned char *string, const unsigned char *strCharSet )
- unsigned char *_mbstok( unsigned char*strToken, const unsigned char *strDelimit )

A description of the multibyte functions can be found in the specialist literature on programming language C.

The functions can be used in C scripts only.

### stdio functions (RT Professional)

#### Function overview

The following stdio functions are available:

- char* fgets (char* s, long int n, FILE* stream);
- char* tmpnam (char* s);
- FILE* fopen (const char* name, const char* mode);
- FILE* freopen (const char* filename, const char* mode, FILE* stream);
- FILE* tmpfile ();
- fprintf();
- long int fclose (FILE* stream);
- long int feof (FILE* stream);
- long int ferror (FILE* stream);
- long int fflush (FILE* stream);
- long int fgetc (FILE* stream);
- long int fgetpos (FILE* stream, fpos_t* ptr);
- long int fputc (long int c, FILE* stream);
- long int fputs (const char* s, FILE* stream);
- long int fseek (FILE* stream, long int offset, long int origin);
- long int fsetpos (FILE* stream, const fpos_t* ptr);
- long int ftell (FILE* stream);
- long int getc (FILE* stream);
- long int putc (long int c, FILE* stream);
- long int remove (const char* filename);
- long int rename (const char* oldname, const char* newname);
- long int setvbuf (FILE* stream, char* buf, long int mode, size_t size);
- long int ungetc (long int c, FILE* stream);
- long int vfprintf (FILE* stream, const char* format, va_list arg);
- long int vsprintf (char* s, const char* format, va_list arg);
- printf();
- size_t fread (void* ptr, size_t size, size_t nobj, FILE* stream);
- size_t fwrite (void* ptr, size_t size, size_t nobj, FILE* stream);
- void clearerr (FILE* stream);
- void rewind (FILE* stream);
- void setbuf (FILE* stream, char* buf);

For a description of the studio functions see the specialist literature on programming language C.

The functions can be used in C scripts only.

### stdlib functions (RT Professional)

#### Function overview

The following stdlib functions are available:

- char* getenv (const char* name);
- div_t div (long int num, long int denom);
- double atof (const char* s);
- double strtod (const char* s, char** endp);
- ldiv_t ldiv (long int num, long int denom);
- long int abs (long int n);
- long int atoi (const char* s);
- long int atol (const char* s);
- long int labs (long int n);
- long int rand ();
- long int srand (unsigned long int seed);
- long int strtol (const char* s, char** endp, long int base);
- long int system (const char* s);
- unsigned long int strtoul (const char* s, char** endp, long int base);
- void abort ();
- void* bsearch (const void* key, const void* base, size_t n, size_t size, long int(* cmp) (const
- void* calloc (size_t nobj, size_t size);
- void exit (long int status);
- void free (void* p);
- void* keyval, const void* datum));
- void* malloc (size_t size);
- void qsort (void* base, size_t n, size_t size, long int* cmp, const void* , const void* );
- void* realloc (void* p, size_t size);

For a description of the stdlib functions see the specialist literature on programming language C.

The functions can be used in C scripts only.

### string functions (RT Professional)

#### Function overview

The following string functions are available:

- char* strcat (char* s, const char* ct);
- char* strchr (const char* cs, long int c);
- char* strcpy (char* s, const char* ct);
- char* strerror (size_t n);
- char* strncat (char* s, const char* ct, size_t n);
- char* strncpy (char* s, const char* ct, size_t n);
- char* strpbrk (const char* cs, const char* ct);
- char* strrchr (const char* cs, long int c);
- char* strstr (const char* cs, const char* ct);
- char* strtok (char* s, const char* ct);
- long int strcmp (const char* cs, const char* ct);
- long int strncmp (const char* cs, const char* ct, size_t n);
- size_t strcspn (const char* cs, const char* ct);
- size_t strlen (const char* cs);
- size_t strspn (const char* cs, const char* ct);

For a description of the string functions see the specialist literature on programming language C.

The functions can be used in C scripts only.

### time functions  (RT Professional)

#### Function overview

The following time functions are available:

- char* asctime (const struct tm* tp);
- char* ctime (const time_t* tp);
- clock_t clock ();
- double difftime (time_t time2, time_t time1);
- size_t strftime (char* s, size_t smax, const char* fmt, const struct tm* tp);
- struct tm* gmtime (const time_t* tp);
- struct tm* localtime (const time_t* tp);
- time_t mktime (struct tm* tp);
- time_t time (time_t* tp);

For a description of the time functions see the specialist literature on programming language C.

The functions can be used in C scripts only.

## Structure definition (RT Professional)

This section contains information on the following topics:

- [Structure definition CCAPErrorExecute (RT Professional)](#structure-definition-ccaperrorexecute-rt-professional)
- [Structure definition CCAPTime (RT Professional)](#structure-definition-ccaptime-rt-professional)
- [Structure definition CMN_ERROR (RT Professional)](#structure-definition-cmn_error-rt-professional)
- [Structure definition DM_TYPEREF (RT Professional)](#structure-definition-dm_typeref-rt-professional)
- [Structure definition DM_VAR_UPDATE_STRUCT (RT Professional)](#structure-definition-dm_var_update_struct-rt-professional)
- [Structure definition DM_VAR_UPDATE_STRUCTEX (RT Professional)](#structure-definition-dm_var_update_structex-rt-professional)
- [Structure definition DM_VARKEY (RT Professional)](#structure-definition-dm_varkey-rt-professional)
- [Structure definition LINKINFO (RT Professional)](#structure-definition-linkinfo-rt-professional)
- [Structure definition MSG_FILTER_STRUCT (RT Professional)](#structure-definition-msg_filter_struct-rt-professional)
- [Structure definition MSG_RTDATA_STRUCT (RT Professional)](#structure-definition-msg_rtdata_struct-rt-professional)

### Structure definition CCAPErrorExecute (RT Professional)

typedef struct {

DWORD dwCurrentThreadID; Thread ID of the current thread

DWORD dwErrorCode1;      Error code 1

DWORD dwErrorCode2;      Error code 2

BOOL bCycle;             cycle/acycle

char* szApplicationName; Name of the application

char* szFunctionName;    Name of the function

char* szTagName;         Name of the tag

LPVOID lpParam;          Pointer to the action stack

DWORD dwParamSize;       Size of the action stack

DWORD dwCycle;           Cycle of the tag

CMN_ERROR* pError;       Pointer to CMN_ERROR

} CCAPErrorExecute;

#### Members

The meaning of the individual error IDs and the structure elements depending on them are specified in the following table:

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![Members](images/36124053003_DV_resource.Stream@PNG-de-DE.png) | ![Members](images/36124060683_DV_resource.Stream@PNG-de-DE.png) | ![Members](images/36124081163_DV_resource.Stream@PNG-de-DE.png) | ![Members](images/36124088843_DV_resource.Stream@PNG-de-DE.png) | ![Members](images/36124096523_DV_resource.Stream@PNG-de-DE.png) | ![Members](images/36124104203_DV_resource.Stream@PNG-de-DE.png) | ![Members](images/36124111883_DV_resource.Stream@PNG-de-DE.png) | ![Members](images/36124119563_DV_resource.Stream@PNG-de-DE.png) | ![Members](images/36124140043_DV_resource.Stream@PNG-de-DE.png) | ![Members](images/36124147723_DV_resource.Stream@PNG-de-DE.png) | ![Members](images/36124155403_DV_resource.Stream@PNG-en-US.png) |
| 1007001 | 0 | x | x | x |  | x | x |  |  | Action requires exception |
| 1007001 | 1 | x | x | x |  | x | x |  |  | Exception when accessing the return result |
| 1007001 | 4097 | x | x | x |  | x | x |  |  | Stack overflow while executing the action |
| 1007001 | 4098 | x | x | x |  | x | x |  |  | The action contains a division by 0 |
| 1007001 | 4099 | x | x | x |  | x | x |  |  | The action contains an access to a non-existing symbol |
| 1007001 | 4100 | x | x | x |  | x | x |  |  | The action contains an access violation |
| 1007004 | 0 | x | x | x |  |  |  |  |  | Function is not known |
| 1007005 | 1 | x | x |  |  |  |  |  |  | Action does not include a P code. |
| 1007005 | 2 | x | x |  |  |  |  |  |  | Incorrect function name |
| 1007005 | 4 | x | x | x |  | x | x |  |  | Return value type is invalid |
| 1007005 | 32768ff | x | x | x |  | x | x |  |  | Ciss Compiler error when loading the action |
| 1007006 | 0 | x | x | x | x | x | x | x |  | Tag is not defined |
| 1007006 | 1 | x | x | x | x | x | x | x |  | Tag timeout |
| 1007006 | 2 | x | x | x | x | x | x | x | x | Tag cannot be returned in the desired format |
| 1007006 | 3 | x | x | x | x | x | x | x | x | Tag returns status violation, status present in CMN_ERROR.dwError1 |
| 1007007 | 1 | x | x | x |  | x | x |  | x | Error with PDLRTGetProp |
| 1007007 | 2 | x | x | x |  | x | x |  | x | Error with PDLRTSetProp |
| 1007007 | 3 | x | x | x |  | x | x |  | x | Error with DM call |

#### Error structure

The OnErrorExecute function uses the error structure to evaluate or to output error messages, if marked by an "x" in the pError column.

### Structure definition CCAPTime (RT Professional)

typedef struct {

DWORD dwCurrentThreadID; ThreadID of the current Thread

DWORD dwCode;            Code

BOOL bCycle;             cycle/acycle

char* szApplicationName; Name of the Application

char* szFunctionName;    Name of the Function

LPVOID lpParam;          Pointer to the Action-Stack

DWORD dwParamSize;       size of the Action-Stack

double dblTime;

DWORD dwFlags;           flags

} CCAPTime;

#### Members

**dwCode**

The structure element dwCode provides information on calling of OnTime:

| Symbol | Meaning |
| --- | --- |
| dwCode = 113 | Call with time definition for each action |
| dwCode = 114 | Call with time monitoring for each action |

**dwFlags**

The structure element dwFlags provides information on the output type:

| Symbol | Meaning |
| --- | --- |
| dwFlags = TRUE | The results are output to a file |
| dwFlags = FALSE | The results are output to the diagnostics window |

### Structure definition CMN_ERROR (RT Professional)

struct CMNERRORSTRUCT {

DWORD       dwError1,

DWORD       dwError2,

DWORD       dwError3,

DWORD       dwError4,

DWORD       dwError5;

TCHAR       szErrorText[MAX_ERROR_LEN];

}

CMN­_ERROR

#### Description

The extended error structure contains the error code and an error text for the error that has occurred. Each application can use the error structure to evaluate or to output error messages.

#### Members

**dwError1 .. dwError5**

These entries can be used in any way by the API functions.

The API descriptions inform about the values the respective entries contain in case of an error. If not specified otherwise, the error codes are present in dwError1.

**szErrorText**

Buffer for the text description of the error cause

The content is determined from the resources and therefore language-dependent.

### Structure definition DM_TYPEREF (RT Professional)

typedef struct {

DWORD dwType;

DWORD dwSize;

char szTypeName[MAX_DM_TYPE_NAME + 1];

}

DM_TYPEREF;

#### Members

**dwType**

Specifies the tag type

| dwType | PLC data type | HMI data type |
| --- | --- | --- |
| DM_VARTYPE_BIT | Binary tag | Bool |
| DM_VARTYPE_SBYTE | Signed 8-bit value | Byte |
| DM_VARTYPE_BYTE | Unsigned 8-bit value | UByte |
| DM_VARTYPE_SWORD | Signed 16-bit value | Short |
| DM_VARTYPE_WORD | Unsigned 16-bit value | UShort |
| DM_VARTYPE_SDWORD | Signed 32-bit value | Integer |
| DM_VARTYPE_DWORD | Unsigned 32-bit value | UInteger |
| DM_VARTYPE_FLOAT | Floating-point number 32-bit IEEE 754 | Float |
| DM_VARTYPE_DOUBLE | Floating-point number 64-bit IEEE 754 | Double |
| DM_VARTYPE_TEXT_8 | Text tag, 8-bit character set | Char |
| DM_VARTYPE_TEXT_16 | Text tag, 16-bit character set | String |
| DM_VARTYPE_RAW | Raw data type | Raw |
| DM_VARTYPE_STRUCT | Structure tag | Struct |
| DM_VARTYPE_TEXTREF | Text reference tag | String |

**dwSize**

Specifies the length of the data type in bytes.

**szTypeName**

In the case of structure tags, contains the name of the structure type

### Structure definition DM_VAR_UPDATE_STRUCT (RT Professional)

typedef struct {

DM_TYPEREF dmTypeRef;

DM_VARKEY dmVarKey;

VARIANT dmValue;

DWORD dwState;

}

DM_VAR_UPDATE_STRUCT;

#### Members

**dmTypeRef**

Contains information on the data type. For performance reasons, nothing is entered into this structure in case of cyclic requests.

**dmVarKey**

Specifies the tags to be edited.

**dmValue**

Tag value

Upon access to the value of the VARIANT a ".u." has to be inserted between the name of the VARIANT and the name of the member.

`Example`

`// Supply variant`

`myVariant.vt = VT_I4;`

`myVariant.u.lVal = 233;`

A description of the data type VARIANT can be found in the associated documentation. The VARIANT dmValue must be initialized with VariantInit() before first use and enabled again with VariantClear(&dmValue) after use. For this reason, the structure DM_VAR_UPDATE_STRUCT must not be deleted with ZeroMemory() or memset().

**dwState**

Identifies the tag status.

### Structure definition DM_VAR_UPDATE_STRUCTEX (RT Professional)

typedef struct {

DM_TYPEREF dmTypeRef;

DM_VARKEY dmVarKey;

VARIANT dmValue;

DWORD dwState;

DWORD dwQualityCode;

}

DM_VAR_UPDATE_STRUCTEX;

#### Members

**dmTypeRef**

Contains information on the data type. For performance reasons, nothing is entered into this structure in case of cyclic requests.

**dmVarKey**

Specifies the tags to be edited.

**dmValue**

Tag value

Upon access to the value of the VARIANT a ".u." has to be inserted between the name of the VARIANT and the name of the member.

`Example`

`// Supply variant`

`myVariant.vt = VT_I4;`

`myVariant.u.lVal = 233;`

A description of the data type VARIANT can be found in the associated documentation. The VARIANT dmValue must be initialized with VariantInit() before first use and enabled again with VariantClear(&dmValue) after use. For this reason, the structure DM_VAR_UPDATE_STRUCTEX must not be deleted with ZeroMemory() or memset().

**dwState**

Identifies the tag status.

**dwQualityCode**

Identifies the QualityCode tag.

### Structure definition DM_VARKEY  (RT Professional)

typedef struct {

DWORD dwKeyType;

DWORD dwID;

char szName[ MAX_DM_VAR_NAME + 1 ];

LPVOID lpvUserData;

}

DM_VARKEY;

#### Members

**dwKeyType**

Defines whether the tag is to be addressed by a key ID or by its name.

DM_VARKEY_ID Specification via key ID

DM_VARKEY_NAME Specification via tag name

**dwID**

Contains the key ID of the tags if dwKey type is set accordingly.

**szName**

Contains the name of the tag if dwKey type is set accordingly.

**lpvUserData**

Pointer to application-specific data

### Structure definition LINKINFO (RT Professional)

typedef struct {

LINKTYPE LinkType;

DWORD dwCycle;

TCHAR szLinkName[256];

}

LINKINFO;

#### Members

#### LinkType

LinkType are enumeration constants defined in the "Trigger.h" file. They are to be integrated into your script with the "#include "Trigger.h" command and the corresponding enumeration constants.

|  |  |  |
| --- | --- | --- |
| BUBRT_LT_NOLINK | 0 | no shortcut |
| BUBRT_LT_VARIABLE_DIRECT | 1 | direct tag |
| BUBRT_LT_VARIABLE_INDIRECT | 2 | indirect tag |
| BUBRT_LT_ACTION | 3 | C action |
| BUBRT_LT_ACTION_WIZARD | 4 | Dynamic Dialog |
| BUB_LT_DIRECT_CONNECTION | 5 | Direct connection |
| BUBRT_LT_ACTION_WIZARD_INPROC | 6 | Dynamic Dialog |

For the SetLink function, only the enumeration constants BUBRT_LT_VARIABLE_DIREKT and BUBRT_LT_VARIABLE_INDIRECT may be used. The GetLink function allows to return all listed enumeration constants.

#### dwCycle

Update cycle time

| Symbol | Meaning |
| --- | --- |
| 255 | Picture cycle |
| 235 | Window Cycle |
| 0 | Upon change |
| 1 | 250ms |
| 2 | 500 ms |
| 3 | 1 s |
| 4 | 2 s |
| 5 | 5s |
| 6 | 10s |
| 7 | 1min |
| 8 | 5min |
| 9 | 10min |
| 10 | 1h |
| 11-15 | User cycle 1-5 |

#### szLinkName

Tag name

---

**See also**

[SetLink (RT Professional)](#setlink-rt-professional)
  
[GetLink (RT Professional)](#getlink-rt-professional)

### Structure definition MSG_FILTER_STRUCT (RT Professional)

typedef struct {

CHAR        szFilterName[MSG_MAX_TEXTLEN+1];

WORD        dwFilter;

SYSTEMTIME  st[2];

DWORD       dwMsgNr[2];

DWORD       dwMsgClass;

DWORD       dwMsgType[MSG_MAX_CLASS];

DWORD                dwMsgState;

WORD        wAGNr[2];

WORD        wAGSubNr[2];

DWORD       dwArchivMode;

char        szTB[MSG_MAX_TB][

MSG_MAX_TB_CONTENT+1]

DWORD       dwTB;

Double      dPValue[MSG_MAX_PVALUE][2];

DWORD       dwPValue[2];

DWORD       dwMsgCounter[2];

DWORD       dwQuickSelect;

}

MSG_FILTER_STRUCT;

#### Description

In this structure the criteria are specified.

#### Members

**dwFilter**

The filter conditions are defined by means of the following constants from the file "m_global.h":

| Symbol | Meaning |
| --- | --- |
| MSG_FILTER_DATE_FROM | Date from |
| MSG_FILTER_DATE_TO | Date to |
| MSG_FILTER_TIME_FROM | Time from |
| MSG_FILTER_TIME_TO | Time to |
| MSG_FILTER_NR_FROM | Message number from |
| MSG_FILTER_NR_TO | Message number to |
| MSG_FILTER_CLASS | Message classes |
| MSG_FILTER_STATE | Message status |
| MSG_FILTER_AG_FROM | AS number from |
| MSG_FILTER_AG_TO | AS number to |
| MSG_FILTER_AGSUB_FROM | AG subnumber from |
| MSG_FILTER_AGSUB_TO | AG subnumber to |
| MSG_FILTER_TEXT | Message texts |
| MSG_FILTER_PVALUE | Process values |

| Symbol | Meaning |
| --- | --- |
| MSG_FILTER_COUNTER_FROM | Internal message counter from |
| MSG_FILTER_COUNTER_TO | Internal message counter to |
| MSG_FILTER_PROCESSMSG | Process messages |
| MSG_FILTER_SYSMSG | System messages |
| MSG_FILTER_BEDMSG | Operator messages |
| MSG_FILTER_DATE | Date from to |
| MSG_FILTER_TIME | Time from to |
| MSG_FILTER_NR | Message number from to |
| MSG_FILTER_VISIBLEONLY | Display visible messages |
| MSG_FILTER_HIDDENONLY | Display hidden messages |

**st**

Date/time from - to

Where st[0] is the start time (from), st[1] the end time (to)

Assign these fields for the criteria: MSG_FILTER_DATE, MSG_FILTER_DATE_FROM, MSG_FILTER_DATE_TO, MSG_FILTER_TIME, MSG_FILTER_TIME_FROM, bzw. MSG_FILTER_TIME_TO

If the current time is needed to pass a SYSTEMTIME- parameter, use the GetLocalTime function and not GetSystemTime.. There is usually a considerable difference between these two functions.

**dwMsgNr**

Message number from - to

Where dwMsgNr[0] is start no. (from), dwMsgNr[1] the end no. (to)

Assign these fields for the criteria: MSG_FILTER_NR, MSG_FILTER_NR_FROM bzw. MSG_FILTER_NR_TO

**dwMsgClass**

Message classes bit-coded.

Assign this field for the criterion: MSG_FILTER_CLASS

**dwMsgType**

Message type per alarm class, bit-coded

Assign this field for the criterion: MSG_FILTER_CLASS

**dwMsgState**

Message status bit-coded.

Assign this field for the criterion: MSG_FILTER_STATE

**wAGNr**

AGNr from - to

Assign these fields for the criteria: MSG_FILTER_AG_FROM or MSG_FILTER_AG_TO

**wAGSubNr**

AGSubNr from - to

Assign this field for the criteria: MSG_FILTER_AGSUB_FROM or MSG_FILTER_AGSUB_TO

**dwArchivMode**

Logging / reporting

Must be assigned 0.

**szTB**

Texts of the text blocks

Assign these fields for the criterion: MSG_FILTER_TEXT

**dwTB**

Active text blocks (from - to, bit-coded)

Assign this field for the criterion: MSG_FILTER_TEXT

**dPValue**

Process values from - to

Assign these fields for the criterion: MSG_FILTER_PVALUE

**dwPValue**

Active process values (from - to, bit-coded)

Assign this field for the criterion: MSG_FILTER_PVALUE

**dwMsgCounter**

Internal message counter from - to

Assign these fields for the criteria: MSG_FILTER_COUNTER_FROM, MSG_FILTER_COUNTER_TO

**dwQuickSelect**

Quick selection for hour, day, month

The parameter is reserved for future upgrades and must be preset to 0.

Assign this field for the criterion: MSG_FILTER_QUICKSELECT

LOWORD Type:

| Symbol | Meaning |
| --- | --- |
| MSG_FILTER_QUICK_MONTH | Quick selection last n months |
| MSG_FILTER_QUICK_DAYS | Quick selection last n days |
| MSG_FILTER_QUICK_HOUR | Quick selection last n hours |

HIWORD Number: 1...n

The end time of the quick selection refers to the current system time of the local computer. The start time is calculated back n * ( months, days, hours ).

### Structure definition MSG_RTDATA_STRUCT (RT Professional)

typedef struct {

DWORD                dwMsgState;

DWORD                dwMsgNr;

SYSTEMTIME           stMsgTime;

DWORD                dwTimeDiff;

DWORD                dwCounter;

DWORD                dwFlags;

WORD                 wPValueUsed;

WORD                 wTextValueUsed;

double               dPValue[MSG_MAX_PVALUE];

MSG_TEXTVAL_STRUCT   mtTextValue[MSG_MAX_PVALUE];

}

MSG_RTDATA_STRUCT;

#### Members

**dwMsgState**

Message status

|  |  |  |
| --- | --- | --- |
| MSG_STATE_COME | 0x00000001 | Message came in |
| MSG_STATE_GO | 0x00000002 | Message went out |
| MSG_STATE_QUIT | 0x00000003 | Message acknowledged |
| MSG_STATE_LOCK | 0x00000004 | Message locked |
| MSG_STATE_UNLOCK | 0x00000005 | Alarm locked |
| MSG_STATE_QUIT_SYSTEM | 0x00000010 | Message acknowledged by system |
| MSG_STATE_QUIT_EMERGENCY | 0x00000011 | Emergency acknowledgement |
| MSG_STATE_QUIT_HORN | 0x00000012 | Alarm alert acknowledgment |
| MSG_STATE_COMEGO | 0x00000013 | Message came in and went out, only displayed in the "Current messages" display |
| MSG_STATE_UPDATE | 0x00010000 | Bit for message update |
| MSG_STATE_RESET | 0x00020000 | Bit for message reset |
| MSG_STATE_SUMTIME | 0x00040000 | Bit active for daylight savings time |
| MSG_STATE_INSTANCE | 0x00080000 | Bit for instance message (n messages of a no.) |

**dwMsgNr**

Message number

stMsgTime

Date/Time: Telegram time depending on the calling function

**dwTimeDiff**

Duration coming/Telegram time in seconds

**dwCounter**

Internal message counter

**dwFlags**

Message flags in the database

|  |  |  |
| --- | --- | --- |
| MSG_FLAG_SUMTIME | 0x00000001 | Daylight savings time active |
| MSG_FLAG_COMMENT | 0x00000002 | Message has comments |
| MSG_FLAG_ARCHIV | 0x00000004 | Archiving |
| MSG_FLAG_PROTOCOL | 0x00000008 | Logging |
| MSG_FLAG_TEXTVALUES | 0x00000010 | Message has values accompanying the text |
| MSG_FLAG_TIMEINVALID | 0x00000020 | Bit for invalid date/time stamp |
| MSG_FLAG_INSTANCE | 0x00000040 | Instance message identification (185269) |

**wPValueUsed**

Process values used, bit-coded. Every bit may only be set in one of the two structure elements "wPValueUsed" or  "wTextValueUsed". An accompanying value may either be a number or a text.

**wTextValueUsed**

text values used, bit-coded. Every bit may only be set in one of the two structure elements "wPValueUsed" or  "wTextValueUsed". An accompanying value may either be a number or a text.
