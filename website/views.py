# this file will have bunch of routes inside 
# all route urls


# all of this routes are to be also included in __init__.py
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json # this is for request comming from index.js as JSON, the id of the note to be deleted 

# current_user will hold the info of the user whos logged in 



views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required  # no home page for user not logged in
def home(): # can be any name
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data = note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note successfully added!', category='success')
    return render_template('home.html', user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)  # will take data as a post request, load it as json object||python dictionary
    noteId = note['noteId']   # we'll access note id
    note = Note.query.get(noteId)  # check if exists or not
    if note:
        #if user owns this note
        if note.user_id == current_user.id:   # if user_id in note table holds reference to the id of the current user 
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})  # returning empty response, jsonifying empty python dictionary
