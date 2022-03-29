What is your motivation? - Solve problem with router freezes.
Why did you build this project? - Solve problem with router freezes.
What problem does it solve? - Solve problem with router freezes.

What did you learn? - How to work with Selenium webdrive on chromium, 
work with Raspberry oi GPIO, work with sqlite.

What makes your project stand out? - Two ways to solve problem - web and relay way.

1. Project's Title: 
Watchdog for Router TENDA 301N 

2. Project Description:

    What your application does,
    Why you used the technologies you used,
    Some of the challenges you faced and features you hope to implement in the future.

Combination of software and hardware technologies to make automatic reboot system for Router  and make simple journalization of these events.
    
Fist of all, TENDA 301N has only web-interface to communicate with (no ssh). That is why only way to make soft reboot is to use web-interface envirement and all actions must execute automaticly in browser. Thats why Selenium web-driver is excellent solution.

Next, in cases when router freezed, reboot must be made by hardware (in our case - arduino relay module is good choice).

For journalization events sqlite3 is apropriate library. 

Finally, for able to use two reboot methods one of appropriate platforms is Raspberry Pi(Raspberry Pi 3b+ in our case). For communication with Raspberry and Relay - GPIO, for main script, web-browser actions and enents listing - python3(+built in sqlite3) and Selenuim web-driver for chromium.

4. How to Install and Run the Project:

To run the Project you need:

1) Raspberry Pi 3b+ with SDCard and Installed Rapsbian
2) 5V Arduino Relay Module (AC range 250V and 10A, DC range 30V and 10A)
3) Male and Feamale connectors(with respectively diameters of your Router) that has terminals for 2 wires.
4) 3 wires (0.5mm sqr diameter, L~10cm)
5) 3 arduino F to F jumpers (L~20 cm)
