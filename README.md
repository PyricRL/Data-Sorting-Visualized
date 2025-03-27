Basic data sorting visualizer which can show data to the screen and show how fast it took visually and in code. 

Work in progress, although I probably wont touch it much anymore as I am working on other projects.

Editing:

line 23-24 of `main.py` can be adjusted within the last 2 values of the rect

```
#array[x] * scaleFactor
rect = (x * gap, HEIGHT - (array[x] * scaleFactor), 4, 4)
                                                    ^  ^
```
The first one of these items adjusts how thick each data set is, and the second adjusts how high it is. 
Adjusting them to both be the same results in a square (or dot depending on how big or small) and if you instead set the second value to the commented line the data will reach to the bottom of the screen and look like traditional data.

Some of the sorting algorithms take longer than others, so to adjust how many pieces of data:
in `sortingManager.py` on line 37:
```createTestData(500)```
adjust the value within this to increase or decreas the size of the data. Setting it to 1000 will create 1000 sets of data etc.

There is also sound involved, so I would reccomend not blasting the audio :)
