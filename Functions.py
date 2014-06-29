
def put(string, pos, newchar):
    # Given a string, we'd like to do the following:
    # string[pos] = newchar
    # ...its not possible so this function enables to do that.
    new = string[:pos] + newchar + string[pos + 1:]

    return new 

