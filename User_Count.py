import os,datetime,glob,csv,time,sys

path = "F:/Freshware/Vortex/Users/*"  #User folder location, USE FORWARD SLASHES

save_path = "F:/Freshware/Vortex/User Counts"  #User count save destination, USE FORWARD SLASHES

dir_length = len(path)-1 #Char length of user path

x = glob.glob(path)

with open('Date.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow('Ignore this file')

filename = os.path.join(save_path, str('Date.csv'))

if os.path.exists(filename):
    os.remove(filename)

os.rename('Date.csv', filename)

curr_date = os.path.getmtime(os.path.join(save_path, 'Date.csv'))

six_months = curr_date - (60*60*24*180)

t = 0

y = int(len(x))  #How many lines are in the list

total = ['Total Users = ' + str(int(len(x)))]

counter = 0

final_list = []

with open('Temp.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    writer.writerow(['Name', 'Date Last Active'])

while y != 0:
    strPath = str(x[t])
    strAlt_Path = (os.path.dirname(strPath + '/') + '/')
    if os.path.exists(os.path.join(strAlt_Path, 'VorCfg.mde')):
        date_modified = os.path.getmtime(os.path.join(strAlt_Path, 'VorCfg.mde'))
        a = strPath[dir_length:], datetime.datetime.fromtimestamp(int(date_modified)).strftime('%Y-%m-%d'), "\n"
        print((strAlt_Path[dir_length:])[:3])
        with open('Temp.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(a)
        final_list.extend(a)
        if date_modified > six_months:
            if str((strAlt_Path[dir_length:])[:3]) != 'ZZZ':
                counter = counter + 1
    else:
        a = strPath[dir_length:] + ' [USER NOT CONFIGURED PROPERLY]', 0
        with open('Temp.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(a)
        final_list.extend(a)
    t = t+1
    y = y-1

now = time.strftime("%d/%m/%Y").replace("/", "")

total_active = ['Total Active Users = ' + str(counter)]

with open('Temp.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    writer.writerow('')
    writer.writerow(total)
    writer.writerow(total_active)

filename = os.path.join(save_path, str('UserCount ' + now + '.csv'))

if os.path.exists(filename):
    os.remove(filename)

os.rename('Temp.csv', filename)

print(*final_list, sep = "\n")
print('')
print('Total Users = ' + str(int(len(x))))
print('Total Active Users = ' + str(counter))
print('File Name: ' + str('UserCount ' + now + '.csv'))
print('')
print('=================DONE=================')
print('')

os.system('pause')