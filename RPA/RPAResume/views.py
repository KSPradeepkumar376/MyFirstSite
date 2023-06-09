from django.shortcuts import render
from django.core.mail import send_mail

from .Forms import *
from .models import *

def rparesumeindex(request):
    if request.method == "POST":
        form = PersonaldetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    item_list = EducationModel.objects.all()

    return render(request, 'RPAResume/Sample.html', {'dataset': item_list})
def personaldetails(request,idx ):
    try:
        personaldetail = Personaldetailsmodels.objects.get(id=idx)
        skills = SkillsModel.objects.get(skill_id=idx)
        Education = EducationModel.objects.all().filter(Education_id=idx).order_by("-id")
        NTechnical = CertificationModel.objects.all().filter(Certification_id=idx,TECHNICAL="NT")
        Technical = CertificationModel.objects.all().filter(Certification_id=idx,TECHNICAL="T")
        Experience = ExperienceModel.objects.all().filter(Experience_id=idx).order_by("-id")
        SocialMedia = SocialModel.objects.all().filter(SocialMedia_id=idx).order_by("-id")
    except Personaldetailsmodels.DoesNotExist:
        raise Http404("ID does not exist")
    return render(request, 'RPAResume/Resume-index.html', {'personaldetails': personaldetail,'Skills': skills,'Education':Education,'NTechnical':NTechnical,'Technical':Technical,'Experience':Experience,'SocialMedia':SocialMedia})
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'RPAResume/Resume-index.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'RPAResume/Resume-index.html', context)
def Dpersonaldetails(request):
    try:
        personaldetail = Personaldetailsmodels.objects.get(id=1)
        skills = SkillsModel.objects.get(skill_id=1)
        Education = EducationModel.objects.all().filter(Education_id=1).order_by("-id")
        NTechnical = CertificationModel.objects.all().filter(Certification_id=1,TECHNICAL="NT")
        Technical = CertificationModel.objects.all().filter(Certification_id=1,TECHNICAL="T")
        Experience = ExperienceModel.objects.all().filter(Experience_id=1).order_by("-id")
        SocialMedia = SocialModel.objects.all().filter(SocialMedia_id=1)
        Testimonials = TestimonialsModel.objects.all().filter(Testimonials_id=1).order_by("id")
        Knowledge = KnowledgeModel.objects.all().filter(knowledgeModel_id=1).order_by("-id")
        Projects = ProjectsModel.objects.all().filter(Projects_id=1).order_by("-id")
        Comments = CommentsModel.objects.get(comments_id=1)
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            form_data = {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            }
            message = '''
            From:\n\t\t{}\n
            Email:\n\t\t{}\n
            subject:\n\t\t{}\n
            Message:\n\t\t{}\n
            '''.format(form_data['name'], form_data['email'], form_data['subject'], form_data['message'])
            send_mail('You got a mail!', message, '', ['pppradeepkumar376@gmail.com'])
    except Personaldetailsmodels.DoesNotExist:
        raise Http404("ID does not exist")
    return render(request, 'RPAResume/Resume-index.html', {'personaldetails': personaldetail,'Skills': skills,'Education':Education,'NTechnical':NTechnical,'Technical':Technical,'Experience':Experience,'SocialMedia':SocialMedia,'Testimonials':Testimonials,'knowledge':Knowledge,'Projects':Projects,'comments':Comments})
def ProjectDetails(request,idx):
    Projects = ProjectsModel.objects.all().filter(id=idx)
    personaldetail = Personaldetailsmodels.objects.get(id=1)
    SocialMedia = SocialModel.objects.all().filter(SocialMedia_id=1)
    ProjectDetail=ProjectDetailsModel.objects.all().filter(projectdetails_id=idx)
    ProjectList = ""
    for j in ProjectDetail:
        if j.board=="":
            ProjectList=""
        else:
            ProjectList = j.board.split("@")

    for i in Projects:
        return render(request, 'RPAResume/ProjectDetails.html',{'personaldetails': personaldetail,'Projects':Projects,'SocialMedia':SocialMedia,'ProjectDetail':ProjectDetail,'ProjectList':ProjectList})