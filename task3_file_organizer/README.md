# Task 3: Automated File Organizer

## Overview
The Automated File Organizer is a Python command-line application that organizes files into separate folders based on their file extensions. It helps keep directories clean and makes files easier to find.

## Features
- Automatically categorizes files by extension.
- Supports images, documents, videos, audio, archives, code, spreadsheets, and presentations.
- Places unrecognized file types into an `Others` folder.
- Handles uppercase and lowercase file extensions.
- Displays a preview before organizing files.
- Requests confirmation before moving files.
- Avoids overwriting files with duplicate names by generating unique filenames.
- Handles invalid folder paths and file-moving errors.
- Leaves subfolders untouched.
- Displays a summary of successful moves and errors.

## Technologies Used
- Python
- `pathlib` — path and folder handling
- `shutil` — moving files

## Requirements
- Python 3.10 or later
- A terminal or command prompt

No external Python packages are required.

## Project Structure

```text
task3_file_organizer/
├── main.py
├── README.md
└── TEST_REPORT.md
```

## How to Run

1. Open the project folder in VS Code.
2. Open a terminal in `task3_file_organizer`.
3. Run:

```bash
python main.py
```

4. Enter the full path of the folder you want to organize.
5. Review the preview.
6. Enter `yes` to proceed or `no` to cancel.

## File Categories

| Category | Examples |
|---|---|
| Images | JPG, JPEG, PNG, GIF, SVG |
| Documents | PDF, DOCX, TXT, RTF |
| Videos | MP4, MKV, AVI, MOV |
| Audio | MP3, WAV, AAC, FLAC |
| Archives | ZIP, RAR, 7Z, TAR |
| Code | PY, JS, HTML, CSS, JAVA, SQL |
| Spreadsheets | XLSX, XLS, CSV |
| Presentations | PPTX, PPT, ODP |
| Others | Unsupported or unrecognized extensions |

## Safety Notes
- Test the program on a sample folder before using it on important files.
- Review the preview before confirming.
- The program moves files rather than copying them.
- Files inside subfolders are not processed recursively.

## Learning Outcomes
This project demonstrates Python functions, dictionaries, sets, loops, conditional statements, path handling, exception handling, user input validation, and file operations.

## Internship
Developed as part of the Datheon Python Programming Internship.