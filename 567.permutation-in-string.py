class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counter = {}
        keys = set()
        for s in s1:
            if counter.get(s) is None:
                counter[s] = [0, 0]
            counter[s][0] += 1
            keys.add(s)
        stack = []
        addIndex = 0
        stackStart = 0
        while addIndex < len(s2):
            for i in range(addIndex, len(s2)):
                ss = s2[i]
                addIndex += 1
                if ss in counter:
                    counter[ss][1] += 1
                    stack.append(i)
                    if counter[ss][0] <= counter[ss][1] and ss in keys:
                        keys.remove(ss)
                    if len(keys) == 0:
                        break
            if len(keys) > 0:
                return False
            if len(stack) < 2:
                return True
            for iii in range(stackStart, len(stack)):
                if counter[s2[stack[iii]]][1] > counter[s2[stack[iii]]][0]:
                    stackStart += 1
                    counter[s2[stack[iii]]][1] -= 1
                else:
                    break
            if len(s1) < len(stack) - stackStart:
                continue
            update = False
            for ii in range(stackStart + 1, len(stack)):
                if stack[ii] - stack[ii - 1] > 1:
                    update = True
                    for j in range(stackStart, ii):
                        counter[s2[stack[j]]][1] = counter[s2[stack[j]]][1] - 1 if counter[s2[stack[j]]][1] > 1 else 0
                        keys.add(s2[stack[j]])
                        stackStart += 1
            if not update and len(s1) == len(stack) - stackStart:
                return True
        return len(s1) == len(stack) - stackStart

s1 = "qiyjjmsiurfwzolbk"
s2 = "sjfqzacmkijurdtkjsvcgvlapehhtxqypyrksepemqygkkwqruqgxhmssncuqnjhukwisexdfwgtbnxnvtzyjrvxvnexoqylquwvselycwlndpnstkusaqgtcqofznabnwxumvhmbbzpubpjbiuorxsqgccmwuxtzzmuiflydvwoshwbzmbzbvawqxnebksmhcezlemrkjasbgltnhwswmodlyjhpyrjfydvnugucmvemejxazfnjuyahbsyisquyeddwcdqqhfmldebhlcvqggzvysqbevtfvgztxoipycmoahotmfjzvycnxylelgvapprablydqhjzpbtzigeepznggnzvczvfmetuyernrjsijrbkqifwuzmoljylrogryeivdqrrqtmhgrvcyjkfbifxtzaacdpxnpbqlhjomktqgtzvoqixuntbnsyndkywkftqjbihdaodgdsxbyrabpjgrppegnomkkhfpyhtlhawbzvjjelayyxgimnsghqbybbsvofcgxhdumrpqdzmykeuzlyivzudshlomjhlkqnjmwwyyaxzsrtujzdokcrhaawlnwpxklgnzfgckujvntwzvupboahvbwjduaoojlvyldiokahefyppamdgrlwsaynuozppgqjaqmzpgrognbrvlupzsjkqhjopjilvjncigrczxwlojtgdqijcmumnhxvnvpbxoumtepzcjffpyiiryuwqbsrlprsnpvfbdlpcjalcoabmrsiemfstncgyspkmxskufzfheitdzzijhwqurywvypwzrbtygowqrhedtwgxcrvoubxqwwhqkyedzludawxknospjothpkcuzwntejjdjgwnajciplncmczthmjmhvbmanepldkechpkwmhcjytqiucweekeahnsjtllgwehclleiykibiihjyrpivpgxciyqitxwqmtncqbgtpogzlxyppdcbrwqtnhucsurkrkwcgapvcsavlfezhhdodgituntplwoqpuxawbftpqgybqwglkqbrslkcladxgilznmmurikhmivjhrpiuovbtucpufxltwnxtqkqsjvdpnkcjccjstpmssdsytfzlwgzcttfpjustxachhwzacpxexlbkpuqyqcvbhrqfcqynhgbkooaubyjatfltoryxesddapmzdqhizblmbivkbdamrbxrqyiyonhzhefvfhlqmtybxlkarfibkqcsdwovvpnlvdqubrewsdusrfromqlgmmqdchnbltxfskowkdzpndkvljvpfkazpbnwdosjmobdetqhfjutphqdsmrlazlbghkehntimokxjusticdnshqrlqxtwdooshkqvkdolkldknchzzhxkjisnnokjdrfhxcevjjuyyeczcvjdeoysxcqueasienqklyuaomeoqjkkmftmhieeuvktolbvazftzqqznonvejiidhbpkpejmqyvkytlncbpxjopomgomgxdktfxbkdbovtzkmvxbidzfjzpwxjvqrqscsppravwpjyevwjqwnwuoiamguqikctjqccnjqfcemyjjrcsxbdzxdgyokvbirlrtqublgoolziqttuunwtwmisdhhnzvazvpjrsfkcyjbaflfazmhttmaynpfqhragkrgzeeiqzwexozhj"


print(Solution().checkInclusion(s1, s2))