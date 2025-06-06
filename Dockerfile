FROM python:3.11

RUN mkdir /pdf && chmod 777 /pdf

WORKDIR /ILovePDF

# Copy requirements.txt files
COPY ILovePDF/requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ILovePDF/libgenesis/requirements.txt ./libgenesis_requirements.txt
RUN pip install -r libgenesis_requirements.txt

# Install system dependencies in one layer
RUN apt-get update && apt-get install -y \
    ocrmypdf \
    wkhtmltopdf \
    tree \
 && rm -rf /var/lib/apt/lists/*

# Copy the ILovePDF folder contents into /ILovePDF
COPY ILovePDF/ .

# Optional: show the directory tree structure
RUN tree

# Copy and use run.sh as the entrypoint
COPY run.sh /ILovePDF/run.sh
RUN chmod +x /ILovePDF/run.sh

CMD ["bash", "run.sh"]
