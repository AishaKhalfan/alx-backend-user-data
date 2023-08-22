import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from uuid import uuid4


def _hash_password(password: str) -> bytes:
        """hash password"""
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

def _generate_uuid():
    id = uuid4()
    return str(id)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        try:
            # finding the user using the given email
            user_a = self._db.find_user_by(email=email)
            raise ValueError(f'User_a.email{email} already exists')

        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
        return user

    def valid_login(self, email, password) -> bool:
        try:
            user_b = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        return bcrypt.checkpw(password.encode('utf-8'),user_b.hashed_password)

    def create_session(self, email: str) -> str:
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            user.session_id = _generate_uuid()
            return user.session_id

    def get_user_from_session_id(self, session_id: str) -> User or None:
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None
        """another way of implemting it:
        if session_id is None:
            return None

        user = self._db.find_user_by(session_id=session_id)

        if not user:
            return None

        return user
        """

    def destroy_session(self, user_id: int) -> None:
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None
        else:
            user.session_id = None
            return None

    def get_reset_password_token(self, email: str) -> str:
        user = self._db.find_user_by(email=email)
        if user is None:
            raise ValueError
        user.reset_token = _generate_uuid()
        return user.reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        if reset_token is None and password is None:
            return None
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except (NoResultFound, InvalidRequestError):
            raise ValueError

        new_passwd = _hash_password(password)

        self._db.update_user((user.id), hashed_password=new_passwd,
            reset_token=None)

        return None
