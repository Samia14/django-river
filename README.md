# django-river
An extended version of django-river lib that can create multiple work flows according to company id.
# Steps to produce these
- python manage.py makemigrations
- pythin manage.py migrate
- python manage.py createsuperuser
- python manage.y runserver
Open admin page and create
- Object of Company
- Objecs of States (eg,initial_state,final_state,etc)
- Object of NewModel(extended workflow model) with 
  - contentType id of model whom you want to maintain states
  - initial state
  - field name
- Object of TransitionMeta with 
  - workflow
  - states
- Objects of TransitionMetaApproval with
   - transition_meta_approval id
- Object of MyModel with
  - company_id
  - state
 
Basic comands to test these functionality is:
- python manahe.py shell
- from polls.models import MyModel
- from river.models import State
- from django.contrib.auth.models import User
- my_model = MyModel.objects.get(id=1)
- my_model.river.my_state_field.approve(as_user=User.objects.get(id=1),next_state=State.objects.get(label='b')) here considering b is the next state to transition

