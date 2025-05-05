users = [
    {
    "id":1,
    "name":"John Doe",
    "email":"john@gmail.com"
    },
    {
    "id":2,
    "name":"Jane Doe",
    "email":"jane@gmail.com"
    }
]
def create_user(id,user, email):
    user = {
        "id": id,
        "name": user,
        "email": email
    }
    users.append(user)
    print(f"appended {user}")

def delete_user(id):
    for user in users:
        if user["id"]==id:
            print(f"deleted {user}")
            users.remove(user)
            break

def update_user(id, name, email):
    for user in users:
        if user["id"] == id:
            user["name"] = name
            user["email"] = email
            print(f"updated {user}")
            break
def read_users():
    for user in users:
        print(user)

id = 2
print(users)
create_user(id+1,"rohan", "rohan@gmail.com")
create_user(id+1,"mohan", "mohan@gmail.com")
delete_user(3)
update_user(2, "rohan raji", "rohan@gmail.com")

# appended {'id': 3, 'name': 'rohan', 'email': 'rohan@gmail.com'}
# appended {'id': 3, 'name': 'mohan', 'email': 'mohan@gmail.com'}
# deleted {'id': 3, 'name': 'rohan', 'email': 'rohan@gmail.com'}
# updated {'id': 2, 'name': 'rohan raji', 'email': 'rohan@gmail.com'}

read_users()

# {'id': 1, 'name': 'John Doe', 'email': 'john@gmail.com'}
# {'id': 2, 'name': 'rohan raji', 'email': 'rohan@gmail.com'}
# {'id': 3, 'name': 'mohan', 'email': 'mohan@gmail.com'}