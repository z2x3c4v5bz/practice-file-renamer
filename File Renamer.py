# coding:utf-8
import os


def fileNamer(fullpath, filename, changetype, specifiedep = 1, formatitemsdigit = 0):
    ''' This function can rename files with a organized format, especially for the episodes.
    changetype: "single" and "pair" are the only accepted values.
    specifiedep: is the abbr for "specified start episode", default is 1.
    formatitemsdigit: is the abbr for "format items digit", default is 0.
    '''
    
    fullpath = fullpath.replace('\\', '/')

    if not fullpath.endswith('/'):
        fullpath += '/'
    
    ignoresubnames = {'ini', 'db'}

    try:
        dirs = os.listdir(fullpath)
        dirs.sort()
    except:
        print('Invalid path!')
        return -1

    if formatitemsdigit > 0:
        formatitemsdigit = '%0' + str(formatitemsdigit) + 'd'
    else:
        filecount = len(dirs)

        if changetype == 'single':
            formatitemsdigit = '%0' + str(len(str(filecount))) + 'd'
        elif changetype == 'pair':
            formatitemsdigit = '%0' + str(len(str(int(filecount / 2)))) + 'd'
        else:
            return -1
    
    if changetype == 'single':
        filecount = specifiedep
    else:
        filecount = (specifiedep - 1) * 2 + 1

    for selectedfile in dirs:
        subnamearr = selectedfile.split('.')
        subname = subnamearr[len(subnamearr) - 1]

        if subname in ignoresubnames:
            print('Ignore file "' + selectedfile + '".')
            continue

        oldname = selectedfile

        if changetype == 'single':
            newname = filename + ' -- ' + formatitemsdigit%(filecount) + '.' + subname
        else:
            newname = filename + ' -- ' + formatitemsdigit%(int((filecount - 1) / 2 + 1)) + '.' + subname

        os.rename(fullpath + oldname, fullpath + newname)
        print('The file "' + oldname + '" has been renamed as "' + newname + '".')
        filecount += 1

    print('Done!')


if __name__ == '__main__':

    fullpath = R'C:\path'
    filename = 'file name'
    changetype = 'single'
    #changetype = 'pair'
    specifiedep = 1
    formatitemsdigit = 0

    print('-> Fullpath: ' + fullpath)
    print('-> File name: ' + filename)
    print('-> Change type: ' + changetype)
    print('-> Specified EP (the counter will start from this EP): ' + str(specifiedep))
    print('-> Format items digit (0 for unassigned): ' + str(formatitemsdigit) + '\n')

    usersresponse = str(input('Would you like to rename files? (yes, no)')).upper()

    if usersresponse == 'YES':
        fileNamer(fullpath, filename, changetype, specifiedep, formatitemsdigit)
    else:
        print('Your response is "' + usersresponse + '", program will stop running.')