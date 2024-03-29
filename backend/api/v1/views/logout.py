#!/usr/bin/pyhton3
"""Logout user"""
from flask import redirect, url_for, flash
from flask_login import logout_user
from flasgger import swag_from
from api.v1.views import app_views


@app_views.route('/logout', methods=['GET'])
@swag_from('documentation/logout/logout.yml', methods=['GET'])
def logout():
    """Logs out the current user."""
    logout_user()
    flash('You have been logged out successfully', 'success')
    return redirect(url_for('index'))
