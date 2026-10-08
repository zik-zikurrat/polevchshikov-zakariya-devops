# Jenkins with Docker CLI and Python, so the pipeline can build and run images
FROM jenkins/jenkins:lts-jdk21

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 procps \
    && rm -rf /var/lib/apt/lists/*
# Docker CLI only; the Docker engine of the host is used through docker.sock
COPY --from=docker:cli /usr/local/bin/docker /usr/local/bin/docker

# Skip the setup wizard, configure Jenkins from casc.yaml
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false" \
    CASC_JENKINS_CONFIG=/var/jenkins_home/casc.yaml

RUN jenkins-plugin-cli --plugins \
    git workflow-aggregator pipeline-stage-view pipeline-graph-view \
    configuration-as-code job-dsl
