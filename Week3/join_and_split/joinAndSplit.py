# From the list, fill the friends list with all the names from the 'csv' 
csv = "Eric,John,Michael,Terry,Graham,TerryG,Brian"

# Using split is much more efficient than repetitively adding names into the new list.
friends_list = csv.split(',')

print("Example of split:", friends_list)

# Example of joining (not written, but it's in the name of the file.. so..)
# Added space after comma to space out the names in the 2nd printed message.
joinedFriends = ', '.join(friends_list)

print("Example of join:", joinedFriends)
