import pandas as pd, json, sys, numpy as np, os

df = pd.read_csv("csv/file_names_to_remove.csv")
df["Status"] = ""
manifest_files = df["Manifest File"].drop_duplicates()

for row in manifest_files:
    path_to_file = f"manifest-files/{row}"
    files_to_remove = df.loc[df["Manifest File"] == row]["File name cleanup"]

    with open(path_to_file, 'r') as f:
        j = json.load(f)

    with open(path_to_file, 'w') as f:
        for canvas in j["sequences"][0]["canvases"]:
            items = canvas["images"][0]["resource"]["item"]
            for i in range(len(items)-1):
                if (items[i]["label"] in files_to_remove):
                    del items[i]
                    print(df.loc[(df["Manifest File"] == row) & (df["File name cleanup"] == items[i]["label"])])
        # you would replace the following line with saving the file using the same file name
        json.dump(j, f, indent=2)

df.to_csv("csv/file_names_to_remove.csv", index = False)