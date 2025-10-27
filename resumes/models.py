from django.db import models

class Candidate(models.Model):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
   

    def __str__(self):
        return self.full_name
    

class Resume(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    
    
    resume_file = models.FileField(upload_to='resumes/')
    extracted_text = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume for {self.candidate.full_name}"