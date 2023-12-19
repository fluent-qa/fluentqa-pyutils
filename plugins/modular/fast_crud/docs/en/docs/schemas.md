The CRUDRouter is able to generate and document your routes based on the schema, a 
[pydantic model](https://pydantic-docs.helpmanual.io/usage/models/#basic-model-usage), that is passed to it.

In general, the all provided CRUDRouter's have the option to pass both a `schema` and a `create` schema to it.  If no
create schema is provided, the CRUDRouter will automatically generate one. Optionally you can also pass an `update` schema
allowing for custom update behavior.

```python
CRUDRouter(
    schema=MyPydanticModel, 
    create_schema=MyPydanticCreateModel, 
    update_schema=MyPydanticUpdateModel
)
```

!!! tip "Automatic Create and Update Schema Generation"
    Leaving the create and/or update schema argument blank when creating your CRUDRouter will result in the crud router automatically
    generating and documenting a create and/or update schema in your routes. In doing so, it automatically removes any field which
    matches the primary key in the database as this will be generated server side.

## Create Schemas
Create schemas are models which typically don't include fields that are generated by a database or other backends. An example of this 
is an `id` field in a model.

```python
from pydantic import BaseModel

class Potato(BaseModel):
    id: int
    color: str
    mass: float

class CreatePotato(BaseModel):
    color: str
    mass: float
```

## Update Schemas
Update schemas allow you to limit which fields can be updated. As an example, the update schema below will only allow you to
update the `color` field when used in the CRUDRouter.

```python
from pydantic import BaseModel

class Potato(BaseModel):
    id: int
    color: str
    mass: float

# Allowing the user to only update the color
class UpdatePotato(BaseModel):
    color: str
```