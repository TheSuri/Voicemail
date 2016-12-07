# ////////////Imports////////////////////////////////////////////////
import urllib2
import re
import os
from subprocess import call
import argparse
import sys
# ////////////Imports////////////////////////////////////////////////
#////////////Code////////////////////////////////////////////////

#downloads MP3 files
def download_file(a):
	url = a
	file_name = url.split('/')[-1]
	#uses URLLiB2 
	u = urllib2.urlopen(url)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)
	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
	        break
	    file_size_dl += len(buffer)
	    f.write(buffer)
	    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	    status = status + chr(8)*(len(status)+1)
	    print status,
	f.close()
	fo = open("sequence.txt", 'a')
	fo.write("%s\n"%file_name)
	fo.close()


#Separates phone number into each and every mp3 files and calls download_file

def phoneNumberMp3(phoneNumber):
	lst=list(phoneNumber)
	phoneList = [int(x) for x in lst]
	for item in phoneList:
		if item==0:
			url="http://www-bcf.usc.edu/~chiso/itp125/project_version_1/0.mp3"
			download_file(url)
			os.system("cat 0.mp3>> phone.mp3")
		if item==1:
			url="http://www-bcf.usc.edu/~chiso/itp125/project_version_1/1.mp3"
			download_file(url)
			os.system("cat 1.mp3>> phone.mp3")
		if item==2:
			url="http://www-bcf.usc.edu/~chiso/itp125/project_version_1/2.mp3"
			download_file(url)
			os.system("cat 2.mp3>> phone.mp3")
		if item==3:
			url="http://www-bcf.usc.edu/~chiso/itp125/project_version_1/3.mp3"
			download_file(url)
			os.system("cat 3.mp3>> phone.mp3")
		if item==4:
			url="http://www-bcf.usc.edu/~chiso/itp125/project_version_1/4.mp3"
			download_file(url)
			os.system("cat 4.mp3>> phone.mp3")
		if item==5:
			url="http://www-bcf.usc.edu/~chiso/itp125/project_version_1/5.mp3"
			download_file(url)
			os.system("cat 5.mp3>> phone.mp3")
		if item==6:
			url="http://www-bcf.usc.edu/~chiso/itp125/project_version_1/6.mp3"
			os.system("cat 6.mp3>> phone.mp3")
		if item==7:
			url="http://www-bcf.usc.edu/~chiso/itp125/project_version_1/7.mp3"
			download_file(url)
			os.system("cat 7.mp3>> phone.mp3")
		if item==8:
			url="http://www-bcf.usc.edu/~chiso/itp125/project_version_1/8.mp3"
			download_file(url)
			os.system("cat 8.mp3>> phone.mp3")
		if item==9:
			url="http://www-bcf.usc.edu/~chiso/itp125/project_version_1/9.mp3"
			download_file(url)
			os.system("cat 9.mp3>> phone.mp3")


#////////////If command line arguments exist do this:////////////
if len(sys.argv) > 1:
	#parsing command line args here
	parser = argparse.ArgumentParser()
	parser.add_argument('g', help='Usage m for male and f for female') #-g (male/female) 
	parser.add_argument('n', help='Usage phone number (as long as 10 digits any format works')#-n (phone number)
	parser.add_argument('b', help='Usage numbers from 1-2')#-b (beginning)
	parser.add_argument('r', help='Usage numbers from 0-4 for male and 0-6 for female')#-r (reasons) 
	parser.add_argument('e', help='Usage numbers from 1-6 for male and 1-2 for female ')#-e (endings)
	parser.add_argument('o', help='Args help')#-o (output name)
	args = parser.parse_args()
	gender = args.g
	phoneNumber = args.n
	beginning = args.b
	reasons = args.r
	ending = args.e
	outputfile = args.o
	print "removing all previous .mp3 files and sequence.txt files"
	os.system("rm *.mp3")
	os.system("rm sequence.txt")
	if (gender=="Male" or gender =="male" or gender=="m" or gender =="M"):
		male=1
	elif (gender=="Female" or gender =="female" or gender=="f" or gender =="F"):
		male=0
	else:
		print 'Invalid entry for gender. Expected: M/m F/f Male/male Femal/female in command line argument'
		sys.exit()


	#////////////Loop for Entry of Phone Number////////////
	#removing all special characters from phone number
	phoneNumber=re.sub('\W+', '', phoneNumber)
	if len(phoneNumber) != 10:
		print 'Phone number entered was invalid/less/more than 10 numerical digits please try again with correct args.'
		sys.exit()	

	#////////////If Male////////////////////////////////////////////////
	if male==1:
		
		fo = open("sequence.txt", 'a')
		fo.write("male\n")
		fo.close()
		lst=list(beginning)
		beginList = [int(x) for x in lst]
		flag=0
		for item in beginList:
			if item>2 or item<1 or len(beginList)>2 or len(beginList)<=0:
				flag=1
		if flag==1:
			print 'You have not entered correct values for beginning message. enter values from 0-2'
			sys.exit()	
		

		lst=list(str(reasons))
		reasonList =[int(x) for x in lst]
		flag=0
		for item in reasonList:
			if item>5 or item<0 or len(reasonList)>6 or len(reasonList)<=0:
				flag=1
		if flag==1:
			print 'You have not entered correct values for reason messages. enter values from 0-6'
			sys.exit()
			
		lst=list(str(ending))
		endList =[int(x) for x in lst]
		flag=0
		for item in endList:
			if item>6 or item<1 or len(endList)>6 or len(endList)<=0:
				print item
				flag=1
		if flag==1:
			print 'You have not entered correct values for ending messages. enter values from 1-6'
			sys.exit()
		
		while True:
			choice= raw_input('Is this information correct? (y/Y/n/N)\n You have picked: male with phone number %s\n Beginning choices: %s\n Reason Choices: %s\n Ending choices: %s\n%s\n' % (phoneNumber, beginning, reasons, ending, outputfile))
			if choice =='y' or choice =='Y':
				break
			elif choice == 'n' or choice== 'N': 
				#Restart program here
				break
			else:
				print 'Only y/Y or N/n answers accepted.'
				continue
		if choice == 'n' or choice== 'N':
			#Restart program here actually
			sys.exit


		#*******************************************Downloading male files here********************************
		for item in beginList:
			if item == 1:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-b1-hello.mp3"
				download_file(url)
				

			elif item == 2:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-b2-have_dialed.mp3"
				download_file(url)
				phoneNumberMp3(phoneNumber)
				os.system("cat phone.mp3>> m-b2-have_dialed.mp3")

		for item in reasonList:
			if item == 0:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-r0-cannot_come_to_phone.mp3"
				download_file(url)


			if item == 1:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-r1-building.mp3"
				download_file(url)

			if item == 2:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-r2-cracking_walnuts.mp3"
				download_file(url)

			if item == 3:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-r3-polishing_monocole.mp3"
				download_file(url)


			if item == 4:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-r4-ripping_weights.mp3"
				download_file(url)

		flag2=False
		for item in endList:
			if item == 1:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-e1-horse.mp3"
				download_file(url)
			
			if item == 2:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-e2-jingle.mp3"
				download_file(url)

			
			if item == 3:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-e3-on_phone.mp3"
				download_file(url)

			
			if item == 4:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-e4-swan_dive.mp3"
				download_file(url)

			if item == 5:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-e5-voicemail.mp3"
				download_file(url)
					
			if item == 6:
				url="http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-leave_a_message.mp3"
				flag2=True
				download_file(url)

		if flag2==True:
			print 'concatenating files now...'
			if(len(endList)>1):
				os.system("cat m-b*.mp3 m-r*.mp3 m-e*.mp3 m-leave_a_message.mp3> %s" %outputfile)
			else:
				os.system("cat m-b*.mp3 m-r*.mp3 m-leave_a_message.mp3> %s" %outputfile)
			os.system("find . -type f -not -name '%s' -not -name '*.py' -not -name '*.txt' | xargs rm" %(outputfile))

		else:
			print 'concatenating files now...'
			os.system("cat m-b*.mp3 m-r*.mp3 m-e*.mp3 > %s" %outputfile)
			os.system("find . -type f -not -name '%s' -not -name '*.py' -not -name '*.txt' | xargs rm" %(outputfile))


	#/////////// If Female/////////////////////////////////////////////
	elif male==0:
		fo = open("sequence.txt", 'a')
		fo.write("female\n")
		fo.close()
		lst=list(beginning)
		beginList = [int(x) for x in lst]
		flag=0
		for item in beginList:
			if item>2 or item<1 or len(beginList)>2 or len(beginList)<=0:
				flag=1
		if flag==1:
			print 'You have not entered correct values for beginning message. enter values from 0-2'
			sys.exit
		
		
		lst=list(str(reasons))
		reasonList =[int(x) for x in lst]
		flag=0
		for item in reasonList:
			if item>6 or item<0 or len(reasonList)>7 or len(reasonList)<=0:
				flag=1
		if flag==1:
			print 'You have not entered correct values for reason messages. enter values from 0-2'
			sys.exit

		
		lst=list(str(ending))
		endList =[int(x) for x in lst]
		flag=0
		for item in endList:
			if item>6 or item<1 or len(endList)>6 or len(endList)<=0:
				flag=1
		if flag==1:
			print 'You have not entered correct values for ending messages. enter values from 0-2'
			sys.exit

		while True:
			choice= raw_input('Is this information correct? (y/Y/n/N)\n You have picked: male with phone number %s\n Beginning choices: %s\n Reason Choices: %s\n Ending choices: %s\n%s\n' % (phoneNumber, beginning, reasons, ending, outputfile))
			if choice =='y' or choice =='Y':
				break
			elif choice == 'n' or choice== 'N': 
				#Restart program here
				break
			else:
				print 'Only y/Y or N/n answers accepted.'
				continue
		if choice == 'n' or choice== 'N':
			#Restart program here actually
			sys.exit

		#*******************************************Downloading female files here********************************
		for item in beginList:
			if item == 1:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-b1-hello_caller.mp3"
				download_file(url)
				

			elif item == 2:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-b2-lady_at.mp3"
				download_file(url)
				phoneNumberMp3(phoneNumber)
				os.system("cat phone.mp3>> f-b2-lady_at.mp3")

		for item in reasonList:
			if item == 0:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-r0.1-unable_to_take_call.mp3"
				download_file(url)


			if item == 1:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-r0.2-she_is_busy.mp3"
				download_file(url)

			if item == 2:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-r1-ingesting_old_spice.mp3"
				download_file(url)

			if item == 3:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-r2-listening_to_reading.mp3"
				download_file(url)


			if item == 4:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-r3-lobster_dinner.mp3"
				download_file(url)

			if item == 5:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-r4-moon_kiss.mp3"
				download_file(url)

			if item == 6:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-r5-riding_a_horse.mp3"
				download_file(url)


		for item in endList:
			if item == 1:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-e1-she_will_get_back_to_you.mp3"
				download_file(url)
			
			if item == 2:
				url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-e2-thanks_for_calling.mp3"
				download_file(url)

		print 'concatenating files now...'
		os.system("cat f-b*.mp3 f-r*.mp3 f-e*.mp3> %s" %outputfile)
		os.system("find . -type f -not -name '%s' -not -name '*.py' -not -name '*.txt' | xargs rm" %(outputfile))





#/////////////////////////////If no args passed/////////////////////////////////////////////////////////////////////
else:
	while True:
		os.system("rm *.mp3")
		os.system("rm sequence.txt")
		while True:
			gender=raw_input('Do you want the male or female version?(enter whole word male or female): ')
			if (gender=="Male" or gender =="male"):
				male=1
				break
			elif (gender=="Female" or gender =="female"):
				male=0
				break
			else:
				print 'Invalid entry Please try again.'


		#////////////Loop for Entry of Phone Number////////////
		while True:
			phoneNumber=raw_input('Please enter your 10 digit phone number: ')
			phoneNumber=re.sub('\W+', '', phoneNumber)
			if len(phoneNumber) == 10:
				break
			else:
				print 'Phone number entered was invalid/less/more than 10 numerical digits please enter again.'
				continue	

		#////////////If Male////////////////////////////////////////////////
		if male==1:
			fo = open("sequence.txt", 'a')
			fo.write("male\n")
			fo.close()
			while True:
				beginning= raw_input('Please enter the beginning (1-2):\n[1]Hello\n[2]You have dialed\n')
				lst=list(beginning)
				beginList = [int(x) for x in lst]
				flag=0
				for item in beginList:
					if item>2 or item<1 or len(beginList)>2 or len(beginList)<=0:
						flag=1
				if flag==1:
					print 'You have not entered correct values for beginning message. enter values from 0-2'
				else:
					break
			
			while True:
				reasons= raw_input('Please enter the reasons you would like (0-5):\n[0] Cannot come to phone because\n[1] Building\n[2] cracking walnuts\n[3] Polishing Monocle\n[4] Ripping weights\n[5]youre welcome\n')
				lst=list(str(reasons))
				reasonList =[int(x) for x in lst]
				flag=0
				for item in reasonList:
					if item>5 or item<0 or len(reasonList)>6 or len(reasonList)<=0:
						flag=1
				if flag==1:
					print 'You have not entered correct values for reason messages. enter values from 0-2'
				else:
					break

			while True:
				ending=raw_input('Please enter the ending you would like (1-6):\n[1] On a horse\n[2] Jingle\n[3] On a Phone\n[4] Swan Dive\n[5] This Voicemail is now diamonds\n[6] But leave a message and theyll return your call\n')
				lst=list(str(ending))
				endList =[int(x) for x in lst]
				flag=0
				for item in endList:
					if item>6 or item<1 or len(endList)>6 or len(endList)<=0:
						flag=1
				if flag==1:
					print 'You have not entered correct values for ending messages. enter values from 0-2'
				else:
					break

			while True:
				choice= raw_input('Is this information correct? (y/Y/n/N)\n You have picked: male with phone number %s\n Beginning choices: %s\n Reason Choices: %s\n Ending choices: %s\n' % (phoneNumber, beginning, reasons, ending))
				if choice =='y' or choice =='Y':
					break
				elif choice == 'n' or choice== 'N': 
					#Restart program here
					break
				else:
					print 'Only y/Y or N/n answers accepted.'
					continue
			if choice == 'n' or choice== 'N':
				#Restart program here actually
				continue


			outputfile=raw_input('What would you like to call your output file?\n')

			#*******************************************Downloading male files here********************************
			for item in beginList:
				if item == 1:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-b1-hello.mp3"
					download_file(url)
					

				elif item == 2:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-b2-have_dialed.mp3"
					download_file(url)
					phoneNumberMp3(phoneNumber)
					os.system("cat phone.mp3>> m-b2-have_dialed.mp3")

			for item in reasonList:
				if item == 0:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-r0-cannot_come_to_phone.mp3"
					download_file(url)


				if item == 1:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-r1-building.mp3"
					download_file(url)

				if item == 2:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-r2-cracking_walnuts.mp3"
					download_file(url)

				if item == 3:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-r3-polishing_monocole.mp3"
					download_file(url)


				if item == 4:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-r4-ripping_weights.mp3"
					download_file(url)

			flag2=False
			for item in endList:
				if item == 1:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-e1-horse.mp3"
					download_file(url)
				
				if item == 2:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-e2-jingle.mp3"
					download_file(url)

				
				if item == 3:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-e3-on_phone.mp3"
					download_file(url)

				
				if item == 4:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-e4-swan_dive.mp3"
					download_file(url)

				if item == 5:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-e5-voicemail.mp3"
					download_file(url)
						
				if item == 6:
					url="http://www-bcf.usc.edu/~chiso/itp125/project_version_1/m-leave_a_message.mp3"
					flag2=True
					download_file(url)

			if flag2==True:
				print 'concatenating files now...'
				if(len(endList)>1):
					os.system("cat m-b*.mp3 m-r*.mp3 m-e*.mp3 m-leave_a_message.mp3> %s" %outputfile)
				else:
					os.system("cat m-b*.mp3 m-r*.mp3 m-leave_a_message.mp3> %s" %outputfile)
				os.system("find . -type f -not -name '%s' -not -name '*.py' -not -name '*.txt' | xargs rm" %(outputfile))

			else:
				print 'concatenating files now...'
				os.system("cat m-b*.mp3 m-r*.mp3 m-e*.mp3 > %s" %outputfile)
				os.system("find . -type f -not -name '%s' -not -name '*.py' -not -name '*.txt' | xargs rm" %(outputfile))


		#/////////// If Female/////////////////////////////////////////////
		elif male==0:
			fo = open("sequence.txt", 'a')
			fo.write("female\n")
			fo.close()
			while True:
				beginning= raw_input('Please pick the beginning (1-2):\n[1]Hello Caller\n[2]Lady at\n')
				lst=list(beginning)
				beginList = [int(x) for x in lst]
				flag=0
				for item in beginList:
					if item>2 or item<1 or len(beginList)>2 or len(beginList)<=0:
						flag=1
				if flag==1:
					print 'You have not entered correct values for beginning message. enter values from 0-2'
				else:
					break
			
			while True:
				reasons= raw_input('Please enter the reasons you would like (0-6):\n[0] Unable to take a call\n[1] She is busy\n[2] Ingesting oldspice\n[3] Listening to reading\n[4] Lobster dinner\n[5]Moon kiss\n[6]Riding a horse\n')
				lst=list(str(reasons))
				reasonList =[int(x) for x in lst]
				flag=0
				for item in reasonList:
					if item>6 or item<0 or len(reasonList)>7 or len(reasonList)<=0:
						flag=1
				if flag==1:
					print 'You have not entered correct values for reason messages. enter values from 0-2'
				else:
					break

			while True:
				ending=raw_input('Please enter the ending you would like (1-6):\n[1] She will get back to you\n[2] Thanks for calling\n')
				lst=list(str(ending))
				endList =[int(x) for x in lst]
				flag=0
				for item in endList:
					if item>6 or item<1 or len(endList)>6 or len(endList)<=0:
						flag=1
				if flag==1:
					print 'You have not entered correct values for ending messages. enter values from 0-2'
				else:
					break

			while True:
				choice= raw_input('Is this information correct? (y/Y/n/N)\n You have picked: female with phone number %s\n Beginning choices: %s\n Reason Choices: %s\n Ending choices: %s\n' % (phoneNumber, beginning, reasons, ending))
				if choice =='y' or choice =='Y':
					break
				elif choice == 'n' or choice== 'N': 
					#Restart program here
					break
				else:
					print 'Only y/Y or N/n answers accepted.'
					continue
			if choice == 'n' or choice== 'N':
				#Restart program here actually
				continue


			outputfile=raw_input('What would you like to call your output file?\n')

			#*******************************************Downloading female files here********************************
			for item in beginList:
				if item == 1:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-b1-hello_caller.mp3"
					download_file(url)
					

				elif item == 2:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-b2-lady_at.mp3"
					download_file(url)
					phoneNumberMp3(phoneNumber)
					os.system("cat phone.mp3>> f-b2-lady_at.mp3")

			for item in reasonList:
				if item == 0:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-r0.1-unable_to_take_call.mp3"
					download_file(url)


				if item == 1:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-r0.2-she_is_busy.mp3"
					download_file(url)

				if item == 2:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-r1-ingesting_old_spice.mp3"
					download_file(url)

				if item == 3:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-r2-listening_to_reading.mp3"
					download_file(url)


				if item == 4:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-r3-lobster_dinner.mp3"
					download_file(url)

				if item == 5:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-r4-moon_kiss.mp3"
					download_file(url)

				if item == 6:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-r5-riding_a_horse.mp3"
					download_file(url)


			for item in endList:
				if item == 1:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-e1-she_will_get_back_to_you.mp3"
					download_file(url)
				
				if item == 2:
					url = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/f-e2-thanks_for_calling.mp3"
					download_file(url)

			print 'concatenating files now...'
			os.system("cat f-b*.mp3 f-r*.mp3 f-e*.mp3> %s" %outputfile)
			os.system("find . -type f -not -name '%s' -not -name '*.py' -not -name '*.txt' | xargs rm" %(outputfile))


		#****************End program loop here******************************
		break
