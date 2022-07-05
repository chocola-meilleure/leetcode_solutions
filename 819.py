class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words=[word for word in re.sub(r'[^\w]',' ',paragraph)
                .lower().split()
                    if word not in banned]  #Preprocessing input data

        counts=collections.defaultdict(int) #if there is no key,make new dict item
        for word in words:
            counts[word]+=1 #Counting word in paragraph

        return max(counts,key=counts.get) 

