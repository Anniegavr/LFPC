#Var23
import re

rules = {'S':['bAC', 'B'], 'A' : ['a', 'aS', 'bCaCb'], 'B':['AC', 'bS', 'aAa'], 'C':['_', 'AB'], 'E':['BA']}

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
                if s.__contains__(guilty):  #guilty = empty string production
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
    #The above code has generated new states for each camel-case
    #The code below shall perform the replacement
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
    for v in dict.values():
        for s in v:
            if len(s) < 2 and s.isupper():
#                 print(s)
#                 print(dict.get(s))
                v.remove(s)
                for it in dict.get(s): 
                    v.append(it)

    return dict

def split_long_productions(dict):
    new_state = {}
    for key, value in dict.items():
        for s in value:
            if (len(re.findall("[A-Z][0-9]", s))==1 and len(s)==3) or (len(re.findall("[A-Z][0-9]", s))>2 and len(s)>4):
                #if the program finds patterns like S0A or S0A1B...:
                item = item[:1]
                if item not in new_state.keys():
                    new_state[item] = key+str(value.index(s))+str(value.index(s))
            elif len(re.findall("[A-Z][0-9]", s)) in range(1,3) and len(s) in range(3, 5):
                #We make sure productions like S0A1 aren't touched
                continue
    for _ in range(2):
        for value in dict.values():
            for s in value:
                if len(s)>1:
                    id = value.index(s)
                    for c in s:
                        if c.islower():
                            value[id] = re.sub(c, new_state[c], s)

    return dict
# print(remove_empty(rules))
# print(split_long_productions(elim_unit_productions(rename_camels(remove_empty(rules)))))

