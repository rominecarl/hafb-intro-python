"""
Set an alarm to take a break
"""

import webbrowser
import time

def main():
    """
    Test function
    :return: none
    """
    counter = 0
    while counter < 3:
        video_address = "https://www.youtube.com/watch?v=Mg91VsButWE"
        # Delay "sleep"
        time.sleep(60 * 60)
        print("it is time to take a break. Time is: ", time.ctime())
        webbrowser.open(video_address)
        counter += 1

if __name__== '__main__':
    main()
    exit(0)

