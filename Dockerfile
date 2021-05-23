FROM runtimeverificationinc/kframework-k:ubuntu-focal-1af793e
MAINTAINER "sasha f sasha07974@gmail.com"
RUN apt-get update && \
    apt-get install -y git

RUN apt-get install -y python3-pip

RUN mkdir /home/sasha_mev && \
    cd /home/sasha_mev && \
    git clone "https://github.com/sashafrolov/mev.git"

RUN cd /home && \ 
    git clone "https://github.com/sashafrolov/kprove_batch.git"

RUN python3 -m pip install requests

RUN cd /home/sasha_mev/mev && \
    kompile mev.k --backend haskell

RUN cd /home/ && \ 
    git clone "https://github.com/pdaian/mev.git"

RUN cd /home/mev && \
    kompile mev.k --backend llvm

WORKDIR /home/mev/
