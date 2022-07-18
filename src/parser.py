
def parse(message):
    msg_secs = message.split("\n\n")
    return msg_secs[0]
    