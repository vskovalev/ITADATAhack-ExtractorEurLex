from algorithms.functions_try.functions_try_collection import try_except_lower, try_except_get


def comparison_laguagues_celexes_docs(df, df_langs):
    list_of_indexes_false_comparison = []
    for index, left_right in enumerate(zip(
                    df['CELEX_ID'].str.split('_')
                            .apply(lambda x: 
                                try_except_lower(
                                    try_except_get(x, 2)))
                            .to_list(), 
                    df_langs['DOC_CONTENT'].to_list())):
        left, right = left_right
        if left != right:
            list_of_indexes_false_comparison.append(index)
    return list_of_indexes_false_comparison
