#cat is one of the most frequently used commands on Unix-like operating systems. It has three related functions with regard to text files: 
# displaying them, combining copies of them and creating new ones.

# cat's general syntax is  cat [options] [filenames] [-] [filenames]



import sys

args = sys.argv[1:]
print('Argument List:', args)
options = []
files = []
for i in args: 
    if i.startswith('-'):
        i = i.strip('-')
        options.extend([x for x in i])
    else:
        files.append(i)

print('options', options)
print(files)
result = ''

def show_ends(s):
    result = ''
    for i in s:
        i = i.rstrip('\n')
        result += i + '$' + '\n'
    return result


def number(s):
    result = ''
    for i in range(0, len(s)):
        line, length = '', 0
        s[i] = s[i].rstrip('\n')
        line += str(i+1) + ' ' + s[i] + '\n'
        length = len(line) + 5
        line = line.rjust(length)
        result += line
    return result


def show_tabs(s):
    result = ''
    for i in s:
        for j in i:
            if j == '\t':
                print(j)
                result += '^I'
            else: 
                result += j
    return result



if len(files) < 2:
    file = files[0]
    with open(file,'r') as f:
        result   = f.readlines()
        print(options)
        print(result)
        if 'E' in options:
            result = show_ends(result)
        if 'n' or 'b' in options:
            if type(result) != list: 
                result = result.split('\n')
            result = number(result)
        if 'T' in options:
            if type(result) != list: 
                result = result.split('\n')
            result = show_tabs(result)

    print(result)







# Options 
# ‘-A’
# ‘--show-all’

#     Equivalent to -vET.
# ‘-b’
# ‘--number-nonblank’

#     Number all nonempty output lines, starting with 1.
# ‘-e’

#     Equivalent to -vE.
# ‘-E’
# ‘--show-ends’

#     Display a ‘$’ after the end of each line.
# ‘-n’
# ‘--number’

#     Number all output lines, starting with 1. This option is ignored if -b is in effect.
# ‘-s’
# ‘--squeeze-blank’

#     Suppress repeated adjacent blank lines; output just one empty line instead of several.
# ‘-t’

#     Equivalent to -vT.
# ‘-T’
# ‘--show-tabs’

#     Display TAB characters as ‘^I’.
# ‘-u’

#     Ignored; for POSIX compatibility.
# ‘-v’
# ‘--show-nonprinting’