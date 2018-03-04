Synopsis

Create a mineral catalogue on the Django framework using PyCharm. The purpose of this website is to be able to display all minerals from a preconfigured json file and drill into their details one by one, while searching and filtering by name and mineral group. There is even a find random mineral button.

Code Example

The code library contains 1 application (minerals) that refers to a database model in **models.py** and form structure in **views.py.**

The application uses the Django framework to route the user between index.html, detail.html, and home.html -> a file layout.html is used to reduce the amount of repeatable .html code in the application, custom templates are used to loop through instances of the minerals object class using a Jinja2 like framework specific to Django.

For Example - in minerals:

**SAMPLE DATA**
Note that this data set is missing many data elements such as "specific gravity"

	{
		"name": "Abelsonite",
		"image filename": "240px-Abelsonite_-_Green_River_Formation%2C_Uintah_County%2C_Utah%2C_USA.jpg",
		"image caption": "Abelsonite from the Green River Formation, Uintah County, Utah, US",
		"category": "Organic",
		"formula": "C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
		"strunz classification": "10.CA.20",
		"crystal system": "Triclinic",
		"unit cell": "a = 8.508 Å, b = 11.185 Åc=7.299 Å, α = 90.85°β = 114.1°, γ = 79.99°Z = 1",
		"color": "Pink-purple, dark greyish purple, pale purplish red, reddish brown",
		"crystal symmetry": "Space group: P1 or P1Point group: 1 or 1",
		"cleavage": "Probable on {111}",
		"mohs scale hardness": "2–3",
		"luster": "Adamantine, sub-metallic",
		"streak": "Pink",
		"diaphaneity": "Semitransparent",
		"optical properties": "Biaxial",
		"group": "Organic Minerals"
	},


The underlying data model behind the ORM is a follows in **models.py**:

	class Mineral(models.Model):
	    name = models.CharField(max_length=250, null=True)
	    image_filename = models.CharField(max_length=250, null=True)
	    image_caption = models.CharField(max_length=250, null=True)
	    category = models.CharField(max_length=250, null=True)
	    formula = models.CharField(max_length=250, null=True)
	    strunz_classification = models.CharField(max_length=250, null=True)
	    crystal_system = models.CharField(max_length=250, null=True)
	    unit_cell = models.CharField(max_length=250, null=True)
	    color = models.CharField(max_length=250, null=True)
	    crystal_symmetry = models.CharField(max_length=250, null=True)
	    cleavage = models.CharField(max_length=250, null=True)
	    mohs_scale_hardness = models.CharField(max_length=250, null=True)
	    luster = models.CharField(max_length=250, null=True)
	    streak = models.CharField(max_length=250, null=True)
	    diaphaneity = models.CharField(max_length=250, null=True)
	    optical_properties = models.CharField(max_length=250, null=True)
	    refractive_index = models.CharField(max_length=250, null=True)
	    crystal_habit = models.CharField(max_length=250, null=True)
	    specific_gravity = models.CharField(max_length=250, null=True)
	    group = models.CharField(max_length=250, null=True)


**urls.py** is used to route the user to /index/detail

	urlpatterns = [
	    path('', views.index, name='index'),
	    path('<int:pk>/', views.detail, name='detail'),
	] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

**views.py** renders the details and index HTML files

	def index(request):
	    minerals = Mineral.objects.all()
	    return render(request, 'index.html', {'minerals': minerals})

**index.html**

	{% extends "layout.html" %}
	{% block content %}
	        <div class="grid-100">
	            <ul class="minerals__container">
	                {% for mineral in minerals %}
	                <li class="minerals__item">
	                    <a class="minerals__anchor" href={% url 'minerals:detail' pk=mineral.pk %}>{{ mineral.name|title }}</a>
	                </li>
	                {% endfor %}
	            </ul>
	        </div>
	{% endblock %}


	def detail(request, pk):
	    mineral = get_object_or_404(Mineral, pk=pk)
	    return render(request, 'detail.html', {'mineral': mineral})

**detai.html**

	{% extends "layout.html" %}
	{% load mineral_extras %}
	{% block content %}
	    <div class="grid-100 mineral__container">
	      <h1 class="mineral__name">{{ mineral.name|title }}</h1>
	      <div class="mineral__image-bg">
	        <img class="mineral__image" src="/static/images/{{ mineral.name }}.jpg">
	        <p class="mineral__caption">{{ mineral.image_caption|title }}</p>
	      </div>
	      <div class="mineral__table-container">
	        <table class="mineral__table">
	          <tr>
	            <td class="mineral__category">Category</td>
	            <td>{{ mineral.category|title }}</td>
	          </tr>
	          <tr>
	            <td class="mineral__category">Formula</td>
	            <td class="mineral__formula">{{ mineral.formula|markdown_to_html }}</td>
	          </tr>
	          <tr>
	            <td class="mineral__category">Strunz Classification</td>
	            <td>{{ mineral.strunz_classification|title }}</td>
	          </tr>
	          <tr>
	            <td class="mineral__category">Unit Cell</td>
	            <td>{{ mineral.unit_cell|title }}</td>
	          </tr>
	          <tr>
	            <td class="mineral__category">Color</td>
	            <td>{{ mineral.color|title }}</td>
	          </tr>
	          <tr>
	            <td class="mineral__category">Crystal Habit</td>
	            <td>{{ mineral.crystal_habit|title }}</td>
	          </tr>
	          <tr>
	            <td class="mineral__category">Mohs Scale Hardness</td>
	            <td>{{ mineral.mohs_scale_hardness|title }}</td>
	          </tr>
	        </table>
	      </div>
	    </div>
	{% endblock %}

Motivation

The motivation for this project was to be able to load non-normalized .json data into a SQLite3 database enabled website built upon the Django framework to fully understand the coding skills needed to be a full stack Python web developer.

Installation

To install the project download all files to a location of your choosing on your computer, log into the terminal (on a MAC) and instantiate the program from the directory where you stored the files as follows:

	1) Unzip the images folder in the static directory
	2) Ensure Django is installed: pip3 install django
	3) Start new Django Project: django-admin startproject minerals_catalogue
	4) Start new Django App in the project directory: python3 manage.py startapp minerals
	5) Load minerals.json data into Django model: python3 -i dataloader.py
	    a) If database is full:
	        1) delete table (in SQLLite you cannot truncate): drop table minerals_mineral 
	        2) false migration: python3 manage.py migrate --fake minerals zero
	        3) migrate models: python3 manage.py migrate
	        4: Run data script python3 -i dataloader.py
	    b) If database is empty simply run the command in step 5

	6) Migrate models.py to minerals project: python3 manage.py migrate
	7) Finalize migrations to minerals project: python3 manage.py makemigrations
	8) Run local environment on port 8000: python3 manage.py runserver 0.0.0.0:8000


Tests

Two tests are built into the project to test both the index and detail data views.

These tests can be run by executing the following command from the terminal.

	python3 -i manage.py tests

Contributors

This project was inspired by the teachers at teamtreehouse.com and was developed by Taylor.

License

Opensource for your enjoyment!