#!/usr/bin/env python3

import iterm2
import time
import threading
from some import pkey, cT0, cT1, cT2, cT3_0, cT3_1, cT3_2, cT3_3, cT4, cT5, cT5
global glWin
import asyncio
timeout_connect = 3
timeout_simple = 1

async def dynamic_call(selfi):
    method_name = ' tab' + str(selfi) 
    print("method_name = "+str(method_name))
    
    # if selfi == 0:
    #     tab0()
    #     iterm2.run_until_complete(tab0)
    
    await eval(method_name+"()") 

        
async def tabAction(iter):
    await dynamic_call(iter)
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # print("\ntab"+str(iter))
    # loop.run_until_complete(  dynamic_call(iter)  )
               
async def tab0():
    global glWin
    tabW = glWin.tabs[0]

    for sesCur in tabW.sessions:
        await sesCur.async_send_text(cT0)
        time.sleep(timeout_connect)
        await sesCur.async_send_text(pkey+'\n')
        # asyncio.ensure_future(await sesCur.async_send_text(pkey+'\n'))

    if 1:
        command = "cd tele\n"
        await glWin.tabs[0].sessions[0].async_send_text(command)
        await glWin.tabs[0].sessions[1].async_send_text(command)
        command = "pkill -f -9 restarter_tele.py & pkill -f -9  catchInput.py && pkill -f -9 restarter_tele.py & pkill -f -9  catchInput.py\n"
        await glWin.tabs[0].sessions[1].async_send_text(command)
        time.sleep(timeout_connect)
        time.sleep(timeout_connect)
        command = "python3.6 restarter_tele.py\n"
        await glWin.tabs[0].sessions[0].async_send_text(command)
    
async def tab1():
    global glWin
    tabW = glWin.tabs[1]
    for sesCur in tabW.sessions:
        await sesCur.async_send_text(cT1)
        time.sleep(timeout_connect)
        await sesCur.async_send_text(pkey+'\n')

        
    
async def tab2():
    global glWin
    tabW = glWin.tabs[2]
    for sesCur in tabW.sessions:
        await sesCur.async_send_text(cT2)
        time.sleep(timeout_connect)
        await sesCur.async_send_text(pkey+'\n')



       
async def tab3():
        global glWin
        command = cT3_0# 4 tab 
        await glWin.tabs[3].sessions[0].async_send_text(cT3_0)
        await glWin.tabs[3].sessions[1].async_send_text(cT3_1)
        await glWin.tabs[3].sessions[2].async_send_text(cT3_2)
        await glWin.tabs[3].sessions[3].async_send_text(cT3_3)
        time.sleep(timeout_connect)
        await glWin.tabs[3].sessions[0].async_send_text(pkey+'\n')
        await glWin.tabs[3].sessions[1].async_send_text(pkey+'\n')
        await glWin.tabs[3].sessions[2].async_send_text(pkey+'\n')
        await glWin.tabs[3].sessions[3].async_send_text(pkey+'\n')



async def tab4():
        #117
        global glWin
        tabW = glWin.tabs[4]
        command = cT4# 4 tab
        for sesCur in tabW.sessions:
            await sesCur.async_send_text(command)
            time.sleep(timeout_connect)
            await sesCur.async_send_text(pkey+'\n')
        time.sleep(timeout_simple)
        for sesCur in tabW.sessions:
            await sesCur.async_send_text('sudo su'+'\n')
        time.sleep(timeout_simple)
        for sesCur in tabW.sessions:
            await sesCur.async_send_text('ulimit -n 1000000 & ulimit -u 99000000'+'\n')
             
             
async def tab5():
        global glWin
        tabW = glWin.tabs[5]
        command = cT5# 5 tab // for connect to 145
        for sesCur in tabW.sessions:
            await sesCur.async_send_text(command)
            time.sleep(timeout_connect+9)
            await sesCur.async_send_text(pkey+'\n')
        time.sleep(timeout_simple)
        for sesCur in tabW.sessions:
            await sesCur.async_send_text('sudo su'+'\n')
        time.sleep(timeout_simple)
        for sesCur in tabW.sessions:
            await sesCur.async_send_text('ulimit -n 1000000 & ulimit -u 99000000'+'\n')



                
                
                
async def main(connection):
    global glWin
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window
    session = app.current_terminal_window.current_tab.current_session
    tab1 = session.tab
    glWin = tab1.window
    if window is not None:
        #await window.async_create_tab()
        #window.
        #print( "echo it works!")
        # for sesCur in tab.sessions:
        #    await sesCur.async_send_text('echo hello'+str(len(tab.sessions))+'\n')
        #     await sesCur.async_send_text('echo hello'+str(len(glWin.tabs))+'\n')



        if 1:
                for i2s in [0,1,2,3,4,5]:
                    await tabAction(i2s)
                        # thread = threading.Thread(target=tabAction, args=(i2s,))
                        # thread.daemon = True
                        # thread.start()


        while threading.active_count()>1: 
                print('threading.active_count() try end ',threading.active_count())
                time.sleep(10)
                
        
    
        command = "tail -f -n 99 /home/mobsted3/docker_mobsted/logs/nginx/pwa_error.log\n"#ru com
        await glWin.tabs[0].sessions[2].async_send_text(command)
        await glWin.tabs[1].sessions[2].async_send_text(command)
        command = "tail -f -n 99 /home/mobsted3/docker_mobsted/logs/nginx/pwa.log\n"#ru com
        await glWin.tabs[0].sessions[3].async_send_text(command)
        await glWin.tabs[1].sessions[3].async_send_text(command)
        command = "tail -f -n 99 /home/mobsted3/docker_mobsted/logs/nginx/error.log\n"
        await glWin.tabs[0].sessions[4].async_send_text(command)
        await glWin.tabs[1].sessions[4].async_send_text(command)
        await glWin.tabs[2].sessions[4].async_send_text(command)
        command = "tail -f -n 99 /home/mobsted3/docker_mobsted/logs/nginx/access.log\n"
        await glWin.tabs[0].sessions[5].async_send_text(command)
        await glWin.tabs[1].sessions[5].async_send_text(command)
        await glWin.tabs[2].sessions[5].async_send_text(command)

        command = "tail -f -n 99 /home/mobsted3/docker_mobsted/logs/php-fpm/alternatives.log\n"#com logintap 
        await glWin.tabs[1].sessions[0].async_send_text(command)
        await glWin.tabs[2].sessions[0].async_send_text(command)


        command = "sudo su\n"
        await glWin.tabs[0].sessions[6].async_send_text(command)
        await glWin.tabs[0].sessions[7].async_send_text(command)
        await glWin.tabs[0].sessions[8].async_send_text(command)
        await glWin.tabs[0].sessions[9].async_send_text(command)
        await glWin.tabs[0].sessions[12].async_send_text(command)
        await glWin.tabs[1].sessions[12].async_send_text(command)
        time.sleep(timeout_simple)
        command = "tail -f -n 99 /home/mobsted3/docker_mobsted/logs/php-fpm/error.log\n"
        await glWin.tabs[0].sessions[6].async_send_text(command)
        await glWin.tabs[1].sessions[6].async_send_text(command)
        await glWin.tabs[2].sessions[6].async_send_text(command)
        command = "tail -f -n 99 /home/mobsted3/docker_mobsted/logs/php-fpm/access.log\n"
        await glWin.tabs[0].sessions[7].async_send_text(command)
        await glWin.tabs[1].sessions[7].async_send_text(command)
        await glWin.tabs[2].sessions[7].async_send_text(command)

        command = "tail -f -n 99 /home/mobsted3/docker_mobsted/logs/php-cli/error.log\n"
        await glWin.tabs[0].sessions[8].async_send_text(command)
        await glWin.tabs[1].sessions[8].async_send_text(command)
        await glWin.tabs[2].sessions[8].async_send_text(command)
        command = "tail -f -n 99 /home/mobsted3/docker_mobsted/logs/php-cli/access.log\n"
        await glWin.tabs[0].sessions[9].async_send_text(command)
        await glWin.tabs[1].sessions[9].async_send_text(command)
        await glWin.tabs[2].sessions[9].async_send_text(command)

        command = "htop\n"
        await glWin.tabs[0].sessions[10].async_send_text(command)
        await glWin.tabs[1].sessions[10].async_send_text(command)
        command = "tail -f -n 99 /home/Aleksandr/confNginx.log\n"
        await glWin.tabs[0].sessions[11].async_send_text(command)
        await glWin.tabs[1].sessions[11].async_send_text(command)

        command = "pkill -f -9 autoConfigSocket.py\n"
        await glWin.tabs[0].sessions[12].async_send_text(command)
        await glWin.tabs[1].sessions[12].async_send_text(command)
        time.sleep(timeout_simple)
        command = "python3.6 /home/Aleksandr/autoConfigSocket.py\n"
        await glWin.tabs[0].sessions[12].async_send_text(command)
        command = "python3.11 /home/Aleksandr/autoConfigSocket.py\n"
        await glWin.tabs[1].sessions[12].async_send_text(command)

        command = "docker container logs telegramhost -f --tail 99\n"# logintap 
        await glWin.tabs[2].sessions[10].async_send_text(command)
        command = "docker container logs viberhost -f --tail 99\n"# logintap 
        await glWin.tabs[2].sessions[12].async_send_text(command)
        command = "docker container logs vkhost -f --tail 99\n"# logintap 
        await glWin.tabs[2].sessions[14].async_send_text(command)
        command = "docker container logs facebookhost -f --tail 99\n"# logintap 
        await glWin.tabs[2].sessions[16].async_send_text(command)
        command = "docker container logs telegram_listener -f  --tail 99\n"# logintap 
        await glWin.tabs[2].sessions[11].async_send_text(command)
        command = "docker container logs viber_listener -f  --tail 99\n"# logintap 
        await glWin.tabs[2].sessions[13].async_send_text(command)
        command = "docker container logs vk_listener -f  --tail 99\n"# logintap 
        await glWin.tabs[2].sessions[15].async_send_text(command)
        command = "docker container logs facebook_listener -f  --tail 99\n"# logintap 
        await glWin.tabs[2].sessions[17].async_send_text(command)

        command = "docker container logs  elated_zhukovsky -f -n 99 \n"
        await glWin.tabs[1].sessions[13].async_send_text(command)
        command = "docker container logs  freegpt -f -n 99 \n"
        await glWin.tabs[1].sessions[14].async_send_text(command)
        
        
        command = "cd /home/Aleksandr/bk/ && ls -lsaht \n"
        await glWin.tabs[4].sessions[1].async_send_text(command)
        command = "cd /home/Aleksandr/YoCol/darknet/ \n"
        await glWin.tabs[4].sessions[2].async_send_text(command)
        command = "ps -ax|grep -i darknet \n"
        await glWin.tabs[4].sessions[3].async_send_text(command)
        command = "cd /home/Aleksandr/YoCol/darknet && tail -f -n 99 output.txt \n\n\n\n\n"
        await glWin.tabs[4].sessions[4].async_send_text(command)
        
        command = "cd nnstream/ \n"
        await glWin.tabs[4].sessions[7].async_send_text(command)
        command = "/usr/local/bin/python3.10 nnfame_yMock.py \n"
        await glWin.tabs[4].sessions[7].async_send_text(command)
        
        
        command = "cd /home/Aleksandr/keras-retinanet/snapshots && ls -lsaht \n"
        await glWin.tabs[5].sessions[1].async_send_text(command)
        command = "cd /home/Aleksandr/keras-retinanet \n"
        await glWin.tabs[5].sessions[2].async_send_text(command)
        command = "ps -ax|grep -i keras_retinanet \n"
        await glWin.tabs[5].sessions[3].async_send_text(command)
        command = "cd  /home/Aleksandr/keras-retinanet && tail -f -n 99 output.txt \n\n\n\n\n"
        await glWin.tabs[5].sessions[4].async_send_text(command)





        




        command = "htop\n"
        await glWin.tabs[4].sessions[0].async_send_text(command)
        await glWin.tabs[5].sessions[0].async_send_text(command)
        # time.sleep(timeout_simple)
        command = "pkill -f -9  findergV82 && pkill -f -9 restarterV82.py\n"
        # await glWin.tabs[4].sessions[1].async_send_text(command)
        # await glWin.tabs[5].sessions[1].async_send_text(command)
        # time.sleep(timeout_simple)
        command = "pkill -f -9  findergV82 && pkill -f -9 restarterV82.py\n"
        # await glWin.tabs[4].sessions[1].async_send_text(command)
        # await glWin.tabs[5].sessions[1].async_send_text(command)
        # time.sleep(timeout_simple)
        command = "python3.6 ./restarterV82.py\n"
        # await glWin.tabs[4].sessions[1].async_send_text(command)
        command = "python3.6 ./restarterReddit.py\n"
        # await glWin.tabs[4].sessions[2].async_send_text(command)
        # await glWin.tabs[5].sessions[1].async_send_text(command)

    else:
        # You can view this message in the script console.
        print("No current window")

iterm2.run_until_complete(main)
