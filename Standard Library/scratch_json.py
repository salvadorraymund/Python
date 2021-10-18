import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# print(todos[:10]

# map of userID to number of complete TODOs for that user
todos_by_user = {}
default_val = 0
# Increment complete TODOs count for each user
for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo['userId']] += 1
        except KeyError:
            todos_by_user[todo['userId']] = 1

# try:
#     # increment the existing user count
#     todos_by_user[todo['userId']] += 1
# except KeyError:
#     # this user has not been seen. set their count to 1
#     todos_by_user[todo['userId']] = 1

# Create a sorted list of (userId, num_complete) pairs
print(todos_by_user)
top_users = sorted(todos_by_user.items(),
                   key=lambda x: x[1], reverse=True)
print('Top users: ', top_users)
# Get the maximum number of complete TODOs
max_complete = top_users[0][1]
print('Max complete: ', max_complete)

# Create a list of users who have completed the max number of TODOs
# users = [str(user)
#          for user, num_complete in top_users if num_complete < max_complete]
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

# s = 's' if len(users) > 1 else ""
# print(f'user{s} {max_users} completed {max_complete} TODOs')

# Define a function to filter out completed TODOs
# of users with max completed TODOs


def keep(todo):
    is_complete = todo['completed']
    has_max_count = str(todo['userId']) in users
    return is_complete and has_max_count


# write filtered TODOs file
with open('filtered_data_file.json', 'w') as json_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, json_file, indent=2)
