# Email Automation with JMP and Python

Easily create emails with JMP data directly into Outlook. Get your graphs into an email report!

This is an example and template other JMP scripters can use. 

## Features
- Exports JMP graphs into images.
- Embeds graphs into Outlook draft emails automatically.
- Works with JMP 14 and above (tested).
- Compatible with Outlook desktop app (not Outlook Web).

## Requirements
- **Python 3**
- Python libraries:
  - `pywin32`
  - `Pillow`

> **Note:** JMP 18 comes with Python built in. This script was originally created before JMP 18, but you can run it directly through JMP’s Python interpreter without needing a separate Python installation.

## Setup
1. Install Python 3.
2. Install the required libraries:
   ```bash
   pip install pywin32 Pillow
3. Update the folder paths in the main.jsl

## Demo
![Demo](demo.gif)


