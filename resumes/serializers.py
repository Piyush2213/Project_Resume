from rest_framework import serializers
from .models import Resume, Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'full_name', 'email']

class ResumeSerializer(serializers.ModelSerializer):
    candidate = CandidateSerializer(required=False)
    class Meta:
        model = Resume
        fields = ['id', 'candidate', 'resume_file', 'extracted_text', 'uploaded_at']

    def create(self, validated_data):
        candidate_data = validated_data.pop('candidate')
        candidate, created = Candidate.objects.get_or_create(
            email=candidate_data.get('email'),
            defaults={'full_name': candidate_data.get('full_name')}
        )
        resume = Resume.objects.create(candidate=candidate, **validated_data)
        return resume
