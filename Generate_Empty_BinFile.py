###########################
# Empty binfile creator   #
# Made by E.Daemen        #
###########################

while True:
  Size = input("Please enter size of bin file (MB):")
  try:
      num = int(Size)
      print("Generating file of: " + str(num) + "MB")
      break;
  except ValueError:
      try:
        num = float(Size)
        break;
      except ValueError:
        print("Input is not a number!")
     
FileName = str(num + ".bin")
with open(FileName, "wb") as binfile:
  binfile.write(b"x\00" * int(Size) * 1024 * 1024)
  print("File generated!")
