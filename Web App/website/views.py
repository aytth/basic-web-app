# Stores the standard routes for the website, i.e. different places user can go
# login goes in auth (authentication)

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__, template_folder="templates")

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method=='POST':
        note = request.form.get('note')
        if (len(note)<1):
            flash("Note is too short", category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')
    # Returns the home page code of home.html
    return render_template('home.html', user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteID = note['noteID']
    note = Note.query.get(noteID)
    
    if note:
        if note.user_id==current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
        