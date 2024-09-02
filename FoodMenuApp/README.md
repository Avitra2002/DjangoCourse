# DjangoCourse

Here are my learning points: 

### Activating Virtal env
```
source Django/bin/activate

```

### Run on local host
```
python3 FoodMenuApp/manage.py runserver

```

### Starting an App
An app is a single page in the website

```
python FoodMenuApp/manage.py startapp food
```
This command makes an app named food that makes a folder 'food' with views, models, admin and apps files.

### Apply Migration for admin, auth, contenttypes, sessions (pre-built apps/views) for the system

```
python FoodMenuApp/manage.py migrate

```
What it does is that it goes to 'setting.py' and look at the INSTALLED_APPS and make database tables for the,. So if we want to make a new database (food item) using migrate we need to add the following:

1. Add the app to Installed App in settings.py
```
'food.apps.FoodConfig',
```
2. Tell Django we have made changes to the model in the food app (food/ folder)
```
python FoodMenuApp/manage.py makemigrations food

```
3. Django will then look into the food/models.py and see the Item class and make a Item migration file in food/migrations/0001_initial.py

4. We can now make a table in sql3 using the migration file created
``` python FoodMenuApp/manage.py sqlmigrate food 0001
```

5. It creates a table called food_item (app name_class name)
6. apply final migrate
``` python FoodMenuApp/manage.py migrate
```

### Storing Data in DB (longer way)
This can be done using the python shell

1. 
```
python FoodMenuApp/manage.py shell
```
2. Use the model class we created in the food.models
```
from food.models import Item
```
3. To access all the objects/entries in the table
 ```
 Item.objects.all()


 ```

 4. To create an entry/object
 ``` a= Item(item_name= 'Pizza',item_desc='Chessy', item_price=20)

    a.save()
``` 
5. to get the id/primary key of a 
```a.id
    a.pk
```


### Creating Super User and Admin User & modify DB 
1. python FoodMenuApp/manage.py createsuperuser
2. Login into django admin in browser in /admin page
3. In food/admin.py register the models admin needs to interact with so it can be shown in the admin browser and editing can be done in the site instead of shell
```
from .models import Item
admin.site.register(Item)
```

### Using Templates in Django
1. create food/templates/food/index.html
2. In views, load the template
``` from django.template import loader
template= loader.get_template('food/index.html')
```
3. return render(request, 'food/index.html', context)

context is the list from DB
eg. context={
        'item_list': item_list,
    }













