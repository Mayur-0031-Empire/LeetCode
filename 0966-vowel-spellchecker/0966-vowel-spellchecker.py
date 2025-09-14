class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact_match = {} # to check exact match or  check with case-insensetive or with errors
        case_insensetive_match = {}
        vowels_errors_match = {}
        def word_with_errors(word):
            word = list(word)
            for i in range(len(word)):
                if word[i] in "aeiou":
                    word[i] = "a"
            return "".join(word)
                
        for word in wordlist:
            if word not in exact_match:
                exact_match[word] = word

            temp = word.lower()
            if temp not in case_insensetive_match:
                case_insensetive_match[temp] = word

            temp = word_with_errors(temp)
            if  temp not in vowels_errors_match:
                vowels_errors_match[temp] = word
        print(exact_match)
        print(case_insensetive_match)
        print(vowels_errors_match)
        ans = []
        for query in queries:
            if query in exact_match:
                ans.append(exact_match[query])
                continue

            temp = query.lower()    
            if temp in case_insensetive_match:
                ans.append(case_insensetive_match[temp])
                continue

            temp = word_with_errors(temp) 
            if temp in vowels_errors_match:
                ans.append(vowels_errors_match[temp])
            else :
                ans.append("")
        
        return ans
            

            


        return queries