def count_letters(text):
    results = {}
    text = text.lower()
    for x in text:
        if x not in results:
            results[x] = 0
        results[x] += 1
    return results

#print(count_letters("Spaces and capitalization is counted as their own. Space ships "))

def iteration():
    dictionary = {"apple" : 3, "orange" : 5, "banana" : 9, "gauva" : 12, "pineapple" : 15}
    for fruits, values in dictionary.items():
        print(f"Number {values} is {fruits}")

    print("Left side are Keys: ", dictionary.keys())
    print("Right side are Values: ", dictionary.values())
#iteration()

fruits = {'1' : ['orange', 'apple'], '2' : ['banana', 'kiwi'], '3' : ['gauva', 'jackfruit']}
new_items = {'1' : ['grape'], '3' : ['grapefruit']}
fruits.update(new_items)


def groups_per_user(group_dictionary):
	user_groups = {}
	for group, users in group_dictionary.items():
		for user in users:
			if user not in user_groups:
				user_groups[user] = []
			user_groups[user].append(group)
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))