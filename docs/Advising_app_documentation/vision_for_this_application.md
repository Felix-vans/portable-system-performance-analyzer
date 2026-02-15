# Application 3: Performance Assistant

## Overview

Application 3 is designed to help users improve their computer's performance by giving clear, actionable advice. It is a command-line interface (CLI) tool that analyzes data collected by Application 2 and guides the user on how to fix issues that slow down their device.  

The main goal is to make the computer faster **safely** without requiring the user to have IT knowledge.

---

## Target Users

- Gamers and casual PC users
- Users who want better performance without figuring out technical settings
- Users who prefer clear guidance rather than automatic changes

---

## Key Design Decisions

1. **Safety First**
   - No automatic registry changes or program deletions.
   - Security is non-negotiable. Any performance improvements that may reduce security are optional and fully explained.

2. **Guidance over Automation**
   - The assistant shows users **what to do** and **how to do it**.
   - Users maintain control over their system.

3. **Portable**
   - Runs from a USB drive with no installation needed.
   - Minimal dependencies to keep it easy to use on any PC.

4. **User-Friendly CLI**
   - Text is organized in clear sections.
   - Color-coded recommendations (green = safe, yellow = optional, red = caution).
   - Numbered steps and simple commands to open settings or tools directly.

---

## How It Works

1. Application 2 collects performance data from the system.
2. Application 3 analyzes this data and identifies issues such as:
   - High CPU or memory usage at startup
   - Unnecessary programs taking up space
   - Settings that can be optimized for performance
3. The assistant presents recommendations to the user:
   - Each recommendation explains **what the issue is** and **why fixing it improves performance**.
   - Optional “risky” changes are clearly flagged with the risks explained.
4. Users can follow the guidance to make the changes manually, or open the corresponding Windows settings directly from the CLI.

---

## Prototype Scope

For the first version, the focus is on:

- Clear, readable output
- Basic color coding for recommendations
- Step-by-step guidance
- No automatic system changes

Future versions may include:

- Tracking improvements over time
- More advanced recommendations
- Optional guided automation for experienced users

---

## Why This Approach

- Keeps the tool **safe and reliable**, which is important for my portfolio and career in cybersecurity.
- Provides **value to non-technical users** without overwhelming them.
- Allows gradual improvements while maintaining user trust and system integrity.

---

## Summary

Application 3 is a portable, CLI-based performance assistant that acts as a guide, not an automated optimizer. It prioritizes safety and clarity, helping users speed up their PC while keeping control in their hands.
