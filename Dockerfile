FROM python
RUN pip install flask
RUN pip install mysql-connector-python
COPY app1.py
CMD ["python","app1.py"]
CMD tail -f /dev/null