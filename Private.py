#coding utf-8
#script By Arif_xeyracodelDev
#Dont Remove My Name In Script!!

#module
import requests , json , re , time , json , random , os , json
from bs4 import BeautifulSoup as par
from datetime import datetime , timedelta
import urllib.request

#rich module
from faker import Faker
from rich import print as cetak
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich.columns import Columns

#index init
kelamin , autoset  = [] , []
ok , cp = 0 , 0
okx , cpx = 0 , 0
autoconfirm , autopasw , proxy = [] , [] , []
ses = requests.Session()
token = 'WyIxMDIxODAzODQiLCI5VmozeHRsVENZMFhNQ3N0aGtOZTY0d1QxZnlXb1orUm9ZcldJbDNRIl0='
id = '28726'

class BotMenu:

    def __init__(Arif_xeyracode):
        Arif_xeyracode.ses = requests.Session()
        Arif_xeyracode.uidx , Arif_xeyracode.pasw = [] , []
        Arif_xeyracode.dataGraphql = {}
        Arif_xeyracode.loop=0
        Arif_xeyracode.count=0
        Arif_xeyracode.uidf = []

    def DelayCreate(Arif_xeyracode , teks , jum):
        hihi = ['+','+','-','•','!','?']
        for x in range(int(jum)):
            jum-=1
            Console().print(f'\r[italic white][[italic green]{random.choice(hihi)}[italic white]] {teks}  [italic white]{jum} Detik        ' , end = '\r');time.sleep(1)

    def GetData(Arif_xeyracode , cok , uid , pasw):
        link = ses.get('https://web.facebook.com' , cookies = {'cookie': cok.splitlines()[0]}).text
        if 'Beri tahu kami bahwa email ini milik Anda. Masukkan kode dalam email yang dikirim ke' in str(link):
            Console(width = 64).print(Panel('[bold green]Akun Belum Dikonfirmasi , Konfirmasikan Akun Anda Terlebih Dahulu !!' , width = 64 , style = 'bold white') , justify = 'center')
            cetak(f'[bold white]([bold green]•[bold white]) User Id : {uid}\n[bold white]([bold green]•[bold white]) Pasword : {pasw}\n[bold white]([bold green]•[bold white]) Cookies : {cok}')
            exit()
        token = re.findall('"token":"(.*?)"' , str(link))
        dtsg = token[0]
        lsd = token[1]
        jazoest = re.search('jazoest=(\\d+)' , str(link)).group(1)
        spinr = re.search('"__spin_r":(.*?),', str(link)).group(1)
        spint = re.search('"__spin_t":(.*?),', str(link)).group(1)
        hs = re.search('"haste_session":"(.*?)"', str(link)).group(1)
        rev = re.search('{"consistency":{"rev":(.*?)}', str(link)).group(1)
        hsi = re.search(r'"hsi":"(.*?)"', str(link)).group(1)
        user = re.search('c_user=(\\d+)' , str(cok)).group(1)
        nama = re.search('"NAME":"(.*?)"' , str(link)).group(1)
        cetak(Panel(f'[bold white]([bold green]•[bold white]) Actor Id : {user}\n[bold white]([bold green]•[bold white]) Nama     : {nama}' , width = 64 , style = 'bold white'))
        Console(width = 64).print(Panel('[bold green]Memulai Requests Pertemanan' , width = 64 , style = 'bold white') , justify = 'center')
        Arif_xeyracode.dataGraphql.update({
           '__hs': hs,
           '__rev': rev,
           '__hsi': hsi,
           'fb_dtsg': dtsg,
           'jazoest': jazoest,
           'lsd': lsd,
           '__spin_r': spinr,
           '__spin_t': spint,
           '__user': user,
           'av': user,
           '__aaid': '0',
           '__a': '1',
           '__req': 'z',
           'dpr': '1',
           '__ccg': 'GOOD',
           '__s': '',
           '__dyn': '',
           '__csr': '',
           '__comet_req': '15',
           '__spin_b': 'trunk',
        })

    def AddFriends1(Arif_xeyracode , uid):
        xx = uid.splitlines()
        try:file = open('/sdcard/Premium/AkunLive.txt' , 'r').readlines()
        except(FileNotFoundError):Console(width=64).print(Panel('[italic Green]Tidak Ada Akun Live' , width = 64 , style = 'bold white') , justify = 'center')
        for x in file:
            uid , pasw , cok = x.split('|')[0] , x.split('|')[0][1] ,  x.split('|')[2]
            Arif_xeyracode.uidx.append(uid+'|'+cok+'|'+pasw)
        Console(width = 64).print(Panel('[bold green]List Uid Akun Live' , width = 64 , style = 'bold white') , justify = 'center')
        for z in Arif_xeyracode.uidx:
            Arif_xeyracode.loop+=1
            uid , cok , pasw = z.split('|')
            cetak(f'[bold white]([bold green]{Arif_xeyracode.loop}[bold white]) {uid}')
        Console(width = 64).print(Panel('[bold green]Pilih Uid Untuk Minta Pertemanan' , width = 64 , style = 'bold white') , justify = 'center')
        user = Console().input('[bold white]([bold green]•[bold white]) Pilih : ')
        actorID , actorCOK , actorPW = Arif_xeyracode.uidx[int(user)-1].split('|')
        try:Arif_xeyracode.GetData(actorCOK , actorID , actorPW)
        except(Exception) as e:
            Console(width = 64).print(Panel('[bold red]Ada Kesalahan Saat Login' , width = 64 , style = 'bold white') , justify = 'center')
            exit()
        for s in xx:
            uid , nama = random.choice(xx).split('|')
            Arif_xeyracode.dataGraphql.update({
               'fb_api_caller_class': 'RelayModern',
               'fb_api_req_friendly_name': 'FriendingCometFriendRequestSendMutation',
               'variables': json.dumps({
                  "input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1736988666996,578699,190055527696468,,",
                  "friend_requestee_ids":[uid],
                  "friending_channel":"PROFILE_BUTTON",
                  "warn_ack_for_ids":[uid],
                  "actor_id": actorID,
                  "client_mutation_id":"2"},
                  "scale":1}),
                  'server_timestamps': 'true',
                  'doc_id': '9012643805460802',
            })
            req = ses.post('https://web.facebook.com/api/graphql/', cookies = {'cookie': actorCOK.splitlines()[0]}, data=Arif_xeyracode.dataGraphql , allow_redirects = True).text
            if 'OUTGOING_REQUEST' in str(req):
                 x = requests.get('https://www.facebook.com/profile.php?id='+str(uid)).text
                 user = re.search('<title>(.*?)</title>' , str(x)).group(1)
                 cetak(Panel(f'[bold white]([bold green]•[bold white]) Target Id : {uid}\n[bold white]([bold green]•[bold white]) Nama      : {user}\n[bold white]([bold green]•[bold white]) Status    : [bold green]Berhasil Requests Pertemanan' , width = 64 , style = 'bold white'))
                 teks = 'Jeda Requess Pertemanan'
                 Arif_xeyracode.DelayCreate(teks , 5)
            else:
                 x = requests.get('https://www.facebook.com/profile.php?id='+str(uid)).text
                 user = re.search('<title>(.*?)</title>' , str(x)).group(1)
                 cetak(Panel(f'[bold white]([bold green]•[bold white]) Target Id : {uid}\n[bold white]([bold green]•[bold white]) Nama      : {user}\n[bold white]([bold green]•[bold white]) Status    : [bold red]Gagal Requests Pertemanan' , width = 64 , style = 'bold white'))
                 teks = 'Jeda Requess Pertemanan'
                 Arif_xeyracode.DelayCreate(teks , 5)
            Arif_xeyracode.count+=1
            if Arif_xeyracode.count >=5:
                 Console(width = 64).print(Panel('[bold green]Anda Hanya Dapat Menambahkan 5 Teman Sehari' , width = 64 , style = 'bold white') , justify = 'center')
                 break

    def AddFriends3(Arif_xeyracode):
        try:file = open('/sdcard/Premium/AkunLive.txt' , 'r').readlines()
        except(FileNotFoundError):Console(width=64).print(Panel('[italic Green]Tidak Ada Akun Live' , width = 64 , style = 'bold white') , justify = 'center')
        for x in file:
            uid , pasw , cok = x.split('|')[0] , x.split('|')[0][1] ,  x.split('|')[2]
            Arif_xeyracode.uidx.append(uid+'|'+cok+'|'+pasw)
        Console(width = 64).print(Panel('[bold green]List Uid Akun Live' , width = 64 , style = 'bold white') , justify = 'center')
        for z in Arif_xeyracode.uidx:
            Arif_xeyracode.loop+=1
            uid , cok , pasw = z.split('|')
            cetak(f'[bold white]([bold green]{Arif_xeyracode.loop}[bold white]) {uid}')
        Console(width = 64).print(Panel('[bold green]Pilih Uid Untuk Minta Pertemanan' , width = 64 , style = 'bold white') , justify = 'center')
        user = Console().input('[bold white]([bold green]•[bold white]) Pilih : ')
        actorID , actorCOK , actorPW = Arif_xeyracode.uidx[int(user)-1].split('|')
        try:Arif_xeyracode.GetData(actorCOK , actorID , actorPW)
        except(Exception) as e:
            Console(width = 64).print(Panel('[bold red]Ada Kesalahan Saat Login' , width = 64 , style = 'bold white') , justify = 'center')
            exit()
        for xx in Arif_xeyracode.uidx:
            uid , cok = xx.split('|')
            if actorID in uid:pass
            else:
                Arif_xeyracode.dataGraphql.update({
                   'fb_api_caller_class': 'RelayModern',
                   'fb_api_req_friendly_name': 'FriendingCometFriendRequestSendMutation',
                   'variables': json.dumps(
                      {"input":{
                         "attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1736988666996,578699,190055527696468,,",
                         "friend_requestee_ids":[uid],
                         "friending_channel":"PROFILE_BUTTON",
                         "warn_ack_for_ids":[uid],
                         "actor_id": actorID,
                         "client_mutation_id":"2"},
                         "scale":1
                      }
                   ),
                   'server_timestamps': 'true',
                   'doc_id': '9012643805460802',
                })
                req = ses.post('https://web.facebook.com/api/graphql/', cookies = {'cookie': actorCOK.splitlines()[0]}, data=Arif_xeyracode.dataGraphql , allow_redirects = True).text
                if 'OUTGOING_REQUEST' in str(req):
                    x = requests.get('https://www.facebook.com/profile.php?id='+str(uid)).text
                    user = re.search('<title>(.*?)</title>' , str(x)).group(1)
                    cetak(Panel(f'[bold white]([bold green]•[bold white]) Target Id : {uid}\n[bold white]([bold green]•[bold white]) Nama      : {user}\n[bold white]([bold green]•[bold white]) Status    : [bold green]Berhasil Requests Pertemanan' , width = 64 , style = 'bold white'))
                    teks = 'Jeda Requess Pertemanan'
                    Arif_xeyracode.DelayCreate(teks , 5)
                    Arif_xeyracode.AccFriends(actorID , uid , actorCOK)
                else:
                    x = requests.get('https://www.facebook.com/profile.php?id='+str(uid)).text
                    user = re.search('<title>(.*?)</title>' , str(x)).group(1)
                    cetak(Panel(f'[bold white]([bold green]•[bold white]) Target Id : {uid}\n[bold white]([bold green]•[bold white]) Nama      : {user}\n[bold white]([bold green]•[bold white]) Status    : [bold red]Gagal Requests Pertemanan' , width = 64 , style = 'bold white'))
                    teks = 'Jeda Requess Pertemanan'
                    Arif_xeyracode.DelayCreate(teks , 5)
                Arif_xeyracode.count+=1
                if Arif_xeyracode.count >=5:
                    Console(width = 64).print(Panel('[bold green]Anda Hanya Dapat Menambahkan 5 Teman Sehari' , width = 64 , style = 'bold white') , justify = 'center')
                    break

class TanyaTanya:

    def UserCreate(Arif_xeyracode , jum):
        global ok , cp
        Console(width = 64).print(Panel('[bold green]Apakah Anda Ingin Menggunakan Pasword Otomatis?' , width = 64 , style = 'bold white') , justify = 'center')
        userZ = Console().input('[bold white]([bold green]•[bold white]) Pilih Y/T : ')
        if userZ in ['y' , 'Y']:autopasw.append('y')
        elif userZ in ['t' , 'T']:
            pas = Console().input('[bold white]([bold green]•[bold white]) Masukan Pasword : ')
            autopasw.append('t')
            autopasw.append(pas)
        Console(width = 64).print(Panel('[bold green]Apakah Anda Ingin Langsung Mengonfirmasi Akun?' , width = 64 , style = 'bold white') , justify = 'center')
        userX = Console().input('[bold white]([bold green]•[bold white]) Pilih Y/T : ')
        if userX in ['y' , 'Y']:
            autoconfirm.append('y')
            cetak(Panel('[italic Green]Apakah Anda Ingin Menggunakan Auto Set Profil? Resiko Akun Terkena Suspen / Checkpoint' , width = 64 , style = 'bold white'))
            user3 = Console().input('[bold white]([bold green]•[bold white]) Pilih Y/T : ')
            if user3 in ['y' , 'Y']:autoset.append('y')
            elif user3 in ['t' , 'T']:autoset.append('t')
        elif userX in ['t' , 'T']:
            autoconfirm.append('t')
        Console(width = 64).print(Panel('[bold green]Apakah Anda Ingin Menggunakan Proxy?' , width = 64 , style = 'bold white') , justify = 'center')
        userV = Console().input('[bold white]([bold green]•[bold white]) Pilih Y/T : ')
        if userV in ['y' , 'Y']:proxy.append('y')
        elif userV in ['t' , 'T']:proxy.append('t')
        Console(width=64).print(Panel('[italic Green]Memulai Pembuatan Akun' , width = 64 , style = 'bold white') , justify = 'center')
        for _ in range(jum):
            try:
                CreateAcount()
                loop = 5
                hihi = ['+','+','-','•','!','?']
                for x in range(int(loop)+1):
                    Console().print(f'\r[italic white][[italic green]{random.choice(hihi)}[italic white]] [italic green]Succes:-{int(cp)}  [italic yellow]Spam:-{int(ok)}  [italic white]Jeda:-{loop}           ' , end = '\r');time.sleep(1)
                    loop-=1
            except(Exception) as e:
                loop = 5
                hihi = ['+','+','-','•','!','?']
                for x in range(int(loop)+1):
                    Console().print(f'\r[italic white][[italic green]{random.choice(hihi)}[italic white]] [italic green]Succes:-{int(cp)}  [italic yellow]Spam:-{int(ok)}  [italic white]Jeda:-{loop}            ' , end = '\r');time.sleep(1)
                    loop-=1
        cetak(Panel(f'[italic green]Total Akun Live [italic white] : {ok}\n[italic yellow]Total Akun Check[italic white] : {cp}' , width = 64 , style = 'bold white'))

    def Menu(Arif_xeyracode):
        global okx , cpx
        os.system('clear')
        cetak(Panel('''[bold red]•[bold yellow]•[bold green]•
[bold green]            ╔═╗┬─┐┌─┐┌─┐┌┬┐┌─┐  ╔╦╗┌─┐┌─┐
            ║  ├┬┘├┤ ├─┤ │ ├┤   ║║║├─┤└─┐
            ╚═╝┴└─└─┘┴ ┴ ┴ └─┘  ╩ ╩┴ ┴└─┘

            [italic bold white]Code By [bold green]ArifXeyraKallDev [italic bold white]| Version[bold green] Private
''' , style = ' bold white' , width = 64 , title = '[bold white] Welcome To Script '))
        cetak(Panel('''\t[bold white]Setatus Anda :[bold green] Premium \t[bold white]Script :[bold green] Not Opensource''' , style = ' bold white' , width = 64 , title = '[bold white] Mnu Info '))
        nel = []
        nel.append(Panel('''[italic bold white]([bold green]01[italic bold white]) Create Akun Facebook
[italic bold white]([bold green]02[italic bold white]) Cek Result Akun
[italic bold white]([bold green]03[italic bold white]) Tampilkan Semua Menu Bot
[italic bold white]([bold red]00[italic bold white]) Lapor Bug / Requests Menu''' , width = 56 , style = 'bold white' , title = '[bold red]•[bold yellow]•[bold green]•[bold white] Menu Script [bold red]•[bold yellow]•[bold green]•'))
        nel.append(Panel('''[italic bold green]ON
[italic bold green]ON
[italic bold green]ON
[italic bold green]ON''' , width = 7 , style = 'bold white'))
        cetak(Columns(nel))
        user = Console().input('[bold white]([bold green]•[bold white]) Pilih : ')
        if user in ['1' , '01']:
            Console(width=64).print(Panel('[italic green]Ingin Membuat Berapa Akun ?' , width = 64 , style = 'bold white') , justify = 'center')
            user1 = Console().input('[bold white]([bold green]•[bold white]) Jumlah : ')
            Console(width=64).print(Panel('[italic green]Jenis Kelamin Cewek/Cowok/Random' , width = 64 , style = 'bold white') , justify = 'center')
            user2 = Console().input('[bold white]([bold green]•[bold white]) Pilih P/L/R : ')
            if user2 in ['p' , 'P']:
                kelamin.append('p')
                Arif_xeyracode.UserCreate(int(user1))
            elif user2 in ['l' , 'L']:
                kelamin.append('l')
                Arif_xeyracode.UserCreate(int(user1))
            elif user2 in ['r' , 'R']:
                kelamin.append('r')
                Arif_xeyracode.UserCreate(int(user1))

        elif user in ['2' , '02']:
            Console(width=64).print(Panel('[italic green]Ingin Mengecek Akun Terkonfirmasi?' , width = 64 , style = 'bold white') , justify = 'center')
            user2 = Console().input('[bold white]([bold green]•[bold white]) Pilih Y/T : ')
            if user2 in ['y','Y']:
                try:
                    os.system('rm -rf /sdcard/Premium/AkunLive.txt')
                    file = open('/sdcard/Premium/AkunCreate.txt' , 'r').readlines()
                    Console(width = 64).print(Panel(f'[italic green]Total Akun Yang Ada Di File : [italic white] {len(file)}' , width = 64 , style = 'bold white') , justify = 'center')
                    for akun in file:
                        email , pasw , cokie = akun.split('|')[0] , akun.split('|')[1] , akun.split('|')[2]
                        userID = re.search('c_user=(\\d+)' , str(cokie)).group(1)
                        x = ses.get('https://www.facebook.com/profile.php?id='+str(userID)).text
                        if 'Konten Ini Tidak Tersedia Saat Ini' in str(x):cpx+=1
                        else:
                            try:
                                name = re.search('<title>(.*?)</title>' , str(x)).group(1)
                                tree = Tree(' ' , guide_style="bold grey100")
                                tree.add('[bold green]'+str(name))
                                tree.add('[bold green]'+str(userID))
                                tree.add('[bold green]'+str(pasw))
                                tree.add('[bold green]m.facebook.com/'+str(userID))
                                tree.add('[bold green]'+str(cokie))
                                cetak(tree)
                                with open('/sdcard/Premium/AkunLive.txt' , 'a') as x:
                                    x.write(userID +' - ' + pasw +' '+ "\n")
                                okx+=1
                            except:pass
                    cetak(Panel(f'[italic green]Total Akun Live [italic white] : {okx}\n[italic yellow]Total Akun Check[italic white] : {cpx}' , width = 64 , style = 'bold white'))
                except(Exception) as e:
                    print(e)
                    Console(width=64).print(Panel('[italic green]Anda Belum Mempunyai File Akun Hasil Create' , width = 64 , style = 'bold white') , justify = 'center')

            elif user2 in ['t','T']:
                try:
                    os.system('rm -rf /sdcard/Premium/AkunLiveN.txt')
                    file = open('/sdcard/Premium/NonConfirmCreate.txt' , 'r').readlines()
                    Console(width = 64).print(Panel(f'[italic green]Total Akun Yang Ada Di File : [italic white] {len(file)}' , width = 64 , style = 'bold white') , justify = 'center')
                    for akun in file:
                        email , pasw , cokie  , kode = akun.split('|')[0] , akun.split('|')[1] , akun.split('|')[2] , akun.split('|')[3]
                        userID = re.search('c_user=(\\d+)' , str(cokie)).group(1)
                        x = ses.get('https://www.facebook.com/profile.php?id='+str(userID)).text
                        if 'Konten Ini Tidak Tersedia Saat Ini' in str(x):cpx+=1
                        else:
                            try:
                                name = re.search('<title>(.*?)</title>' , str(x)).group(1)
                                tree = Tree(' ' , guide_style="bold grey100")
                                tree.add('[bold green]'+str(name))
                                tree.add('[bold green]'+str(userID))
                                tree.add('[bold green]'+str(pasw))
                                tree.add('[bold green]'+str(kode.replace('\n','')))
                                tree.add('[bold green]m.facebook.com/'+str(userID))
                                tree.add('[bold green]'+str(cokie))
                                cetak(tree)
                                with open('/sdcard/Premium/AkunLiveN.txt' , 'a') as x:
                                    x.write(userID + ' - ' + pasw + ' - ' + kode.replace('\n','') + ' - ' + '\n')
                                okx+=1
                            except:pass
                    cetak(Panel(f'[italic green]Total Akun Live [italic white] : {okx}\n[italic yellow]Total Akun Check[italic white] : {cpx}' , width = 64 , style = 'bold white'))
                except(Exception) as e:
                    print(e)
                    Console(width=64).print(Panel('[italic green]Anda Belum Mempunyai File Akun Hasil Create' , width = 64 , style = 'bold white') , justify = 'center')

        elif user in ['3','03']:
            bot = []
            bot.append(Panel('''[italic bold white]([bold green]01[italic bold white]) Bot Auto Add Friends
[italic bold white]([bold green]02[italic bold white]) Bot Auto React Post
[italic bold white]([bold green]03[italic bold white]) Bot Auto Komen
[italic bold white]([bold green]04[italic bold white]) Bot Auto Follow
[italic bold white]([bold green]05[italic bold white]) Bot Auto Join Group
[italic bold white]([bold green]06[italic bold white]) Bot Auto Set Profile [bold green] (Bio, Cover, Pp)''' , width = 56 , style = 'bold white' , title = '[bold red]•[bold yellow]•[bold green]•[bold white] Menu Bot [bold red]•[bold yellow]•[bold green]•'))
            bot.append(Panel('''[italic bold green]ON
[italic bold red]OFF
[italic bold red]OFF
[italic bold red]OFF
[italic bold red]OFF
[italic bold red]OFF''' , width = 7 , style = 'bold white'))
            cetak(Columns(bot))
            userX = Console().input('[bold white]([bold green]•[bold white]) Pilih : ')
            if userX in ['1','01']:
                cetak(Panel('''[italic bold white]([bold green]01[italic bold white]) Add Friends Dari Random Uid / Dari File Dump
[italic bold white]([bold green]02[italic bold white]) Add Friends Akun Ok''' , width = 64 , style = 'bold white'))
                userXX = Console().input('[bold white]([bold green]•[bold white]) Pilih : ')
                if userXX in ['1','01']:
                    Console(width = 64).print(Panel('[bold green]Ketik [bold white]R [bold green]Jika Ingin Add Lewat Random Uid , Ketik [bold white]F [bold green]Untuk Add Lewat File Yg Anda Berikan' , width = 64 , style = 'bold white') , justify = 'center')
                    userZ = Console().input('[bold white]([bold green]•[bold white]) Pilih : ')
                    if userZ in ['R','r']:
                        uid = ses.get('https://pastebin.com/raw/aNGic1MA').text
                        BotMenu().AddFriends1(uid)
                    elif userZ in ['f','F']:
                        BotMenu().AddFriends1()
                elif userXX in ['3','03']:
                    BotMenu().AddFriends3()

        elif user in ['0','00']:
            Console(width = 64).print(Panel(f'[italic green]Laporkan Bug Pada Sc Atau Requests Menu :)' , width = 64 , style = 'bold white') , justify = 'center')
            Console(width = 64).print(Panel(f'[italic green]Anda Akan Di Arahkan Ke Whatsapp Author!!' , width = 64 , style = 'bold white') , justify = 'center')
            os.system('xdg-open https://wa.me/6285767630210')
            Console(width = 64).print(Panel(f'[italic green]Terima Kasih Atas Sarannya. ArifXeyraKallDev!!' , width = 64 , style = 'bold white') , justify = 'center')

class CreateAcount:

    def __init__(Arif_xeyracode):
        Arif_xeyracode.ses = requests.Session()
        Arif_xeyracode.ok , Arif_xeyracode.cp , Arif_xeyracode.loop = 0 , 0 , 0
        Arif_xeyracode.headers , Arif_xeyracode.data = {} , {}
        Arif_xeyracode.data2 , Arif_xeyracode.headers2 = {} , {}
        Arif_xeyracode.DataGraphql = {}
        Arif_xeyracode.Params = {}
        Arif_xeyracode.HeadGraph = {}
        Arif_xeyracode.file = open('/sdcard/Premium/data.txt','r').read().splitlines()
        if proxy[0] in ['y','Y']:
            Arif_xeyracode.prox = {'http': random.choice(Arif_xeyracode.file)}
        elif proxy[0] in ['t','T']:
            Arif_xeyracode.prox = None
        # Foto Untuk Kelamin Perempuan
        if kelamin[0] in ['p','P']:
            Arif_xeyracode.Urls = str(random.choice(['https://i.pinimg.com/736x/98/0e/72/980e72bb5e88d824b42e8164b735b9a5.jpg','https://i.pinimg.com/736x/50/2d/5e/502d5e4df73ca296acfb85ead3f702f2.jpg' , 'https://i.pinimg.com/736x/81/30/16/81301600554be7606a4881c183437399.jpg']))
            Arif_xeyracode.Cover = str(random.choice(['https://i.pinimg.com/736x/5d/4d/18/5d4d1863f6d4fc9496fc1abb93007776.jpg' , 'https://i.pinimg.com/736x/22/59/40/22594070dead79796882c7975c9debc4.jpg' , 'https://i.pinimg.com/736x/c2/11/b7/c211b7476d74b693bf226307ad9dc4e3.jpg']))
       # Foto Untuk Kelamin Laki Laki
        elif kelamin[0] in ['L','l']:
            Arif_xeyracode.Urls = str(random.choice(['https://i.pinimg.com/736x/77/3d/e8/773de85e694e8f88ed08ff5509ae4355.jpg' , 'https://i.pinimg.com/736x/e5/65/c3/e565c31d3cdba8e304da1506659f5e86.jpg' , 'https://i.pinimg.com/736x/c0/9e/44/c09e44863fcfaa524812d911a8b9323c.jpg']))
            Arif_xeyracode.Cover = str(random.choice(['https://i.pinimg.com/736x/56/67/93/5667936906181a6fbe0501b471e2b5bd.jpg' , 'https://i.pinimg.com/736x/b2/09/dc/b209dce21b92e97bdb284415079ec592.jpg' , 'https://i.pinimg.com/736x/58/bf/59/58bf591519c4a7ec769aac603e8de5a0.jpg']))
       # Foto Untuk Kelamin Random :v
        elif kelamin[0] in ['R','r']:
            Arif_xeyracode.Urls = str(random.choice(['https://i.pinimg.com/736x/77/3d/e8/773de85e694e8f88ed08ff5509ae4355.jpg' , 'https://i.pinimg.com/736x/e5/65/c3/e565c31d3cdba8e304da1506659f5e86.jpg' , 'https://i.pinimg.com/736x/c0/9e/44/c09e44863fcfaa524812d911a8b9323c.jpg' , 'https://i.pinimg.com/736x/98/0e/72/980e72bb5e88d824b42e8164b735b9a5.jpg','https://i.pinimg.com/736x/50/2d/5e/502d5e4df73ca296acfb85ead3f702f2.jpg' , 'https://i.pinimg.com/736x/81/30/16/81301600554be7606a4881c183437399.jpg']))
            Arif_xeyracode.Cover = str(random.choice(['https://i.pinimg.com/736x/56/67/93/5667936906181a6fbe0501b471e2b5bd.jpg' , 'https://i.pinimg.com/736x/b2/09/dc/b209dce21b92e97bdb284415079ec592.jpg' , 'https://i.pinimg.com/736x/58/bf/59/58bf591519c4a7ec769aac603e8de5a0.jpg' , 'https://i.pinimg.com/736x/5d/4d/18/5d4d1863f6d4fc9496fc1abb93007776.jpg' , 'https://i.pinimg.com/736x/22/59/40/22594070dead79796882c7975c9debc4.jpg' , 'https://i.pinimg.com/736x/c2/11/b7/c211b7476d74b693bf226307ad9dc4e3.jpg']))
        Arif_xeyracode.GetBio = str(random.choice(['Tidak Ada Yg Tidak Mungkin Di Dunia Ini' , 'Keberanianmu untuk mencoba adalah kunci utama menuju pencapaian besar.' , 'Percayalah Pada Tuhanmu']))
        Arif_xeyracode.GetData()
        Arif_xeyracode.CreateBirthday()
        Arif_xeyracode.CreateEmail()
        Arif_xeyracode.CreateEmailIo()
        Arif_xeyracode.CreatePassword()
        Arif_xeyracode.InputData()

    def GetData(Arif_xeyracode):
        crome = random.randint(100,200)
        ua = str(random.choice([
           'Mozilla/5.0 (Linux; Android 13; SM-A715F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36',
           'Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36',
           'Mozilla/5.0 (Linux; Android 13; SM-A336B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36',
           'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.0.0 Mobile DuckDuckGo/5 Safari/537.36',
           'Mozilla/5.0 (Linux; arm_64; Android 13; Retroid Pocket 4 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.96 YaBrowser/24.4.3.96.00 SA/3 Mobile Safari/537.36',
           'Mozilla/5.0 (Linux; Android 13; 20JJS0CU1M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.113 Safari/537.36',
           'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-F7210) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36',
           'Mozilla/5.0 (Linux; arm_64; Android 13; 23021RAA2Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.1.88.00 SA/3 Mobile Safari/537.36',
           'Mozilla/5.0 (Linux; arm_64; Android 13; 23021RAAEG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaApp_Android/23.34.1 YaSearchBrowser/23.34.1 BroPP/1.0 SA/3 Mobile Safari/537.36',
           'Mozilla/5.0 (Linux; Android 13; SM-F936W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
           'Mozilla/5.0 (Linux; Android 13; 23030RAC7Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36 OPR/75.3.3978.72666   Opera Mobile 75',
           'Mozilla/5.0 (Linux; Android 13; 2303CRA44A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36'
        ]))

        headers = {
           'authority': 'web.facebook.com',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
           'referer': 'https://web.facebook.com/?lsrc=lbr&__req=5',
           'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': '"Linux"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'same-origin',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': ua,
        }

        params = {'entry_point': 'login'}
        pos = Arif_xeyracode.ses.get('https://web.facebook.com/r.php', params = params , headers = headers , cookies = Arif_xeyracode.ses.cookies.get_dict()).text

        Arif_xeyracode.headers.update({
           'authority': 'web.facebook.com',
           'accept': '*/*',
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
           'content-type': 'application/x-www-form-urlencoded',
           'origin': 'https://web.facebook.com',
           'referer': 'https://web.facebook.com/r.php?next=https%3A%2F%2Fm.facebook.com%2Fconfirmemail.php%3Fnext%3Dhttps%253A%252F%252Fweb.facebook.com%252F%253Flsrc%253Dlbr%26wtsid%3Drdr_0gANHXYCTrh4uk9DI&locale=id_ID&display=page&entry_point=login',
           'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-platform': '"Android"',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-origin',
           'user-agent': ua,
           'x-asbd-id': str(random.randrange(100000, 999999)),
           'x-fb-lsd': re.search('name="lsd" value="(.*?)"' , str(pos)).group(1)
        })

        jazoest = re.search('name="jazoest" value="(.*?)"' , str(pos)).group(1)
        lsd = re.search('name="lsd" value="(.*?)"' , str(pos)).group(1)
        ri = re.search('name="ri" value="(.*?)" ' , str(pos)).group(1)
        reg = re.search('name="reg_instance" value="(.*?)"', str(pos)).group(1)
        captcha = re.search('name="captcha_persist_data" value="(.*?)" ' , str(pos)).group(1)
        hs = re.search('"haste_session":"(.*?)"', str(pos)).group(1)
        rev = re.search('{"consistency":{"rev":(.*?)}', str(pos)).group(1)
        hsi = re.search(r'"hsi":"(.*?)"', str(pos)).group(1)
        spinr = re.search('"__spin_r":(.*?),', str(pos)).group(1)
        spint = re.search('"__spin_t":(.*?),', str(pos)).group(1)

        Arif_xeyracode.data.update({
           'jazoest': jazoest,
           'lsd': lsd,
           'ri': ri,
           'reg_instance': reg,
           'captcha_persist_data': captcha,
           '__hs': hs,
           '__rev': rev,
           '__hsi': hsi,
           '__spin_r': spinr,
           '__spin_t': spint,
        })

    def DelayCreate(Arif_xeyracode , teks , jum):
        hihi = ['+','+','-','•','!','?']
        for x in range(int(jum)):
            jum-=1
            Console().print(f'\r[italic white][[italic green]{random.choice(hihi)}[italic white]] {teks}  [italic white]{jum} Detik        ' , end = '\r');time.sleep(1)

    def CreateBirthday(Arif_xeyracode):
        tanggal = str(random.randint(1,5))
        bulan = str(random.randint(1,12))
        tahun = str(random.randint(1990, 2005))
        return tanggal , bulan , tahun

    def  CreateEmail(Arif_xeyracode):
        anb = random.choice(['abcdefghijklmnopqrstuvwxyz'])
        mail = ''.join(random.choice(anb) for _ in range(random.randint(8,12)))
        gabung = mail + '@fexbox.org'
        return gabung

    def CreateEmailIo(Arif_xeyracode):
        headers = {
           'authority': 'api.internal.temp-mail.io',
           'accept': 'application/json, text/plain, */*',
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
           'application-name': 'web',
           'application-version': '2.4.2',
           'origin': 'https://temp-mail.io',
           'referer': 'https://temp-mail.io/',
           'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-platform': '"Android"',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-site',
           'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
        }
        domain = str(random.choice(['zlorkun.com','somelora.com','vvatxiy.com','dygovil.com','tidissajiiu.com','vafyxh.com','knmcadibav.com','smykwb.com','wywnxa.com','qacmjeq.com','qejjyl.com','zvvzuv.com','bltiwd.com','qzueos.com','vwhins.com','jxpomup.com','ibolinva.com','wyoxafp.com','osxofulk.com' , 'jkotypc.com']))
        nama = ''.join(random.choice(random.choice('abcdefghijklmnopqrstuvwxyz')) for _ in range(int(random.randint(8,10))))
        data = {'name': nama,'domain': domain}
        mail = Arif_xeyracode.ses.post('https://api.internal.temp-mail.io/api/v3/email/new', json = data).json()['email']
        return mail

    def CreatePassword(Arif_xeyracode):
        abs = random.choice(['abcdefghijklmnopqrstuvwxyz'])
        abc = ''.join(random.choice(abs) for _ in range(random.randint(8,12)))
        nom = random.randint(111,555)
        gabung = abc + str(nom)
        return gabung

    def InputData(Arif_xeyracode):
        global cp , ok
        # Input Kelamin Perempuan
        if kelamin[0] in ['p','P']:
            fake = Faker('id_ID')
            depan = fake.first_name_female()
            belakang = fake.last_name_female()
            jenis = 'Perempuan'
            sex = '1'

        # input Kelamin Laki Laki
        elif kelamin[0] in ['l','L']:
            fake = Faker('id_ID')
            depan = fake.first_name_male()
            belakang = fake.last_name_male()
            jenis = 'Laki-Laki'
            sex = '2'

       # Input Kelamin Random
        elif kelamin[0] in ['r','R']:
            fake = Faker('id_ID')
            depanL = fake.first_name_male()
            belakangL = fake.last_name_male()
            jenisL = 'Laki-Laki'
            sexL = '2'
            depanP = fake.first_name_female()
            belakangP = fake.last_name_female()
            jenisP = 'Perempuan'
            sexP = '1'
            laki = depanL+'|'+belakangL+'|'+jenisL+'|'+sexL
            perempuan = depanP+'|'+belakangP+'|'+jenisP+'|'+sexP
            gabung = str(random.choice([laki , perempuan]))
            depan , belakang , jenis , sex = gabung.split('|')

        # Tanggal Lahir
        TanggalLahir = Arif_xeyracode.CreateBirthday()
        tanggal = TanggalLahir[0]
        bulan = TanggalLahir[1]
        tahun = TanggalLahir[2]

        # Email & Pasword
        Email = Arif_xeyracode.CreateEmailIo()
        if autopasw[0] in ['y','Y']:
            pasw = Arif_xeyracode.CreatePassword()
        elif autopasw[0] in ['t','T']:
            pasw = autopasw[1]

        Arif_xeyracode.data.update({
           'firstname': depan,
           'lastname': belakang,
           'birthday_day': tanggal,
           'birthday_month': bulan,
           'birthday_year': tahun,
           'birthday_age': '',
           'did_use_age': 'false',
           'sex': sex,
           'preferred_pronoun': '',
           'custom_gender': '',
           'reg_email__': Email,
           'reg_email_confirmation__': '',
           'reg_passwd__': f'#PWD_BROWSER:0:{str(int(time.time()))}:{pasw}',
           'referrer': '',  
           'asked_to_login': '0',
           'use_custom_gender': '',
           'terms': 'on',
           'ns': '0',
           'action_dialog_shown': '',
           'invid': '',
           'a': '',
           'oi': '',
           'locale': 'id_ID',
           'app_bundle': '',
           'app_data': '',
           'reg_data': '',
           'app_id': '',
           'fbpage_id': '',
           'reg_oid': '',
           'openid_token': '',
           'uo_ip': '',
           'guid': '',
           'key': '',
           're': '',
           'mid': '',
           'fid': '',
           'reg_dropoff_id': '',
           'reg_dropoff_code': '',
           'ignore': 'captcha|reg_email_confirmation__',
           'captcha_response': '',
           '__user': '0',
           '__a': '1',
           '__req': '5',
           'dpr': '1',
           '__ccg': 'EXCELLENT',
           '__s': '',
           '__dyn': '',
           '__csr': '',
           '__spin_b': 'trunk',
        })
        poss = Arif_xeyracode.ses.post('https://web.facebook.com/ajax/register.php', headers = Arif_xeyracode.headers, data = Arif_xeyracode.data , cookies = Arif_xeyracode.ses.cookies.get_dict() , proxies = Arif_xeyracode.prox, allow_redirects = True).text
        if 'c_user' in Arif_xeyracode.ses.cookies.get_dict():
            next = re.search(r'"redirect":"(.*?)"' , str(poss)).group(1).replace(r'\/','/')
            posss = Arif_xeyracode.ses.get(next , cookies = Arif_xeyracode.ses.cookies.get_dict() , allow_redirects = True).text
            cokie = '; '.join([str(x)+"="+str(y) for x,y in Arif_xeyracode.ses.cookies.get_dict().items()])
            if 'Beri tahu kami bahwa email ini milik Anda. Masukkan kode dalam email yang dikirim ke' in str(posss):
                data = Tree(Panel('   [bold green]Data Akun' , width = 20) , guide_style="bold grey100")
                data.add(f'Username : [bold green]{depan} {belakang}')
                data.add(f'Pasword  : [bold green]{pasw}')
                data.add(f'Email    : [bold green]{Email}')
                data.add(f'Ttl      : [bold green]{tanggal}-{bulan}-{tahun}')
                data.add(f'kelamin  : [bold green]{jenis}')
                cok = Tree(Panel('   [bold green]Cookie & UserAgent' , width = 29) , guide_style="bold grey100")
                cok.add(f'Cookie    : [bold green]{cokie}')
                cok.add(f'UserAgent : [bold green]{Arif_xeyracode.headers["user-agent"]}')
                gabung = Tree(Panel('         [bold green]Berhasil Buat Akun' , width = 40) , guide_style="bold grey100")
                gabung.add(data , style = 'bold white')
                gabung.add(cok , style = 'bold white')

                lsd = re.search('"token":"(.*?)"},323', str(posss)).group(1)
                dtsg = re.search('name="fb_dtsg" value="(.*?)" ' , str(posss)).group(1)
                jazoest = re.search('name="jazoest" value="(.*?)" ',str(posss)).group(1)
                spinr = re.search('"__spin_r":(.*?),', str(posss)).group(1)
                spint = re.search('"__spin_t":(.*?),', str(posss)).group(1)
                hs = re.search('"haste_session":"(.*?)"', str(posss)).group(1)
                rev = re.search('{"consistency":{"rev":(.*?)}', str(posss)).group(1)
                hsi = re.search(r'"hsi":"(.*?)"', str(posss)).group(1)
                user = Arif_xeyracode.ses.cookies.get_dict()['c_user']

                Arif_xeyracode.headers2.update({
                  'authority': 'web.facebook.com',
                  'accept': '*/*',
                  'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                  'content-type': 'application/x-www-form-urlencoded',
                  'origin': 'https://web.facebook.com',
                  'referer': 'https://web.facebook.com/confirmemail.php?next='+next,
                  'sec-ch-prefers-color-scheme': 'light',
                  'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                  'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-ch-ua-model': '""',
                  'sec-ch-ua-platform': '"Linux"',
                  'sec-ch-ua-platform-version': '""',
                  'sec-fetch-dest': 'empty',
                  'sec-fetch-mode': 'cors',
                  'sec-fetch-site': 'same-origin',
                  'user-agent': Arif_xeyracode.headers['user-agent'],
                  'x-asbd-id': str(random.randrange(100000, 999999)),
                  'x-fb-lsd': lsd,
               })
                Arif_xeyracode.data2.update({
                  'jazoest': jazoest,
                  'fb_dtsg': dtsg,
                  'lsd': lsd,
                  '__spin_r': spinr,
                  '__spin_t': spint,
                  '__hsi': hsi,
                  '__rev': rev,
                  '__hs': hs,
                  '__user': user
               })
                Arif_xeyracode.GetCodeV2(gabung , Email , pasw , cokie)
            elif 'checkpoint' in str(posss):
                data = Tree(Panel('   [bold green]Data Akun' , width = 20) , guide_style="bold grey100")
                data.add(f'Username : [bold green]{depan} {belakang}')
                data.add(f'Pasword  : [bold green]{pasw}')
                data.add(f'Email    : [bold green]{Email}')
                data.add(f'Ttl      : [bold green]{tanggal}-{bulan}-{tahun}')
                data.add(f'kelamin  : [bold green]{jenis}')
                cok = Tree(Panel('   [bold green]Cookie & UserAgent' , width = 29) , guide_style="bold grey100")
                cok.add(f'Cookie   : [bold green]{cokie}')
                cok.add(f'UserAgent : [bold green]{Arif_xeyracode.headers["user-agent"]}')
                gabung = Tree(Panel('         [bold green]Berhasil Buat Akun' , width = 40) , guide_style="bold grey100")
                gabung.add(data , style = 'bold white')
                gabung.add(cok , style = 'bold white')
                cetak(gabung)
                cp+=1

    def GetCodeV2(Arif_xeyracode , gabung , Email , pasw , cokie):
        global ok
        headers = {
           'authority': 'api.internal.temp-mail.io',
           'accept': 'application/json, text/plain, */*',
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
           'application-name': 'web',
           'application-version': '2.4.2',
           'origin': 'https://temp-mail.io',
           'referer': 'https://temp-mail.io/',
           'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-platform': '"Android"',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-site',
           'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
        }
        mail = Arif_xeyracode.data["reg_email__"]
        getcode = Arif_xeyracode.ses.get(f'https://api.internal.temp-mail.io/api/v3/email/{mail}/messages').json()
        teks = 'Menunggu Kode Konfirmasi'
        Arif_xeyracode.DelayCreate(teks , 20)
        try:
            ges = getcode[0]['subject']
            cods = re.search('FB-(.*?) adalah kode konfirmasi' , str(ges)).group(1)
        except(Exception) as e:Arif_xeyracode.GetCodeV2(gabung , Email , pasw , cokie)
        verif = Tree(Panel('  [italic green]Verifikasi Akun Anda' , width = 29) , guide_style="bold grey100")
        try:prox = Arif_xeyracode.prox["http"]
        except:prox = Arif_xeyracode.prox
        if autoconfirm[0] in ['y','Y']:
            with open('/sdcard/Premium/AkunCreate.txt' , 'a') as fu:
                fu.write(Email +'|' +pasw +'|'+ cokie + '\n')
            verif.add(f'Kode   : [italic green]{cods}')
            verif.add(f'Proxy  : [italic green]{prox}')
            Arif_xeyracode.ConfirmEmail(cods , gabung , verif)
        elif autoconfirm[0] in ['t','T']:
            with open('/sdcard/Premium/NonConfirmCreate.txt' , 'a') as fu:
                fu.write(Email +'|' +pasw +'|'+ cokie + '|' +cods + '\n')
            verif.add(f'Kode     : [italic green]{cods}')
            verif.add(f'Proxy    : [italic green]{prox}')
            verif.add('Status   : [italic green]Akun Belum Terkonfirmasi')
            gabung.add(verif , style = 'bold white')
            cetak(gabung)
            ok+=1

    def GetCoode(Arif_xeyracode , gabung):
        headers = {
           'authority': 'tempmail.plus',
           'accept': 'application/json, text/javascript, */*; q=0.01',
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
           'referer': 'https://tempmail.plus/en/',
           'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-platform': '"Android"',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-origin',
           'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
           'x-requested-with': 'XMLHttpRequest'
        }
        params = {'email': Arif_xeyracode.data['reg_email__'],'limit': '20','epin': ''}
        posc = Arif_xeyracode.ses.get('https://tempmail.plus/api/mails', params=params , headers = headers).json()
        teks = 'Menunggu Kode Konfirmasi'
        Arif_xeyracode.DelayCreate(teks , 20)
        try:
            ges = posc['mail_list'][0]['subject']
            cods = re.search('FB-(.*?) adalah kode konfirmasi' , str(ges)).group(1)
        except:Arif_xeyracode.GetCoode(gabung)
        verif = Tree(Panel('  [italic green]Verifikasi Akun Anda' , width = 29) , guide_style="bold grey100")
        verif.add(f'Kode   : [italic green]{cods}')
        Arif_xeyracode.ConfirmEmail(cods , gabung , verif)

    def ConfirmEmail(Arif_xeyracode , code , gabung , verif):
        global ok
        params = {
           'next': 'https://web.facebook.com/?lsrc=lbr',
           'cp': Arif_xeyracode.data['reg_email__'],
           'from_cliff': '1',
           'conf_surface': 'hard_cliff',
           'event_location': 'cliff',
        }
        Arif_xeyracode.data2.update({
           'code': code,
           'source_verified': 'www_reg',
           'confirm': '1',
           '__a': '1',
           '__req': '5',
           'dpr': '1',
           '__ccg': 'EXCELLENT',
           '__s': '',
           '__dyn': '',
           '__csr': '',
           '__spin_b': 'trunk',
        })
        possss = Arif_xeyracode.ses.post('https://web.facebook.com/confirm_code/dialog/submit/' , params = params , data = Arif_xeyracode.data2 , cookies = Arif_xeyracode.ses.cookies.get_dict() , allow_redirects = True).text
        cokie = '; '.join([str(x)+"="+str(y) for x,y in Arif_xeyracode.ses.cookies.get_dict().items()])
        verif.add('Status : [italic green]Berhasil Konfirmasi Akun')
        gabung.add(verif , style = 'bold white')
        if 'y' in autoset:Arif_xeyracode.SetBio(gabung)
        elif 't' in autoset:cetak(gabung)

    def SetBio(Arif_xeyracode , gabung):
        global cp
        teks = 'Beralih Ke Halaman Profile Jeda '
        Arif_xeyracode.DelayCreate(teks , 5)
        cokie = '; '.join([str(x)+"="+str(y) for x,y in Arif_xeyracode.ses.cookies.get_dict().items()])
        user = re.search('c_user=(\\d+)' , str(cokie)).group(1)
        Arif_xeyracode.HeadGraph.update({
           'authority': 'web.facebook.com',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
           'cache-control': 'max-age=0',
           'dpr': '1.7000000476837158',
           'sec-ch-prefers-color-scheme': 'light',
           'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
           'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-model': '""',
           'sec-ch-ua-platform': '"Linux"',
           'sec-ch-ua-platform-version': '""',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'same-origin',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
           'viewport-width': '980',
        })
        link = Arif_xeyracode.ses.get(f'https://web.facebook.com/profile.php?id={user}&_rdc=1&_rdr', cookies = {'cookie' : cokie} , allow_redirects = True).text

        teks = 'Membuat Bio Profile Jeda'
        Arif_xeyracode.DelayCreate(teks , 5)
        jazoest = re.search('jazoest=(\\d+)' , str(link)).group(1)
        user = re.search('"USER_ID":"(.*?)"' , str(link)).group(1)
        lsd = re.search('"token":"(.*?)"},323' , str(link)).group(1)
        hsi = re.search('"hsi":"(.*?)"' , str(link)).group(1)
        hs = re.search('"haste_session":"(.*?)"' , str(link)).group(1)
        rev = re.search('"rev":(\\d+)' , str(link)).group(1)
        spinr = re.search('"__spin_r":(\\d+)' , str(link)).group(1)
        spint = re.search('"__spin_t":(\\d+)' , str(link)).group(1)
        dtsg = re.search('"token":"(.*?)"},258' , str(link)).group(1)

        Arif_xeyracode.DataGraphql.update({
           'av': user,
           '__aaid': '0',
           '__user': user,
           '__a': '1',
           '__req': '13',
           '__hs': hs,
           'dpr': '1',
           '__ccg': 'EXCELLENT',
           '__rev': rev,
           '__s': '',
           '__hsi': hsi,
           '__dyn':'',
           '__csr': '',
           '__comet_req': '15',
           'fb_dtsg': dtsg,
           'jazoest': jazoest,
           'lsd': lsd,
           '__spin_r': spinr,
           '__spin_b': 'trunk',
           '__spin_t': spint,
        })

        Arif_xeyracode.Params.update({
           'av': user,
           '__aaid': '0',
           '__user': user,
           '__a': '1',
           '__req': '13',
           '__hs': hs,
           'dpr': '1',
           '__ccg': 'EXCELLENT',
           '__rev': rev,
           '__s': '',
           '__hsi': hsi,
           '__dyn': '',
           '__csr': '',
           '__comet_req': '15',
           'fb_dtsg': dtsg,
           'jazoest': jazoest,
           'lsd': lsd,
           '__spin_r': spinr,
           '__spin_b': 'trunk',
           '__spin_t': spint,
        })

        Arif_xeyracode.DataGraphql.update({
           'fb_api_caller_class': 'RelayModern',
           'fb_api_req_friendly_name': 'ProfileCometSetBioMutation',
           'variables': json.dumps({"input":
               {
               "attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1735565985577,197676,190055527696468,,",
               "bio": Arif_xeyracode.GetBio,
               "publish_bio_feed_story": False,
               "actor_id": user,
               "client_mutation_id":"1"
               },
               "hasProfileTileViewID": True,
               "profileTileViewID": f"profile_tile_view:{user}:intro:intro_bio:intro_card_bio:profile_timeline:1",
               "scale":1,
               "useDefaultActor": False
           }),
           'server_timestamps': 'true',
           'doc_id': '9404371009573934'
        })
        pos = Arif_xeyracode.ses.post('https://web.facebook.com/api/graphql/', data = Arif_xeyracode.DataGraphql , cookies = {'cookie' : cokie} , allow_redirects = True).text
        if 'profile_intro_card' in str(pos):
            teks = '[italic green]Berhasil Membuat Bio [italic white] Jeda'
            Arif_xeyracode.DelayCreate(teks , 10)
            Arif_xeyracode.SetCover(gabung)
        else:
            setprof = Tree(Panel('    [italic green]Auto Set Profile' , width = 29) , guide_style="bold grey100")
            setprof.add('Status : [italic red]Gagal Menambahkan Bio')
            setprof.add('Status : [italic red]Gagal Menambahkan Foto Sampul')
            setprof.add('Status : [italic red]Gagal Menambahkan Foto Profile')
            gabung.add(setprof , style = 'bold white')
            cetak(gabung)
            cp+=1

    def SetCover(Arif_xeyracode , gabung):
        teks = 'Membuat Foto Cover Profile Jeda '
        Arif_xeyracode.DelayCreate(teks , 5)
        cokie = '; '.join([str(x)+"="+str(y) for x,y in Arif_xeyracode.ses.cookies.get_dict().items()])
        user = re.search('c_user=(\\d+)' , str(cokie)).group(1)
        Arif_xeyracode.Params.update({'profile_id': user})
        files = {'file': ('image.jpg', urllib.request.urlopen(Arif_xeyracode.Cover).read())}
        pos = Arif_xeyracode.ses.post('https://web.facebook.com/profile/cover/comet_upload/', cookies = {'cookie' : cokie}, params = Arif_xeyracode.Params, files = files).text
        if 'checkpoint' in str(pos):Arif_xeyracode.SetProfile(gabung)
        elif 'blurredURI' in str(pos):
            fbid = re.search('"fbid":"(.*?)"' , str(pos)).group(1)
            Arif_xeyracode.DataGraphql.update({
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'ProfileCometCoverPhotoUpdateMutation',
            'variables': json.dumps({
                "input":{
                    "attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1736066501949,746649,190055527696468,,",
                    "cover_photo_id":fbid,
                    "focus":{
                       "x":0.5,
                       "y":0.4996502933450491
                    },
                    "target_user_id": user,
                    "actor_id":user,
                    "client_mutation_id":"2"
                },
                "scale":1,
                "contextualProfileContext": None
            }),
            'server_timestamps': 'true',
            'doc_id': '9129648493722372',
            })
            pos1 = Arif_xeyracode.ses.post('https://web.facebook.com/api/graphql/' , data = Arif_xeyracode.DataGraphql , cookies = {'cookie' : cokie} , allow_redirects = True).text
            if 'user_update_cover_photo' in str(pos1):
                teks = '[italic green]Berhasil Membuat Cover [italic white] Jeda'
                Arif_xeyracode.DelayCreate(teks , 10)
                Arif_xeyracode.SetProfile(gabung)
            else:
                teks = '[italic green]Berhasil Membuat Cover [italic white] Jeda'
                Arif_xeyracode.DelayCreate(teks , 10)
                Arif_xeyracode.SetProfile(gabung)

    def SetProfile(Arif_xeyracode , gabung):
        global ok
        cokie = '; '.join([str(x)+"="+str(y) for x,y in Arif_xeyracode.ses.cookies.get_dict().items()])
        user = re.search('c_user=(\\d+)' , str(cokie)).group(1)
        teks = 'Membuat Foto Profile Jeda'
        Arif_xeyracode.DelayCreate(teks , 5)
        Arif_xeyracode.Params.update({'profile_id': user,'photo_source': '57',})
        files = {'file': ('image.jpg', urllib.request.urlopen(Arif_xeyracode.Urls).read())}
        pos = Arif_xeyracode.ses.post('https://web.facebook.com/profile/picture/upload/', cookies = {'cookie' : cokie}, params = Arif_xeyracode.Params, files = files).text
        if 'checkpoint' in str(pos):
            setprof = Tree(Panel('   [italic green]Auto Set Profile' , width = 29))
            setprof.add('Status : [italic red]Gagal Menambahkan Bio')
            setprof.add('Status : [italic red]Gagal Menambahkan Foto Sampul')
            setprof.add('Status : [italic red]Gagal Menambahkan Foto Profile')
            gabung.add(setprof , style = 'bold white')
            cetak(gabung)
        elif 'profileID' in str(pos):
            fbid = re.search('"fbid":"(.*?)"' , str(pos)).group(1)
            Arif_xeyracode.DataGraphql.update({
           'fb_api_caller_class': 'RelayModern',
                        'fb_api_req_friendly_name': 'ProfileCometProfilePictureSetMutation',
                        'variables': json.dumps({
                                'input': {
                                        'attribution_id_v2': 'ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1729674295794,691444,190055527696468,,',
                                        'caption': '',
                                        'existing_photo_id': fbid,
                                        'expiration_time': None,
                                        'profile_id': user,
                                        'profile_pic_method': 'EXISTING',
                                        'profile_pic_source': 'TIMELINE',
                                        'scaled_crop_rect': {
                                                'height': 1,
                                                'width': 1,
                                                'x': 0,
                                                'y': 0 },
                                        'skip_cropping': True,
                                        'actor_id': user,
                                        'client_mutation_id': '2' },
                                'isPage': False,
                                'isProfile': True,
                                'sectionToken': 'UNKNOWN',
                                'collectionToken': 'UNKNOWN',
                                'scale': 3,
                                '__relay_internal__pv__ProfileGeminiIsCoinFlipEnabledrelayprovider': False
                        }),
                        'server_timestamps': 'true',
                        'doc_id': '28132579203008372'
                        })
            pos1 = Arif_xeyracode.ses.post('https://web.facebook.com/api/graphql/' , data = Arif_xeyracode.DataGraphql , cookies = {'cookie' : cokie} , allow_redirects = True).text
            if 'profilePhoto' in str(pos1):
                setprof = Tree(Panel('    [italic green]Auto Set Profile' , width = 29) , guide_style="bold grey100")
                setprof.add('Status : [italic green]Berhasil Menambahkan Bio')
                setprof.add('Status : [italic green]Berhasil Menambahkan Foto Sampul')
                setprof.add('Status : [italic green]Berhasil Menambahkan Foto Profile')
                gabung.add(setprof , style = 'bold white')
                cetak(gabung)
                ok+=1

def cekdurasi(created , exp , key):
    tahun , bulan , tanggal = exp.split('T')[0].split('-')
    opoki = datetime(int(tahun) , int(bulan) , int(tanggal))
    opoke = opoki.strftime('%Y-%m-%d %H:%M:%S')
    opoku = datetime.strptime(opoke , '%Y-%m-%d %H:%M:%S')
    ceku = opoku - datetime.now()
    if ceku.days<1:
        keyu = str(ceku).split('.')[0]
        nol = keyu.split(':')[0]
        if int(nol)<1:
            cetak(f'[bold white]([bold red]×[bold white]) Lisensi Anda Telah Berakhir Pada : {tahun}-{bulan}-{tanggal}')
            os.remove('/Datakey/.licenkey')
        else:
            cetak('\n[bold white]([bold green]©[bold white]) Arif Xeyracode')
            cetak('\n[bold white]([bold green]•[bold white]) Lisensi Terdaftar')
            cetak(f'[bold white]([bold green]•[bold white]) Key     : {key}')
            cetak(f'[bold white]([bold green]•[bold white]) Create  : {created.split("T")[0]}')
            cetak(f'[bold white]([bold green]•[bold white]) Expires : {exp.split("T")[0]}')
            cetak(f'[bold white]([bold green]•[bold white]) Sisa    : {keyu}')
            open('/Datakey/.licenkey' , 'w').write(key)
    else:
        sisa = str(ceku).split(',')[0]
        cetak('\n[bold white]([bold green]©[bold white]) Arif Xeyracode')
        cetak('\n[bold white]([bold green]•[bold white]) Lisensi Terdaftar')
        cetak(f'[bold white]([bold green]•[bold white]) Key     : {key}')
        cetak(f'[bold white]([bold green]•[bold white]) Create  : {created.split("T")[0]}')
        cetak(f'[bold white]([bold green]•[bold white]) Expires : {exp.split("T")[0]}')
        cetak(f'[bold white]([bold green]•[bold white]) Sisa    : {sisa}')
        open('/Datakey/.licenkey' , 'w').write(key)

def lisensi():
    try:
        key = open('/Datakey/.licenkey' , 'r').read()
    except(FileNotFoundError):
        os.system('clear')
        cetak(f'[bold white]([bold green]01[bold white]) Beli Lisensi\n[bold white]([bold green]02[bold white]) Masukan Lisensi')
        user = Console().input('\n[bold white]([bold green]•[bold white]) Pilih : ')
        if user in ['01','1']:
            cetak(f'[bold white]([bold green]•[bold white]) Kamu Akan Diarahkan Ke Whatsapp Author')
            os.system('xdg-open https://wa.me/+6285767630210?text=assalamualaikum%20bang%20ArifXeyracode%20Dev,%20beli%20license%20dong')
            exit()
        elif user in ['02','2']:
            key = Console().input('[bold white]([bold green]•[bold white]) Masukan Lisensi : ')
    try:
        link = ses.get('https://api.cryptolens.io/api/key/GetKey?token=%s&ProductId=%s&Key=%s&Sign=True'%(token , id , key)).json()['licenseKey']
        block = link['block']
        created = link['created']
        expires = link['expires']
        if block == False:
            cekdurasi(created , expires , key)
            time.sleep(5)
            TanyaTanya().Menu()
        elif block == True:
            cetak('[bold white]([bold red]×[bold white]) Maaf Lisensi Anda Telah Di Blokir')
            os.remove('/Datakey/.licenkey')
    except(FileNotFoundError) as s:pass
    except(Exception) as e:
        cetak(f'[bold white]([bold red]×[bold white]) Lisensi Anda Tidak Valid')

if __name__ == '__main__':
    try:os.mkdir('Datakey')
    except:pass
    lisensi()