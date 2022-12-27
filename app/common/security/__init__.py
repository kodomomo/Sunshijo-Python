from app.core.user import Role


class AuthProperties:
    _authorization_url = {
        # Teacher
        '/teacher/token': {
            'PUT': [Role.TEACHER]
        },
        '/teacher/list': {
            'GET': [Role.TEACHER]
        },

        # Record
        '/records': {
            'POST': [Role.TEACHER],
            'GET': [Role.TEACHER],
            'PATCH': [Role.TEACHER],
        },
        '/records/list': {
            'GET': [Role.TEACHER]
        }
    }

    @staticmethod
    def role_list(path: str, method: str):
        method_dict = AuthProperties._authorization_url.get(path)

        return None if method_dict is None else method_dict.get(method)
