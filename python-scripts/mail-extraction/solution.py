import re

def main(txt):
    emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', txt)
    data = {}
    sorted_emails = []
    sorted_domains = []
    results = []
    for email in emails:
        email = email.lower()
        user, domain = email.split("@")
        try:
            data[domain].append(email)
        except KeyError:
            data[domain] = [email] 
        sorted_domains = [v for _, v in sorted(data.items(), key=lambda x: x[0])]
    for domain in sorted_domains:
        domain = list(set(domain))

        domain.sort()
        sorted_emails.append(domain)
    results = sum(sorted_emails, [])
    return results

main("chalie@microsoft.com ANCY@microsoft.com ancy@microsoft.com dan@netex.co.il chris@yahoo.com")