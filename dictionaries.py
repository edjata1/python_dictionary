print()
print('*********** Dictionaries *************')
# store values in [key : value] pairs 
band = {
    "vocals" : "Plant",
    "guitar" : "Page"
}
print(band)
print(type(band))
print(len(band))

band2 = dict(vocals="Plant", guitar = "Page") # with constructor
print(band2)
print(type(band2))
print(len(band2))


print()
print('*********** access items in Dictionary *************')
print(band['vocals'])
print(band.get("guitar"))
print(band2['vocals'])
print(band2.get("guitar"))

print()
print('*********** list all keys in Dictionary *************')
print(band.keys())
print(band2.keys())

print()
print('*********** list all value in Dictionary *************')
print(band.values())
print(band2.values())

print()
print('*********** list of key/value pairs as tuples *************')
print(band.items())
print(band2.items())


print()
print('*********** verify key exists in dictionary *************')
print("guitar" in band)
print("vocals" in band)
print("singer" in band)
print("guitar" in band2)
print("vocals" in band2)
print("singer" in band2)

print()
print('*********** change values in dictionary *************')
band["vocals"] = "Coverdale" 
band.update({"bass": "RVR"})
print(band)

band2["vocals"] = "Cyndy" 
band2.update({"bass": "JPJ"})
print(band2)

print()
print('*********** Remove items in dictionary *************')
print(band.pop("bass"))
print(band)

print(band2.pop("bass"))
print(band2)

band["drums"] = " Bonham" # adding to dictionary
band2["drums"] = " Goodie" # adding to dictionary
print(band)
print(band2)

print(band.popitem()) # returns as tuple
print(band2.popitem()) # returns as tuple
print(band)
print(band2)

print()
print('*********** delete and clear from dictionary *************')
band["drums"] = " Bonham" # adding to dictionary
band2["drums"] = " Goodie" # adding to dictionary

del band['drums']
print(band)

band2.clear()
print(band2)

del band2

print()
print('*********** copy dictionary *************')
# DOES NOT COPY!!!
band2 = band # Creates a reference. referring to same location in memory
print("BAD COPY!!")
print(band2)
print(band)
band2["drums"] = "Empress"
print(band) # WAS CHANGED, BUT NOTHING DONE TO BAND

print("GOOD COPY!!")
band2 = band.copy()
band2["drums"] = "Dave"
print(band2)
print(band)

# or use the dict() constructure function
print("Good copy! Using constructure")
band3 = dict(band)
print(band3)

print()
print('*********** Nested dictionary *************')
# the value for key can be another dictionary
member1 = {"name": "Plant", "instrument": "vocals"}
member2 = {"name": "Page", "instrument": "guitar"}
band4 = {"member1": member1, "member2": member2}
print(band4)
# get specific value
print(band4["member1"]["name"])

x = band4.pop("member1")

print(x)
