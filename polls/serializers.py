from rest_framework import serializers
from polls.models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        # fields = '__all__'
        fields = ('id', 'question_text', 'pub_date', 'was_published_recently')
