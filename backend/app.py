# This should be the main backend entry point.

# It should:

# create the app
# enable CORS
# register menu routes
# register order routes
# start the server

# So app.py should be small. It should mostly wire everything together.
from backend.repository import get_menu, get_all_orders

print(get_menu().get_categories())
print(len(get_menu().get_items()))
print(get_all_orders())