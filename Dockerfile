FROM python

WORKDIR /app 

COPY API_SERVER.py      \ 
    MY_modules.py       \
    mysql_DB.py         \
    requirements.txt    \
    clean_cache.sh      \
    /app/

RUN pip install -r /app/requirements.txt

EXPOSE 5004

CMD python API_SERVER.py