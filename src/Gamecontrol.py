# import library
import struct
import time
from bluepy.btle import Peripheral
from pynput.keyboard import Key, Controller

keyboard = Controller() 

my_gamesir = Peripheral('C7:06:A1:09:0B:XX', 'random') # Put your MAC address here 'C7:06:A1:09:0B:XX' replace

services = my_gamesir.getServices() # get bluetooth service from device

for service in services:

    services_to_list = list(services) #convert dict to liste

    control_service = services_to_list[2] #get elements on index 2  

    charac_dics = control_service.getCharacteristics() # get bluetooth characteristics 

    for charac in charac_dics:
        #print(charac.uuid)
        #print(charac)
        pass


    while True:
        #time.sleep(0.01)

        charac1, charac2, charac3  = [item.read() for item in charac_dics]

        status_code = struct.unpack('H', charac1[:2])[0] #extract binaire and do the handling
        #print(status_code)

        if status_code == 50593:
            on_press_key = struct.unpack('I', charac1[9:13])[0] # key value, each key on the joystick has a fixed value.

            bar_status = struct.unpack('5B', charac1[2:7]) 
            bar_status_bin = ''.join([bin(item).split('b')[1].rjust(8).replace(' ', '0') for item in bar_status])

            left_drag = int(bar_status_bin[0:10], 2)
            left_push = int(bar_status_bin[10:20], 2)
            right_drag = int(bar_status_bin[20:30], 2)
            right_push = int(bar_status_bin[30:40], 2)

            
            """
            #DEBUG and PRINT value from joystick

            print("status %s" % status_code, end='  ')
            print("on_press %s" % on_press_key, end='  ')
            #print("press_counter %s" % press_counter, end='  ') #-
            print("left_drag %s" % left_drag, end='  ')
            print("right_drag %s" % right_drag, end='  ')
            print("left_push %s" % left_push, end='  ')
            print("right_push %s" % right_push, end='\r')
            """

            #this section is dedicated to the interpretation of the keys of the 4 direction arrows on the joystick, 
            #simulating a press on the keypad at system level

            if (on_press_key == 196608):
                print("right \n")
                keyboard.press(Key.right)
                keyboard.release(Key.right)

            elif (on_press_key == 458752 ):
                print("left \n")
                keyboard.press(Key.left)
                keyboard.release(Key.left)

            elif (on_press_key == 65536):
                print("haut \n")
                keyboard.press(Key.up)
                keyboard.release(Key.up)

            elif (on_press_key == 327680):
                print("bas \n")
                keyboard.press(Key.down)
                keyboard.release(Key.down)


        # break
