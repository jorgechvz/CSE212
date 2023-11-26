"""
CSE212 
(c) BYU-Idaho
05-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def find_pairs(words):
    """
    The words parameter contains a list of two character 
    words (lower case, no duplicates). Using sets, find an O(n) 
    solution for displaying all symmetric pairs of words.  

    For example, if words was: [am, at, ma, if, fi], we would display:

    am & ma
    if & fi

    The order of the display above does not matter.  'at' would not 
    be displayed because 'ta' is not in the list of words.

    As a special case, if the letters are the same (example: 'aa') then
    it would not match anything else (remember no the assumption above
    that there were no duplicates) and therefore should not be displayed.
    """    
    seen = set()  # Create an empty set to store seen words
    symmetric_pairs = set()  # Create an empty set to store symmetric pairs
    
    for word in words:
        reverse_word = word[::-1]  # Reverse the word
        
        # Check if the reversed word is in the seen set
        # and if it's not the same as the original word
        if reverse_word in seen and reverse_word != word:
            # Add the symmetric pair to the symmetric_pairs set
            symmetric_pairs.add((word, reverse_word))
        
        # Add the word to the seen set
        seen.add(word)
    
    # Print the symmetric pairs
    if symmetric_pairs: 
        for pair in symmetric_pairs:
            print(pair[0], "&", pair[1])
    else:
        print("None: There aren't symmetric pairs")
    
    

find_pairs(["am","at","ma","if","fi"])      # ma & am, fi & if
print("=============")
find_pairs(["ab", "bc", "cd", "de", "ba"])  # ba & ab
print("=============")
find_pairs(["ab","ba","ac","ad","da","ca"]) # ba & ab, da & ad, ca & ac
print("=============")
find_pairs(["ab", "ac"])                    # None
print("=============")
find_pairs(["ab", "aa", "ba"])              # ba & ab
print("=============")
find_pairs(["23","84","49","13","32","46","91","99","94","31","57","14"])
                                            # 32 & 23, 94 & 49, 31 & 13