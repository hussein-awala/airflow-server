from invoke import Collection, task

from .utils import docker_compose_command


@task
def up_airflow(ctx, version=1, build=False, extra_services=None):
    services = [
        "airflow-metadata",
        "airflow-scheduler",
        "airflow-webserver",
        "airflow-init",
    ]
    if extra_services is not None:
        services += extra_services
    docker_compose_command(
        ctx, f"up -d {'--build' if build else ''} {' '.join(services)}", version=version
    )


@task
def down(ctx, volumes=False, version=1):
    docker_compose_command(
        ctx, f"down {'--volumes' if volumes else ''}", version=version
    )


@task
def stop(ctx, version=1):
    docker_compose_command(ctx, f"stop", version=version)


@task
def command(ctx, cmd, version=1):
    docker_compose_command(ctx, cmd, version=version)


docker_compose_collection = Collection()
docker_compose_collection.add_task(up_airflow, name="up_airflow")
docker_compose_collection.add_task(down, name="down")
docker_compose_collection.add_task(stop, name="stop")
docker_compose_collection.add_task(command, name="cmd")
