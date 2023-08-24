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
        path=executable_path, 
        type_of_doc=".txt",
    )

    txt_names = list(filter(lambda x: 'chapter' in x, txt_names))
    celex_lists = {key: "" for key in range(20)}
    celex_lists_for_return = []

    for num, name in enumerate(txt_names):
        if 'general' in name:
            pattern = r"[^{}',\n\s]+"
            txt_path = executable_path + "\\" + name
            with open(txt_path, "r") as file:
                savings = [celex for celex in re.findall(pattern, file.read()) 
                    if any(character.isdigit() for character in celex)]
                celex_lists[num + 1] = pd.DataFrame(savings)
                celex_lists[num + 1]["Directory code"] = num

    celex_series = pd.concat(list(celex_lists.values())[1:])\
                        .rename(columns={0: 'CELEX_ID'})
    celex_series = celex_series.groupby('CELEX_ID')['Directory code']\
                                .agg(list).reset_index()
    return celex_series
