import os

# Function to create sub-folders based on language names
def create_subfolders(folder_path):
    # Get the list of all text files in the specified folder path
    files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

    # Iterate over the files and create sub-folders for each language
    for file in files:
        # Extract the language name from the file name
        language = file.split('-')[0]

        # Create the sub-folder if it doesn't exist
        if not os.path.exists(language):
            os.mkdir(language)

        # Move the file to the corresponding sub-folder
        source = os.path.join(folder_path, file)
        destination = os.path.join(language, file)
        os.rename(source, destination)

# Specify the folder path that contains the text files
folder_path = './one-k-files/files'

# Call the function to create sub-folders
create_subfolders(folder_path)
