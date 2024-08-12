title = input()

ntit = title.replace(" ", "_")
ntit = ntit.replace(".", "")
ntit = ntit.replace(",", "")
ntit = ntit.replace("'", "")
ntit = ntit.lower()

print(ntit)
