from utils import load_data, load_template, append_to_notes, build_response, remove_from_notes, update_notes
import urllib
from database import Note, Database

def index(request):

    if request.startswith('POST'):
        request = request.replace('\r', '')
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        for chave_valor in corpo.split('&'):
            chave_valor = urllib.parse.unquote_plus(chave_valor, encoding='utf-8', errors='replace')
            chave_valor_split = chave_valor.split('=')
            chave = chave_valor_split[0]
            valor = ''.join(chave_valor_split[1:])
            params[chave] = valor

        note = Note(title=params['titulo'],content=params['detalhes'])
        if('create' in params.keys()):
            append_to_notes(note)
        elif('delete' in params.keys()):
            remove_from_notes(note)
        elif('update' in params.keys()):
            old_note = Note(title=params['old_title'],content=params['old_details'])
            update_notes(note, old_note)

        return build_response(code=303, reason='See Other', headers='Location: /')

    note_template = load_template('components/note.html')
    notes_li = list()
    for note in load_data('banco'):
        if type(note.title) == type(None) or note.title == 'None':
            notes_li.append(note_template.format(title='', details=note.content))
        else:
            notes_li.append(note_template.format(title=note.title, details=note.content))
    notes = '\n'.join(notes_li)

    return build_response(load_template('index.html').format(notes=notes))