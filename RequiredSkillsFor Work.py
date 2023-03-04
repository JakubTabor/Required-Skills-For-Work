

def has_required_skills(person, skills):
    return all(skill in person['skills']for skill in skills)


Jane = {'name': 'Jane Smith',
        'age': 30,
        'skills': ['Python']
        }

John = {'name': 'John Brant',
        'age': 35,
        'skills': ['Python', 'C++']
        }


required_skills = ["Python", "C++"]

print(has_required_skills(Jane, required_skills))
print(has_required_skills(John, required_skills))


