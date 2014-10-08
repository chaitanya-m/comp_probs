#construct a regex that matches an email address

import re

s = raw_input()
emailPattern = re.compile("^[a-zA-Z0-9\_\-\.]+\@[a-zA-Z0-9]+.[a-z]{2,3}$")
if emailPattern.match(s) is not None:
    print "Valid email"
else:
    print "Not a valid email"
