# Build `x86_64` images on `arm64` architecture

## Enable experimental features

`buildx` is experimental and must be specifically enabled:

```bash
# Before
cat ~/.docker/config.json
{
  "stackOrchestrator" : "swarm",
  "experimental" : "disabled",
  "auths" : {

  },
  "credsStore" : "desktop"
}

# Make relevant changes
vim ~/.docker/config.json

# After
cat ~/.docker/config.json
{
  "stackOrchestrator" : "swarm",
  "experimental" : "enabled",
  "auths" : {

  },
  "credsStore" : "desktop"
}
```

Restart Docker and check if the feature was enabled properly:

```bash
docker buildx version
github.com/docker/buildx v0.5.1-docker ...
```

## Build an image - `arm64`

```bash
docker build --tag smallimg .
docker run --rm smallimg
```

## Build an image - `x86_64`

The desired target should be shown in the output of `docker buildx ls`.

```bash
# Create builder
docker buildx create --use --name m1builder

# Build image
docker buildx build --platform linux/amd64 --tag smallimg-x86 .
```

You need to push the image somewhere to be able to use it:
```bash
docker buildx build --platform linux/amd64 --tag bogeholm/buildxtest --push .
```

### Test from `x86_64` machine

```bash
uname -p
x86_64

docker run bogeholm/buildxtest
Unable to find image 'bogeholm/buildxtest:latest' locally
latest: Pulling from bogeholm/buildxtest
...
NumPy version: 1.20.2
Pandas version: 1.2.4
SciPy version: 1.6.2
```

## Resources

- [docs.docker.com/buildx/working-with-buildx](https://docs.docker.com/buildx/working-with-buildx/)
- [github.com/docker/buildx](https://github.com/docker/buildx/)
- [How to Actually Deploy Docker Images Built on M1 Macs With Apple Silicon](https://betterprogramming.pub/how-to-actually-deploy-docker-images-built-on-a-m1-macs-with-apple-silicon-a35e39318e97)
- [How to build x86 (and others!) Docker images on an M1 Mac](https://blog.jaimyn.dev/how-to-build-multi-architecture-docker-images-on-an-m1-mac/)
