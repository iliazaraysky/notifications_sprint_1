from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from .settings import Config
from flask_migrate import Migrate


db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()


def create_app(config=Config):
    app = Flask(__name__)
    app.config['SWAGGER'] = {
        'title': 'Authentication Service. Sprint 6',
        'uiversion': 3
    }
    swagger = Swagger(app)
    app.config.from_object(config)
    config_blue(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)


    from api.v1.swagger import swagger_view
    from api.v1 import VERSION_PREFIX

    app.add_url_rule('/auth' + VERSION_PREFIX + 'registration',
                     view_func=swagger_view.RegistrationView.as_view('registration'),
                     methods=['POST'])

    app.add_url_rule('/auth' + VERSION_PREFIX + 'login',
                     view_func=swagger_view.LoginView.as_view('login'),
                     methods=['POST'])

    app.add_url_rule('/auth' + VERSION_PREFIX + 'logout',
                     view_func=swagger_view.LogoutView.as_view('logout'),
                     methods=['DELETE'])

    app.add_url_rule('/auth' + VERSION_PREFIX + 'user/token/refresh',
                     view_func=swagger_view.RefreshToken.as_view('refresh'),
                     methods=['POST'])

    app.add_url_rule('/auth' + VERSION_PREFIX + 'user/change-password/<uuid:user_uuid>',
                     view_func=swagger_view.ChangeUserPassword.as_view('change password'),
                     methods=['PATCH'])

    app.add_url_rule('/auth' + VERSION_PREFIX + 'user/<uuid:user_uuid>',
                     view_func=swagger_view.GetUserHistory.as_view('user hishory'),
                     methods=['GET'])

    app.add_url_rule('/auth' + VERSION_PREFIX + 'user/<uuid:user_uuid>/add-role',
                     view_func=swagger_view.AddUserRole.as_view('user role'),
                     methods=['POST'])

    app.add_url_rule('/auth' + VERSION_PREFIX + 'user/<uuid:user_uuid>/delete-role',
                     view_func=swagger_view.DeleteUserRole.as_view('delete role'),
                     methods=['POST'])

    app.add_url_rule('/auth' + VERSION_PREFIX + 'roles',
                     view_func=swagger_view.CreateRole.as_view('create role'),
                     methods=['POST'])

    app.add_url_rule('/auth' + VERSION_PREFIX + 'roles',
                     view_func=swagger_view.GetRoleList.as_view('roles list'),
                     methods=['GET'])

    app.add_url_rule('/auth' + VERSION_PREFIX + 'roles/<uuid:role_uuid>',
                     view_func=swagger_view.EditRole.as_view('edit role'),
                     methods=['PATCH'])

    app.add_url_rule('/auth' + VERSION_PREFIX + 'roles/<uuid:role_uuid>',
                     view_func=swagger_view.DeleteRole.as_view('delete roles'),
                     methods=['DELETE'])

    app.add_url_rule('/auth' + VERSION_PREFIX + 'permission',
                     view_func=swagger_view.CreatePermission.as_view('create permission'),
                     methods=['POST'])

    app.add_url_rule('/auth' + VERSION_PREFIX + 'roles/<uuid:role_uuid>/add-permission',
                     view_func=swagger_view.AddRolePermission.as_view('add role permission'),
                     methods=['POST'])

    app.add_url_rule('/auth' + VERSION_PREFIX + 'roles/<uuid:role_uuid>/delete-permission',
                     view_func=swagger_view.DeleteRolePermission.as_view('delete role permission'),
                     methods=['POST'])

    return app


def config_blue(app):
    from api.v1.users_view import blueprint as users_blueprint
    from api.v1.users_view import blueprint_admin_create as admin_blueprint

    from api.v1.roles_view import blueprint as roles_blueprint
    from api.v1.permissions_view import blueprint as permissions_blueprint

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(roles_blueprint)
    app.register_blueprint(permissions_blueprint)
