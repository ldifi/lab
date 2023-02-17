god = input()
god = int(god)
if god % 4 == 0 and god % 100 != 0 or god % 400 == 0:
    print("Visokosniy")
else:
    print("Nevisokosniy")