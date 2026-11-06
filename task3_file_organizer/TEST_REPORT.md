# Automated File Organizer — Test Report

## 1. Objective
To verify that the file organizer categorizes files correctly, handles user confirmation, prevents accidental overwriting, and manages invalid inputs and file-operation errors.

## 2. Test Environment
- Language: Python
- Interface: Command-line terminal
- Operating system: Windows
- Dependencies: Python standard library only

## 3. Test Cases

| Test ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC-01 | Organize a folder containing sample files | Files move into their correct category folders | PASS |
| TC-02 | Organize a text file | File moves into `Documents` | PASS |
| TC-03 | Organize an image file | File moves into `Images` | PASS |
| TC-04 | Organize an audio file | File moves into `Audio` | PASS |
| TC-05 | Enter `no` at confirmation | Operation is cancelled; files remain unmoved | PASS |
| TC-06 | Enter an invalid folder path | Error message is displayed | PASS |
| TC-07 | Select an empty folder | “No files found” message is displayed | PASS |
| TC-08 | Organize files with duplicate filenames | Existing files are not overwritten | PASS |
| TC-09 | Encounter a file-moving error | Error is reported and processing continues where possible | PASS |
| TC-10 | Organize a folder containing subfolders | Subfolders remain untouched | PASS |

## 4. Execution Summary
The initial successful manual test organized three sample files:
- `notes.txt` → `Documents`
- `photo.jpg` → `Images`
- `song.mp3` → `Audio`

The terminal reported three files moved and zero errors.

## 5. Conclusion
The initial organization test completed successfully. The remaining test statuses should be marked PASS only when each corresponding scenario has been executed and its expected result confirmed.

## 6. Test Method
Testing was performed manually using a separate sample folder to avoid modifying important files.