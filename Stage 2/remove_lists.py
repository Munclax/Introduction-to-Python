games=["COC","Forza Horizon 4","NFS Heat","Witcher","Genshin"]
print(games) #prints the entire list of games
games.remove("COC") #remove() method removes the first matching value, not a specific index
games.pop(2) #pop() method removes the item at the specified index
print(games[2])
print(len(games))
del games[2] #del statement removes the item at the specified index
print(games) #prints the entire list of games
print(len(games))