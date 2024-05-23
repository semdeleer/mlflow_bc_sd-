terraform {
  required_providers {
    # We recommend pinning to the specific version of the Docker Provider you're using
    # since new versions are released frequently
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.23.1"
    }
  }
}
# Configure the docker provider
provider "docker" {
}
# Create a docker image resource
resource "docker_image" "my_mlflow2" {
  name = "my_mlflow2"
  build {
    path = "."
    tag  = ["my_mlflow2:develop"]
    build_arg = {
      name : "my_mlflow2"
    }
    label = {
      author : "vbo"
    }
  }
}
# Create a docker container resource
resource "docker_container" "my_mlflow2" {
  name    = "my_mlflow2"
  image   = docker_image.my_mlflow2.image_id
  ports {
    external = 5000
    internal = 5000
  }
}
