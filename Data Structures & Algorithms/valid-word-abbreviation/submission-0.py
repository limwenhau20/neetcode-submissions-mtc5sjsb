class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i = 0 # word pointer
        j = 0 # abbr pointer

        while i < len(word) and j < len(abbr):
            
            # if the letters are the same
            if word[i] == abbr[j]:
                i += 1
                j += 1
            
            # if the letters are NOT same, and its still a letter
            elif abbr[j].isalpha() or abbr[j] == "0":
                return False

            # if the letter are NOT same, but is a number:
            elif not abbr[j].isalpha():
                
                n_letters = "0"

                while j < len(abbr) and not abbr[j].isalpha():
                    n_letters += abbr[j]
                    j += 1

                n_letters = int(n_letters)
                i += n_letters

        return i == len(word) and j == len(abbr)




                    
                





        
        