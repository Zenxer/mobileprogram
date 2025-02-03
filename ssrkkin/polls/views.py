from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# def index(request):
#     latest_question_list = Question.objects.order_by("-Pub_date")[:10]
#     #output = ", ".join( [q.question_field for q in latest_question_list])
#     context = { "latest_question_list":latest_question_list }
#     return render(request, "polls/index.html", context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        browser = self.request.META.get('HTTP_USER_AGENT', '')
        context = super().get_context_data(**kwargs)

        if (('Mobile' in browser) or ('Symbian' in browser)
            or ('Opera M' in browser) or ('Android' in browser)
            or ('HTC_' in browser.upper()) or ('Fennec/' in browser)
            or ('Blackberry' in browser.upper()) or ('Windows Phone' in browser)
            or ('WP7' in browser) or ('WP8' in browser)):
            context["browser"] = 'Mobile'
        else:
            context["browser"] = 'Desktop'

        return context

    def get_queryset(self):
        return Question.objects.filter(
            Pub_date__lte=timezone.now()
        ).order_by("-Pub_date")[:10]

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404('Такого вопроса нет')
#     return render(request, "polls/detail.html", { "question": question } )

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        browser = self.request.META.get('HTTP_USER_AGENT', '')
        context = super().get_context_data(**kwargs)

        if (('Mobile' in browser) or ('Symbian' in browser)
            or ('Opera M' in browser) or ('Android' in browser)
            or ('HTC_' in browser.upper()) or ('Fennec/' in browser)
            or ('Blackberry' in browser.upper()) or ('Windows Phone' in browser)
            or ('WP7' in browser) or ('WP8' in browser)):
            context["browser"] = 'Mobile'
        else:
            context["browser"] = 'Desktop'

        return context

    def get_queryset(self):
        return Question.objects.filter(
            Pub_date__lte=timezone.now()
        )

# def results(request, question_id):
#     # return HttpResponse("Результаты опроса по вопросу№" + str(question_id))
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question":question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        browser = self.request.META.get('HTTP_USER_AGENT', '')
        context = super().get_context_data(**kwargs)

        if (('Mobile' in browser) or ('Symbian' in browser)
            or ('Opera M' in browser) or ('Android' in browser)
            or ('HTC_' in browser.upper()) or ('Fennec/' in browser)
            or ('Blackberry' in browser.upper()) or ('Windows Phone' in browser)
            or ('WP7' in browser) or ('WP8' in browser)):
            context["browser"] = 'Mobile'
        else:
            context["browser"] = 'Desktop'

        return context

    def get_queryset(self):
        return Question.objects.filter(
            Pub_date__lte=timezone.now()
    )

def vote(request, question_id):
    # return HttpResponse('Вы проголосовали в вопросе №' + str(question_id))
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Вы выбрали некорректный вариант ответа"
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect( reverse("polls:results", args=(question_id, )) )