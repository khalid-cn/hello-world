FROM mizzlr/gitpod-workspace-supercharged as supercharged
WORKDIR ./

FROM gitpod/workspace-full
COPY --from=supercharged ./ ./

# Install custom tools, runtimes, etc.
# For example "bastet", a command-line tetris clone:
# RUN brew install bastet
#
# More information: https://www.gitpod.io/docs/config-docker/
