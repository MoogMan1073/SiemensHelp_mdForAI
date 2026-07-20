---
title: "Additional information"
package: TSNenUS
topics: 5
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Additional information

This section contains information on the following topics:

- [CloudConnect](#cloudconnect)

## CloudConnect

This section contains information on the following topics:

- [Permitted Characters](#permitted-characters)
- [Onboarding in MindConnect IoT Extension](#onboarding-in-mindconnect-iot-extension)
- [JSON escape sequences](#json-escape-sequences)

### Permitted Characters

#### Characters not allowed for names

The following characters are not permitted for names:

- 0x22 (")

  Quotation marks are generally not permitted.
- 0x20 (SP)

  Spaces are allowed within most names. Exception: CloudConnect data point

  Leading and trailing spaces are automatically deleted.

#### Permitted characters

See below for ASCII character sets.

| Parameter | Characters | Number of characters |
| --- | --- | --- |
| Name of:  - DB variable ***** | Permitted characters:  - Standard characters (numbers, letters) - Special characters 0x21 .. 0x7E - Special characters ≥ 0x80 |  |
| CloudConnect *****  - Data point name | Permitted characters:  - Standard characters (numbers, letters) - Special characters ≥ 0x80 - Special characters 0x21 .. 0x60 with exceptions   The following are not permitted:  - Space - ! / . < > ^ \ # ! & = { } - Tabs   The following strings are also not permitted:  - PUBLISH_TIMESTAMP - DATAPOINT_ARRAY - GROUP |  |
| CloudConnect *****  - Topic name   (does not apply to Group) | Permitted characters:  - Standard characters (numbers, letters) - Special characters ≥ 0x80 - Special characters 0x21 .. 0x7E with exceptions   The following are not permitted:  - # + /  - $ as first character in the name |  |
| CloudConnect *****  - Device name | Permitted characters:  - Standard characters (numbers, letters) - Special characters ≥ 0x80 - Special characters 0x60 - Special characters 0x21 .. 0x7E with exceptions   The following are not permitted:  - " ' / | 1 ... 128 |
| Name of:  - NTP server - Host - S7 station, CPU, CP | Permitted characters according to RFC1035 and RFC1123:  - Standard characters (numbers, letters)   No station names with digits only - 0x2D ( - ) .. 0x2E ( . ) |  |
| User names, passwords | Permitted characters:  - Standard characters (numbers, letters) - Following special characters:   - 0x2D ( - )   - 0x2E ( . )   - 0x40 ( @ )   - 0x5F ( _ ) |  |
| ***** Cloud messages in JSON format: The escape sequences of the JSON standard apply to special characters in station names, topic names and data point names. |  |  |

#### ASCII character sets

The ASCII characters are listed with their hexadecimal code and the corresponding characters.

**Standard characters**

- **0x30 .. 0x39**

  0 1 2 3 4 5 6 7 8 9
- **0x41 .. 0x5A**

  A B C D E F G H I J KL M N O P Q R S T U V W X Y Z
- **0x61 .. 0x7A**

  a b c d e f g h i j k l m n o p q r s t u v w x y z

**Special characters < 0x80**

- **0x21 .. 0x2F**

  ! " # $ % & ' ( ) * + , - . /
- **0x3A .. 0x40**

  : ; < = > ? @
- **0x5B .. 0x60**

  [ \ ] ^ _ `
- **0x7B .. 0x7E**

  { | } ~

**Special characters ≥ 0x80 (ISO/IEC 8859‑1)**

- **0x80, 0x82 .. 0x89, 0x8A .. 0x8C, 0x8E, 0x91 .. 0x9C, 0x9E .. 0x9F**

  € , ƒ „ … † ‡ ˆ ‰ Š ‹ Œ Ž ‘ ’ “ ” • – — ˜ ™ š › œ ž Ÿ
- **0xA1 .. 0xAC, 0xAE .. 0xB5, 0xB8 ..0xBF**

  ¡ ¢ £ ¤ ¥ ¦ § ¨ © ª « ¬ - ® ¯ ° ± ² ³ ´ μ ¸ ¹ º » ¼ ½ ¾ ¿
- **0xC0 .. 0xFF**

  À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß à á â ã ä å æ ç è é ê ë ì í î ï ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ ÿ

### Onboarding in MindConnect IoT Extension

#### Device parameters

With a connection to Siemens MindSphere ‑ MindConnect IoT Extension, two parameters are used to identify your device during the Onboarding process once the connection is established between the device and MindConnect IoT Extension.

- **Device Name**

  The CP is registered with the Onboarding process under this name.

  The Device name is displayed in MindConnect IoT Extension at the following location:  
  Device > Device profile > "NAME"

  You assign the name in the parameter group "Security > CloudConnect > General" of the CP.

  The default name is composed as follows:  
  <PLC name>.<CP name>

  Impermissible characters are deleted from the components of the name. Note the rules for assigning names, see [Permitted Characters](#permitted-characters).
- **Device Type**

  The parameter cannot be configured and is permanently set with the following string:

  - c8y_MQTTDevice

  The parameter is required in MindConnect IoT Extension to determine the device type.

  The Device type is displayed in MindConnect IoT Extension at the following location:  
  Device > Device profile > "Type"

You can find additional information on setting up the IoT Extension on the Internet at:  
[Link:](https://support.industry.siemens.com/cs/ww/en/ps/15248)

### JSON escape sequences

#### JSON escape sequences

When using the JSON format for the payload, the following characters are converted into escape sequences by the CP as a publisher.

With the CP as a subscriber, the escape sequences are converted in the reverse direction.

| Characters | JSON escape sequence | Note |
| --- | --- | --- |
| \n | \\n | New line ***** |
| \r | \\r | Line break ***** |
| \t | \\t | Tab ***** |
| \" | \\" | Quotation marks |
| \\ | \\\\ | Double backslash |
| \u0000 | \\u0000 |  |
| \u0001 | \\u0001 |  |
| \u0002 | \\u0002 |  |
| \u0003 | \\u0003 |  |
| \u0004 | \\u0004 |  |
| \u0005 | \\u0005 |  |
| \u0006 | \\u0006 |  |
| \u0007 | \\u0007 |  |
| \b | \\u0008 |  |
| \t | \\u0009 |  |
| \n | \\u000A |  |
| \u000b | \\u000B |  |
| \f" | \\u000C |  |
| \r | \\u000D |  |
| \\u000e | \\u000E |  |
| \u000f | \\u000f |  |
| \u0010 | \\u0010 |  |
| \u0011 | \\u0011 |  |
| \u0012 | \\u0012 |  |
| \u0013 | \\u0013 |  |
| \u0014 | \\u0014 |  |
| \u0015 | \\u0015 |  |
| \u0016 | \\u0016 |  |
| \u0017 | \\u0017 |  |
| \u0018 | \\u0018 |  |
| \u0019 | \\u0019 |  |
| \u001a | \\u001a |  |
| \u001b | \\u001b |  |
| \u001c | \\u001c |  |
| \u001d | \\u001d |  |
| \u001e | \\u001e |  |
| \u001f | \\u001f |  |
| \u007F | \\u007F |  |
| ***** Not configurable in STEP 7 as name component |  |  |
