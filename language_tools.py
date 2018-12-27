class aLanguageHelper:
    def __init__(self,words):
        self._suggestions=[]
        self._queryList=[]
        self._capWords=([x.title() for x in words])
        self._words={'Alice','alive','alike','lice','moose','Tony','Missouri','dimmer','Papa','Peter'}
        self._words = sorted(self._words, key = str.lower) #sorting words independently 
        self._lowerWords = set(w.lower() for w in self._words) #making new set
        self._lowerWords = sorted(self._lowerWords) #sorting self._lowerWords

    def __contains__(self,query):
        #Returns true/false if query is contained in the set. Including case-sensitivity 
        if query in self._words:
            return True
        else:
            if query in lowerWords:
                return True
                '''
                location = lowerWords.index(data0)
                print('True, but upper')
                print(words[location].upper())
                '''
            else:
                return False

    def getSuggestions(self,query):
        if aLanguageHelper.__contains__:
            alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            self._queryList=list(query)
            if self._queryList[0].isupper():
                self._words=([x.title() for x in self._words])
                #Checks for case-sensitivity 
            if query not in self._words:
                if query in self._lowerWords:
                    location = self._lowerWords.index(query)
                    if query[0].isupper():
                        self._suggestions.append(self._words[location].title())
                    else:
                        self._suggestions.append(self._words[location])
            
                # Suggests a word if user switched letters
            for number in range(len(self._queryList)-1):
                self._queryList[number],self._queryList[number+1]=self._queryList[number+1], self._queryList[number]
                queryListJoin=''.join(self._queryList)
                if queryListJoin in self._words:
                    self._suggestions.append(queryListJoin)
                    self._queryList=list(query)
                else:
                    self._queryList=list(query)

                #Suggests a word if it needs to replace a letter
            for number in range(len(self._queryList)):
                for letter in alphabet:
                    self._queryList[number]=letter
                    queryListJoin=''.join(self._queryList)
                    if queryListJoin in self._words:
                        self._suggestions.append(queryListJoin)
                        self._queryList=list(query)
                    else:
                        self._queryList=list(query)
                        
                #Suggests a word if user added an extra letter
            for number in range(len(self._queryList)):
                del self._queryList[number]
                queryListJoin=''.join(self._queryList)
                if queryListJoin in self._words:
                    self._suggestions.append(queryListJoin)
                    self._queryList=list(query)
                else:
                    self._queryList=list(query)

                #Suggests a word if user is missing a letter
            for number in range(len(self._queryList)+1):
                for letter in alphabet:
                    self._queryList.insert(number,letter)
                    queryListJoin=''.join(self._queryList)
                    if queryListJoin in self._words:
                        self._suggestions.append(queryListJoin)
                        self._queryList=list(query)
                    else:
                        self._queryList=list(query)

        

        #sorts list alphabetically, removes duplicates and prints output only if it's not empty
        output = sorted(list(set(self._suggestions)))
        if len(self._suggestions)!=0:
            print(output)
        for suggestion in output:
            print('Did you mean',suggestion+ '?')

#unit test for code

if __name__=='__main__':
    test=aLanguageHelper([])
    test.getSuggestions('alie')
