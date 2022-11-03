import re 

def main(sentence: str) -> str:
    pattern = "([,; .])"
    list_of_words = re.split(f'{pattern}', sentence)
    cpt_list = [word.capitalize() for word in list_of_words]
    return "".join(cpt_list)

main("I don't like this excercise")
