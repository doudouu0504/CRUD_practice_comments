from django.shortcuts import redirect, get_object_or_404
from resumes.models import Resume
from .models import Comments


def index(request, id):
    resumes = get_object_or_404(Resume, id=id)
    content = request.POST.get("content")
    comment = resumes.comments_set.create(content=content)
    comment.save()
    return redirect("resumes:show", id=resumes.id)


def delete(request, id):
    comments = get_object_or_404(Comments, id=id)
    if request.POST:
        comments.delete()
        return redirect("resumes:show", id=comments.resume.id)


# Create your views here.
