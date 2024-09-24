mode: command
-

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
