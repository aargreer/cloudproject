FROM python:3.8

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && apt-get update -y && apt-get install google-cloud-sdk -y

RUN

ENV VIRTUAL_ENV /env
ENV PATHpip3 install --upgrade virtualenv && \
            virtualenv /env -p python3 /env/bin:$PATH

ADD main.py /

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt



CMD ["python", "./main.py" ]
