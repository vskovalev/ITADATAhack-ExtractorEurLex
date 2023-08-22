import re
import pandas as pd
from functions.functions_os.names_extractor_from_folder_by_type import \
    names_extractor_from_folder_by_type


def get_list_of_celexes():
    executable_path = ".\\files\\txts"
    txt_names = names_extractor_from_folder_by_type(
        path=executable_path, type_of_doc=".txt"
    )
    celex_lists = {key: "" for key in range(1, 21)}
    celex_lists_for_return = []

    for num, name in enumerate(txt_names):
        pattern = r"[^{}',\n\s]+"
        txt_path = executable_path + "\\" + name
        with open(txt_path, "r") as file:
            celex_lists_for_return.append(re.findall(pattern, file.read()))
    return celex_lists_for_return


def get_seria_of_celexes():
    executable_path = ".\\files\\txts"
    txt_names = names_extractor_from_folder_by_type(
        path=executable_path, type_of_doc=".txt"
    )
    celex_lists = {key: "" for key in range(1, 21)}
    celex_lists_for_return = []

    for num, name in enumerate(txt_names):
        pattern = r"[^{}',\n\s]+"
        txt_path = executable_path + "\\" + name
        with open(txt_path, "r") as file:
            celex_lists[num + 1] = pd.DataFrame(re.findall(pattern, file.read()))
            celex_lists[num + 1].columns = ["CELEX_ID"]
            celex_lists[num + 1]["Directory code"] = num + 1

    celex_series = pd.concat(celex_lists.values())
    return celex_series
