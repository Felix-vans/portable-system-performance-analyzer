# Obsolete Software Detection Tool

## Overview

This program scans a Windows system to identify potentially obsolete software based on disk usage, installation date, and estimated size.  
It does not uninstall programs — it only lists candidates for manual review.

---

## How It Works

### 1. Disk Usage Check
The program checks how much of the `C:` drive is used.

- If usage is below 50%, the user is informed cleanup is not necessary.
- The user can still choose to continue.
- If usage is 50% or higher, the scan proceeds automatically.

---

### 2. Collect Installed Programs
Installed programs are retrieved from Windows Registry uninstall keys:

- `HKEY_LOCAL_MACHINE\...\Uninstall`
- `HKEY_LOCAL_MACHINE\...\WOW6432Node\...\Uninstall`
- `HKEY_CURRENT_USER\...\Uninstall`

For each program, the tool attempts to collect:
- `DisplayName`
- `EstimatedSize` (KB)
- `InstallDate` (`YYYYMMDD`)

Programs without a name or valid install date are skipped.  
Missing size values default to `0`.

---

### 3. Scoring System

For each program, the following is calculated:

- **Size (MB)**
- **Age (days since installation)**
- **Remove Score = age_days × size_mb**

Programs are sorted by remove score (highest first).  
The top 30 candidates are displayed in a table.

---

## Limitations

- Registry data is often incomplete.
- `EstimatedSize` can be inaccurate (especially for games).
- Microsoft Store apps and portable software may not be detected.
- Not all installed applications are stored in the scanned registry keys.

This tool provides estimates, not exact disk analysis.

---

## Safety Note

Only remove software you recognize and understand.  
Deleting essential programs or drivers may cause system instability.

---

## Possible Improvements

- Detect Microsoft Store apps.
- Calculate real disk usage instead of using `EstimatedSize`.
- Identify automatically installed or bundled software.
- Improve the scoring algorithm.
