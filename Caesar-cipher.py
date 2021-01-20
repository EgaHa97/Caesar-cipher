def encrypt(string):
   alf = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
   new = []
   for i in string:
       if i not in alf:
           new.append(i)
       else:
           if  i == "z":
               new.append("a")
           else:
               new.append(alf[alf.index(i)+3])
   return "".join(new)
word = input('Enter a word for encryption: ')
print(encrypt(word))