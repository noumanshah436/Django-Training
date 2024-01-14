from django import forms

COUNTRY_CHOICES = (
    ("1", "Philippines"),
    ("2", "Japan"),
    ("3", "Korea"),
    ("4", "Singapore"),
    ("5", "USA"),
)
CHOICES = [('male', 'Male'),
           ('female', 'Female')]


class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter first name", max_length=50)
    lastname = forms.CharField(label="Enter last name", max_length=100)
    country = forms.ChoiceField(choices=COUNTRY_CHOICES)
    date = forms.DateField()
    age = forms.DecimalField()
    email = forms.EmailField()
    photo = forms.FileField()
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    accept = forms.BooleanField(label="Accept privacy and terms")

    def __str__(self):
        return self.firstname


"""

gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

will get the html as:

*******************


<p>

<label for="id_gender_0">Gender:</label> 
  
<ul id="id_gender">
    
    <li>  
        <label for="id_gender_0">  <input type="radio" name="gender" value="male" required id="id_gender_0">
        Male
        </label>
    </li>

    <li>
        <label for="id_gender_1">
        <input type="radio" name="gender" value="female" required id="id_gender_1">
        Female
        </label>
    </li>

</ul>

</p>

"""
