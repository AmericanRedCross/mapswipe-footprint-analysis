###############
# BUILD IMAGE #
###############
FROM python:3.9-slim-buster AS build

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential=12.6 \
        libpq-dev \
        unixodbc-dev

RUN apt-get install -y gpg-agent
RUN apt-get install -y software-properties-common 
RUN apt-get install -y ca-certificates wget

RUN add-apt-repository ppa:ubuntugis/ppa -y &&  apt-get update
RUN apt-get install -y gdal-bin libgdal-dev

ARG CPLUS_INCLUDE_PATH=/usr/include/gdal
ARG C_INCLUDE_PATH=/usr/include/gdal
RUN pip install GDAL

RUN apt-get install -y binutils libproj-dev gdal-bin
ENV GDAL_DATA=/usr/share/gdal

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# add and install requirements
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#################
# RUNTIME IMAGE #
#################
FROM python:3.9-slim-buster AS runtime

# setup user and group ids
ARG USER_ID=1000
ENV USER_ID $USER_ID
ARG GROUP_ID=1000
ENV GROUP_ID $GROUP_ID

# add non-root user and give permissions to workdir
RUN groupadd --gid $GROUP_ID user && \
          adduser user --ingroup user --gecos '' --disabled-password --uid $USER_ID && \
          mkdir -p /usr/src/app && \
          chown -R user:user /usr/src/app

# copy from build image
COPY --chown=user:user --from=build /opt/venv /opt/venv

# set working directory
WORKDIR /usr/src/app

# switch to non-root user
USER user

# disables lag in stdout/stderr output
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# Path
ENV PATH="/opt/venv/bin:$PATH"

# Run streamlit
CMD streamlit run project/app.py