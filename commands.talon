mode: command
-
settings():
    key_hold = 120

# Shortcuts to open things:
view log:
    user.view_log()

view config:
    user.view_config()

code:
    user.code()

# Transcription tools:

type:
    user.type()

heading <number>:
    number = number - 1
    insert("#")
    repeat(number)
    insert(" ")

yes:
    insert("y\n")

no:
    insert("n\n")

split:
    insert("s\n")

quit:
    insert("q\n")

standard <user.word>:
    insert("std::")
    insert(word)

sift <user.text>:
    insert("sf::")
    insert(user.hammer(text))

void <user.text>:
    insert("void ")
    insert(user.snake(text))
    insert("() {}")

get push:
    insert("git push\n")

gap:
    insert("gap\n")

get commit:
    insert("gcm \"\"")
    key(left)

ammend:
    insert("git commit --amend\n")

ricky:
    key(right)

larry:
    key(left)

dennis:
    key(down)

up:
    key(up)

doc string:
    insert('""""""')
    key(left)
    key(left)
    key(left)

half colon:
    insert(";")