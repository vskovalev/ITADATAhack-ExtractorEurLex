import os


def names_extractor_from_folder_by_type(*,
                                        path='./files/',
                                        type_of_doc='.pdf') -> list:
    '''Getter of files names from directory'''
    new_list_of_files_names = \
        [file_in_path for file_in_path in os.listdir(path)]
    return [
        name for name in new_list_of_files_names
        if (name.endswith(type_of_doc) or name.endswith(type_of_doc.upper()))
    ]