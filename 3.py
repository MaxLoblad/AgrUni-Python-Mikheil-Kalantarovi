

str0 = input('Input date: ')
str1 = str0.split('-')
str2 = str1[2].split(':')
str3 = str2[0].split('T')
str4 = str2[2].split('.')
str5 = str0[-6:len(str0)]

print(str3[0],'-',str1[1],'-',str1[0],' ',int(str3[1])%12,':',
      str2[1],':',str4[0],' ',str5[0],int(str5[1:3]),sep='')