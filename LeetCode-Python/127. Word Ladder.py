# import sys
#
# class Solution(object):
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: Set[str]
#         :rtype: int
#         """
#         visited = []
#         result = self.backtrackLadderLength(beginWord, endWord, wordList, {}, visited)
#         if result == sys.maxint : return 0
#         else: return result
#
#     def checkWords(self, word1, word2):
#         if len(word1) == len(word2):
#             count_diffs = 0
#             for a, b in zip(word1, word2):
#                 if a != b:
#                     if count_diffs: return False
#                     count_diffs += 1
#             return True
#         else : return False
#
#     def backtrackLadderLength(self, beginWord, endWord, wordList, hash, visited):
#         if beginWord in hash.keys():
#             return hash[beginWord]
#
#         if beginWord == endWord:
#             return 1
#
#         result = sys.maxint
#         for word in wordList:
#             if word not in visited and self.checkWords(beginWord, word):
#                 visited.append(word)
#                 hash[word] = self.backtrackLadderLength(word, endWord, wordList, hash, visited)
#                 visited.pop(-1)
#                 result = min(result, 1 + hash[word])
#
#         return result




import time
class Solution(object):
    def neighbors(self, x, y):
        ed = 0
        for i in range(0, len(x)):
            if x[i] != y[i]:
                ed += 1
            if ed > 1:
                return False
        return True

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        graph = {}
        wordList.append(beginWord)
        wordList.append(endWord)
        for w in wordList:
            s = set()
            for v in wordList:
                if w == v:
                    continue
                if self.neighbors(w, v):
                    s.add(v)
            graph[w] = s

        visited = set()
        q = []
        q.append(beginWord)
        last = beginWord
        visited.add(beginWord)
        level = 1

        while len(q) != 0:
            cur = q.pop(0)
            if cur == endWord:
                return level  # done
            for c in graph[cur]:
                if c not in visited:
                    q.append(c)
                    visited.add(c)
            if cur == last:
                level += 1  # new level begins
                if len(q) > 0:
                    last = q[-1]  # last
        return 0


obj = Solution()
# obj.ladderLength("hit","cog",["hot","dot","dog","lot","log"])
obj.ladderLength("a","c",["a", "b", "c"])
# obj.ladderLength("hot",
# "dog",
# ["hot","dog","cog","pot","dot"])
obj.ladderLength("cet",
"ism",
["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa",
 "cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay",
 "col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump",
 "dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal",
 "lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan",
 "map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log",
 "tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara",
 "dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe",
 "gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam",
 "ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod",
 "hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod",
 "day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum",
 "pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus",
 "rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may",
 "shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo",
 "hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate",
 "gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir",
 "nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son",
 "ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad",
 "rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin",
 "mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm",
 "nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit",
 "hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil",
 "red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton",
 "sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig",
 "fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode",
 "stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan",
 "mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com",
 "ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia",
 "kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid",
 "god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz",
 "fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot",
 "are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee",
 "pin","dun","pat","ten","mob"])

