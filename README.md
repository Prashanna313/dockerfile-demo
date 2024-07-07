## Dockerfile-Demo
- This repo is mainly for demonstrating my docker skills
- I've added a sample application with Go, Python and NodeJs
- Also added the relevant `Dockerfile`
### Dockerfile Best Practices
- Use `.dockerignore` to minimize the files passed into build
- Try to keep the image light by following below
    - Store only required app files and remove build files using MultiStage builds
    - In `Dockerfile` have the frequently changed steps at the end. For example, installing dependicies can be kept at end, so other layers will not be rebuilt again
- Ensure using a secure base image and perform security scanning with tools like `trivy`
- Chain run commands for using build cache