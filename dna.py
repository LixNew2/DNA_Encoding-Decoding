"""
    DNA     |   Binary
------------|-----------
     A      |     00
     T      |     11
     C      |     01
     G      |     10

Convert Hello World (Text -> Binary -> DNA): 
    
    - Text Seq :    Hello World 
                        H       e        l        l        o      Escape     W        o         r        l        d
    - Binary :      01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100
    - DNA :           CAGA     CGCC     CGTA     CGTA     CGTT     AGAA     CCCT     CGTT      CTAG    CGTA     CGCA
    - DNA Seq:      CAGACGCCCGTACGTACGTTAGAACCCTCGTTCTAGCGTACGCA

Convert DNA (DNA -> Binary -> Text): 

    - DNA Seq:      CAGACGCCCGTACGTACGTTAGAACCCTCGTTCTAGCGTACGCA
    - DNA :           CAGA     CGCC     CGTA     CGTA     CGTT     AGAA     CCCT     CGTT      CTAG    CGTA     CGCA
    - Binary :      01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100
                       H       e        l        l        o      Escape     W        o         r        l        d
    - Text Seq :    Hello World

"""

class Cipher:
    def __init__(self) -> None:
        self.CIPHER = {
                    "A":"00",
                    "T":"11",
                    "C":"01",
                    "G":"10",
                    "00":"A",
                    "11":"T",
                    "01":"C",
                    "10":"G"
                            }

class DNA(Cipher):
    def __init__(self) -> None:
        super().__init__()

    def text_to_binary(self, t):
        unicode = []
        binary = []

        #Convert text (user input) to binary list by characters
        for i in t:
            unicode.append(ord(i))
        for k in unicode:
            binary.append(bin(k)[2:])

        #Check that the element has 8 characters
        for i in range(len(binary)):
            if len(binary[i]) % 8 != 0:
                zero_to_add = 8 - len(binary[i])
                binary[i] = "0" * zero_to_add + binary[i]

        return binary
    

    def binary_to_dna(self, b):
        dna = ''

        #Convert the 2 selected values to the value corresponding to the key (2 selected values)
        for i in b:
            for x in range(0, len(i), 2):
                bits = i[x:x+2]
                dna += self.CIPHER[bits]

        return dna
    

class Text(Cipher):
    def __init__(self) -> None:
        super().__init__()

    def seq_to_binary(self, s):
        binary = ''
        count = 0

        #Convert DNA sequence to characters
        for i in s:
            count += 1
            binary += self.CIPHER[i]

        return binary

    def binary_to_text(self, b):
        sentance = ''

        #Convert binary sequence to text
        for i in range(0, len(b), 8):
            sentance += chr(int(b[i:i+8], 2))
        
        return sentance

while True:
    print("Text to DNA : 1 | DNA to Text : 2 ")
    user_input = int(input(": "))

    if user_input == 1:
        dna = DNA()
        sentance = input("Text : ")
        convert = dna.binary_to_dna(dna.text_to_binary(sentance))
        print("DNA : ", convert)
    elif user_input == 2:
        text = Text()
        sentance = input("DNA : ")
        convert = text.binary_to_text(text.seq_to_binary(sentance))
        print("Text : ", convert)
    elif user_input == 0:
        exit()
    else:
        print("Unknow command !")