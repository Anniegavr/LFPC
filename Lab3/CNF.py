#Var23
import re

rules = {'S':['bAC', 'B'], 'A' : ['a', 'aS', 'bCaCb'], 'B':['AC', 'bS', 'aAa'], 'C':['_', 'AB'], 'E':['BA']}
leftRules = []
rightRules = []

# for key, value in rules:
#     leftRules.append(key)
#     rightRules.append(value)

def remove_empty(dict):
    emp = False
    temp = {}
    for k, val in dict.items():
        if '_' in val:
           val.remove('_')
           guilty = k
           emp = True
           print(guilty)
    if emp:
        num = []
        for val in dict.values():
            for s in val:
                if s.__contains__(guilty):
                    if s.count(guilty)>1:
                        sn = s[::-1]
                        s = re.sub(guilty, '', s, 1)
                        sn = re.sub(guilty, '', sn, 1)
                        if val.__contains__(s) == False:
                            val.append(s)
                        if val.__contains__(sn[::-1])==False:
                            val.append(sn[::-1])
                    elif s.count(guilty) == 1:
                        s = re.sub(guilty, '', s)
                        if val.__contains__(s) == False:
                            val.append(s)
    return rules

def rename_camels(dict):
    for key, value in dict.items():
        for s in value:
            # print(s)
            camel = re.findall("[a-z][A-Z]", s)
            if camel:
                for i in range(len(camel)):
                    sn = re.sub('bA', key+str(i+1), s, 1)
            # print(s)
            value.remove(s)
            value.append(sn)

    return dict

print(remove_empty(rules))
# print(rename_camels(remove_empty(rules)))

