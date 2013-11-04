
# name : abosloh
# email : cinema48@gmail.com


# replace seconds to clock h:m:s (00:00:00)
def getClock(s):
    clock = ""
    clock+= "%02d:" % (s/3600,) # find hours
    s = s%3600 # decrement seconds
    clock+= "%02d:" % (s/60,) # find minutes
    s = s%60 # decrement seconds
    clock+= "%02d" % (s,) # find seconds
    return clock # return clock as (h:m:s)
