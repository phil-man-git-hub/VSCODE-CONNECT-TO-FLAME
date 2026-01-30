# Insight: Listing Backburner Wiretap Servers

This document explains the naming rules for Wiretap servers and how to find them on your network.

**Target Audience:** Novice technical artists interested in network identification.

---

## 1. The Naming Formula

Every Wiretap server ID is made of two parts joined by a colon:
**`Hostname : DatabaseType`**

- **`Hostname`**: The name of the computer (e.g., `workstation01`).
- **`DatabaseType`**: The "Language" it speaks. For background rendering, this is always **`Backburner`**.

**Example:** `workstation01:Backburner`

---

## 2. Searching the Network

You don't have to guess which machines are running Backburner. You can use the `wiretap_server_dump` command to "Scan" the network for specific types of servers:

`wiretap_server_dump -d Backburner`

This will return a list of every machine ready to receive render jobs.

---

## 3. Testing the Connection

If you want to see if your own computer is ready, you can use the "Loopback" address:

`wiretap_ping -h localhost:Backburner`

---

## 4. Key Takeaway for Beginners

Think of the Wiretap ID as a **Radio Station**. The `Hostname` is the frequency, and the `DatabaseType` is the station name. By using the `-d Backburner` flag, you are tuning your radio to only hear the rendering stations on your network.
