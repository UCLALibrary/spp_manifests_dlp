# spp_manifests_dlp

This script takes a list of files and folder of json manifests and removes those file names from the manifest files


### Set up
**Requirements**
- python3.6
- pandas
- numpy

### Usage

```python
python3 remove_from_manifests.py
```

The script will then prompt you for the path to the csv file containing filenames to remove and the path to the folder containing manifests

```python
Enter path to csv containing file names to remove: /path/to/file.csv
Enter path to folder containing manifests: /path/to/folder
```

