from utils import load_data, append_to_notes
from database import Note

print(load_data('banco'))
append_to_notes(Note(title='Realizando teste',content='Yes! Funfou!'))
print(load_data('banco'))