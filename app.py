from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetAddForm, PetEditForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secretsecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """Show pets index"""
    pets = Pet.query.all()
    return render_template('pets_index.html', pets=pets)

@app.route('/pets/add', methods=['GET', 'POST'])
def new_pet_form():
    """Show/handle new pet form"""
    form = PetAddForm()

    if form.validate_on_submit():
        ##dictionary comprehension and kwargs spread for dynamic values excluding csrf token
        data = {k:v for k, v in form.data.items() if k != 'csrf_token'}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash('Pet Successfully Added', 'bg-success text-white p-2')
        return redirect('/')
    
    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/pets/<int:pet_id>')
def show_pet_details(pet_id):
    """Show pet details page"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_details.html', pet=pet)

@app.route('/pets/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_pet_form(pet_id):
    """Show/handle pet edit form"""
    pet = Pet.query.get_or_404(pet_id)
    form = PetEditForm(obj=pet)

    if form.validate_on_submit():
        pet.img_url = form.img_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash('Pet Successfully Updated', 'bg-success text-white p-2')
        return redirect(f'/pets/{pet_id}')
    
    else:
        return render_template('edit_pet_form.html', form=form)