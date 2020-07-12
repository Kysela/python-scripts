import os, sys, stat, datetime

def filetypeToString(mode):
    if stat.S_ISDIR(mode):
        return "directory"
    elif stat.S_ISCHR(mode):
         return "character device"
    elif stat.S_ISBLK(mode):
         return "block device"
    elif stat.S_ISREG(mode):
         return "regular file"
    elif stat.S_ISFIFO(mode):
         return "FIFO (named pipe)"
    elif stat.S_ISLNK(mode):    
         return "symbolic link"
    elif stat.S_ISDOOR(mode):
         return "door"
    elif stat.S_ISPORT(mode):
         return "event port"
    else:
         return "unknown"

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)


statinfo = os.stat('LICENSE')
print("FileSize: " + sizeof_fmt(statinfo.st_size))
print("FilePermissions: " + stat.filemode(statinfo.st_mode))
print("File type: " + filetypeToString(statinfo.st_mode))
print("Access time: " + str(datetime.datetime.fromtimestamp(statinfo.st_atime)))


