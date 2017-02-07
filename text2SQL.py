
#from nltk import * 
import difflib

def findCloseMatch(word_m,list_m):
                cc=difflib.get_close_matches(word_m, list_m)

                if(len(cc)>0):
                        return list_m.index(cc[0])
                else:
                        return (-1)

def m_fun(sql_m):
	print("log: inside parsing function")
	final_message = ""

	table_name=""
	column_name=""
	#where_clause=""

	table_names=['parts','employee','station']
	column_names=['unit','part_id','process_id','station']
	#where_values=

	#def findCloseMatch(word_m,list_m):
		#cc=difflib.get_close_matches(word_m, list_m)
		
		#if(len(cc)>0):
			#return list_m.index(cc[0])
		#else:
			#return (-1)
			
		

	text=sql_m
	#tokens = word_tokenize(text)
	#print('tokens',tokens)

	#tags=pos_tag(tokens)
	#print('tags',tags)
	tokens=text.split(' ')
	table_match = -1
	
	for each in tokens:
		table_match = findCloseMatch(each,table_names)
		if table_match != -1:
			table_name =  table_names[table_match]
			break
	print('LOG: table_name'+table_name)

	if(table_match==-1):
		final_message="Please provide me details such as "+str(table_names)
		return final_message
		
	column_match=-1
	for each in tokens:
		column_match = findCloseMatch(each,column_names)
		if column_match != -1:
			column_name =  column_names[column_match]
			break
	if(column_match==-1):
		final_message="Please provide me details such as "+str(column_names)
		return final_message
	print("log: got column name")
	value_match=-1
	for each in tokens:
		try:
			if(type(int(each))==int):
				value_match=int(each)
				break
		except:
			pass
	print("got value")
			
	query=""
	if(value_match==-1):
		#final_message="Please provide me details such as "+str(column_names)
		#return final_message
		query = 'select * from' + table_name 
	else:
		query = 'select * from ' + table_name + ' where ' +column_name+'='+str(value_match) 
	
	print(query)
	return query 

#sql_m="show parts details for part id 103"
#ddm=m_fun(sql_m)		


