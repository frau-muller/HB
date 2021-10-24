from django.urls import path
from .views import Quiz, RandomQuestion, QuizQuestion
from django.urls import path
from .views import Quiz, RandomQuestion, QuizQuestion

app_name='history'

urlpatterns = [
    path('', Quiz.as_view(), name='history'),
    path('r/<str:topic>/', RandomQuestionTopic.as_view(), name='RandomQuestionTopic'),
    path('single/<str:title>/', StartQuiz.as_view(), name='history'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
