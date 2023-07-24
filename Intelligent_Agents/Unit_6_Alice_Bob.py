from pykqml import KQMLPerformative
from pyparsing import nestedExpr

def alice():
    # Alice asks about the available stock of 50-inch televisions
    content = '(request (stock-level (product-type "50-inch TV")))'
    alice_message = KQMLPerformative(content)
    return alice_message

def bob(message):
    # Bob processes Alice's message
    content = message.get_parameter('content')
    parsed_content = nestedExpr(opener='(', closer=')').parseString(content).asList()

    if parsed_content[0][0] == 'request' and parsed_content[1][0] == 'stock-level':
        # Bob responds to Alice's stock-level query
        response_content = '(inform (stock-level (product-type "50-inch TV") 10))'
        bob_response = KQMLPerformative(response_content)
        return bob_response

    if parsed_content[0][0] == 'request' and parsed_content[1][0] == 'number-of-slots':
        # Bob responds to Alice's number-of-slots query
        response_content = '(inform (number-of-slots (product-type "50-inch TV") 4))'
        bob_response = KQMLPerformative(response_content)
        return bob_response

    return None

# Simulate the dialogue
alice_message = alice()
print(f'Alice: {alice_message}')

bob_response = bob(alice_message)
print(f'Bob: {bob_response}')
