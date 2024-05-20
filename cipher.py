from words import alphabets
from ascii_art import caeser_cipher

def cipher(text,direction,shift):
  msg=""
  if direction=="decode":
    shift*=-1
  for i in text:
    if i in alphabets:
      position=alphabets.index(i)
      msg+=alphabets[position+shift]
    else:
      msg+=i
  print(f"The {direction}d text is \'{msg}\'")

repeatition=True
print(caeser_cipher)

while repeatition==True:
  direction=input("Type \'encode\' to encrypt, type \'decode\' to decrypt:- ")
  
  text=input("Type your message:- ")
  shift=int(input("Type the shift number:- "))
  
  if shift>=26:
    shift%=26
  
  cipher(text,direction,shift)
  
  r=input("Type \'yes\' if you want to go again. Otherwise type \'no\'.")
  if r=="no":
    repeatition=False
    print("See you soon.......Goodbye")
