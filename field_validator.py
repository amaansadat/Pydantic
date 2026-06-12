from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

    name: str
    age: Annotated[int,Field(gt=0,lt=100)]
    weight: Annotated[float,Field(gt=0,strict=True)]
    #To Suppress the type coercision/data_conversion behaviour of pydantic,using strict parameter=True.
    email: EmailStr
    Linkedin: Optional[AnyUrl]
    Married: Annotated[bool,Field(default=False)]
    Allergies: Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    contact_details: Dict[str,AnyUrl]

    @field_validator('name')
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        domain = value.split('@')[-1]

        if domain not in valid_domains:
            raise ValueError('Not a valid domain')

        return value
    
    @field_validator('name')
    @classmethod
    def transform_name_to_uppercase(cls, value):
        return value.upper()
    
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')


def display_patient_details(patient : Patient):

   print(patient.name)
   print(patient.age)
   print(patient.weight)
   print(patient.email)
   print(patient.Linkedin)
   print(patient.Married)
   print(patient.Allergies)
   print(patient.contact_details)
   
patient_info={'name': 'Amaan', 'age':20, 'weight': 65.0, 'email': 'amaansadat707@gmail.com', 'Linkedin': 'https://www.linkedin.com/in/amaansadat707/', 'Married': False, 'Allergies': ['Dust','Pollen'], 'contact_details': {'home': 'https://www.home.com', 'work': 'https://www.work.com'}}

patient1 = Patient(**patient_info)

display_patient_details(patient1)

