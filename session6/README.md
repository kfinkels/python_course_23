# **Getting started**

create virtualenv: `virtualenv -p python3 venv`

activate the virtualenv: `source venv/bin/activate`

install requirements: <br>
`pip3 install -r requirements.txt` <br>
`pip3 install -r dev.txt`

run application: `python3 app_swagger.py`

run tests: `pytest`

# **Exercises**

* Fixture (work on test_swagger_with_class.py):
> * Add a class fixture that will replace the setup function. 
> * This fixture should be automatically used
> * HINT: fixture should get a request and put the url&headers on it  

* Parameterize: 
> * Write a method that compares 2 dictionaries and returns a dictionary with all the matching items (key and value) 
> * Add the the following tests:
>> * There are no matched items
>> * All items match
>> * One item match
>> * dict1\dict2 is None
>> * dict1\dict2 is not a dict

* Mock: 
> * Write a unittest for swagger/pet_store.py::get_pet(pet_id)
> * Validate that the function returns a tuple `(<pet_dict>, 200)`
> * Validate that the result pet dict values are as expected
> * HINT: You should patch get_pet_by_id

