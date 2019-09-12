#!/usr/bin/env python

import requests, json, os, sys, signal, platform

if platform.system().lower() == "windows":
  os.system('color')

default_filename='youtube_file'
if len(sys.argv) != 2:
  print('\n    \033[1;31mpy\033[0m\033[1;77mtube v1.0\033[0m')
  print('    \033[1;77mcoded by:\033[1;31m github.com/LenteraHacker\033[0m\n')
  print('\n\033[1;77m[\033[0m\033[1;31m+\033[0m\033[1;77m]\033[0m\033[1;77m Pemakaian: decryptbabi.py youtube_url_kode\033[0m')
  print('\033[1;77m[\033[0m\033[1;31m+\033[0m\033[1;77m]\033[0m\033[1;93m E.g.: python decryptbabi.py Nd6qN167wKo\033[0m')
  exit()

user_agent = 'Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0'
sess = requests.Session()
yt_req = sess.post('https://node3.youtubnow.com/node/', headers={
        'Referer': 'https://www.youtubnow.com/',
        'Content-Type': 'application/json',
        'origin': 'https://www.youtubnow.com',
        'user-agent': user_agent
 }, json={"url":"www.youtube.com/watch?v="+sys.argv[1]})
params=yt_req.json()

def humanbytes(B):
  B = float(B)
  KB = float(1024)
  MB = float(KB ** 2)
  GB = float(KB ** 3)
  TB = float(KB ** 4)

  if B < KB:
    return '{0} {1}'.format(B, 'Bytes' if 0 == B > 1 else 'Byte')
  elif KB <= B < MB:
    return '{0:.2f} KB'.format(B/KB)
  elif MB <= B < GB:
    return '{0:.2f} MB'.format(B/MB)
  elif GB <= B < TB:
    return '{0:.2f} GB'.format(B/GB)
  elif TB <= B:
    return '{0:.2f} TB'.format(B/TB)


def format_types():
  _list1=params['formats']
  if sys.version_info[0] < 3:
    title=params['title'].encode('utf-8')
  else:
    title=params['title']
  print ('\n\033[1;77m[\033[0m\033[1;31m+\033[0m\033[1;77m]\033[0m \033[1;93mTitle:\033[0m \033[1;77m {} \033[0m\n'.format(title))

  for x in range(0,len(_list1)):

     list_url.append(params['formats'][x]['url'])
     list_type.append(params['formats'][x]['type'])
     list_filesize.append(params['formats'][x]['fileSize'])

     try: 
        list_size.append(params['formats'][x]['size'])
     except KeyError:
        try:
           list_size.append(params['formats'][x]['quality_label'])
        except KeyError:
           list_size.append('Null')


  for y in range(0,len(list_type)):
    print('\033[1;93m{}:\033[0m type: {}, resolution: {}, size: {}'.format(y,list_type[y].split()[0],list_size[y], humanbytes(list_filesize[y])))
  print('\033[1;31m99:\033[0m\033[1;77m Exit\033[0m')


url_number=0
def download_wget(url_number):

  if "webm" in list_type[url_number]:
    os.system('wget -O \'{0}.webm\' \'{1}\''.format(file_name,list_url[url_number]))

  elif  "mp4" in list_type[url_number]:
    os.system('wget -O \'{0}.mp4\' \'{1}\''.format(file_name,list_url[url_number]))

  else:
    os.system('wget -O \'{0}.mp4\' \'{1}\''.format(file_name,list_url[url_number]))


def download(url_number):

  sess = requests.Session()
  r = sess.get(list_url[url_number], allow_redirects=True)
  if "webm" in list_type[url_number]:
    open('%s.webm' % file_name, 'wb').write(r.content)

  elif  "mp4" in list_type[url_number]:
    open('%s.mp4' % file_name, 'wb').write(r.content)

  else:
    open('%s.mp4' % file_name, 'wb').write(r.content)

def shutdown(signal, frame):
  print('\n\033[1;77m[\033[0m\033[1;31m+\033[0m\033[1;77m] Ctrl + c was pressed, exiting...\033[0m') 
  sys.exit()

print('\n\033[1;77m[\033[0m\033[1;31m+\033[0m\033[1;77m]\033[0m\033[1;31m py\033[0m\033[1;77mtube v1.0\033[0m')  
while True:

 signal.signal(signal.SIGINT, shutdown)
 list_filesize=[]
 list_size=[]
 list_type=[]
 list_url=[]
 format_types()

 choose=int(input('\n\033[1;77m[\033[0m\033[1;31m+\033[0m\033[1;77m] Pilih pilhan untuk download: \033[0m'))

 if choose in range(len(list_type)):

  if sys.version_info[0] < 3:
   file_name=raw_input('\033[1;77m[\033[0m\033[1;31m+\033[0m\033[1;77m] Filename: ')

  else:
   file_name=input('\033[1;77m[\033[0m\033[1;31m+\033[0m\033[1;77m] Filename: ')

  if file_name == '':
     file_name=default_filename

  print('\033[1;77m 1: Python requests\033[0m')
  print('\033[1;77m 2: Wget\033[0m')
  download_option=int(input('\033[1;77m[\033[0m\033[1;31m+\033[0m\033[1;77m] Download menggunakan: \033[0m'))

  if download_option == 1:
    print('\033[1;77m[\033[0m\033[1;31m+\033[0m\033[1;77m] Downloading, tunggu sebentar...\033[0m')
    download(choose)

  elif download_option == 2:
    print('\033[1;77m[\033[0m\033[1;31m+\033[0m\033[1;77m] Downloading, please wait, it can take a long time...\033[0m')
    download_wget(choose)

  else:
    print('\033[1;77m[\033[0m\033[1;31m+\033[0m\033[1;77m] Downloading menggunakan Python requests, mohon bersabar...\033[0m')
    download(choose)
   
 elif choose == 99:
   exit()
 else:
   print('\033[1;77m[\033[0m\033[1;31m+\033[0m\033[1;77m]\033[0m \033[1;93mPilihan tidak diketahui!\033[0m')


