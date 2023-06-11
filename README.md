# DNA Encoding / Decoding

## Script details

1. You can convert your sentence (human language) in DNA sequence
2. You can convert your DNA sequence in sentence (human language)

## How does it work ?

### Converting human language into DNA

It works on the principle of binary conversion of your sentence (human language) into DNA.

```
    DNA     |   Binary
------------|-----------
     A      |     00
     T      |     11
     C      |     01
     G      |     10
```

To encode the sentence in a DNA sequence.

Exemple : 

        - My sentence : Hello World 

                                           H        e        l        l        o      Escape     W        o        r        l        d
                                           ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓
        - Sentence in Binary :          01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100
                                           ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓
        - Binary sequences in DNA :       CAGA     CGCC     CGTA     CGTA     CGTT     AGAA     CCCT     CGTT      CTAG    CGTA     CGCA
                                            
                                           
        - Decomposition of "01001000" into DNA (Go to the table above ↑) :
                                       
                                                                                01 00 10 00
                                                                               ↙   ↓   ↓   ↘
                                                                              C    A   G     A      

        - DNA sequence : CAGACGCCCGTACGTACGTTAGAACCCTCGTTCTAGCGTACGCA

To decode the DNA sequence into a sentence, it's the other way around. 

Exemple :

        
        - My DNA sequence : CAGACGCCCGTACGTACGTTAGAACCCTCGTTCTAGCGTACGCA

                                          CAGA     CGCC     CGTA     CGTA     CGTT     AGAA     CCCT     CGTT      CTAG    CGTA     CGCA
                                           ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓
        - DNA sequence in Binary :      01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100
                                           ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓        ↓
        - Binary sequences in sentence :   H        e        l        l        o      Escape     W        o        r        l        d

        - My sentece : Hello World
            

## WARNING !!! 

Only the DNA sequence of a sentence encoded with this script can be decoded with this script!
All other DNA sequences originating from anywhere other than this script will not be decoded correctly and will be greatly distorted. 