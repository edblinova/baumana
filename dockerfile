FROM oraclelinux:9

WORKDIR /opt/oracle
RUN yum install -y wget unzip libaio && \
    rm -rf /var/cache/yum
RUN wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip && \
    unzip instantclient-basiclite-linuxx64.zip && \
    rm -f instantclient-basiclite-linuxx64.zip && \
    cd instantclient* && \
    rm -f *jdbc* *occi* *mysql* *jar uidrvci genezi adrci && \
    echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf && \
    ldconfig

WORKDIR /app
RUN yum install -y oracle-epel-release-el9 && \
    yum install -y python3 pip gcc openldap-devel python-devel && \
    python3 -m pip install cx_Oracle setuptools pyOpenSSL && \
    rm -rf /var/cache/yum

COPY requirments.txt

RUN python3 --version
RUN pip install -r requirments.txt

COPY . .

EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]
