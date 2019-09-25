import adhesive

from adhesive import scm
from adhesive.workspace import docker


@adhesive.task('Build docker image')
def build_docker_image(context):
    scm.checkout(context.workspace)
    docker.build(context.workspace,
                 "bmst/pandoc")


adhesive.build()
