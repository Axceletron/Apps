FROM python
RUN pip install flask
RUN pip install flask-mysqldb
RUN pip install mysql-connector-python
ENV USER=root
ENV HOST=10.175.172.29
ENV PASSWORD=root123
ENV DB_NAME=my_db
COPY app.py app.py
RUN mkdir templates
COPY index.html templates/index.html
EXPOSE 8000
CMD sleep 10
CMD ["python","app.py"]