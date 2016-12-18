FROM andrewosh/binder-base

MAINTAINER Christian Ferko <cferko@alum.mit.edu>

USER root

# Add dependency
RUN apt-get update
RUN apt-get install libsndfile1-dev

USER main

# Install requirements for Python 2
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt