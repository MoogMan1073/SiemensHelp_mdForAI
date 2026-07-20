---
title: "Programming Custom Web Controls (RT Unified)"
package: CuCoWCCUenUS
topics: 25
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Programming Custom Web Controls (RT Unified)

This section contains information on the following topics:

- [Custom web controls (RT Unified)](#custom-web-controls-rt-unified)
- [General structure and folder structure (RT Unified)](#general-structure-and-folder-structure-rt-unified)
- [Contract-based interaction and the manifest file (RT Unified)](#contract-based-interaction-and-the-manifest-file-rt-unified)
- [Interaction between control and container via the API (RT Unified)](#interaction-between-control-and-container-via-the-api-rt-unified)
- [Extensions (RT Unified)](#extensions-rt-unified)
- [Revision of a graphical user interface (RT Unified)](#revision-of-a-graphical-user-interface-rt-unified)
- [Creating the ZIP file (RT Unified)](#creating-the-zip-file-rt-unified)
- [Restrictions (RT Unified)](#restrictions-rt-unified)
- [Installing and using Custom Web Controls (RT Unified)](#installing-and-using-custom-web-controls-rt-unified)
- [Updating Custom Web Controls (RT Unified)](#updating-custom-web-controls-rt-unified)

## Custom web controls (RT Unified)

Custom Web Controls represent an independent web page with interface to Runtime. Custom Web Controls offer you the option of adding your own elements to the visualization elements provided. Custom Web Controls thus extend usability and functionality to achieve an optimal visualization result.

Custom web controls are run on the web client and hosted in Runtime. A Custom Web Control can be displayed as an independent Web page in any browser and on any mobile device.

> **Note**
>
> Observe the performance limit of Unified Comfort Panels. We do not recommend using, for example, Custom Web Controls with 3D representations for Unified Comfort Panels.

![Figure](images/134132252171_DV_resource.Stream@PNG-de-DE.png)

### Requirements for a web-based graphic interface

To use a Custom Web Control in WinCC, the Control must be anchored in a container. The container is provided on the user side by the Custom Web Control framework and contains components of the graphical user interface (GUI).

The following requirements apply when a web-based GUI component if it is to be provided in a Custom Web Control container:

- The component must be HTML5-based and interpretable by current browsers.
- The component must be executable exclusively on the client side.
- The component must work without interaction with client-side components outside the container.
- The component must comply with the principle of a Single Page Application (SPA) and fit on a web page. All code (HTML, JavaScript and CSS) must be received when the page is called or dynamically added during user actions. The web page may not reload at any time.
- The component must not know in which environment it is deployed. The component must be executable independent of the environment.
- All data exchange must take place through communication between client and server.

### Application example

Based on an application example, you can learn more about the structure and development of a Custom Web Control: [SIOS entry](https://support.industry.siemens.com/cs/ww/en/view/109779176).

## General structure and folder structure (RT Unified)

A ready-to-use Custom Web Control must be available as a "*.zip" file that contains all graphics and code files used. The structure is divided into two folders, "assets" and "control", and a "*.json" file (manifest.json).

The "assets" folder contains a logo that is displayed in the TIA Portal. The "control" folder contains "*.html", "*.js" and "*.css" files, as well as used graphics and icons that the Control needs for the display.

A Custom Web Control has the following folder structure:

![Figure](images/135029750283_DV_resource.Stream@PNG-de-DE.png)

Contents of the "control" folder:

![Figure](images/135042870539_DV_resource.Stream@PNG-de-DE.png)

Contents of the "assets" folder:

![Figure](images/135042878859_DV_resource.Stream@PNG-de-DE.png)

## Contract-based interaction and the manifest file (RT Unified)

This section contains information on the following topics:

- [Basics for the manifest (RT Unified)](#basics-for-the-manifest-rt-unified)
- [Manifest structure (RT Unified)](#manifest-structure-rt-unified)
- [Data types and references in the manifest (RT Unified)](#data-types-and-references-in-the-manifest-rt-unified)

### Basics for the manifest (RT Unified)

To enable the Unified Runtime server to communicate with the provided control, the control must reveal methods, events and properties to the Unified Runtime server.

The sum of the information that the control releases with it is called the "contract". For the custom web control container, this information is contained in a "*.json" file (manifest.json). The manifest file contains multiple sectors that each reveal elements to the container.

| ![Figure](images/101804624523_DV_resource.Stream@PNG-de-DE.png) | Tips for an efficient procedure |
| --- | --- |
| To verify that you have created a valid JSON file, use the notes in Visual Studio Code or copy the content of the file to an online validation tool, such as "https://jsonlint.com". |  |

### Manifest structure (RT Unified)

Each manifest has two root elements:

- "mver": Specifies the manifest version.
- "control": Specifies the manifest type.

The "control" element provides the following sectors.

- "identity" sector
- "environment" sector
- "metadata" sector
- "contracts" sector

  The "contracts" sector contains the following:

  - Methods
  - Events
  - Properties
- "types" sector

#### "identity" sector

The "identity" sector contains identity information.

The following information of the data type "String" is required:

- "name": Defines the name of the Custom Web Control.
- "version": Defines the version of the Custom Web Control.
- "displayname": Defines the display name of the Custom Web Control.

  > **Note**
  >
  > Special characters must not be used, e.g. #,$,*,%,.,/,;,?;[,],~,'".
- "icon" (optional)

  Includes the path for the logo that is displayed in the "Toolbox &gt; My Controls" task card in the TIA Portal.

  The path can be specified as follows:

  - URL starting with "http://" or "https://"
  - Relative path to the storage location of the manifest starting with "./"
  - Data URL that contains a Base64 encoded image starting with "data:"

  The referenced image must be between 120x120 pixels and 320x320 pixels in size. The following image formats are supported:

  - JPG and JPEG
  - PNG
  - ICO
  - TIFF
  - BMP

  Use a square image to avoid distortions.

  If "icon" is not specified, only the display name ("displayname") is shown under "My Controls".
- "type": Each Custom Web Control can be referenced via the identity type and therefore requires a pre-defined structure. Types must follow the 8-4-4-4-12 pattern of a 128-bit integer (GUID).

  > **Note**
  >
  > **GUID generation**
  >
  > For example, a GUID can be created as follows:
  >
  > - In Visual Studio under "Tools &gt; Create GUID"
  > - Under [https://www.guidgenerator.com/](https://www.guidgenerator.com/)
- "start" (optional): The start directory must be specified to set the starting point of the Custom Web Control for the browser.

  If this value is not defined, "./control/index.html" is used.

#### Example: "identity"

"identity": {

   "name": "GaugeMeter",

   "version": "1.0",

   "displayname": "GaugeMeter",

   "icon": "./assets/logo.ico",

   "type": "guid://551BF148-2F0D-4293-99C2-C9C3A1A6A073",

   "start": "./control/index.html"

}

#### "environment" sector

The optional "environment" sector provides information on the environment that is integrated into the Custom Web Control. If the sector does not exist, then no requirements and dependencies exist.

Requirements are specified under the element "prerequesites". "renderingspace" can be used below "prerequesites". Restrictions of the display of the Custom Web Control can be specified under "renderingspace".

The following restrictions are permitted:

| Restriction | Data type | Description |
| --- | --- | --- |
| minwidth | integer | Specifies the minimum width that is necessary to display the Custom Web Control. |
| maxwidth | integer | Specifies the maximum width that is permitted to display the Custom Web Control. |
| defaultwidth | integer | Specifies the default width of the Custom Web Control.   The value must be between "minwidth" and "maxwidth". |
| minheight | integer | Specifies the minimum height that is necessary to display the Custom Web Control. |
| maxheight | integer | Specifies the maximum height that is permitted to display the Custom Web Control. |
| defaultheight | integer | Specifies the default height of the Custom Web Control. The value must be between "minheight" and "maxheight". |
| unit | string | Specifies the unit of the display restrictions. The following values are permitted:  - "px" - "cm" - "mm" - "in" - "pt"   If "unit" is not specified, "px" is used. |

Extensions can be specified under "extensions".

Each extension has the following optional fields:

- "mandatory": Specifies whether the Custom Web Control can be used without the extension.

  Regardless of the value in this field, extensions of a Custom Web Control are always necessary.
- "version": Specifies a compatible version or versions.

You can find available extensions at [Extensions](#extensions-rt-unified).

#### Example: "environment"

"environment": {

  "prerequisites": {

    "renderingspace": {

      "defaultwidth": 450,

      "defaultheight": 300,

      "unit": "px"

    }

  }

  "extensions": {

    "HMI": {

      "mandatory": true,

      "version": "~1.0.0"

    }

  }

}

#### "metadata" sector

The following optional information can be stored, for example, as metadata:

- Author
- Keywords
- Description of the Custom Web Control
- Homepage

Metadata are not relevant for the execution of the Custom Web Control. User-defined metadata can be supplemented.

#### Example: "metadata"

"metadata":{

  "author": "Siemens",

  "keywords": [

    "Gauge",

    "GaugeMeter"

  ]

  "description": "Display tag value with a gauge."

"homepage": "https://www.siemens.com"

"company": "Siemens AG"

}

#### "contracts" sector

The "contracts" sector contains methods, events and properties as interface for use in the TIA Portal.

The Custom Web Control has access to methods, events and properties and therefore receives tag changes from the PLC, for example.

Data types can be used or referenced in this sector.

> **Note**
>
> A data type can be assigned with the keyword "type" below an element or it can be referenced with "$ref". The two keywords cannot be used at the same time.
>
> You can find additional information at [Data types and references in the manifest](#data-types-and-references-in-the-manifest-rt-unified).

Note the following restrictions when naming methods, events, properties, arguments and parameters:

- Only alphanumeric characters of the ASCII character set and "_" are permitted.
- The names must not start with a number.
- The entry is case-sensitive.
- Special characters are not permitted.

#### Methods

"methods" contain a list of methods used by the Custom Web Control.

Methods of a Custom Web Control can be used in Unified Scripting to transfer information from the Unified server to the custom web control in the client. Methods are always executed asynchronously.

For example, a method to flash the passed zone can be called as follows:

`Screen.Items('GaugeMeter_1').BlinkZone(2)`

The following optional elements can be assigned to a method:

- "return": Specifies or references a data type.

  An additional "promise" field of the type "Boolean" returns whether the method is actually running asynchronously and is not fulfilled in a defined time period. The default value is "false". If the value is "true", the type specified with "return" is valid for the fulfilled value of the Promise object.

  You can react as follows to the Promise object:

  "`const result = await Screen.Items('GaugeMeter_1').BlinkZone(2) HMIRuntime.Trace(result);` "
- "parameters": Each parameter specifies or references a data type.
- "description": Specifies the description of the method.

#### Example: "methods"

"methods": {

  "BlinkZone": {

    "parameters": {

      "zoneIndex": {

        "type": "number"

      }

    },

    "description": "Let the given zone blink."

  }

}

#### Events

"events" contain a list of events used by the Custom Web Control.

Events are triggered by the Custom Web Control itself at any time. Events can be used in Unified Scripting to transfer information from the client to the server. They can be found in the engineering system under "Properties &gt; Events".

An event can be assigned the following optional elements:

- "arguments": Contains arguments. Each argument specifies or references a data type.
- "description": Specifies the description of the event.

#### Example: "events"

"events": {

  "ZoneChanged": {

    "arguments": {

      "zoneIndex": {

        "type": "number"

      }

    },

    "description": "Whenever the zone is changed, this event is raised and gives you the new zone index."

  }

}

#### Properties

"properties" contain a list of properties used by the Custom Web Control.

Properties can be found in the engineering system under "Properties &gt; Properties &gt; Interfaces".

The following elements can be assigned to a property:

- "type" or "$ref": A data type must be specified or referenced.

  > **Note**
  >
  > **Only individual elements can be connected**
  >
  > When using complex data types, such as an array or user data types, only the elements of the bottom level can be linked to a property.
- "default" (optional): Specifies the default value of the property.
- "description" (optional): Specifies the description of the property.

#### Example: "properties"

"properties": {

  "GaugeValue": {

    "type": "number",

    "default": 20

    "description": "This property represents the value of the gauge."

  },

  "MinValue": {

    "type": "number",

    "default": 0

    "description": "This property represents the minimum value of the gauge."

  },

  "MaxValue": {

    "type": "number",

    "default": 50

    "description": "This property represents the maximum value of the gauge."

  },

}

#### "types" sector

The "types" sector contains local definitions for user-defined data types, objects and arrays.

A data type that is defined in this sector can only be referenced within this manifest. External data types from a JSON Schema can be referenced under "contract" or "types".

#### Example: "types"

"types": {

  "Color": {

    "$id": "http://tia.siemens.com/wincc-unified/types/s/color",

    "type": "number"

  },

  "AlignmentPart": {

    "type": "object",

    "properties": {

      "Vertical": {

        "$ref":"#/control/types/VerticalAlignment"

      }

    }

  },

  "VerticalAlignment": {

    "type": "string",

    "enum": [

      "Top",

      "Center",

      "Bottom"

    ],

    "default": "Center"

  }

}

---

**See also**

[Creating the ZIP file (RT Unified)](#creating-the-zip-file-rt-unified)

### Data types and references in the manifest (RT Unified)

#### Data types

Data types in the "contracts" sector of the manifest can be specified or referenced as follows:

- As basic data type

  The following basic data types can be used without reference:

  - Boolean: Can accept "true" or "false".
  - Number: Any representable number, for example:

    Integer: 1; -3

    Float: 5.21

    Numbers in exponential format: 2.99792458e8
  - String: Any text
  - Null: Displays the zero object and is used as return type for methods without return value.
- As local reference to the "types" sector of the manifest

  Arrays, objects or user-defined data types can be defined in the "types" sector.
- As external reference to a JSON Schema that is offered by Siemens, for example:

  - "$id": "http://tia.siemens.com/wincc-unified/types/s/color"
  - "$id": "http://tia.siemens.com/wincc-unified/types/c/font"

User-defined data types are, for example, structured data types or basic data types with restrictions.

The following type restrictions are permitted in the manifest:

| Type restriction | Description |
| --- | --- |
| enum | Specifies the permitted String values of an enumeration. |
| items | Specifies the permitted data type of an array. |
| minItems | Specifies the minimum number of elements in an array. |
| maxItems | Specifies the maximum number of elements in an array. |
| minimum | Specifies the minimum value of a number of the data type "number" or "integer". |
| maximum | Specifies the maximum value of a number of the data type "number" or "integer". |
| pattern | Specifies the permitted pattern as regular expression that defines the content of a string. |
| minLength | Specifies the minimum length of a string. |
| maxLength | Specifies the maximum length of a string. |
| required | Specifies a list of mandatory properties within a structure. |

#### Identification of a data type

When you define a data type in the "types" sector, you can specify a Uniform Resource Identifier (URI) or a fragment in the optional "$id" field. This information uniquely identifies the data type across multiple manifests. Within the manifest in which a data type is defined, this data type can also be referenced by using its ID.

> **Note**
>
> Absolute URIs are preferred over fragments.

#### Referencing a data type

Data types in the "contracts" or "types" sector can be referenced with "$ref".

You have the following options for referencing data types:

- As reference to the "types" sector without using the "$id"

  Example: `"BackColor":{"$ref": "#/control/types/color"}`
- As reference to the "types" sector using the "$id"

  Example: `"BackColor":{"$ref": "http://tia.siemens.com/wincc-unified/types/s/color"}`

## Interaction between control and container via the API (RT Unified)

A single API object ("WebCC" object) is used to enable communication between the Custom Web Control and the Unified Runtime server.

The following requirements apply to this API object:

1. All functionalities that the Control needs for independent executability must be available on the client side.
2. The API object must be created and extended with the specific functionalities that the control provides through the manifest file.

### The API object

The API object represents the interface through which the methods, events and properties of the Control are called or received from the framework.

For the initialization of the Custom Web Control, the properties, methods and events of the manifest file must be declared.

You can link the properties, methods and events to your code.

> **Note**
>
> **Declaration**
>
> The name must match the name of the manifest file.
>
> Note the following restrictions:
>
> - Only alphanumeric characters of the ASCII character set and "_" are permitted.
> - The names must not start with a number.
> - The entry is case-sensitive.
> - Special characters are not permitted.

### Example: API object

{

//Methods

methods: {

BlinkZone: function(zoneIndex){

//code

}

},

//Events

events: ['ZoneChanged', 'Event2'],

//Properties

properties:{

GaugeValue: " ",

Property2: " "

}

}

### Integrating the "WebCC" object

Integrating the API object makes the corresponding namespaces available to the Custom Web Control.

As a requirement, a JavaScript file (webcc.min.js) must be integrated in "index.html", which performs a handshake between the control and the container.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Do not change "webcc.min.js" file**  The "webcc.min.js" file is used to establish the connection and must not be changed. |  |

The "index.html" file is the entry point of your web page.

> **Note**
>
> **Download "webcc.min.js"**
>
> You can find the file "webcc.min.js" in the application example: [SIOS entry](https://support.industry.siemens.com/cs/ww/en/view/109779176)

The "webcc.min.js" file contains the connection data to WinCC Unified.

After the connection setup, you can access the data that is defined in the "manifest.json" file from any position in your application.

### Example: Integrating the "WebCC" object

&lt;!doctype html&gt;

&lt;head&gt;

  &lt;script&gt;…&lt;/script&gt;

  &lt;!-- Web Custom Control Facade --&gt;

  &lt;script type= text/JavaScript src='webcc.min.js'&gt;

&lt;/head&gt;

### Initialization of the "WebCC" object

The API object must have been successfully initialized before the Control can be created. To check this, the tag "result" of the parameter "function(result)" is queried. It is used as an indicator and must supply "true" to continue. As an additional parameter, extensions can be called during initialization.

### Example: Initialization of the "WebCC" object

WebCC.start( function( result ) {

      if ( result ) {

        //startup succeeded

        //add subscriptions

      } else {

        //startup failed

      }

    },

controlInit.ControlApi,

  ['HMI'] };

---

**See also**

[Extensions (RT Unified)](#extensions-rt-unified)

## Extensions (RT Unified)

This section contains information on the following topics:

- [Basics of extensions (RT Unified)](#basics-of-extensions-rt-unified)
- [HMI extension (RT Unified)](#hmi-extension-rt-unified)
- [Formatting extension (RT Unified)](#formatting-extension-rt-unified)
- [Dialog extension (RT Unified)](#dialog-extension-rt-unified)

### Basics of extensions (RT Unified)

With extensions you can use additional functions in Custom Web Controls.

The following extensions can be used:

- HMI extension:

  - Obejct "WebCC.Extensions.HMI.Properties" provides access to all properties of the container that contains the Custom Web Control.
  - Object "WebCC.Extensions.HMI.Style" allows access to the active style
  - The "DatePrecise", "Big", and "Variant" prototypes as extensions to the integrated JavaScript objects.
- Formatting extension: The "WebCC.Extensions.Formatting.Output" object enables the formatting of text.
- Dialog extension: Allows access to a dialog window.

When using extensions, follow these steps:

1. You integrate the extensions used in the manifest in the "environment" sector.

   This permits the environment to check whether the respective extension exists.
2. You call the extensions used during the initialization of the "WebCC" object.
3. Call the extension as property of the "WebCC" object at any point in your Custom Web Control.

#### Integration in the manifest

Integrate extensions in the "environment" sector of the manifest as follows:

"environment": {

  "extensions": {

    "HMI": {

      "mandatory": true,

      "version": "~1.0.0"

    }

    "Formatting": {

      "mandatory": true,

      "version": "~1.0.0"

    }

    "Dialogues": {

      "mandatory": true,

      "version": "~1.0.0"

    }

  }

}

#### Initialization of the "WebCC" object

WebCC.start( function( result ) {

      if ( result ) {

        //startup succeeded

        //add subscriptions

      } else {

        //startup failed

      }

    },

controlInit.ControlApi,

  ['HMI', 'Formatting', 'Dialogues'] };

---

**See also**

[Dialog extension (RT Unified)](#dialog-extension-rt-unified)
  
[Formatting extension (RT Unified)](#formatting-extension-rt-unified)
  
[HMI extension (RT Unified)](#hmi-extension-rt-unified)

### HMI extension (RT Unified)

This section contains information on the following topics:

- ["Properties" object (RT Unified)](#properties-object-rt-unified)
- ["Style" object (RT Unified)](#style-object-rt-unified)
- [Data types (RT Unified)](#data-types-rt-unified)

#### "Properties" object (RT Unified)

The "WebCC.Extensions.HMI.Properties" object provides access to all properties of the container that contains the Custom Web Control. The properties are placed after the "Properties" object.

You can find all available properties in the WinCC Unified object model under [WebControl](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#webcontrol-rt-unified).

The extension enables the "WebCC.onPropertyChanged.subscribe" event that can be used to register for changes of properties.

#### "Style" object (RT Unified)

The "WebCC.Extensions.HMI.Style" object has the "Name" property that contains the name of the active style.

The "WebCC.Extensions.HMI.Style.onChanged" event is initiated when the style is changed in runtime. The event contains the name of the style that is being activated.

##### Example

`WebCC.Extensions.HMI.Style.onChanged.subscribe( function( currentStyle) {`

`console.log(currentStyle);`

`});`

#### Data types (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified)
- ["DatePrecise" prototype (RT Unified)](#dateprecise-prototype-rt-unified)
- ["Big" prototype (RT Unified)](#big-prototype-rt-unified)
- ["Variant" prototype (RT Unified)](#variant-prototype-rt-unified)

##### Introduction (RT Unified)

Prototypes are provided as extension of the installed JavaScript objects; they are used in the HMI environment.

The prototypes are available in the global namespace.

##### "DatePrecise" prototype (RT Unified)

The JavaScript object "Date" provides millisecond accuracy, while Unified Runtime works with nanosecond accuracy.

The "DatePrecise" object is used to work with nanosecond accuracy. The "DatePrecise" object does not contain any information about time zones and uses coordinated universal time (UTC) for calculations.

###### Constructors and methods

| Constructor | Description |
| --- | --- |
| `DatePrecise()` | Creates a "DatePrecise" object for the current date and time. |
| `DatePrecise(year, month[, day[, hours[, minutes[, seconds[, milliseconds[, microseconds[, nanoseconds]]]]]]])` | Creates a "DatePrecise" object. This constructor corresponds to the JavaScript "Date" constructor, but enables additional parameters for microseconds and nanoseconds.  The parameters "year" and "month" are mandatory. |
| `DatePrecise(DomHighResTimeStamp)` | Creates a "DatePrecise" object that accepts the "DomHighResTimeStamp" object of a browser with a millisecond value since January 1, 1970, and an accuracy in the microsecond range. |
| `DatePrecise([seconds, nanoseconds])` | Creates a "DatePrecise" object that accepts the second value since January 1, 1970, and an additional nanosecond offset. |
| `DatePrecise(date)` | Creates a "DatePrecise" object from a passed JavaScript "Date" object. The nanoseconds are "0". |
| `DatePrecise(precise)` | Creates a "DatePrecise" object from a passed "DatePrecise" object. |

| Method | Description |
| --- | --- |
| `getMicroseconds()` | Returns the number of microseconds (from 0 to 999). |
| `getNanoseconds()` | Returns the number of nanoseconds (from 0 to 999). |
| `getTime()` | Returns the number of milliseconds since January 1, 1970. This method corresponds to the method of the JavaScript "Date" object. |
| `getHrTime()` | Returns a precise date as an array with two numerical values. The first value represents the seconds elapsed since January 1, 1970. The second value is the offset in nanoseconds. |
| `setMicroseconds(microseconds)` | Sets the microseconds (from 0 to 999). |
| `setNanoseconds(nanoseconds)` | Sets the nanoseconds (from 0 to 999). |
| `setTime(DomHighResTimeStamp)` | Determines the date over a specific number of milliseconds, starting from January 1, 1970.  This method corresponds to the method of the JavaScript "Date" object. |
| `setHrTime([seconds, nanoseconds])` | Specifies a precise date as array with two numerical values. The first value represents the seconds elapsed since January 1, 1970. The second value is the offset in nanoseconds. |
| `toDate()` | Returns a "Date" object. The nanosecond accuracy is lost. |
| `valueOf()` | Returns a "DomHighResTimeStamp" object. The nanosecond accuracy is lost. The object is compatible with the JavaScript "Date" object. |

###### Examples

var ms = window.DatePrecise([1593862222, 545410000]).getTime();

var date = window.DatePrecise(Date.UTC(1960, 11, 24, 18, 4, 5, 10));

var jsdate = date.toDate();

##### "Big" prototype (RT Unified)

The "Big" prototype enables processing of large numbers with any desired precision. You can find the library and application examples at "Big.js".

###### Constructors and methods

> **Note**
>
> The "n" parameter can take on the following data types:
>
> - JavaScript data type "Number"
> - "Big" data type
> - "String" data type that contains a numerical value

| Constructor | Description |
| --- | --- |
| `Big(n)` | Creates a number of the data type "Big" with the value "n". |

| Method | Description |
| --- | --- |
| `abs()` | Returns the absolute value of the "Big" number. |
| `cmp(n)` | Compares two "Big" numbers. The following return values occur:  - If the "Big" number is greater than "n", 1 is returned. - If the "Big" numbers are the same, 0 is returned. - If the "Big" number is less than "n", -1 is returned. |
| `div(n)` | Returns the value of the "Big" number divided by "n". |
| `eq(n)` | Returns a Boolean value that indicates whether the "Big" number and "n" are the same. |
| `gt(n)` | Returns a Boolean value that indicates whether the "Big" number is greater than "n". |
| `gte(n)` | Returns a Boolean value that indicates whether the "Big" number is greater than or equal to "n". |
| `lt(n)` | Returns a Boolean value that indicates whether the "Big" number is less than "n". |
| `lte(n)` | Returns a Boolean value that indicates whether the "Big" number is less than or equal to "n". |
| `minus(n)` | Returns the value of the "Big" number minus "n". |
| `mod(n)` | Returns the value of the "Big" number using modulo of value "n". |
| `plus(n)` | Returns the value of the "Big" number plus "n". |
| `pow(exp)` | Returns the value of the "Big" number to the power of "exp". The value for "exp" must be an integer between -1e+6 and +1e+6. |
| `round([dp [, rm]])` | Returns the rounded value of the "Big" number to a maximum of "dp". The value for "dp" must be an integer between -1e+6 and +1e+6. The default value for the parameter "dp" is 20.  The "rm" parameter supports the following modes:  - 0: Rounded to zero. - 1: Rounded to the nearest neighbor. If the distance is equal, the figures are rounded up. - 2: Rounded to the nearest neighbor. If the distance is the same, it is rounded to the straight neighbor. - 3: Rounded up. |
| `sqrt()` | Returns the square root of the "Big" number. |
| `times(n)` | Returns the value of the "Big" number multiplied by "n". |
| `toExponential([dp])` | Returns a string that represents the value of the "Big" number type in exponential notation. The "dp" parameter defines the number of decimal places displayed. The value for "dp" must be an integer between 0 and 1e+6. The default value for the parameter "dp" is 20. |
| `toFixed([dp])` | Returns a string that represents the value of the "Big" number type in standard notation. The "dp" parameter defines the number of decimal places displayed. The value for "dp" must be an integer between 0 and 1e+6. The default value for the parameter "dp" is 20. |
| `toPrecise(sd)` | Returns a string that represents the number of significant digits of the "Big" number. The "sd" parameter defines the number of decimal places displayed. The value for "sd" must be between 1 and 1e+6. The default value for the parameter "sd" is 20.  If the "Big" number has more than the number of significant digits defined by "sd", the return value is rounded to the number of significant digits defined by 'sd'. The rounding mode is 1. |
| `toString()` | Returns a string that represents the value of the "Big" number. Under the following conditions, the value is displayed in exponential notation:  - The positive exponent is greater than or equal to 21. - The negative exponent is less than or equal to -7. |

##### "Variant" prototype (RT Unified)

Basic data types can be mapped with the "Variant" prototype.

###### Constructors and methods

| Constructor | Description |
| --- | --- |
| `Variant(value, type)` | Creates a "Variant" object using any value and data type. |

| Methods | Description |
| --- | --- |
| `typeOf()` | Returns a numerical value that identifies the elementary data type. |
| `valueOf()` | Returns the value that was converted into the corresponding data types "Number", "Boolean", "String", "DataPrecise" or "Big".  "Time" and "DateTime" are returned as values of the type "DatePrecise".   Numerical values that cannot be mapped without loss of accuracy are returned as values of the type "Big". |

###### Examples

var variant = window.Variant(47111, 0x5);

var big = variant.valueOf();

### Formatting extension (RT Unified)

The "WebCC.Extensions.Formatting.Output" object enables the creation and formatting of text according to the parameters passed.

#### Methods

| Methods | Description |
| --- | --- |
| `format(value, pattern [, lcid])` | Takes any number or random text and formats it according to the parameters passed.  The language can optionally be specified via the LCID. When the LCID is not transferred, the current language is used. |

#### Example

`var floatValue = WebCC.Extensions.Formatting.Output.format( 42.1111111, '{F2}', 'de-DE' );`

`//Ergebnis: 42,11`

`var hexValue = WebCC.Extensions.Formatting.Output.format( 45054, '{H,2}' );`

`//Ergebnis: AF FE`

`var dateValue = WebCC.Extensions.Formatting.Output.format( 1609745948315, '{D,@yyyy/MM/dd} {T,@HH:mm:ss}');`

`//Ergebnis: 2021/01/04 07:39:08`

---

**See also**

[Basics of extensions (RT Unified)](#basics-of-extensions-rt-unified)

### Dialog extension (RT Unified)

The dialog extension enables you to open a dialog window that is not limited by the display range of the Control. A URL is made available to the user interface; it is displayed in the dialog. A JSON data model is also made available. It is transferred to the dialog and returned as soon as the dialog is closed.

The use of dialogs is asynchronous.

#### "WebCC.Extensions.Dialogues" object

The "WebCC.Extensions.Dialogues" object allows for the creation and use of one or more dialogs.

The object has the following methods and properties:

| Methods | Description |
| --- | --- |
| `create(id, view, data, [options])` | Creates a "Dialog" object.   The "id" parameter is transferred as a string. The "view" parameter is transferred as a string that contains a relative URL. The "data" parameter contains random data this is transferred to the dialog. The optional "options" parameter contains a JSON object with the following options:  - Information on the size of the dialog box: "minwidth", "maxwidth", "minheight", "maxheight" and "unit". - A Boolean value "resizable" that defines whether the size of the dialog box can be changed. - A "caption" string that is displayed in the title of the dialog. |
| `list()` | Returns a string array that contains the IDs of currently created and opened dialog boxes.  As soon as the dialog box is closed, the ID is no longer displayed in the string array. |
| `get(id)` | Returns a "Dialog" object with the transferred ID. If the ID does not exist, ZERO is returned. |

| Property | Description |
| --- | --- |
| `self` | The "self" property contains the "Dialog" object. |

#### "WebCC.Extensions.Dialog" prototype

The "WebCC.Extensions.Dialog" prototype enables the interaction with the dialog instance and offers the following methods and events:

| Methods | Description |
| --- | --- |
| `open(width, height)` | Creates a dialog and returns a "promise" property. If the dialog is already open, only the "promise" property is returned.  The dialog is displayed in the current screen with the specified width and height. |
| `close([result])` | Closes a dialog and fulfills the associated "promise" property.   The "result" parameter is optional and can be of any type. The "result" parameter normally contains the data that were transferred when the dialog was opened and were subsequently changed. |
| `cancel([reason])` | Closes a dialog. The "promise" property is rejected.   The "reason" parameter is optional and can be of any type. |

| Property | Description |
| --- | --- |
| `id` | The "id" property contains the ID of the dialog. The ID is available as a string. |
| `promise` | The "promise" property contains information about the status of a dialog. |
| `data` | The "data" property contains the data that were transferred when a dialog was created. |

#### Example: Opening a dialog

var dialog = WebCC.Extensions.Dialogues.create('id_1','input.html', 'myData',

{ caption: 'GaugeValue', resizeable: false } );

if ( dialog ) {

  // open( width, height ) returns promise

  dialog.open( 250, 150 ).then(

    function success( data ) {

      // close called

      WebCC.Properties.GaugeValue = data;

      updateValue( data );

  }).catch(

    function ( reason ) {

      // cancel called

  });

}

#### Example: Access to data within a dialog

var self = WebCC.Extensions.Dialogues.self;

if ( self ) {

  // initialize dialog data

  var inputValue = self.data;

  // 'myData'

}

#### Example: Closing a dialog with fulfilled promise

var self = WebCC.Extensions.Dialogues.self;

if ( self ) {

  // close([result]) fullfill dialog promise

  self.close( data );

}

#### Example: Closing a dialog in case of cancellation

var self = WebCC.Extensions.Dialogues.self;

if ( self ) {

  // cancel([reason]) reject dialog promise

  self.cancel();

}

---

**See also**

[Basics of extensions (RT Unified)](#basics-of-extensions-rt-unified)

## Revision of a graphical user interface (RT Unified)

### Introduction

User interfaces can be used as Custom Web Control by using the framework. This document is intended to describe the process by means of an example and uses a provided user interface. With this user interface, a slider controls the movement of a pointer.

The user interface can be found in the application example at the following address: [SIOS entry](https://support.industry.siemens.com/cs/ww/en/view/109779176)

The code examples shown in this section can be found in the "index.html" file of the application example.

### Conversion of the color coding

The TIA Portal and the manifest file use different color coding. The manifest file is not able to work with hexadecimal values, but only accepts decimal values. The author of the manifest file must convert the hexadecimal values as defined in the TIA Portal into decimal values.

To use a web page as a Custom Web Control, the encoding must be converted.

### Example: Color coding

function toColor(num) {

  num &gt;&gt;&gt;= 0;

  var b = num &amp; 0xFF,

      g = (num &amp; 0xFF00) &gt;&gt;&gt; 8,

      r = (num &amp; 0xFF0000) &gt;&gt;&gt; 16,

      a = ((num &amp; 0xFF000000) &gt;&gt;&gt; 24) / 255;

  return 'rgba(' + [r, g, b, a].join(',') + ')';

}

### Defining the default values of properties

Default properties are defined in the TIA Portal and for Runtime projects. These default properties define, among other things, font size, line thickness and value ranges. Default properties are obtained in Runtime during initialization of the setup.

### Example: Defining default values

var defaultProperties = {

  GaugeValue: 20,

  GaugeBackColor: 4294967295,

  Alignment:

  {

    Vertical: 'Center'

  },

  LineThickness: 20,

  FontSize: 16,

  MinValue: 0,

  MaxValue: 50,

  DivisionCount: 5,

  Zones: [

    { Min: 0, Max: 30, StrokeColor: 4281381677 },

    { Min: 30, Max: 40, StrokeColor: 4294958336 },

    { Min: 40, Max: 50, StrokeColor: 4293934654 }

  ]

}

### Initialization of the Custom Web Control

To be able to function as a Custom Web Control within WinCC, the "WebCC" object must be initialized. After that the Control can be created.

Initialization takes place in "index.html".

### Initialization of the Custom Web Control

WebCC.start(

// callback function; occurs when the connection is done or failed.

// "result" is a boolean defining if the connection was successfull or not.

function (result) {

if (result) {

console.log('connected successfully');

initializeGauge();

// Set current values

setProperty({ key: 'GaugeBackColor', value: WebCC.Properties.GaugeBackColor });

setProperty({ key: 'Alignment', value: WebCC.Properties.Alignment });

setProperty({ key: 'LineThickness', value: WebCC.Properties.LineThickness });

setProperty({ key: 'DivisionCount', value: WebCC.Properties.DivisionCount });

setProperty({ key: 'FontSize', value: WebCC.Properties.FontSize });

setProperty({ key: 'Zones', value: WebCC.Properties.Zones });

setProperty({ key: 'MaxValue', value: WebCC.Properties.MaxValue });

setProperty({ key: 'MinValue', value: WebCC.Properties.MinValue });

setProperty({ key: 'GaugeValue', value: WebCC.Properties.GaugeValue });

// Subscribe for value changes

WebCC.onPropertyChanged.subscribe(setProperty);

}

else {

console.log('connection failed');

}

},

// contract (see also manifest.json)

{

// Methods

methods: {

},

// Events

events: {

    },

    //Properties

    //////////

properties: defaultProperties

  },

// placeholder to include additional Unified dependencies (not used in this example) [],

// connection timeout

10000

);

### Operating the Control via WinCC

To operate the Custom Web Control via WinCC, some functions need to be implemented. The functions show an example of the use of the API object. The sequences of the functions are specific to this example, so they are not explained in detail.

### Example: Operating the Control

// Updates the value shown by the gauge whenever it is changed, e.g. by a WinCC Unified tag or script.

// This function will be called by "setProperty" whenever the contract property GaugeValue is changed.

// - value: number that contains the new value to be shown in the gauge meter. function updateValue(value) {

gauge.set(value);

const newZoneIndex = gauge.options.staticZones.indexOf(

gauge.options.staticZones.

filter(zone =&gt; zone.min &lt;= gauge.value &amp;&amp; gauge.value &lt;= zone.max).pop()

);

if (newZoneIndex != currentZoneIndex) {

currentZoneIndex = newZoneIndex;

WebCC.Events.fire('ZoneChanged', newZoneIndex);

}

}

`// Updates the alignment of the whole gauge inside the control. You can place it at the top, middle or bottom.`

`// This function will be called by "setProperty" whenever the user changes the alignment.`

`// - alignment: object that contains an enum property "Vertical" that can be either "Top", "Center" or "Bottom".`

function updateAlignment(alignment) {

  const item = document.getElementById('gauge');

  let vertVal = '0';

  let topVal = '0';

  switch (alignment.Vertical) {

    case 'Top':

      break;

    case 'Center':

      topVal = '50%';

      vertVal = '-50%';

      break;

    case 'Bottom':

      topVal = 'inherit';

      break;

  }

  item.style.top = topVal;

  item.style.transform = 'translate(0,' + vertVal + ')';

}

`// Updates the labels of the gauge. All labels have to be updated whenever the DivisionCount, MaxValue, MinValue or FontSize is changed.`

`// This function will be called by "setProperty" whenever one of those contract properties change.`

function updateLabels() {

  const labels = new Array(.Properties.DivisionCount).fill(0).map(

    (x, i) =&gt; (i + 1) * (WebCC.Properties.MaxValue - WebCC.Properties.MinValue/WebCC.Properties.DivisionCount + WebCC.Properties.MinValue

  );

  labels.unshift(WebCC.Properties.MinValue);

  gauge.setOptions({

    staticLabels: {

      font: WebCC.Properties.FontSize + 'px "Siemens Sans"',

      labels: labels

    }

  });

}

`// Paints the given zones inside the gauge. This function will be called by "setProperty" whenever a zone is changed or`

`// zones will be added or removed.`

`// - zones: array of new zones to be painted`

function updateZones(zones) {

  gauge.setOptions({

    staticZones: zones.map(item =&gt; {

      return { strokeStyle: toColor(item.StrokeColor), min: item.Min, max: item.Max };

    })

  });

}

// This is a callback function that is called every time a contract property changes. The function forwards the change to

// other functions so you can see the new value in the control.

// - data: object containing a key and a value property. The "key" contains the name of the changed contract property and the "value" contains the new value.

function setProperty(data) {

`// console.log('onPropertyChanged ' + data.key); // uncomment this line to check whether data is incoming in the browser console from WinCC Unified`

  switch (data.key) {

  case 'GaugeValue':

    updateValue(data.value);

    break;

  case 'GaugeBackColor':

    document.body.style.backgroundColor = toColor(data.value);

    break;

  case 'Alignment':

    updateAlignment(data.value);

    break;

  case 'LineThickness':

    gauge.setOptions({ lineWidth: data.value / 100 });

    break;

  case 'FontSize':

    updateLabels();

    break;

  case 'MinValue':

    gauge.setMinValue(data.value);

    updateLabels();

    break;

  case 'MaxValue':

    gauge.maxValue = data.value;

    updateLabels();

    break;

  case 'DivisionCount':

    updateLabels();

    break;

  case 'Zones':

    updateZones(data.value);

    break;

  }

}

// Let the given zone blink by descreasing and increasing the alpha value of the zone color from 0% to 100% and back to original value 2 times.

// - zoneIndex: integer as index of the zone that will blink.

function blinkZone(zoneIndex) {

const currentZone = gauge.options.staticZones[zoneIndex];

const rgba = currentZone.strokeStyle.split(',');

const originalRgba = Number(rgba[3].replace(')', ''));

let currentRgba = originalRgba;

let state = 0; // 0: falling, 1: raising, 2: falling again

let currentRound = 0;

const timerId = setInterval(() =&gt; {

switch (state) {

case 0:

currentRgba -= 0.2;

if (currentRgba &lt;= 0) {

currentRgba = 0;

state = 1;

}

break;

case 1:

currentRgba += 0.2;

if (currentRgba &gt;= 1) {

currentRgba = 1;

state = 2;

}

break;

case 2:

currentRgba -= 0.2;

if (currentRgba &lt; originalRgba) {

currentRound++;

if (currentRound &gt;= 2) {

clearInterval(timerId);

return;

} else {

currentRgba = originalRgba;

state = 0;

}

}

break;

} rgba[3] = currentRgba.toFixed(1);

currentZone.strokeStyle = rgba.join(',') + ')';

gauge.setOptions(gauge.options.staticZones);

}, 50);

}

## Creating the ZIP file (RT Unified)

To use the Custom Web Control, the hierarchy of folders and files must be compressed. The data must be available in compressed form. To create the file, you can use any application that can generate a valid file with the extension ".zip".

The name of the ZIP file must match the GUID, for example, "{551BF148-2F0D-4293-8E10-C9C3A1A6A073}.zip".

> **Note**
>
> **GUID generation**
>
> For example, a GUID can be created as follows:
>
> - In Visual Studio under "Tools &gt; Create GUID"
> - Under [https://www.guidgenerator.com/](https://www.guidgenerator.com/)

## Restrictions (RT Unified)

### Unified Comfort Panel

When you make the Custom Web Control available on a Unified Comfort Panel, note the following special features:

- The Custom Web Control is executed locally without being hosted in a web server.
- Links outside of the Custom Web Control are not supported, e.g. http links.
- The retrieval of external data or adding of contents is not supported, for example, via the "XMLHttpRequest" object or "fetch".
- Debugging of the Custom Web Control on the Unified Comfort Panel is not supported.

| ![Unified Comfort Panel](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | Tips for an efficient procedure |
| --- | --- |
| If you want to test whether your Custom Web Control can be executed on the Unified Comfort Panel, run the file "Index.html" locally on a PC without hosting the Custom Web Control in its own web server. |  |

### Rounding error

The JavaScript data type "Number" is a 64-bit floating point data type. For integer values, a secure display of up to 15 digits is possible before rounding errors occur.

Tags that use "DInt" or "Date", for example, can therefore lead to rounding errors when used in Custom Web Controls.

To avoid rounding errors, use the prototypes "Big" and "DatePrecise".

### Logic operation of complex data types

When using complex types, such as an array or user data types, only the elements of the bottom level can be linked to a property.

### Access of devices outside of the network

When the custom web control is accessed by a device outside of the network, it may not be possible to display or operate the Custom Web Control. In this case, access to the Custom Web Control depends on the network and security settings.

## Installing and using Custom Web Controls (RT Unified)

Custom Web Controls are freely-programmable and serve as a specific solution that goes beyond the functionalities of the toolbox provided. You can use Custom Web Controls like any other tool in the screens.

### Requirement

- A project has been created.
- An HMI device has been created.
- A screen has been created.

### Installing Custom Web Control

To install Custom Web Controls for a TIA Portal project, follow these steps:

1. Open the directory of your project.
2. Open the "UserFiles" subfolder.
3. Create a folder with the name "CustomControls".
4. Store the created program as *.zip file in the "CustomControls" folder.
5. In the TIA Portal, click on the ![Installing Custom Web Control](images/137628691979_DV_resource.Stream@PNG-de-DE.png) "Update" button in the "Toolbox" &gt; "My Controls" task card.

   The Custom Web Control is displayed in the "Toolbox" task card of the "Screens" editor.

### Using Custom Web Control

1. Drag the Custom Web Control from the "Toolbox" &gt; "My Controls" task card onto the screen.
2. Select the Control.
3. In the Inspector window, go to "Properties &gt; Events".
4. Configure system functions or scripts for the events used in the Control.
5. In the Inspector window, go to "Properties &gt; Properties &gt; Interface".
6. Assign static values for the interface properties or dynamize the interface properties according your requirements.

   When dynamizing with tags, note that the Control's access to the tags is "Read only" by default.

   If you want the Control to change the values of the tags, remove the check mark.
7. Compile and load the Runtime project.

## Updating Custom Web Controls (RT Unified)

### Introduction

After changing the properties for custom web controls or configuring new events, you can update custom web controls.

### Updating custom web controls

If you have changed the properties for custom web controls or configured new events, you can update the custom web controls as follows:

1. Click the Update icon ![Updating custom web controls](images/137628691979_DV_resource.Stream@PNG-de-DE.png) in the "My Controls" palette.
2. Custom web controls are updated.
3. A message appears in the Inspector window:

   - "The object '{0}' was updated successfully".
   - "The object '{0}' was updated successfully, but some properties have been lost due to incompatible changes to the interface."
   - "All objects are up to date". You have not changed any properties or alarms.
   > **Note**
   >
   > The placeholder '{0}' stands for a unique and complete path on which the custom web control is stored.

### Restrictions for the update

If you have opened a project as read-only, the update is not possible.

The following changes to the custom web control prevent the automatic update:

- Renaming properties or events
- Deleting properties or events
- Changing the data type
