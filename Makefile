#	Author:	    Venus Velazquez
#	Major:      CS
#	Due Date:   TBD
#	Course:	    CSC328 020
#	Assignment: Socket programming
#	Filename:   Makefile
#	Purpose:    Creates executable for project5 and cleans up artifacts

#interpreter
PYTHON = python

all: project5

project5: 

.PHONY: clean submit
clean:
	rm -f *.o
	rm -f project5
submit:
	~schwesin/bin/submit csc328 project5
