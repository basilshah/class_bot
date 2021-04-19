from meet import enter_meet
from gomeet import gomet
import datetime
import calendar
import pause



# enter your .mec gmail account

meet_creds = {'email': '@mec.ac.in' , 'passwd':''} 



subjects = {'monday' : ['dc','oops','vlsi','rtos','dip'],
            'tuesday' : ['awp','awp','dc','rtos','es'],
            'wednesday' :['vlsi','es','awp','dc','oops'],
            'thursday' :['rtos','es','vlsi','dip','dc'],
            'friday' :['oops','dip','comp','comp','mentoring']
            }

links = {'vlsi' : 'gwg-wujn-nzu',
         'awp' : 'urk-btek-hxu',
         'dc' : 'pjz-ansb-xwq',
         'oops' : 'hzb-cenu-fbh',
         'dip' : 'qgs-pzcc-vkv',
         'es' :'wzx-nsxo-znd',
         'comp': 'nbc-ohes-fur',
         'rtos':'naj-wyno-usw'
        }

goomeet ={'vlsi' : '',
         'awp' : '825966725',
         'dc' : '825966725',
         'oops' : 'hzb-cenu-fbh',
         'dip' : 'qgs-pzcc-vkv',
         'es' :'311215293',
         'comp': 'nbc-ohes-fur'
        }

xtra =['dc','es','awp']

#to find the day of the week
def find_day():
    date = datetime.date.today()
    date = date.weekday()
    day = calendar.day_name[date]
    return day.lower()


#to find the current class
def find_class():
    global tiee
    day = find_day()
    classes = subjects[day]
    times =['08:35-09:30','09:35-10:30','10:35-11:30','11:35-12:30','12:35-13:30']
    ftimes = ['08:35-09:10','09:20-10:00','10:10-10:50','11:00-11:40','11:50-12:30']
    time = str(datetime.datetime.now().time()).split(':')
    cls = ''
    ti = time[0]+':'+time[1]
    if day == 'friday':
        for i in range(5):
            if ti >= ftimes[i].split('-')[0] and ti < ftimes[i].split('-')[1]:
                cls = classes[i]
                tiee = ftimes[i].split('-')[1]
            elif ti > ftimes[4].split('-')[1]:
                exit()
    else:
        for i in range(5):
            if ti >= times[i].split('-')[0] and ti < times[i].split('-')[1]:
                cls = classes[i]
                tiee = times[i].split('-')[1]
            elif ti > times[4].split('-')[1]:
                exit()

    return cls, tiee


def g_meet():
    clss = find_class()[0]
    print(clss)
    print(links[clss])
    enter_meet(meet_creds['email'], meet_creds['passwd'],links[clss])



def stop():
    tii = find_class()[1]
    t = tii.split(':')
    tim = t[0]+':'+ str(int(t[1])+20)
    timee = str(datetime.datetime.now().time()).split(':')
    ti = timee[0] + ':' + timee[1]
    print(ti)
    print(tim)

while True:
    clss = find_class()[0]
    tim = find_class()[1]
    q = datetime.datetime.now()
    timee = str(q.time()).split(':')
    ti = timee[0] + ':' + timee[1]
    a = datetime.datetime.strptime(tim,'%H:%M')
    b= datetime.datetime(q.year,q.month,q.day,a.hour,a.minute)


    if ti < tim :
        if clss in xtra:
            print("gommeet")
            gomet(goomeet[clss])
        else :
            g_meet()
        print("pause until : ",b)
        pause.until(b)
