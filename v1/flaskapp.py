# coding=utf-8
from v1 import app, api, api_version

# CONTROLLERS
# ADMIN
from v1.resources.admin.ClientController import ClientController, ClientListController
from v1.resources.admin.UserController import UserListController, UserController
from v1.resources.admin.LoginController import LoginController
from v1.resources.admin.LogoutController import LogoutController
from v1.resources.admin.AccountController import AccountController, AccountListController
from v1.resources.admin.DeviceController import DeviceController, DeviceListController
from v1.resources.admin.SessionController import SessionController, SessionListController
# LIBRARY
from v1.resources.library.LibraryController import LibraryListController, LibraryController
from v1.resources.library.SchoolController import SchoolListController, SchoolController
from v1.resources.library.BookController import BookController, BookListController
from v1.resources.library.SearchController import SearchListController
from v1.resources.library.NewBookController import NewBookListController


"""
    API BOOKS UNAM
    version: v1
    
    URI: api/version/
    
    USERS:      /users                  [POST, GET, PUT, DELETE, PATCH]
    LOGIN:      /users/login            [POST]
    LOGOUT:     /users/logout           [POST]
    ACCOUNT:    /accounts               [POST, GET, PUT, DELETE, PATCH]
    LIBRARIES:  /libraries              [POST, GET, PUT, DELETE, PATCH]
           
"""


# ACCESS POINT 'users':
api.add_resource(UserController, api_version + "/users/<string:id>")
api.add_resource(UserListController, api_version + "/users")
api.add_resource(LoginController, api_version + "/users/login")
api.add_resource(LogoutController, api_version + "/users/logout")

# ACCESS POINT 'account':
api.add_resource(AccountController, api_version + "/accounts/<string:id>")
api.add_resource(AccountListController, api_version + "/accounts")

# ACCESS POINT 'library':
api.add_resource(LibraryController, api_version + "/libraries/<string:id>")
api.add_resource(LibraryListController, api_version + "/libraries")

# ACCESS POINT 'clients':
api.add_resource(ClientController, api_version + "/clients/<string:id>")
api.add_resource(ClientListController, api_version + "/clients")

# ACCESS POINT 'schools':
api.add_resource(SchoolController, api_version + "/schools/<string:id>")
api.add_resource(SchoolListController, api_version + "/schools")


# ACCESS POINT 'devices':
api.add_resource(DeviceController, api_version + "/devices/<string:id>")
api.add_resource(DeviceListController, api_version + "/devices")

# ACCESS POINT 'sessions':
api.add_resource(SessionController, api_version + "/sessions/<string:id>")
api.add_resource(SessionListController, api_version + "/sessions")

# ACCESS POINT 'books':
api.add_resource(BookController, api_version + "/books/<string:id>")
api.add_resource(BookListController, api_version + "/books")

# ACCESS POINT 'search':
api.add_resource(SearchListController, api_version + "/search")
# ACCESS POINT 'news books':
api.add_resource(NewBookListController, api_version + "/news")



if __name__ == '__main__':
    app.run(app.config['IP'], app.config['PORT'])
