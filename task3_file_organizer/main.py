
from pathlib import Path
import shutil


# File extensions and their destination folders
FILE_CATEGORIES = {
    "Images": {
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"
    },
    "Documents": {
        ".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"
    },
    "Videos": {
        ".mp4", ".mkv", ".mov", ".avi", ".webm"
    },
    "Audio": {
        ".mp3", ".wav", ".aac", ".flac", ".ogg"
    },
    "Archives": {
        ".zip", ".rar", ".7z", ".tar", ".gz"
    },
    "Code": {
        ".py", ".js", ".html", ".css", ".java", ".cpp",
        ".c", ".php", ".sql", ".json"
    },
    "Spreadsheets": {
        ".xls", ".xlsx", ".csv", ".ods"
    },
    "Presentations": {
        ".ppt", ".pptx", ".odp"
    },
}


def get_category(file_path):
    """Return the category for a file based on its extension."""
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_destination(destination):
    """Avoid overwriting an existing file."""
    if not destination.exists():
        return destination

    parent = destination.parent
    stem = destination.stem
    suffix = destination.suffix
    counter = 1

    while True:
        new_destination = parent / f"{stem}_{counter}{suffix}"

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_files(folder_path):
    """Preview and organize files in the selected folder."""
    folder = Path(folder_path).expanduser().resolve()

    if not folder.exists() or not folder.is_dir():
        print("Error: The folder path is invalid.")
        return

    # Only process files directly inside the selected folder.
    files = [
        item for item in folder.iterdir()
        if item.is_file()
    ]

    if not files:
        print("No files found in the selected folder.")
        return

    # Create a plan without moving files yet.
    plan = []

    for file_path in files:
        category = get_category(file_path)
        destination_folder = folder / category
        destination_file = get_unique_destination(
            destination_folder / file_path.name
        )

        plan.append((file_path, destination_folder, destination_file))

    print("\n=== File Organizer Preview ===")

    for source, destination_folder, destination_file in plan:
        print(f"{source.name} -> {destination_folder.name}/"
              f"{destination_file.name}")

    confirmation = input(
        "\nProceed with organizing these files? (yes/no): "
    ).strip().lower()

    if confirmation not in {"yes", "y"}:
        print("Operation cancelled. No files were moved.")
        return

    moved_count = 0
    error_count = 0

    for source, destination_folder, destination_file in plan:
        try:
            destination_folder.mkdir(parents=True, exist_ok=True)

            # Recheck in case a destination appeared after the preview.
            destination_file = get_unique_destination(destination_file)

            shutil.move(str(source), str(destination_file))
            print(f"Moved: {source.name} -> {destination_folder.name}/")
            moved_count += 1

        except OSError as error:
            print(f"Could not move {source.name}: {error}")
            error_count += 1

    print("\n=== Organization Summary ===")
    print(f"Files moved: {moved_count}")
    print(f"Errors: {error_count}")
    print("Organization process finished.")


def main():
    """Get the folder path and start the organizer."""
    print("=== Automated File Organizer ===")
    print("Enter the path of the folder you want to organize.")

    folder_path = input("Folder path: ").strip().strip('"')

    if not folder_path:
        print("Error: Folder path cannot be empty.")
        return

    organize_files(folder_path)


if __name__ == "__main__":
    main()
