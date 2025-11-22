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
                 "GMandWMT1wT2wSubjectsAge.csv": "59732288",
                 "R1BothSubjects.csv": "59732309",
                 "R1Slope.csv": "59732315",
                 "MatchedFullTermsSubjects.csv": "59732285",
                 "MatchedFulltermsTracts.csv": "59732291",
                 "MatchedPretermsAtFulltermTracts.csv": "59732294",
                 "PretermAtFulltermMatchedSubjects.csv": "59732300",
                 "MatchedPretermsTracts.csv": "59732297",
                 "PretermMatchedSubjects.csv": "59732303"}

    for kk, vv in file_dict.items():
        if not os.path.exists("inputData/" + kk):
            urllib.request.urlretrieve(figshare_url + vv, "inputData/" + kk)
