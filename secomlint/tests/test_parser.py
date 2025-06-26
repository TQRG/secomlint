from secomlint.message import Message
import messages

def norm_message(msg):
    return msg.value.lower().split('\n')

def test_get_sections_all():    
    lines = norm_message(messages.Message.MSG1)
    message = Message(lines)
    message.parse()
    for section in message.get_sections():
        print(section, section.tag, section.lines)
    assert len(message.sections) == 12
    
def test_get_sections_no_body():    
    lines = norm_message(messages.Message.MSG2)
    message = Message(lines)
    message.parse()
    message.get_sections()
    assert len(message.sections) == 14
    
def test_get_sections_no_body_and_no_metadata():    
    lines = norm_message(messages.Message.MSG3)
    message = Message(lines)
    message.parse()
    print(message.get_sections())
    assert len(message.sections) == 14