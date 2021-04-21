FROM runtimeverificationinc/kframework-k:ubuntu-focal-1af793e
MAINTAINER "sasha f sasha07974@gmail.com"
RUN apt-get update && \
    apt-get install -y git

RUN apt-get install -y python3-pip

RUN cd /home && \
    git clone "https://github.com/sashafrolov/mev.git"

RUN cd /home && \
    git clone "https://github.com/sashafrolov/kprove_batch.git"

RUN python3 -m pip install requests

RUN cd /home/mev && \
    kompile mev.k --backend haskell

WORKDIR /home/mev/
