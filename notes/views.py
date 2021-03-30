from django.shortcuts import render, redirect
from .models import Note, Tag

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = None

        if (request.POST.__contains__('tag')):
            tagType = request.POST.get('tag')
            tags = Tag.objects.all()
            tag = Tag(tag=tagType, label=tagType.replace(' ', '').title())
            for _tag in tags:
                if _tag.tag == tagType:
                    tag = _tag
                    break

        if (request.POST.__contains__('id')):
            id = request.POST.get('id')
            if (tag is not None):
                note = Note(id=id, title=title, content=content, tag=tag)
            else:
                note = Note(id=id, title=title, content=content, tag=tag)
        else:
            if (tag is not None):
                note = Note(title=title, content=content, tag=tag)
            else:
                note = Note(title=title, content=content, tag=tag)

        if (request.POST.__contains__('create')):
            tag.save()
            note.save()
        elif (request.POST.__contains__('delete')):
            note.delete()
        elif (request.POST.__contains__('update')):
            if(request.POST.__contains__('old_title') or request.POST.__contains__('old_details')):
                Note.objects.filter(id=note.id).delete()
                note.save()

        return redirect('/')
    else:
        all_notes = Note.objects.all()
        all_tags = Tag.objects.all()
        tag_path = request.get_full_path()[1:]
        if (len(tag_path) > 0):
            tag_label = tag_path.split('=')[-1]
            for tag in all_tags:
                if (tag.label == tag_label):
                    id = tag.id
                    return render(request, 'notes/index.html', {'notes': all_notes.filter(tag_id=id), 'tags': all_tags.filter(label=tag_label)})
        return render(request, 'notes/index.html', {'notes': all_notes, 'tags': all_tags})
