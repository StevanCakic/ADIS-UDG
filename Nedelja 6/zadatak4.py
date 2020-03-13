def mostly_repeated(lista):
    skup = set(lista)
    max_count = 0 

    for elem in skup:
        if lista.count(elem) >= max_count:
            max_count = lista.count(elem)
            result = (elem, max_count)
    
    return result

common_friends = []
with open("friends.txt") as file:
    all_friends = file.read().split("\n")
    list_with_ids = []
    for friend in all_friends:
        friend_info = friend.split(",")
        list_with_ids.append(int(friend_info[0]))
  
    friend_with_most_common_friends = mostly_repeated(list_with_ids)
    friends_ids = []
    file_name = ""
    for friend in all_friends:
        friend_info = friend.split(",")
        num = int(friend_info[0])
        if num == int(friend_with_most_common_friends[0]):
            file_name = str(friend_info[1] + " " + friend_info[2])
            friends_ids.append(friend_info[3])

    for friend in all_friends:
        friend_info = friend.split(",")
        friend_id = friend_info[0]
        if friend_id in friends_ids:
            common_friends.append(f"{friend_info[1]} {friend_info[2]}")
            friends_ids.pop(0)
    
with open(file_name.lower() + ".txt", mode="w") as file:
    for friend in common_friends:
        file.write(friend + "\n")