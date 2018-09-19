def encrypt(msg, encbook):

    for c in msg:
        if c in encbook:
            msg = msg.replace(c, encbook[c])

    return msg