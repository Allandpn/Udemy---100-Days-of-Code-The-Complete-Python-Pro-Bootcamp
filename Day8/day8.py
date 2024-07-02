from day8_art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direct_range = ["encode", "decode"]
continu = True



print(logo)
    
def ceasar(text, shift, direction):
    if direction not in direct_range:
        print(f"Word {direction} is not a valid direction")
        return    
    result_text = ""
    if direction == "decode":
        shift *= -1
    for l in text:
        if l not in alphabet:
            result_text = l
        else:
            index = (alphabet.index(str.lower(l)) + shift) % 26
            result_text += alphabet[index]
    print(f"The {direction} text is {result_text}")




while continu:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    ceasar(text=text, shift=shift, direction=direction)
    
    continu_ = input("Do you want continue? ")
    
    if continu_ == "no":
        continu = False
        print("Goodbye")