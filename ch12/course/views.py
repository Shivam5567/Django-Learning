from django.shortcuts import render

# using variable
def learn_django(req):
    context = {
        "n": "Shivam",
        "student": {
            "name": "Shivam Kumar",
            "age": 22,
            "course": "Django",
            "city": "Patna"
        }
    }
    return render(req, 'course/django.html', context)
