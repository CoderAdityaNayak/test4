from django import forms
class inputform(forms.Form):
    BIO_GEND=[  #biological gender of patients
        ('M','Male'),
        ('F','Female'),
    ]
    input0=forms.CharField(label="Enter the Patient Name", max_length=25, required=True)
    input1=forms.FloatField(label="Enter your Height(in cm)",min_value=10,max_value=100000)
    input2=forms.FloatField(label="Enter your Weight(in kg)",min_value=1,max_value=350)
    input3=forms.FloatField(label="Enter your IVSd value(cm)",required=True)
    input4=forms.FloatField(label="Enter your LVIDd value(cm)", required=True)
    input5=forms.FloatField(label="Enter your PWTd value(cm)", required=True)
    input6=forms.ChoiceField(label=" Gender",choices=BIO_GEND,widget=forms.Select,required=True)
    