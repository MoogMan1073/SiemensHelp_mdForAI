---
title: "Migrating WinCC projects"
package: MigrationWCCPenUS
topics: 6
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Migrating WinCC projects

This section contains information on the following topics:

- [Migrating WinCC flexible 2008 projects](#migrating-wincc-flexible-2008-projects)
- [Migrating WinCC V7 projects](#migrating-wincc-v7-projects)
- [Log files](#log-files)

## Migrating WinCC flexible 2008 projects

This section contains information on the following topics:

- [Migration (WinCC flexible)](#migration-wincc-flexible)

### Migration (WinCC flexible)

#### Migrating projects from WinCC flexible

Migrating projects from WinCC flexible is not supported.

## Migrating WinCC V7 projects

This section contains information on the following topics:

- [Migration (WinCC V7)](#migration-wincc-v7)

### Migration (WinCC V7)

#### Projects from WinCC V7

Migrating projects from WinCC V7 is not supported.

## Log files

Windows 11 does not allow you to directly open log files in XML format, such as the results of a migration.

Instead, the files must be opened in a text editor and manually searched for messages.

### Workaround:

To open local files in the Chrome browser:

1. Enter "cmd" in the search field of the taskbar.

   The Windows command line input opens.
2. Go to the Chrome installation folder,

   e.g. `cd C:\Users\your-user-name\AppData\Local\Google\Chrome\Application`.
3. Enter the following command:

   `chrome.exe --allow-file-access-from-files`
4. Press "Enter".

To open local files in the Edge browser:

- In the Internet options, under "Security &gt; Local intranet &gt; Sites &gt; Advanced", specify the local file path.
- In the browser, under "Settings &gt; Downloads", specify the types of files to be opened automatically after downloading.
