# 403Jumper
The purpose of this tool is to bypass 403 forbidden returning pages. 
It basically brute-forces certain bypass headers with localhost's address 127.0.0.1.

Usage:
python 403jumper.py <target url>

If any of the headers are successful then it will look like this:
![image](https://user-images.githubusercontent.com/68515706/183657162-ae82ecf8-9ecb-4b9a-8b62-02a73056dc47.png)

And if it is not it will look like this:

![image](https://user-images.githubusercontent.com/68515706/183657334-07a73b3d-c7ac-46cc-be37-2cc82217d3cb.png)

Make sure the headers.txt and 403jumper.py are in the same directory.
