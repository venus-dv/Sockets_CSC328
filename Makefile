#	Author:	    Venus Velazquez
#	Major:      CS
#	Due Date:   Oct. 31 2023
#	Course:	    CSC328 020
#	Assignment: Socket programming
#	Filename:   Makefile
#	Purpose:    Creates executable for project5 and cleans up artifacts

# interpreter
PYTHON = python
# output file name
OUTPUT_FILE = client
# default target
all: client

client: project5.py
	$(PYTHON) project5.py
	chmod u+x client

.PHONY: clean submit
clean:
	rm -rf __pycache__
	rm -f client
submit:
	~schwesin/bin/submit csc328 project5
