import json
import os
from database import Note, Database

def extract_route(request):
    
    end = 0
    for i in range(4, len(request)):
        if request[i] == ' ':
            end = i
            break
    return request[5 : end]

def read_file(Path):

    path = str(Path)
    f_type = path.split('.')[-1]

    if(f_type in ['txt','html','css','js']):
        with open(path,'r',encoding='utf-8') as f:
            return f.read().encode()
    else:
        with open(path,'rb') as f:
            return f.read()

def load_data(db):

    database = Database(f'data/{db}')
    return database.get_all()

def load_template(file):

    with open(f'templates/{file}', 'r', encoding='utf-8') as f:
        return f.read()

def append_to_notes(note,db='banco'):

    database = Database(f'data/{db}')
    database.add(note)

def remove_from_notes(note,db='banco'):

    database = Database(f'data/{db}')
    notes = database.get_all()
    id = None
    for _note in notes:
        if ((_note.title == note.title) and (_note.content == note.content)) or ((_note.title == '' and note.title == '/') and (_note.content == note.content)) or ((_note.title == note.title) and (_note.content == '' and note.content == '/')):
            id = _note.id
            break
    database.delete(id)

def update_notes(note,old_note,db='banco'):

    database = Database(f'data/{db}')
    notes = database.get_all()
    id = None
    for _note in notes:
        if ((_note.title == old_note.title) and (_note.content == old_note.content)) or ((_note.title == '' and old_note.title == '/') and (_note.content == old_note.content)) or ((_note.title == old_note.title) and (_note.content == '' and old_note.content == '/')):
            id = _note.id
            break
    note.id = id
    database.update(note)


def build_response(body='', code=200, reason='OK', headers=''):
    
    if len(headers) > 0:
        return f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'.encode()
    return f'HTTP/1.1 {code} {reason}\n\n{body}'.encode()