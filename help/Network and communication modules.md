---
title: "Network and communication modules"
package: RMSimNetenUS
topics: 3
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Network and communication modules

This section contains information on the following topics:

- [S7-CM/CP](#s7-cmcp)
- [Media converters](#media-converters)

## S7-CM/CP

### No S7 routing with CP 300/400 < V3 as router

With S7 routing between S7‑1200 or S7‑1500 stations, no connection is established when older S7‑300/400 CPs are connected in between as routers. The following types of communication that run over ISO transport or ISO-on-TCP connections are affected:

- S7 communication
- PG communication
- HMI communication

The behavior applies to S7‑300/400 CPs with a firmware version < V3.0 for which the TSAP length is limited to 2 bytes.

In contrast, like the S7‑1200/1500, S7‑300/400 CPs as of V3.0 support long TSAPs and thus also S7 routing.

## Media converters

When you migrate a project, you need to reconfigure the media converters.
