import hashlib, urllib2, time

#access url and read line by line
link = urllib2.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt')
password = link.read().split("\n")

def sha1():
    hash = raw_input('enter hash \n')
    # start timing
    start_time = time.time()
    count = 0
    for attempt in password:
        # hash the password
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

def salt ():
    saltTerm = raw_input('enter salt term \n')
    start_time = time.time()
    count = 0
    for saltAttempt in password:
        # hash the password
        saltHashAttempt = hashlib.sha1(bytes(saltAttempt)).hexdigest()
        count += 1
        # check if match
        if saltHashAttempt == saltTerm:
            print 'The salt term is ', saltAttempt
            hash = raw_input('enter hash \n')
            for attempt in password:
                # hash the password
                hashAttempt = hashlib.sha1(bytes(saltAttempt + attempt)).hexdigest()
                count += 1
                # check if match
                if hashAttempt == hash:
                    print 'Match! The password is ', saltAttempt + attempt
                    print 'It takes ', count, 'attempt(s) in ', time.time() - start_time
                    exit()
                elif hashAttempt != hash:
                    continue
            print 'Cannot find a match'
        elif saltHashAttempt != saltTerm:
            continue
    print 'Cannot find a match'

def space ():
    hash = raw_input('enter hash \n')
    start_time = time.time()
    count = 0
    for firstAttempt in password:
        for secondAttempt in password:
            hashAttempt = hashlib.sha1(bytes(firstAttempt + " " + secondAttempt)).hexdigest()
            print 'checking ', firstAttempt + " " + secondAttempt
            count += 1
    # check if match
            if hashAttempt == hash:
                print 'MATCH! THE PASSWORD IS ', firstAttempt + " " + secondAttempt
                print 'It takes ', count, 'attempt(s) in ', time.time() - start_time
                exit ()
            elif hashAttempt != hash:
                continue
    print 'Cannot find a match'
    
sha1()
# salt ()
# space ()
