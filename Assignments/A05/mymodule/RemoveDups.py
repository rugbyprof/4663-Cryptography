def remove_dups(key):
    """ Removes duplicate letters from a given key, since they
        will break the encryption.

        Example: 
            key = 'helloworldhowareyou'
            returns 'helowrdayu'

    """
    newkey = []             # create a list for letters
    for i in key:           # loop through key
        if not i in newkey: # skip duplicates
            newkey.append(i)
    
    # create a string by joining the newkey list as a string
    return ''.join(str(x) for x in newkey)