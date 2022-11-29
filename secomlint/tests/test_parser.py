from secomlint.message import Message
import messages

def norm_message(msg):
    return msg.value.lower().split('\n')

def test_get_sections_all():    
    lines = norm_message(messages.Message.MSG1)
    message = Message(lines)
    message.get_sections()
    assert len(message.sections) == 9
    
def test_get_sections_no_body():    
    lines = norm_message(messages.Message.MSG2)
    message = Message(lines)
    message.get_sections()
    assert len(message.sections) == 8
    
def test_get_sections_no_body_and_no_metadata():    
    lines = norm_message(messages.Message.MSG3)
    message = Message(lines)
    message.get_sections()
    assert len(message.sections) == 4