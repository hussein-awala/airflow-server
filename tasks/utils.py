from pathlib import Path


def get_project_dir(ctx) -> Path:
    return Path(ctx.run("git rev-parse --show-toplevel").stdout.strip())


def docker_compose_command(ctx, command, version=2):
    docker_compose_folder_path = get_project_dir(ctx).joinpath("docker-compose")
    compose_files = ["airflow"]
    compose_cmd = "docker compose" if version == 2 else "docker-compose"
    cmd = f"{compose_cmd} {' '.join([f'-f {docker_compose_folder_path.joinpath(file)}.yml' for file in compose_files])} {command}"
    print(cmd)
    ctx.run(cmd)
