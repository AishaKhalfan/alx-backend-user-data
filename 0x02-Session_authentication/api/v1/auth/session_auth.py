#!/usr/bin/env python3
"""
Module for authentication using Session auth
"""
from api.v1.auth.auth import Auth
from models.user import User
from uuid import uuid4
import uuid
from typing import Dict


class SessionAuth(Auth):
    """
    inherits from Auth
    """
    user_id_by_session_id: Dict = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        # self.user_id_by_session_id = {session_id: user_id}
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID:
        Args:
            session_id: String of the session
        Return:
            User ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        user_id: str = self.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        """
        Returns a User instance based on a cookie value
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)

        if user_id is None:
            return None
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """
        deletes the user session / logout:
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        try:
            del self.user_id_by_session_id[session_id]
        except Exception:
            pass

        return True
