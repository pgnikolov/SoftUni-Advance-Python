import os

def generate_report(directory):
    files_with_extensions = []

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item)
            ext = ext.lower()
            files_with_extensions.append((item, ext))

    files_with_extensions.sort(key=lambda x: (x[1], x[0]))

    report_lines = []
    current_extension = None

    for file_name, ext in files_with_extensions:
        if ext != current_extension:
            current_extension = ext
            report_lines.append(f"{current_extension}")
        report_lines.append(f"- - - {file_name}")

    report_path = os.path.join(directory, "report.txt")
    with open(report_path, 'w') as report_file:
        report_file.write("\n".join(report_lines))

    print(f"Report generated at: {report_path}")

directory_to_scan = input("Enter the directory path to scan: ")
generate_report(directory_to_scan)
