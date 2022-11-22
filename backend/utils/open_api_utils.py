from fastapi import FastAPI
from fastapi.routing import APIRoute


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    route_names = set()
    for route in app.routes:
        if isinstance(route, APIRoute):
            if route.name in route_names:
                raise Exception("Function names must be unique")
            route.operation_id = route.name
            route_names.add(route.name)