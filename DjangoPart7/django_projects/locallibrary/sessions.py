""""Using sessions"""
# Get a session value by its key (e.g. 'my_car'), raising a KeyError if the key is not present
my_car = request.session['my_car']

# Get a session value, setting a default if it is not present ('mini')
my_car = request.session.get('my_car', 'mini')

# Set a session value
request.session['my_car'] = 'mini'

# Delete a session value
del request.session['my_car']

""""Saving session data"""

# This is detected as an update to the session, so session data is saved.
request.session['my_car'] = 'mini'

"""
If you're updating some information within session data, then Django will not recognize that you've made a change to the session and save the data (for example,
if you were to change "wheels" data inside your "my_car" data, as shown below). In this case you will need to explicitly mark the session as having been modified.
"""
# Session object not directly modified, only data within the session. Session changes not saved!
request.session['my_car']['wheels'] = 'alloy'

# Set session as modified to force data updates/cookie to be saved.
request.session.modified = True

"""Simple example — getting visit counts
As a simple real-world example we'll update our library to tell the current user how many times they have visited the LocalLibrary home page.

Open /locallibrary/catalog/views.py, and add the lines that contain num_visits into index() (as shown below)."""
