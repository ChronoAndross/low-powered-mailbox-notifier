# low-powered-mailbox-notifier
A low powered notification system that can be used for things like mailboxes.

# Introduction
The purpose of this code is to demonstrate a low cost system which notifies a user by text message if it discovers activity. This would be mostly used in the instance of a mailbox. It resembles something close to [this](https://www.walmart.com/ip/WiFi-Mailbox-Alert-Briidea-500ft-Wireless-Alert-Delivered-Mail-IP67-Waterproof-Real-Time-Delivery-Notifications-Save-Time-Remote-Monitoring/11596202325?wmlspartner=wlpa&selectedSellerId=101086089&sourceid=dsn_ad_fac153e8-a819-4e04-9af5-1c5d04a29929&veh=dsn&wmlspartner=dsn_ad_fac153e8-a819-4e04-9af5-1c5d04a29929&cn=FY26-MP-PMax_cnv_dps_dsn_dis_ad_mp_s_n&gclsrc=aw.ds&wl9=pla&wl11=online&gad_source=1&gad_campaignid=22532405497&gbraid=0AAAAADmfBIqcXCoTSZSOFjIZeasBzeasO&gclid=Cj0KCQiA5uDIBhDAARIsAOxj0CHJXD-KizMr2vVKsXhvqliDpWUfLlkxCXalyXMgLPgGtaeWbJXCvnEaAti_EALw_wcB). It attempts to use an IR sensor, a microphone, and a temperature sensor to figure out when to send a text message via the Twilio API. This system allows two different modes: high power and low power. High power will be run by default, while low power has to be specified at runtime.

# Getting Started
Requirements to run this code:
- python3
- any version of raspian
- a `keys.txt`file that contains twilio related keys (ask Andrew Gorbaty for this file)
- install [this library](https://github.com/adafruit/Adafruit_Python_DHT) into your local python
- [HC-SR501 PIR sensor](http://www.hiletgo.com/5pcs-HC-SR501-PIR-Infrared-Sensor-Human-Body-Infrared-Motion-Module-for-Arduino-Raspberry-Pi-PG30063)
- [sound detector with SKU 552413 with Switch Electronics](https://www.switchelectronics.co.uk/products/sound-detection-sensor-module?currency=GBP&variant=45334952345909&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=bbf1d20e1ed7&srsltid=AfmBOooJ0antrPI2meRuOjvOfBIQQ0E2--tXP5pATGsy-GfU6i3jqcfOTpg)
- [DHT11 temperature sensor](https://www.digikey.com/htmldatasheets/production/2071184/0/0/1/dht11-humidity-temp-sensor.html?gclsrc=aw.ds&gad_source=1&gad_campaignid=120565755&gbraid=0AAAAADrbLlipAy5eYZzI81Tl7NFeOAjor&gclid=Cj0KCQiA5uDIBhDAARIsAOxj0CHUeXZXfYaQxI8oPOXgwdhhBGywrUqu4uOosua_7d2dweDhMsjGWAcaAks5EALw_wcB)

# How to run
NOTE: Before running, please make sure `keys.txt` is placed in the top level of the directory.
You can also specify the board GPIO ports the interrupts use within `main()`.
To run it on high power, run it like this:
```
python3 main.py
```
This will run the system using a while loop that runs forever that checks the interrupts. This should use quite a bit of power since it never stops executing.

To run it in low power, run it like this:
```
python main.py low_power
```

or 

```
python main.py lp
```

This should transition the system into using low power. This includes
- having the interrupts be event driven
- clock gating to shut down UART/WiFi within transition windows
- duty cycling which transmits the messages at defined intervals

## I2C Wattmeter graph
This code also includes code which shows a graph for precise measurements via the ina219 I2C wattmeter. If connected appropriately (use [this guide](https://www.dfrobot.com/product-1827.html?srsltid=AfmBOoqU1gFV82EL-XfqefH7owhVnppxaNpzOtrHkUG2Vl4-3J5haMLu) for reference), you'll see a graph that looks something like the following:

![wattmeter_sample](assets/wattmeter_sample.png)