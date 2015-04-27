'''Your name is toby program
toby.py'''

n = "something"
def wiyn():
    while 1:
        print "What is your name?"
        n = raw_input()
        if n == "Toby":
            print "Good. Now say it louder for everyone to hear."
            louder()
            return
        else:
            print "No. Your name is Toby. Its a fine name."
def louder():
    while 1:
        m = raw_input()
        if m == "TOBY":
            print "Good. Cut him down"
            return
        elif m.lower() == "toby":
            print "Go on now! Say it louder!"
        else:
            print "No your name is Toby."
            wiyn()
            return
wiyn()
