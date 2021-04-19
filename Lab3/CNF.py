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
    new_state = {}
    for key, value in dict.items():
        for s in value:
            # print(s)
            camel = re.findall("[a-z+][A-Z]", s, 1)
            # print(camel)
            for item in camel:
                item = item[:1]
                if item not in new_state.keys():
                    new_state[item] = key+str(value.index(s))
                    print(item, new_state[item])
    for _ in range(2):
        for value in dict.values():
            for s in value:
                if len(s)>1:
                    id = value.index(s)
                    for c in s:
                        if c.islower():
                            value[id] = re.sub(c, new_state[c], s)
                            print(value[id])

    return dict

def elim_unit_productions(dict):
    for k, v in dict.items():
        for s in v:
            id = v.index(s)
            if len(s)==1 and re.findall("[A-Z]", s):
                v[id] = re.sub(s, dict.get(s), s)

    return dict
print(remove_empty(rules))
# print(rename_camels(remove_empty(rules)))

