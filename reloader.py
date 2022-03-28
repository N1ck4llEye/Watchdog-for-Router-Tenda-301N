from actions import whreload, eventsinfo
import os, time
resettype=''
#Default state of link
linkst='UP' 
while True:
    #Router reloading time(RouterOS + wifi module + relay reset)
    time.sleep(30)
    #Check and removing for duplicates of "reloader.py" script
    look4copy=str(os.popen('ps aux | grep reloader.py').read())
    for i in range(int(look4copy.count('/re'))-1):
        start=(look4copy.find('\n')+5)
        end=(look4copy.find('\n')+16)
        idfindfer=look4copy[start:end]
        print(idfindfer)
        look4copy=look4copy[end:]
        os.popen(('kill -9 {}').format(idfindfer)).read()
    #Test for Router state
    pins=os.popen('ping 192.168.0.1 -c 5').read()
    pinr=pins.find('packet loss')
    #Test for availability connection to Google DNS-server
    pinDNS=os.popen('ping 8.8.8.8 -c 5').read()
    pinDNSr=pinDNS.find('packet loss')
    #Check in case .find() method returns '-1' (no substring in pinr) and DNS response 
    if pinr ==-1 or (int(pinDNS[int(pinDNSr)-4:int(pinDNSr)-2])>5 or
                   pinDNS[int(pinDNSr)-4:int(pinDNSr)-2]=='00'):
        #Change of link state and add "Downlink" event to database 
        if linkst=='UP':
            linkst='DOWN'
            eventsinfo.spreadsheet(linkst)
        else:
            pass
        #Choose type of reset Router (via web browser or relay reset)
        if pins=='' or int(pins[int(pinr)-4:int(pinr)-2])>5:
            resettype='hard'
            print(os.popen('echo Router out of reach!').read())
        else:
            resettype='web'
            print(os.popen('echo Router works, global network is not. Trying to fix it!').read())
        whreload.reloaders(resettype)
    else:
        #Change of link state and add "Uplink" event to database 
        if linkst=='DOWN':
            linkst='UP'
            eventsinfo.spreadsheet(linkst)
            print(os.popen('echo Local and Global networks are work now!').read())
        else:
            print(os.popen('echo Local and Global networks are still work, for now...').read())
            print(os.popen('date').read())
