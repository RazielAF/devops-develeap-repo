import re


def main(sentence):
    if sentence.strip() == "": return ""
    list_of_words = re.findall(r"[\w]+|[,.;:'(){}!?]", sentence)
    return max(list_of_words, key=len)
