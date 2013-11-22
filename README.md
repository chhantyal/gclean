gclean
======

Free GMail inbox from unwanted junk.

## Problem
I love web. Sometimes I love just too much, and end up getting emails from everywhere. Most of them, unwanted. My inbox is full of emails which I don't want to read. Even if I want to open, I can't because they are just too many. 

This is just too messy. Let's make it clean. I still love web. Unsubscribing is not really the solution, unless it is spam (Google handles it nicely ;)

## Solution
If I don't open and read an email for 15 days (my email habit), probably I will never read it. So, archive all the unread messages older then 15 days (delete optional)

That's exactly what the script does. Simple. Inbox is clean again :)

## Usage

```
1. Install https://github.com/charlierguo/gmail
2. git clone git@github.com:neokya/gclean.git
3. cd gclean/
4. python gclean.py
5. Go out, get some fresh air!
```
If you want to automate with crontab:

``` 
1. sudo crontab -e
2. Add this job: * * */15 * * /path/to/bin/python /path/to/gclean.py
```
Note: username and password must be provided.