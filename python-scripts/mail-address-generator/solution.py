import re

def email_generator(first_name, last_name, id):
    full_name = [first_name, last_name]
    if id < 2:
        email = f'{".".join(full_name)}@company.com'
    else: 
        email = f'{".".join(full_name)}{id}@company.com'
    return email

def main(names):
    names = names.split(',')
    emails = []
    regex = re.compile('[^a-zA-Z]')

    for full_name in names:
        fullsname = re.sub(' +', ' ', full_name).split()
        name = full_name.lstrip().rstrip()
        processed_name = [regex.sub('', name.lower()) for name in fullsname]
        duplicate = True
        id = 1
        while duplicate:
            email = email_generator(processed_name[0], processed_name[-1], id)
            if not list(filter(lambda x: x[1] == email, emails)):
                duplicate = False
            id += 1
        emails.append((name, email))

    return emails

print(main("   Maciej   Krzysztof   Groszyk   "))