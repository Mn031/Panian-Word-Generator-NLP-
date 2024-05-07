# -*- coding: utf-8 -*-\
class container:
    def __init__(self,type,original):
        self.type = type
        self.upadesh = original
        self.edit = list()
        self.IT_marker = list()

def Gunaadesh(upadesh,index):
    global IK,GUNA
    if index == -1:
        if upadesh[index] in IK:
            affix = list(GUNA[IK.index(upadesh[index])])
            upadesh.pop(index)
            upadesh = list(upadesh + list(affix))
    elif index == -2:
        if upadesh[index] in IK:
            affix  = list(GUNA[IK.index(upadesh[index])])
            upadesh.pop(index)
            for i in range(len(affix)):
                upadesh.insert(index+1,affix[-i])
    return upadesh
def encoder(upadesh):
    global AJ
    d = {'ा':'आ',
     'ि':'इ',
     'ी':'ई',
     'ु':'उ',
     'ू':'ऊ',
     'ृ':'ऋ',
     'ॄ':'ॠ',
     'ॢ':'ऌ',
     'ॣ':'ॡ',
     'े':'ए',
     'ै':'ऐ',
     'ो':'ओ',
     'ौ':'औ',
     'क':'क्' + 'अ',
     'ख':'ख्' + 'अ',
     'ग':'ग्' + 'अ',
     'घ':'घ्' + 'अ',
     'ङ':'ङ्' + "अ",
     "च":"च्" + "अ",
     "छ":"छ्" + "अ",
     "ज":"ज्" + "अ",
     "झ":"झ्" + "अ",
     "ञ":"ञ्" + "अ",
     "ट":"ट्" + "अ",
     "ठ":"ठ्" + "अ",
     "ड":"ड्" + "अ",
     "ढ":"ढ्" + "अ",
     "ण":"ण्" + "अ",
     "त":"त्" + "अ",
     "थ":"थ्" + "अ",
     "द":"द्" + "अ",
     "ध":"ध्" + "अ",
     "न":"न्" + "अ",
     "प":"प्" + "अ",
     "फ":"फ्" + "अ",
     "ब":"ब्" + "अ",
     "भ":"भ्" + "अ",
     "म":"म्" + "अ",
     "य":"य्" + "अ",
     "र":"र्" + "अ",
     "ल":"ल्" + "अ",
     "व":"व्" + "अ",
     "ळ":"ळ्" + "अ",
     "श":"श्" + "अ",
     "ष":"ष्" + "अ",
     "स":"स्" + "अ",
     "ह":"ह्" + "अ",
     "क्ष":"क्" + "ष्" + "अ",
     "ज्ञ्":"ज्" + "ञ्" + "अ",
      }
    result = list()
    t = 0
    for i in range(len(upadesh)):
        if upadesh[i] in d:
            for j in  d[upadesh[i]]:
                result.append(j)
        else:
            result.append(upadesh[i])
            t = t+1
    i = 1
    while(i<len(result)):
        if result[i] in AJ:
            if(result[i-1] == "अ" ):
                result.pop(i-1)
            else:
                i = i+1
        else:
            i = i + 1
    i = 0
    while(i<len(result)-1):
        if(result[i] =="अ" and result[i+1] == '्'):
            result.pop(i)
            result.pop(i)
        else:
            i = i + 1
    i = 0
    while(i<len(result)):
        if(result[i] == '्'):
            result.pop(i)
        else:
            i = i + 1
    return result

def decoder(upadesh):
    global HAL
    rev_dict = {
     'अ':'',
     'a':'अ',
     'आ':'ा',
     'इ': 'ि',
     'ई': 'ी',
     'उ': 'ु',
     'ऊ': 'ू',
     'ऋ': 'ृ',
     'ॠ': 'ॄ',
     'ऌ': 'ॢ',
     'ॡ': 'ॣ',
     'ए': 'े',
     'ऐ': 'ै',
     'ओ': 'ो',
     'औ': 'ौ'}
    upadesh_copy = upadesh.copy()
    result = list()
    t = 0
    if upadesh_copy[0] == 'अ':
        upadesh_copy[0] = 'a'
    if upadesh_copy[-1] in HAL:
        upadesh_copy.append('्')
    for i in range(len(upadesh_copy)):
        if upadesh_copy[i] in HAL and upadesh_copy[i+1] in HAL:
            upadesh_copy.insert(i+1,'्')
    for i in range(len(upadesh_copy)):
        if upadesh_copy[i] in rev_dict:
            for j in  rev_dict[upadesh_copy[i]]:
                result.append(j)
        else:
            result.append(upadesh_copy[i])
            t = t+1
    return result

GUNA = ["ए","ओ",'अर','अल',"ए","ओ",'अर','अल'] # 1.1.2
IK = ["इ","उ","ऋ","ऌ","ई","ऊ","ॠ","ॡ"] #For 1.1.3\\
AJ = ["अ", "आ", "इ", "ई", "उ", "ऊ", "ऋ", "ॠ", "ऌ", "ॡ", "ए", "ऐ", "ओ", "औ"]
HAL = ["क", "ख", "ग", "घ", "ङ", "च", "छ", "ज", "झ", "ञ", "ट", "ठ", "ड", "ढ", "ण", "त", "थ", "द", "ध", "न", "प", "फ", "ब", "भ", "म", "य", "र", "ल", "व", "ह", "श", "ष", "स"]
TUVARG = ["त", "थ", "द", "ध", "न"] # For 1.3.4
CHUVARG = ["च", "छ", "ज" , "झ", "ञ"] #For 1.3.7 
TTUVARG = ["ट", "ठ", "ड", "ढ", "ण"] #For 1.3.7
KUVARG = ["क", "ख", "ग", "घ", "ङ"] #For 1.3
PUVARG = [ "प", "फ", "ब", "भ", "म"]
TADDHIT = list()
upadesh = list(input("Enter the dhatu: "))
print("For the upadesh " + "".join(decoder(encoder(upadesh))))
upadesh = encoder(upadesh)
upadesh_type = "MOOLDHATU"
container_holder = list()
container_holder.append(container(upadesh_type,upadesh))
container_holder[0].IT_marker = [0 for i in range(len(upadesh))]
i = 0
for i in range(len(upadesh)):
    if(upadesh[i-1] in AJ and upadesh[i]== 'ँ'):
        container_holder[0].IT_marker[i-1] = 1
        container_holder[0].IT_marker[i] = 1
        print("".join(decoder(upadesh[i-1:i+1])) + " is IT")
    elif(len(upadesh)== i +1 and upadesh[i] in HAL):
        container_holder[0].IT_marker[i] = 1
        print(upadesh[i] + "्" + " is IT")
    elif(i == 0  and ((upadesh[i] == 'ञ' and upadesh[i+1] == 'इ') or (upadesh[i] == 'ट' and upadesh[i+1] == 'उ') or (upadesh[i] == 'ड' and upadesh[i+1] == 'उ'))):
        container_holder[0].IT_marker[i] = 1 
        container_holder[0].IT_marker[i+1] = 1
        print("".join(decoder(upadesh[i:i+2])) + " is IT")#Not printing correctly
    elif(upadesh_type == "MOOLPRATYAY" and i == 0 and (upadesh[i] == 'ष' and upadesh[i+1] in HAL)):
        container_holder[0].IT_marker[i] = 1
        print(upadesh[i] + " is IT")
    elif(upadesh_type == "MOOLPRATYAY" and i == 0 and ((upadesh[i] in CHUVARG or upadesh[i] in TTUVARG) and upadesh[i+1] in HAL)):
        container_holder[0].IT_marker[i] = 1
        print(upadesh[i] + " is IT")
    elif (upadesh_type == "MOOLPRATYAY"  and i == 0 and ((upadesh[i] in KUVARG or upadesh[i] == 'ल' or upadesh[i] == 'श') and upadesh[i+1] in HAL)):
        container_holder[0].IT_marker[i] = 1
        print(upadesh[i] + " is IT")
for i in range(len(container_holder[0].IT_marker)):
    if(container_holder[0].IT_marker[i]==0):
        container_holder[0].edit.append(container_holder[0].upadesh[i])
print("After removing IT, we get " + str("".join(decoder(container_holder[0].edit))))
upadesh = list("अनीयर्")
upadesh_type = "MOOLPRATYAY"
upadesh = encoder(upadesh)
print("For the upadesh " + "".join(decoder(upadesh)))
container_holder.append(container(upadesh_type,upadesh))
container_holder[1].IT_marker = [0 for i in range(len(upadesh))]
for i in range(len(upadesh)):
    if(upadesh[i-1] in AJ and upadesh[i]== 'ँ'):
        container_holder[1].IT_marker[i-1] = 1
        container_holder[1].IT_marker[i] = 1
        print("".join(upadesh[i-1:i+1]) + " is IT")
    elif(len(upadesh)== i +1 and upadesh[i] in HAL):
        container_holder[1].IT_marker[i] = 1
        print(upadesh[i] + "्" + " is IT")
    elif(0==i and ((upadesh[i] == 'ञ' and upadesh[i+1] == 'इ') or (upadesh[i] == 'ट' and upadesh[i+1] == 'उ') or (upadesh[i] == 'ड' and upadesh[i+1] == 'उ'))):
        container_holder[1].IT_marker[i] = 1 
        container_holder[1].IT_marker[i+1] = 1
        print("".join(upadesh[i-1:i+1]) + " is IT")#Not printing correctly
    elif(upadesh_type == "MOOLPRATYAY" and i == 0 and (upadesh[i] == 'ष' and upadesh[i+1] in HAL)):
        container_holder[1].IT_marker[i] = 1
        print(upadesh[i] + " is IT")
    elif(upadesh_type == "MOOLPRATYAY" and i == 0 and ((upadesh[i] in CHUVARG or upadesh[i] in TTUVARG) and upadesh[i+1] in HAL)):
        container_holder[1].IT_marker[i] = 1
        print(upadesh[i] + " is IT")
    elif (upadesh_type == "MOOLPRATYAY"  and i == 0 and ((upadesh[i] in KUVARG or upadesh[i] == 'ल' or upadesh[i] == 'श') and upadesh[i+1] in HAL)):
        container_holder[1].IT_marker[i] = 1
        print(upadesh[i] + " is IT")
for i in range(len(container_holder[1].IT_marker)):
    if(container_holder[1].IT_marker[i]==0):
        container_holder[1].edit.append(container_holder[1].upadesh[i])
print("After removing IT, we get " + str("".join(decoder(container_holder[1].edit))))

if container_holder[0].edit[-1] in IK:
   container_holder[0].edit =  Gunaadesh(container_holder[0].edit , -1)
elif container_holder[0].edit[-2] in IK:
    container_holder[0].edit =  Gunaadesh(container_holder[0].edit , -2)

if container_holder[0].edit[-1] in AJ:
    SANDHI = {"ए":"अ" + "य",
              "ओ":"अ" + "व",
              "ऐ":"आ" + "य",
              "औ":"आ" + "व"}
    affix = SANDHI[container_holder[0].edit[-1]]
    container_holder[0].edit.pop()
    container_holder[0].edit = list(container_holder[0].edit + list(affix))
              
SADHU = container_holder[0].edit + container_holder[1].edit
print("After sandhi we get: " + "".join(decoder(SADHU)))
NATV = AJ + ["ह","य","व","र"] + KUVARG + PUVARG
for i in range(len(SADHU)):
    if SADHU[i] == "न":
        for j in range(i+1):
            if j == i-1 and(SADHU[j] == "र" or SADHU[j] == "ष"):
                SADHU[i] = "ण"
            elif SADHU[j] == "र" or SADHU[j] == "ष":
                for k in range(j,i+1):
                    if k == i:
                        SADHU[i] = "ण"
                    if SADHU[k] not in NATV:
                        break        
            
print("The final word is: " + "".join(decoder(SADHU)))
