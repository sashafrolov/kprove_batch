FROM runtimeverificationinc/kframework-k:ubuntu-focal-1af793e
MAINTAINER "sasha f sasha07974@gmail.com"
RUN apt-get update && \
    apt-get install -y git

RUN cd /home && \
    git clone "https://github.com/pdaian/mev.git"

RUN cd /home && \
    git clone "https://github.com/sashafrolov/kprove_batch.git"

WORKDIR /home/mev/
