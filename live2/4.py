# 0 - 3 -> Junior
# 3 - 5 -> Pleno
# >   5 -> Senior

anos_dev = int (input("Quando ano como desenvolvedor? "))

if (anos_dev <= 3):
    print ("Desenvolvedor Junior")
elif (anos_dev <= 5):
    print ("Desenvolvedor Pleno")
else:
    print ("Desenvolvedor Senior")