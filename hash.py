import hashlib, urllib2, time

#take hash inputs
hash = raw_input('enter hash \n')
#start timing
start_time = time.time()
#access url and read line by line
link = urllib2.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt')
password = link.read().split("\n")
count = 0
#loop to find the match
for attempt in password:
    #hash the password
    hashAttempt = hashlib.sha1(bytes(attempt)).hexdigest()
    print "checking ", attempt
    count += 1
    #check if match
    if hashAttempt == hash:
        print 'Match! The password is ', attempt
        print 'It takes ', count , 'attempt(s) in ', time.time() - start_time
        exit()
    elif hashAttempt != hash:
        continue
print 'Cannot find a match'