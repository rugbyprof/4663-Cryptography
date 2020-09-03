import sys

class AdfgxLookup:
    def __init__(self,k=None):
        self.key = self.remove_duplicates(k)

        self.alphabet = [chr(x+97) for x in range(26)]
        self.adfgx = ['A','D','F','G','X']
        self.keylen = 0

        if self.key:
            self.keylen = len(self.key)

        self.polybius = None
        self.lookup = None

    def remove_duplicates(self,key):
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
       

    def build_polybius_string(self,key=None):
        """Builds a string consisting of a keyword + the remaining
           letters of the alphabet. 
           Example:
                key = 'superbatzy'
                polybius = 'superbatzycdfghiklmnoqvwx'
        """
        # no key passed in, used one from constructor
        if key != None:
            self.key = self.remove_duplicates(key)

        # NO key!
        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # key exists ... continue
        self.keylen = len(self.key)

        # prime polybius_string variable with key
        self.polybius = self.key

        for l in self.alphabet:
            if l == 'j':        # no j needed!
                continue
            if not l in self.key:    # if letter not in key, add it
                self.polybius += l
        return self.polybius

    def build_polybius_lookup(self,key=None):
        """ Builds a lookup dictionary so we can get the two letter pairs for each
            polybius letter. 
            Example:
                key = superbatzy
                polybius = superbatzycdfghiklmnoqvwx
                lookup = 
                {'a': 'DD',
                'b': 'DA',
                'c': 'FA',
                'd': 'FD',
                'e': 'AG',
                'f': 'FF',
                'g': 'FG',
                'h': 'FX',
                'i': 'GA',
                'k': 'GD',
                'l': 'GF',
                'm': 'GG',
                'n': 'GX',
                'o': 'XA',
                'p': 'AF',
                'q': 'XD',
                'r': 'AX',
                's': 'AA',
                't': 'DF',
                'u': 'AD',
                'v': 'XF',
                'w': 'XG',
                'x': 'XX',
                'y': 'DX',
                'z': 'DG'}
        """
        if key != None:
            self.key = self.remove_duplicates(key)

        # NO key!
        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # no polybius built, make one!
        if self.polybius == None:
            self.build_polybius_string()

        # init our dictionary
        self.lookup = {}            # dict as our adfgx reverse lookup
        for l in self.polybius:     # loop through the 1D matrix we created
            self.lookup[l] = ''     # init keys in the dictionary

        row = 0 
        col = 0

        # loop through the polybius 1D string and get the 2 letter pairs
        # needed to do the initial encryption
        for row in range(5):
            for col in range(5):
                i = (5 * row) + col
                self.lookup[self.polybius[i]] = self.adfgx[row]+self.adfgx[col]

        return self.lookup


    def sanity_check(self):
        """ This method lets you look at an actual "matrix" that you built using 
            a keyword. 
            Example: 
                key = 'superbatzy'
                output = 
                      A D F G X 
                    A s u p e r 
                    D b a t z y 
                    F c d f g h 
                    G i k l m n 
                    X o q v w x 
        """

        if not self.key:
            print("Error: There is NO key defined to assist with building of the matrix")
            sys.exit(0)

        # no polybius built, make one!
        if self.polybius == None:
            self.build_polybius_string()

        row = 0
        col = 0
       
        sys.stdout.write('\n  ')
        for l in self.adfgx:
            sys.stdout.write(l+' ')
        sys.stdout.write('\n')
        for l in self.adfgx:
            sys.stdout.write(l+' ')
            for ll in self.adfgx:
                i = (5 * row) + col
                sys.stdout.write(self.polybius[i]+' ')
                col += 1
            row += 1
            col = 0
            sys.stdout.write("\n")

