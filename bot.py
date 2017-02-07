import fbchat
import MySQLdb as mdb
from fuzzywuzzy import fuzz
import random
import text2query
class EchoBot(fbchat.Client):
	def __init__(self,email, password, debug=True, user_agent=None):
		fbchat.Client.__init__(self,email, password, debug, user_agent)
	def on_message(self, mid, author_id, author_name, message, metadata):
		self.markAsDelivered(author_id, mid) #mark delivered
		self.markAsRead(author_id) #mark read
		print("%s said: %s"%(author_id, message))
		
		social_flag=0
		if str(author_id) != str(self.uid):
			#inventory part
			try:
				inventory_query=""
				inventory_query=text2query.m_fun(message)
				print("log: back to bot file:"+inventory_query)	
			
				con=mdb.connect('localhost','username','password','dababase_name')
				cur=con.cursor()
				#sql="select * from qa1"
				cur.execute(inventory_query)
				data=cur.fetchall()
				if(len(data)>0):
					social_flag=1
			
				self.send(author_id,str(data))
			except:
				pass
			
			if(social_flag==0):
				#social part
				con=mdb.connect('localhost','username','password','databaseName')
				cur=con.cursor()
				sql="select * from qa1"
				cur.execute(sql)
				data=cur.fetchall()
				flag=0
				bestMsg=""
				fuz=0
				if(message.find('AAA')!=(-1)):
					q=message.split('AAA')[0]
					a=message.split('AAA')[1]
					cur.execute("""insert into qa1 values(%s,%s)""",(q,a))
					#cur.execute(sql)
					con.commit()

				for r in data:
					#if(r[0]==message):
					if(fuzz.ratio(r[0].lower(), message.lower())>fuz):
						bestMsg=r[1]
						fuz=fuzz.ratio(r[0], message)
						print(str(fuz))

					#if(fuzz.ratio(r[0], message)>50):
						#if str(author_id) != str(self.uid):
				if(fuz>50):
					self.send(author_id,bestMsg)
					flag=1
							
				if(flag==0):
				
					if(message.find('AAA')!=(-1)):
						q=message.split('AAA')[0]
						a=message.split('AAA')[1]
						cur.execute("""insert into qa1 values(%s,%s)""",(q,a))
						#cur.execute(sql)
						con.commit()

					else:
						if str(author_id) != str(self.uid):
							randomAnswer=random.randint(1, 5)
							if(randomAnswer==1):
								self.send(author_id,"Sorry! I didn't understand :-( ")
							elif(randomAnswer==2):
								self.send(author_id,"what?")
							elif(randomAnswer==3):
								self.send(author_id,"what do you mean?")	
							elif(randomAnswer==4):
								self.send(author_id,"what do you mean by -"+message)
							else:
								self.send(author_id,"do i need to check internet? I could not get it")	
							#elf.send(author_id,"Please give me in this format- questionAAAanswer")
							
							self.send('mentorId',message)

							#if you are not the author, echo
							#if str(author_id) != str(self.uid):
							#self.send(author_id,message)
			cur.close()
			con.close()


bot = EchoBot("facebook_id", "password")
bot.listen()
