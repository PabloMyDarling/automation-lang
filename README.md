# automation-lang
A programming language you can use for automation of daily tasks.

## About automation-lang
automation-lang is a programming language that you can use for automation. It's a very simple tool based off of [Python3](https://www.python.org) and pyautogui. You use this by writing in a file and putting it through the compiler (compiler.pyw).

## How to install automation-lang

*Step 0:* Download [Python3](https://www.python.org).  

*Step 1:* Click the "Code" button and then click "Download ZIP".  

*Step 2:* Extract the ZIP file and save ``compiler.pyw`` and ``requirements`` to a folder.  

*Step 3:* Go to the folder and open the Terminal there.  

*Step 4:* Type the following command:  

``pip3 install -r requirements`` or ``pip install -r requirements``  

After that, you can move on to How to use automation-lang!  

## How to use automation-lang
This section will teach you how to actually program in this lang.  

**Command 1:** open  
This command will start a file. If you input the path to a file/folder, it'll open it. If you input the path to an executable, it'll execute the app.  
*Usage:*  
``open: /path/to/file``  

**Command 2:** type  
This command will type whatever you inputted into the command.  
*Usage:*  
``type: Lorem ipsum``  

**Command 3:** keyboard  
This command will press a hotkey that you input.  
*Usage:*  
``keyboard: Key1, Key2, Key3,...``  

**Command 4:** move_mouse  
This command will move your mouse to a position you input in a given duration.  
*Usage:*  
``move_mouse: x_axis, y_axis, duration``  

**Command 5:** click_mouse  
This command with click a mouse button you input it. Whether it'd be "left", "right" or "middle".  
*Usage:*  
``click_mouse: left`` (left clicks your mouse)  

**Command 6:** screenshot  
This command will screenshot your whole screen.  
*Usage:*  
``screenshot: save_path, file_name``  
