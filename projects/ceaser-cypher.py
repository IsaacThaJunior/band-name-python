alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(start_text, shift_amount, cipher_direction):
    complete_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for i in start_text:
        if i in alphabet:
            position = alphabet.index(i)

            new_position = position + shift_amount
            complete_text += alphabet[new_position]
        else:
            complete_text += i
    print(f'The {cipher_direction}d text is {complete_text}')

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  caeser(start_text=text, shift_amount=shift, cipher_direction=direction)

  result = input('Type yes to contine and no to stop ')
  if result == 'no':
    should_continuen= False

