from invoke import Collection

from .docker_compose import docker_compose_collection

ns = Collection()
ns.add_collection(docker_compose_collection, "compose")
