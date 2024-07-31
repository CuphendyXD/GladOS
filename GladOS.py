L = list ["1.Info", "2.Test Subjects", "3.Test Chambers","4.Footage"]

U = input("User: ")
P = input("password:")
print("welcome", P)

print("""-------------------------------GladOS---------------------------------
              .,-:;//;:=,
          . :H@@@MM@M#H/.,+%;,
       ,/X+ +M@@M@MM%=,-%HMMM@X/,
     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
  ,%MM@@MH ,@%=             .---=-=:=,.
  =@#@@@MX.,                -%HX$$%%%:;
 =-./@M@M$                   .;@MMMM@MM:
 X@/ -$MM/                    . +MM@@@M$
,@M@H: :@:                    . =X#@@@@-
,@@@MMX, .                    /H- ;@M@M=
.H@@@@M@+,                    %MM+..%#$.
 /MMMM@MMH/.                  XM@MH; =;
  /%+%$XHH@$=              , .H@@@@MX,
   .=--------.           -%H.,@@@@@MX,
   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.
     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
       =%@M@M#@$-.=$@MM@@@M; %M%=
         ,:+$+-,/H#MMMMMMM@= =,
               =++%%%%+/:-.""")
print("Aperture science Inc. Welcomes you to the Genetic Lifeform and Disk Operating System")

#option chosing

def menu():
       print("[0]Exit")
       print("[1]Test records")
       print("[2]Test Recordings")
       print("[3]Handbook")

menu()
option = int(input("enter your option: "))
#options
while option != 5:
       if option == 0:
              print("""Exiting...
orders will no longer be taken""")
              option = 6
#option 1
       elif option == 1:
              print("folder is empty*")
              R = input("return to selection? ")
              if R == "yes":
                     option = 5
              else:
                     option = 6

#option 2
       elif option == 2:
              input("""1·Jake-16/4.avi
2·William-28/6.avi
3·Aaron-29/7.avi
4·Chell-30/7.avi
""")
              print("video file corrupt or non existant")
              R = input("return to selection? ")
              if R == "yes":
                     option = 5
              else:
                     option = 6
#option 3

       elif option == 3:
              print("to be uploaded...")
              option = 5
       R = input("return to selection? ")
       if R == "yes":
              option = 5
       else:
              option = 6

#Repeat

if option != 6:
       option = 5
       print()
       menu()
       option = int(input("Enter your option: "))
