import sys

bitmap = """
    **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
"""

print("Bitmap message")
while True:
    message = input("Enter the message to display with the bitmap : ")
    if message == ' 'or message == " ":
        print("You have to enter a message to display")
    
    for line in bitmap.splitlines():
        for i, bit in enumerate(line):
            if bit == ' ':
                print(" ", end='')
            else:
                print(message[i % len(message)], end='')
        print()
    exit()