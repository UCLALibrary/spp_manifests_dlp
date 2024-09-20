import pandas as pd, json, sys

path_to_csv = sys.argv[1]#input("Enter path to csv containing file names to remove: ")
path_to_manifests = sys.argv[2]#input("Enter path to folder containing manifests: ")

# import filenames to delete
df = pd.read_csv(f"{path_to_csv}")

# create new column for 
df["Status"] = ""

# create list of unique manifest files
manifest_files = df["Manifest_File"].drop_duplicates()



# iterate over manifest files and remove item if label name is in list of files to delete
for row in manifest_files:
    path_to_file = f"{path_to_manifests}/{row}"
    files_to_remove = df.loc[df["Manifest_File"] == row]["File_name_cleanup"]
    with open(path_to_file, 'r') as f:
        j = json.load(f)

    with open(path_to_file, 'w') as f:
        for canvas in j["sequences"][0]["canvases"]:
            items = canvas["images"][0]["resource"]["item"]
            for i in reversed(range(len(items)-1)):
                label = items[i]["label"]
                if (label in files_to_remove.values):
                    del items[i]
                    row_index = df.query("Manifest_File == @row and File_name_cleanup == @label").index[0]
                    df.loc[row_index, "Status"] = "Success"
        # save file
        json.dump(j, f, indent=2, separators=(',', ' : '))

df.to_csv("csv/file_names_to_remove.csv", index = False)