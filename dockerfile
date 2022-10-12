FROM python:3
RUN git clone https://github.com/AugustoKark/SudokuAK.git
WORKDIR /SudokuAK
RUN pip install -r requirements.txt
CMD ["python3","-m", "unittest"]