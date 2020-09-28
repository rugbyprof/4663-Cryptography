import sys
import os
import requests

alphabet = [chr(x+97) for x in range(26)]

typical_frequency = {
    "a": 8.167,
    "b": 1.492,
    "c": 2.782,
    "d": 4.253,
    "e": 12.702,
    "f": 2.228,
    "g": 2.015,
    "h": 6.094,
    "i": 6.966,
    "j": 0.153,
    "k": 0.772,
    "l": 4.025,
    "m": 2.406,
    "n": 6.749,
    "o": 7.507,
    "p": 1.929,
    "q": 0.095,
    "r": 5.987,
    "s": 6.327,
    "t": 9.056,
    "u": 2.758,
    "v": 0.978,
    "w": 2.360,
    "x": 0.150,
    "y": 1.974,
    "z": 0.074
}

class frequency():
    def __init__(self):
        self.text = ""
        self.freq = {}
        self.freq_percent = {}
        self.sort_freq = None

        for l in alphabet:
            self.freq[l] = 0
            self.freq_percent[l] = 0
    
    def typical(self):
        return typical_frequency
    
    def count(self,text):
        for l in text:
            l = l.lower()
            if l in alphabet:
                self.freq[l] += 1

        for k in self.freq_percent:
            self.freq_percent[k] = round(self.freq[k] / len(text),2)
        
        # https://realpython.com/python-lambda/
        self.sort_freq = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)

    def print(self):
        if self.sort_freq:
            for f in self.sort_freq:
                print(f"{f[0]}:{f[1]}")
        else:
            print(self.freq)

    def getNth(self,n):
        if self.sort_freq:
            return self.sort_freq[n][0]

        return None

if __name__=='__main__':
    url = "https://www.gutenberg.org/files/2701/2701-0.txt"
    #url = "https://www.gutenberg.org/files/2600/2600-0.txt"
    print("Downloading book ...")
    f = requests.get(url)
    text = f.text


    print("Calculating frequency...")
    F = frequency()

    F.count(text)

    F.print()

    print(F.getNth(2))

