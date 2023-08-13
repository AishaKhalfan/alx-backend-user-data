#!/usr/bin/env python3
"""
Module for authentication using Session auth
"""
from api.v1.auth.auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """
    inherits from Auth
    """
