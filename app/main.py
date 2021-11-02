import json
from fastapi import FastAPI
from graphene.types.field import Field
from graphene.types.objecttype import ObjectType
from graphene.types.scalars import String, Int
from graphene.types.schema import Schema
from graphene.types.structures import List
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp

from app.controllers import routers

app = FastAPI()
app.include_router(routers.router)


class DescriptionType(ObjectType):
    text = String(required=True)
    type = String()


class InternshipType(ObjectType):
    id = Int(required=True)
    title = String(required=True)
    description = Field(DescriptionType)
    publish_date = String()


class Query(ObjectType):
    internship_list = None
    get_internship = Field(List(InternshipType), id=List(Int))

    async def resolve_get_internship(self, info, id=None):
        with open("app/internships.json") as internships:
            internship_list = json.load(internships)
        if (id):
            res = []
            for internship in internship_list:
                if internship['id'] in id:
                    res.append(internship)
            return res
        return internship_list


app.add_route("/", GraphQLApp(
  schema=Schema(query=Query),
  executor_class=AsyncioExecutor)
)
