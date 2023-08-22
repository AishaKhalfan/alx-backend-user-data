"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Make a new user"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()

        return new_user

    def find_user_by(self, **kwargs):
        if not kwargs:
            raise InvalidRequestError

        users = self._session.query(User).filter_by(**kwargs).first()
        if not users:
            raise NoResultFound

        return users

    def update_user(self, user_id: int, **kwargs) -> None:
        if not kwargs:
            raise ValueError
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            setattr(user, key, value)  # Update the user's attribute

        self._session.commit()
