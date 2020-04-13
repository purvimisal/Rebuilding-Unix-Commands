# ls - list directory contents
# ls [OPTION]... [FILE]...
# Lists  information  about  the FILEs (the current directory by default).

import sys
import stat
import os
import grp
import pwd
import locale
import time

if len(sys.argv) == 1:
    files = os.listdir(".")
    files = [filename for filename in files if filename[0] != '.']
else:
    files = sys.argv[1:]

files.sort()

now = int(time.time())
recent = now - (6*30*24*60*60)


def get_mode_info(mode):

    perms = "-"
    colour = "default"
    link = ""

    if stat.S_ISDIR(mode):
        perms = "d"
    elif stat.S_ISLNK(mode):
        perms = "l"
        link = os.readlink(filename)
    mode = stat.S_IMODE(mode)
    for who in "USR", "GRP", "OTH":
        for what in "R", "W", "X":
            if mode & getattr(stat, "S_I"+what+who):
                perms = perms+what.lower()
            else:
                perms = perms+"-"
    return (perms, link)


for filename in files:
    try:
        stat_info = os.lstat(filename)
    except:
        sys.stderr.write("%s: No such file or directory\n" % filename)
        continue

    perms, link = get_mode_info(stat_info.st_mode)

    nlink = f"%4d" % stat_info.st_nlink
    try:
        name = f"%-8s" % pwd.getpwuid(stat_info.st_uid)[0]
    except KeyError:
        name = f"%-8s" % stat_info.st_uid

    try:
        group = f"%-8s" % grp.getgrgid(stat_info.st_gid)[0]
    except KeyError:
        group = f"%-8s" % stat_info.st_gid

    size = f"%8d" % stat_info.st_size

    ts = stat_info.st_mtime
    if (ts < recent) or (ts > now):
        time_fmt = f"%b %e  %Y"
    else:
        time_fmt = f"%b %e %R"
    time_str = time.strftime(time_fmt, time.gmtime(ts))

    sys.stdout.write("%s %s %s %s %s %s " %
                     (perms, nlink, name, group, size, time_str))
    sys.stdout.write(filename)

    if link:
        sys.stdout.write(" -> ")

        
    print(link)
