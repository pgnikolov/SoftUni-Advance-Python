string_ = [char for char in (input())]

rev_string = [string_.pop() for i in range(len(string_))]
print("".join(rev_string))
