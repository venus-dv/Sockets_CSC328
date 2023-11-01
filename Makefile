#	Author:	    Venus Velazquez
#	Major:      CS
#	Due Date:   Oct. 31 2023
#	Course:	    CSC328 020
#	Assignment: Socket programming
#	Filename:   Makefile
#	Purpose:    Creates executable for project5 and cleans up artifacts

# default target
all: client

client: project5.py
	@touch client
	@echo 'python project5.py "$$@"' > ./client
	@chmod u+x client

.PHONY: clean submit
clean:
	rm -f client
submit:
	~schwesin/bin/submit csc328 project5
