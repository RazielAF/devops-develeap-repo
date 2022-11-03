def main(input):
    letters = list(input)
    result = []
    i = 0
    for letter in letters:
        i += 1
        part = letter*i
        result.append(part.capitalize())
    return "-".join(result)


