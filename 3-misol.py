def kutib_olish(ism_shahar_davlat):

    birlashtirilgan_satr = " ".join(ism_shahar_davlat)

    return f"Salom, {birlashtirilgan_satr}!"

print(kutib_olish(["Ali"]))                        
print(kutib_olish(["Ali", "Toshkent"]))              
print(kutib_olish(["Ali", "Toshkent", "O'zbekiston"])) 
