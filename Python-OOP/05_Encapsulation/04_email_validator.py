class EmailValidator:
    def __init__(self, min_lenght, mails: list, domains: list):
        self.min_lenght = min_lenght
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_lenght

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        email = email.split("@")
        mail, domain = email[1].split(".")
        name = email[0]
        return self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)
