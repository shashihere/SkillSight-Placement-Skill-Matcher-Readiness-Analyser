import base64
import io
import re
from PyPDF2 import PdfReader

from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

SKILLS_DB = [
    "html","css","javascript","react","redux",
    "node.js","nodejs","express","mongodb","mysql",
    "sql","python","java","c","c++",
    "excel","power bi","tableau",
    "machine learning","deep learning","tensorflow","keras","nlp",
    "pandas","numpy","git","github","docker","aws","api","rest api"
]

ROLE_SKILLS = {
    "Frontend Developer": ["html","css","javascript","react"],
    "Backend Developer": ["node.js","express","mongodb","sql"],
    "Full Stack Developer": ["html","css","javascript","react","node.js","mongodb"],
    "Data Analyst": ["python","sql","excel","power bi"],
    "AI/ML Engineer": ["python","machine learning","deep learning","tensorflow","nlp"]
}

def clean_text(txt):
    if not txt:
        return ""
    txt = txt.lower()
    return re.sub(r'\s+', ' ', txt)

def detect_skills(text):
    lower_text = clean_text(text)
    detected = []
    for skill in SKILLS_DB:
        if skill.lower() in lower_text:
            detected.append(skill)
    return detected

def calculate_resume_score(skills, role):
    required = ROLE_SKILLS.get(role, [])
    if not required:
        return 0
    matched = [skill for skill in required if skill in skills]
    return round((len(matched) / len(required)) * 100)

@api_view(['GET'])
def root_view(request):
    return Response("SkillSight Server Running 🚀")

@api_view(['POST'])
@parser_classes([JSONParser])
def analyze_pdf(request):
    try:
        file_data = request.data.get('fileData', '')
        if not file_data:
            return Response({'error': 'No file data'}, status=400)
            
        buffer = base64.b64decode(file_data)
        reader = PdfReader(io.BytesIO(buffer))
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
            
        return Response({'text': text})
    except Exception as e:
        return Response({'error': 'PDF parsing failed'}, status=500)

@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_resume(request):
    try:
        role = request.data.get('role', 'Frontend Developer')
        resume_file = request.FILES.get('resume')
        
        if not resume_file:
            return Response({'error': 'No resume file'}, status=400)
            
        reader = PdfReader(resume_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
            
        skills = detect_skills(text)
        required = ROLE_SKILLS.get(role, [])
        gap = [skill for skill in required if skill not in skills]
        score = calculate_resume_score(skills, role)
        
        return Response({
            'score': score,
            'detectedSkills': skills,
            'requiredSkills': required,
            'skillGap': gap
        })
    except Exception as e:
        return Response({'error': 'Upload failed'}, status=500)

@api_view(['POST'])
@parser_classes([JSONParser])
def get_suggestions(request):
    try:
        data = request.data
        role = data.get('role', 'Unknown Role')
        final_score = data.get('finalScore', 0)
        missing_skills = data.get('missingSkills', [])
        
        is_fit = final_score >= 60
        
        reason = "Good technical + test performance." if is_fit else "Needs improvement in core skills."
        
        improvement_plan = [
            "Practice missing skills daily",
            "Build real-world projects",
            "Improve GitHub profile",
            "Prepare for interviews"
        ]
        
        roadmap = [
            "Step 1: Learn fundamentals",
            "Step 2: Practice coding",
            "Step 3: Build projects",
            "Step 4: Mock interviews",
            "Step 5: Apply for jobs"
        ]
        
        missing_skills_str = ", ".join(missing_skills) if missing_skills else "None"
        
        output = f"""

ROLE: {role}

REASON: {reason}

SKILL GAPS: {missing_skills_str}

IMPROVEMENT PLAN:
- {"\n- ".join(improvement_plan)}

ROADMAP:
- {"\n- ".join(roadmap)}

MOTIVATION:
Stay consistent — success will come 🚀  
You are very close to success 💪  
Keep improving daily 🔥
"""
        return Response({
            'response': output,
            'isFit': is_fit
        })
    except Exception as e:
        return Response({'response': 'Error generating suggestions'}, status=500)

@api_view(['POST'])
@parser_classes([JSONParser])
def register(request):
    try:
        data = request.data
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return Response({'error': 'Email and password required'}, status=400)
        if User.objects.filter(username=email).exists():
            return Response({'error': 'User already exists'}, status=400)
        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'name': user.first_name, 'email': user.email})
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
@parser_classes([JSONParser])
def login_view(request):
    try:
        data = request.data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'name': user.first_name, 'email': user.email})
        return Response({'error': 'Invalid credentials'}, status=401)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

