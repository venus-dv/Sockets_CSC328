#	Author:	    Venus Velazquez
#	Major:      CS
#	Due Date:   Oct. 31 2023
#	Course:	    CSC328 020
#	Assignment: Socket programming
#	Filename:   Makefile
#	Purpose:    Creates executable for project5 and cleans up artifacts

# interpreter
# PYTHON = python
# output file name
# OUTPUT_FILE = client
# default target
# all: client

PYTHON_FILE = project5.py
OUTPUT_FILE = client

client:
	pyinstaller --onefile $(PYTHON_FILE) --name $(OUTPUT_FILE)

# client:
# 	$(PYTHON) project5.py
# 	chmod u+x client

.PHONY: clean submit
clean:
	rm -rf __pycache__
	rm -f $(OUTPUT_FILE)
submit:
	~schwesin/bin/submit csc328 project5
