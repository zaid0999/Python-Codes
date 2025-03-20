str1='single line string'
str2='can "embed" double quotes'
print(str1,str2)

print("========================================")

str3="single line string"
str4="can 'embed' single quotes"
print(str3)
print(str4)

print("========================================")

str5='''naresh i technologies
ameerpet
hyderabad'''
print(str5)

print("========================================")

str6="""Naresh I Technologies
emeerpet
hyderabad"""
print(str6)


print("========================================")


str7=str("naresh")
str8=str(65)
str9=str(1.5)
str10=str(3+2j)
str11=str([10,20,30,40,50])
print(str7,str8,str9,str10,str11,sep="\n")
print(type(str7),type(str8),type(str9),type(str10),type(11))


print()

str12=str()
print(str12,type(str12))