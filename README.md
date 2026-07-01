# Music Player
"Work in progress"


## Features
Until now, I added all the core functions that are necessary to consider a full music player,
even though it cannot access the mp3 files they are not yet integrated,
since I am testing on the terminal environment with in-memory data.

This project was constructed in Python and C++. "lembre-se de passar o core a C++"


## **Core Functions**

* Next Button:
I have implemented an index and starting at zero that increments.  Once it is clicked,
it checks if the user has reached the end of the playlist,
preventing it from exceeding the limit.

* Prev Button:
It does exactly the same.  However, it decrements rather than incrementing the index.
When the user reaches the beginning of the playlist, it checks, preventing it from
accessing an impossible range.

* Shuffle Button:
It shuffles the user's playlist, saving the current state and resetting the index.
NOTE: It might be a problem in the near future. As a **potential bug**, It needs to be fixed.

* Pause Button:
It pauses the current song using a var as a verifier that is negated by the user every time they click it.

![cat](asset/gato_pensando.jpg)
