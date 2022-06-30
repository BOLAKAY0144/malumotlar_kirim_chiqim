print('\nWELCOME MY PROGRAMM !!!')
# n=0
# while True:
#     kalit=input('Malumotlarimga kirish uchun kalit: ')
#     if kalit!='Bobur':
#         n+=1
#     if kalit=='BOBUR' and n!=3:
#         oilam={
#             'Dadam' : "ismi Rashid yoshi 42 Xorazim viloyatida tug'ilgan ",
#             'Onam' : "ismi Adolat yoshi 40 Xorazim viloyatida tug'ilgan ",
#             'Ukam' : "ismi Bunyod yoshi 16 Xorazim viloyatida tug'ilgan "
#         }
#         malumot=input('Kim haqda: ')
#         if malumot in oilam:
#             print(oilam[malumot])
#     elif n!=3:
#         continue
#     else:
#         break


print('Malumot o\'rnida !!!\n0: tugatish\n1: o\'ynash\n2: malumot qo\'shish\n3: malumot o\'chirish\n4: qidirish')
taomlar=['osh','chuchvara','do\'lma','kabob','no\'xot','makaron']
odamlar=['Samandar','Aka','Habibullo','Bobur','Azizbek','Nodir']
t_o={}
for i in range(len(odamlar)):
    t_o[odamlar[i]]=taomlar[i]
while True:
    kalit=int(input('Nima buyurasiz: '))
    if kalit==0:
        break
    elif kalit==1:
        for i in odamlar:
            print(t_o[i])
    elif kalit==2:
        n=int(input('malumotlar soni: '))
        for i in range(n):
            a=input('kalitini kiriting: ')
            b=input('malumotni kiriting: ')
            odamlar.append(a)
            taomlar.append(b)
            t_o[a]=b
    elif kalit==3:
        m=int(input('malumotlar soni: '))
        if m<=len(odamlar):
            for i in range(m):
                malumot=input('kalitini kiriting: ')
                if malumot in odamlar:
                    odamlar.remove(malumot)
                    taomlar.remove(t_o[malumot]) 
                    del t_o[malumot]
        else:
            print('ERROR ???')
    elif kalit==4:
        kalit2=input('Qidirayotgan malumotizzi kaliti: ')
        if kalit2 in t_o:
            print(t_o[kalit2])
        else:
            print('uzur janob bizda bu xaqda malumot yoq ???')
    else:
        print('ERROR ???')
        



