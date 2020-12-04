names = ("Atik","Kiran","Harsh","Atik")
##Here we are enter two "Atik" but we got just one "Atik" in output
                ###In 2nd line too
comps = ("Dell","Apple","MS","Dell")


zipped = dict(zip(names,comps))  ##From this line we got dictionary format
zipped1 = set(zip(names,comps))
print(zipped)
print(zipped1)