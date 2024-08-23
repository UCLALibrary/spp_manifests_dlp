import pandas as pd, json, sys, numpy as np, os

df = pd.read_csv("csv/file_names_to_remove.csv")
df["Status"] = ""
manifest_files = df["Manifest_File"].drop_duplicates()

for row in manifest_files[0:2]:
    path_to_file = f"{row}"
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
        # you would replace the following line with saving the file using the same file name
        json.dump(j, f, indent=2, separators=(',', ' : '))

df.to_csv("csv/file_names_to_remove.csv", index = False)