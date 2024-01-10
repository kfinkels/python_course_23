# **Getting started**

Create virtual env:

`virtualenv -p python3 env`

`source env/bin/activate`

Install poetry and dependencies:

`pip install poetry`

`poetry install`

Run the server:

`uvicorn pet_store.main:app --reload`

# **FastAPi**

`https://fastapi.tiangolo.com/`
`https://www.uvicorn.org/`
`https://docs.pydantic.dev/latest/`


# **Pet Store OpenAPI**

`http://127.0.0.1:8000/docs`

# **Sqlalchemy**

`https://www.sqlalchemy.org/`


# **Tutorial Example**

`https://www.gormanalysis.com/blog/building-a-simple-crud-application-with-fastapi/`

# **Exercises**

1. Implement add pet 
2. Implement get pet by ID
3. Implement delete pet by ID
4. Implement get all pets created after DATE
5. Change animal_type to one of (enum)
6. Disallow pet from the same name and same type (hint: use exception)

