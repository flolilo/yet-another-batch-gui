=====================
yet-another-batch-gui
=====================

Seemed a nice idea at the time, but actually, using:

::

    printf "<DRAGNDROP>" | sed -e "s:' ':\n:g" -e "s:'::g" > FILE.txt
    cat FILE.txt | parallel -q <CMD> {}

seems way faster than to do a whole lot of programming.
