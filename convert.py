# -*- coding: utf-8 -*-
from googletrans import Translator
translator=Translator()
lang='fr'

file_name='dum.po'
all_words= [ line for line in open(file_name) if 'msgid' in line]


def find_between( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""



final_list=[]
for word in all_words:
	a=find_between(word,'id','"')
	a=a.replace('"','')
	translated_word=translator.translate(a,dest=lang)
	final_list.append({a:translated_word.text})
print final_list


# write to file
file = open('final.mo','w') 
 
for lis in final_list:
	for key, value in lis.iteritems():
		file.write('msgid "'+str(key)+'"\n')
		value=value.encode('utf-8').strip()
		file.write('msgstr "'+str(value)+'"\n')
		file.write('\n\n') 
	
file.close()
