print("3. feladat:")                        #lead - ólom, copper - réz
dens_lead = 11.34
dens_copper = 8.69
vol_lead = 18 #cm^3
vol_copper = 23 #cm^3
mass_of_lead =  vol_lead*dens_lead
mass_of_copper = vol_copper*dens_copper
if(mass_of_copper > mass_of_lead): print("A réz nehezebb")
elif(mass_of_copper < mass_of_lead): print("Az ólom nehezebb")
else: print("Az ólom súlya megegyezik a réz súlyával")

#Eredetileg órán:
print(mass_of_copper>mass_of_copper)
