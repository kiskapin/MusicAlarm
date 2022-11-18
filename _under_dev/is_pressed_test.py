from codecs import escape_encode
import keyboard  # using module keyboard
while True:  # making a loop
    print(keyboard.read_key())
    try:
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed q Key!')
            continue
            #break  # finishing the loop
        elif keyboard.is_pressed('s'):  # if key 's' is pressed 
            print('You Pressed s Key!')
            #break  # finishing the loop
        """ due to the else part - the code immediately goes into it
        else:
            print('You Pressed wrong Key!')
            break  # finishing the loop
        """
    except:
        print('You Pressed wrong Key!')
        break  # finishing the loop


#
#
# 
#
#