
Watchdog for Router TENDA 301N 

This project is combination of software and hardware technologies which helps you to make automatic reboot system for Router and make simple events journalization.

!TENDA 301N has only web interface to communicate with user(no ssh)!

Suitable way to make soft reboot via browser is to use Selenium WebDriver.
If router freezed, reboot must be made by hardware (arduino relay module).
For journalization of these events sqlite3 is apropriate library.
To make automated script for all actions python3 perfectly fit.

So, Raspberry Pi(Raspberry Pi 3b+) as all-in-one platform is best solution.

To run the Project you will need:

Hardware:
1) Raspberry Pi 3b+ with mouse, keyboard, monitor, power adapter and SDCard(16GB is best choise) 
2) 5V Arduino Relay Module (AC range 250V and 10A, DC range 30V and 10A)
3) Male and Feamale connectors(with respectively connectors diameter of your Router and power adapter) that has terminals for 2 wires.
4) 3 wires (0.5mm sqr diameter, L~10cm)
5) 3 arduino F to F jumpers (L~20 cm)
6) Phillips "plus" screwdriver

Software:
1) RapspbianOS 
2) Chromium web browser (Preinstalled in RapsbianOS)
3) Chromium WebDriver (Version of WebDriver and web browser must be same)
4) Selenium WebDriver (See link below)

!All connection must execute with unpluged arduino and router power adapters!

To get set you need to connect RapsberriPi GPIO pins(co) and Relay module pins(low-voltage group) using jumpers (GPIO pin 4(5V to VCC), 6(GND to GND) and 12(GPIO 18 to IN)). Using Phillips scredriver to connect terminals(relay module high-voltage group) of F and M connectors using wires (wire 1 - GND line directly F to M terminal, wire 2 - Voltage line F to COM, wire 3 - Voltage line M to NC). 

Insert power adapter to F connector, insert M connetor to router, plug arduino and router adapters in powergrid.

Download project files (unzip them if it was an archive) and write correct path in "eventsinfo.py" and "events_list.py". In "reloader.py" and "whreload.py" write correct Router ip-address, and correct password.

In terminal write:  #crontab -e
At bottom add new line and write:
@reboot  ***/reloader.py 
Reboot your RaspberryPi.

If you want to check list of events, just startup "events_list.py" 
(via terminal: #python3 ***/events_list.py)

(*** - paths to files respectively).

Useful links:
https://www.raspberrypi.com/documentation/computers/getting-started.html
https://selenium-python.readthedocs.io/installation.html
https://www.researchgate.net/figure/Schematic-zoom-of-the-Raspberry-Pi-3-B-pins-Adapted-from-14_fig2_351755761
