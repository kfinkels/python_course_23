# **Getting started**

Create virtual env:

```
virtualenv -p python3 env
source env/bin/activate
```

Install poetry and dependencies:

```
pip install poetry
poetry install
```

Run the server:

`poetry run start`

Run tests: 

`pytest`

# **Exercises**

* Fixture (work on test_pet_store.py):
> * Add a class fixture that will replace the setup/teardown functions. 
> * This fixture should be automatically used

* Parameterize: 
> * Write a method that compares 2 dictionaries and returns a dictionary with all the matching items (key and value) 
> * Add the following tests:
>> * There are no matched items
>> * All items match
>> * One item match
>> * dict1\dict2 is None
>> * dict1\dict2 is not a dict

* Mock: 
> * Write a **unittest** for pet_store:main:get_pet(pet_id)
> * Validate that the function returns a tuple `(<pet_dict>, 200)`
> * Validate that the result pet dict values are as expected
> * HINT: You should patch get_pet_by_id
