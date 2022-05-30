import re

def email_parse(email):
    valid = re.match(r'\w+\@\w+\.\w+', email)
    if valid:
        pars = re.split(r'@', email)
        print({'username': pars[0], 'domain': pars[1]})
    else:
        raise ValueError(f'Incorrect email: {email}')

email_parse('fghfgh@mail.rurur')
email_parse('rt56yrt65y@google.com')
email_parse('hihihih@fro..mru')
