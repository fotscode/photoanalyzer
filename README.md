# photoanalyzer with prnt.sc

This code basicly downloads an image from prnt.sr and converts it to text, then finds throughtout the text certain keywords, if one or more of the keywords are found the image will be stored on a folder called "imageswithkeywords" on the same path of the code.

We utilized prnt.sr as our main source of getting random images, we found out that their hashing of screenshots isn't the best, basicly with 6 digits of numbers or letters we could make a valid hash that leads to another's person screenshot.

Program running

![alt text](https://github.com/fotscode/photoanalyzer/blob/master/images/program%20running.png)


Image downloaded as a temporary file

![alt text](https://github.com/fotscode/photoanalyzer/blob/master/images/tempfile.png)


Image finally stored in the folder with the name of the hash

![alt text](https://github.com/fotscode/photoanalyzer/blob/master/images/imagewithkeyword.png)
