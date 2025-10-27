from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResumeSerializer
from .utils import extract_text_from_pdf, extract_email_from_text

class ResumeUploadView(APIView):
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            file = request.FILES['resume_file']

            # Extract text from PDF
            text = extract_text_from_pdf(file)

            # Extract fields
            email = extract_email_from_text(text)
            
            # Update candidate info
            candidate_data = {
                "email": email
            }

            # Save the resume
            resume = serializer.create({
                "candidate": candidate_data,
                "resume_file": file,
                "extracted_text": text
            })

            return Response(ResumeSerializer(resume).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
