from app.core.user import Role


class AuthProperties:
    _authorization_url = {
        '/teacher': {
            'GET': [Role.TEACHER]
        },
        '/records': {
            'POST': [Role.TEACHER],
            'GET': [Role.TEACHER]
        }
    }

    @staticmethod
    def role_list(path: str, method: str):
        method_dict = AuthProperties._authorization_url.get(path)

        return None if method_dict is None else method_dict.get(method)
