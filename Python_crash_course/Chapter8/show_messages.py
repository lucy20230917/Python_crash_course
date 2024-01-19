messages = ['good luck!','hello,world','have a nice day!']
sent_messages = []

def show_messages(messages):
    for message in messages:
        print(f'\nYou get a new massage: {message}')


def send_messages(unsend_messages,sent_messages):
    while unsend_messages:
        current_senting = unsend_messages.pop()
        print(f"Senting message: {current_senting}")
        sent_messages.append(current_senting)
send_messages(messages[:],sent_messages)
show_messages(messages)
