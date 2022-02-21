def res(hod1):
    if '-' not in hod1 or len(hod1) != 5:
        return 'ERROR'
    hod = hod1.split('-')
    was = list(hod[0])
    will = list(hod[1])
    if type(was[0]) != str or type(will[0]) != str:
        return 'ERROR'
    if ord(was[1]) < 48 or ord(was[1]) > 57 or ord(will[1]) <48 or ord(will[1]) > 57:
        return 'ERROR'
    if ord(will[0]) > 104 or int(will[1]) > 8:
        return 'ERROR'
    if list(hod1)[2] != '-':
        return 'ERROR'
    if ord(will[0]) <= 104:
        if int(will[1]) <= 8:
            if int(will[1]) - int(was[1]) == 2 or int(will[1]) - int(was[1]) == -2:
                if ord(was[0]) - ord(will[0]) == 1 or ord(was[0]) - ord(will[0]) == -1:
                    return 'YES'
    return 'NO'


print(res(input()))
