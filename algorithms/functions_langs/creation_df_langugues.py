from algorithms.functions_try.functions_try_collection import  try_except_detect


def creation_df_langugues(df):
    df_langs = df.applymap(lambda x: try_except_detect(x))
    return df_langs