mode: command
-

heading <number>:
    number = number - 1
    insert("#")
    repeat(number)
    insert(" ")

view log:
    user.view_log()

view config:
    user.view_config()

type:
    user.type()