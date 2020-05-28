def httpcheck(domain):
    if domain.startswith("http"):
        return domain
    else:
        domain =  "http://" + domain
        return domain

# site = 'https://cloud9sheesha.com'
# site = httpcheck(site)

# print(site)