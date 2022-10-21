from django.shortcuts import redirect, render
from .forms import CommentForm, ReviewForm
from .models import Review, Comment
# Create your views here.

def index(request):
    reviews=Review.objects.all()
    context={
        'reviews':reviews
    }
    return render(request,'reviews/index.html', context)

def create(request):
    if request.method =="POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:index')
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'reviews/create.html',context)


def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm()
    context = {
        "review":review,
        'comment_form':comment_form,
        'comments':review.comment_set.all(),
    }
    return render(request, "reviews/detail.html", context)


def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("reviews:detail", review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        "form": form,
        "review": review,
    }
    return render(request, "reviews/update.html", context)


def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect("reviews:index")

def create_comment(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment_form.save()
    return redirect('reviews:detail', review.pk)