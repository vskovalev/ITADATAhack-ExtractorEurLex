from langdetect import detect


def try_except_detect(text):
    try:
        return detect(text)
    except:
        return None


def try_except_get(listik, index):
    try:
        return listik[index]
    except:
        return None


def try_except_lower(text):
    try:
        return text.lower()
    except:
        return None
