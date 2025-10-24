s=input()
palindrome=s[::-1]==s
mirror_dict={
    'A': 'A',
    'M': 'M',
    '1':'1',
    '8':'8',
    'H':'H',
    'I':'I',
    'O':'O',
    'U':'U',
    'V':'v',
    'T':'T',
    'W':'W',
    'X':'X',
    'E':'3',
    'S':'2',
    'Z':'5',
    '5':'Z',
    '2':'S',
    '3':'E',
    'L':'J',
    'Y':'Y'

}
mirror_s=''
for c in s:
    if c not in mirror_dict.keys():
       break
    mirror_s+=mirror_dict[c]
mirrorstring=mirror_s[::-1]==s 
if mirrorstring and palindrome:
    print('зеркальный палиндром')
elif mirrorstring:
    print('зеркальная строка')
elif palindrome:
    print('палиндром')
else:
    print('просто строка')