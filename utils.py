import os
import urllib.request


def get_data():
    os.makedirs("figures", exist_ok=True)
    os.makedirs("inputData", exist_ok=True)
    os.makedirs("outputData", exist_ok=True)
    # Get data
    figshare_url = "https://figshare.com/ndownloader/files/"
    file_dict = {"GMandWMT1wT2ws.csv": "59732279",
                 "R1WMandGM.csv": "59732318",
                 "GMandWMT1wT2wSubjects.csv": "59732282",
                 "R1BothSubjects.csv": "59732309",
                 "R1Slope.csv": "59732315"}

    for kk, vv in file_dict.items():
        urllib.request.urlretrieve(figshare_url + vv, "inputData/" + kk)
