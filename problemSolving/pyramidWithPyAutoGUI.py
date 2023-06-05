import pyautogui

rows = int(input())

for i in range(rows):
    for j in range(i+1):
        pyautogui.write('#', interval=1)
    pyautogui.write("\n")