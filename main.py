import os


def print_profile_nodes_and_inodes(folder_path):
    directory_list = []
    file_list = []

    # Recursive function to traverse through directories
    def traverse_directory(directory):
        for entry in os.scandir(directory):
            if entry.is_file():
                # Store file name, inode in file_list
                file_list.append({
                    "Name": entry.name,
                    "Inode": entry.inode()
                })
            elif entry.is_dir():
                # Store directory name and inode in directory_list
                directory_list.append({
                    "Name": entry.name,
                    "Inode": entry.inode()
                })
                traverse_directory(entry.path)

    # Call the recursive function for the provided folder
    traverse_directory(folder_path)

    # Print directory information
    print(f"Profile node and inodes for folder: {folder_path}")
    print("-----------------------------------------------------")
    for directory in directory_list:
        print(f"Directory name: {directory['Name']}      Inode: {directory['Inode']}")
    for file in file_list:
        print(f"Directory name: {file['Name']}      Inode: {file['Inode']}")


# Get folder path from user
folder_path = input("Enter the folder path: ")

# Call the function
print_profile_nodes_and_inodes(folder_path)
