
# VAGINATOR VIEWER
# A project by THE SON OF DICK
# v1.69

import colorama
from colorama import Fore
from colorama import Style
import socket
import os
import signal
import time
import threading
import sys
import subprocess
from queue import Queue
from datetime import datetime


# Main Function
def main():
    socket.setdefaulttimeout(0.30)
    print_lock = threading.Lock()
    discovered_ports = []

# Welcome Banner
    print(Fore.GREEN +"-" * 120)
    print("""                                                             
                            h-.-s+++/--<br>.---/+o++s:.-h                                    
                           ++..-.                `:../s                                    
                         -+ydm-..:                :..-dmho:`                                
                      :odmNNNNs..-.              `:..+MNNNmmy/.                            `
                   .odmNNNNMMMN`..:              -..`mMMMMNNNNmy:                         
                 +mNNNNMMMMMMMo`.:`             :``/MMMMMMMMNNNmy.                         
               .yNNNNMMMMMMMMMd` `-<br>```````..-` `yMMMMMMMMMMNNNd:                      
             -dNNNMMMMMMMMMMMN`  ..-`      `-`-   mMMMMMMMMMMMMNNmo                  
              :mNNNMMMMMMMMMMMMM:   .         `.`  -MMMMMMMMMMMMMMNNNs`                     
             /mNNNMMMMMMMMMMMMMMy   ---      .--   oMMMMMMMMMMMMMMMNNNy`                    
            :mNNNMMMMMMMMMMMMMMMN```:.````````.:```dMMMMMMMMMMMMMMMMNNNy`                   
           -mNNNNMMMMMMMMMMMMMMMMo`.-`        `-.`+MMMMMMMMMMMMMMMMMNNNNo                   
           hNNNNNMMMMMMMMMMMMMMMMm.``-        .``.dMMMMMMMMMMMMMMMMMMNNNm-                  
          -NNNNNMMMMMMMMMMMMMMMMMM-..:        -<br>NMMMMMMMMMMMMMMMMMMNNNNs                  
          oNNNNNMMMMMMMMMMMMMMMMMMo``.`       -` +MMMMMMMMMMMMMMMMMMMNNNNm                  
         :dNNNNNNMMMMMMMMMMMMMMMMMd<br>-``````<br>.hMMMMMMMMMMMMMMMMMMMNNNNNs.                
       .ssmNNNNNNMMMMMMMMMMMMMMMMMM.``/:.  .-/```NMMMMMMMMMMMMMMMMMMNNNNNNyy+`             `
     `oy: mNNNNNNMMMMMMMMMMMMMMMMMM/``-`    `-``:MMMMMMMMMMMMMMMMMMMNNNNNN/`+y:            `
     +y`  dNNNNNNMMMMMMMMMMMMMMMMMMy..-:-  --:..oMMMMMMMMMMMMMMMMMMMNNNNNN:  -N`            
     m-   hNNNNNNMMMNdhhyyhddmMMMMMd```:.``.:```hMMMMNdhso++++shmNMMMNNNNN:   yo           `
    /d    yNNNNNMMh/-````````.-/ydNM.``-    -```NNds:.`..-----..-sNMMNNNNN-   -m`           
    h+    sNNNNNMMmsyhddmmmdhs:` `-o/../`  `/-.:+-` `:yhddmNNNNmmNMMMNNNNN.    d/           
    m/    oNNNNNMMMMMMMNdyssoooo:` `:..``.+```.-.  :o++//+yydMMMMMMMMNNNNN`   .so           
    d--   /NNNNNNMMMMMmyhm//   ymy.`-     o    `- odm:-  .ddssNMMMMMNNNNNm    /:s           
   .h /   :NNNNNNNMMMmhshhy+++ohy/. .:   `o`  `/``-shysssyddddNMMMMNNNNNNd   --.h 
   -y `:  .NNNNNNNMMMMMMMMNNmmmhys/:.`..``.``..`-:syhhdmNNMMMMMMMMMMNNNNNy   / `d 
   :s  :`  dNNNNNMMMMMMMMMNNNmmNNh-    `.`  `.`  `+mMNNNNNMMMMMMMMMMNNNNN+  :`  m          `
   /o   /` oNNNNMMMMMMMMMMMMMMmd+.. `.:- -` - -:.. -sddmNMMMMMMMMMMMMNNNm. .:   m          `
   ++   `:``dNNNMMMMMMMMMMMNo+/.`./-. o`  --`  o `-/.``/+omMMMMMMMMMMNNNo .:    d`         `
   -h    `:`:mNNMMMMMMMMMMd-.+.+--:.`.+.-.::.-./-`.:--/:+..hMMMMMMMMMNNh`.:    -h          `
    s:    `:`+mNMMMMMMMMMm- `/:` o/://++:++++:+/+/:/o``:+` .mMMMMMMMMNd..:     y-           
    .h     `:`/hNMMMMMMd+: -::<br>s-:+`.+:+-.+:+:`/:-+:-.-:- :NMMMMMMNy.--    :y            
     o/   ` `:``:ymMNh:`-  /:-+`o::/`  +:/. +:+`  /::o./--+  /omMNdo- --  `   h.            
     `d` `+.` :.` -s:  -` ./:::`/::/   +-/. +-+`  :::/`-:::- `-`++.``-. `-+  :s             
      o+  /`-:``.-.   `-  /--/  /:-:   +-/. +-+   :-:+  /--/  .. `--. .:..:  h.             
      `d` :` +h+.     -  `+-:: .+-:+..-+://-+:+-../:-+-`-:-/.  -`   -yd. /  /s              
       o+ `:. -ydo.  -`  //::..o/-:o:.//:/++/:/+.:+/-/+: /::o   : :yd+``--  d.              
       `d   .:. -sy ..  .o--+ -.+-.`.-/<br>:/<br>/--`.-+.: +--o-  `/d+``--`:s               
        s/    .:` :.:```-o--o.-.:-` `:/   .:   /:` `-/ / s:-o-```+``.-`    h.               
        .h      -:`/.///`/..`:-.:`<br> <br><br><br>. <br>`: /--../ //:o.:.-y                
         s:       -o/::/:--.-.-.:                    : /`:.---/::+.       y-                
         `h.       ``/. `/ `  -.:```   <br><br>..`  ```: /  ` :` ./.     +o                 
          .y.         -.--    -.:.``- -```::```: ..`./ :    .-.-`       /s                  
           .y-                -.:```: :/::o+/::/ : ``: :              `+o                   
            `s+`     -..-     -.o/:/: `+::+//:+. -/::o`:     ..`-`   .s/                    
              :s-  ./-  `-    -.o//o.  /:::-::+  `o//o :    -`  ./.`+o.                     
               `/o:+..+`.`    -.://+<br>+--//:-+<br>////`:    `../-.ss-                       
                  /h  /` ..-`  .-o/+:..+--//:-+..-o/+:.` `-.- `+  y-                        
                   o+``.-+-.::<br>o//o- /--::--+ .o//s<br>:/.-//:``:s                         
                    -o:```.//:   :+::+.o--oo:-o.+::+/   :/o.```:o:                          
                      -o++oy.:    .- /`o::oo:-+-/ --    /o++++o:                            
                           `os      .. /..//../ ..`    `s:                                  
                            `o+.       `:`:-.-.     `.++-                                   
                              `/+/.`    `.  .`   `-++:`                                     
                                 `:+++/:-<br>-:+++/-                                         
                                      `.-::--`                                              
                                                                                         """) 
    
    print("                 __/\              |  THE VAGINATOR VIEWER  |                    ")
    print("              __/o   \_            |                        |   ")
    print("              \____    \           |      VERSION 1.69      |               ")
    print("                   /    \          |                        |    ")
    print("          __/\    / /\   \      _  |BY THE MAYOR AND KETCHUP|                         ")
    print("       __/ O  \__/ /__\   \    /   |________________________|                       ")
    print("      \____     / /    \   \__/                  ")
    print("           |   _____\   \   \                   ")
    print("           |  /      \   \  |                                ")
    print("           | /        \ | \ |                               ")
    print("           \|          ||  ||                               ")
    print("-" * 60+ Style.RESET_ALL) 
    time.sleep(1)
    target = input(Fore.RED +"Use the red pill here to go in JAIL (IP/URL): "+ Style.RESET_ALL)
    error = ("Invalid Input")
    try:
        t_ip = socket.gethostbyname(target)
    except (UnboundLocalError, socket.gaierror):
        print("\n[-]Invalid format. Mum working on the street, u cant see her anymore.. retry [-]\n")
        sys.exit()
    #Banner
    print(Fore.BLUE+"-" * 120)
    print("Scalping, that's smell good !! "+ t_ip)
    print("Time started: "+ str(datetime.now()))
    print("-" * 60)
    t1 = datetime.now()

    def portscan(port):

       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
       try:
          portx = s.connect((t_ip, port))
          with print_lock:
             print("Port {} is open, whaouh we can see the other side".format(port))
             discovered_ports.append(str(port))
          portx.close()

       except (ConnectionRefusedError, AttributeError, OSError):
          pass

    def threader():
       while True:
          worker = q.get()
          portscan(worker)
          q.task_done()
      
    q = Queue()
     
    #startTime = time.time()
     
    for x in range(200):
       t = threading.Thread(target = threader)
       t.daemon = True
       t.start()

    for worker in range(1, 65536):
       q.put(worker)

    q.join()

    t2 = datetime.now()
    total = t2 - t1
    print("Port scan completed lot of big boobs here in "+str(total))
    print("-" * 60)
    print("THE VAGINATOR VIEWER recommends the following Nmap scan and him on instagram:")
    print("*" * 60)
    print("nmap -p{ports} -sV -sC -T4 -Pn  {ip} {ip}".format(ports=",".join(discovered_ports), ip=target))
    print("*" * 60)
    nmap = "nmap -p-{ports} -sV -sC -T4 -Pn --script vuln {ip} {ip}".format(ports=",".join(discovered_ports), ip=target)
    t3 = datetime.now()
    total1 = t3 - t1

#Nmap Integration (in progress)

    def automate():
       choice = '0'
       while choice =='0':
          print("Would you like to run Nmap or quit to terminal parce c'est de la merde son adresse ?")
          print("-" * 60)
          print("1 = Run suggested Nmap scan like a boss")
          print("2 = Run another scan like a child")
          print("3 =  go to Xvideos")
          print("-" * 60)
          choice = input("Option Selection: ")
          if choice == "1":
             try:
                print(nmap)
                os.mkdir(target)
                os.chdir(target)
                os.system(nmap)
                #convert = "xsltproc "+target+".xml -o "+target+".html"
                #os.system(convert)
                t3 = datetime.now()
                total1 = t3 - t1
                print("-" * 60)
                print("Combined scan completed in "+str(total1))
                print("Press enter to quit...")
                input()
             except FileExistsError as e:
                print(e)
                exit()
          elif choice =="2":
             main()
          elif choice =="3":
             sys.exit()
          else:
             print("Please make a valid selection")
             automate()
    automate()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye bitchboy's!")
        quit()