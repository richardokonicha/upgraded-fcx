
from tgbot.models.database import Database, create_tables
from tgbot.models.model import User

# Create the tables
create_tables()

# Create an instance of the Database class
db = Database()

# Access the User class outside the Database
UserClass = User

# Use the User class to create users
user_instance = UserClass(user_id=9, name="Biden")

# Commit changes
db.session.add(user_instance)
db.commit()
