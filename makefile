############################################################################
# VARIABLES                                                                #
############################################################################

NAME?=Crystal_splice
BUILD?=1
VERSION?=1.3.0

############################################################################
# DISTRIBUTION                                                             #
############################################################################

all: release debug 

ARCHIVE:=/var/tmp/${NAME}.tar.gz
EXCLUDE:=--exclude-vcs --exclude-backups --exclude '*~' \
         --exclude './versions' --exclude './test_data' --exclude './backup' --exclude './non_combined'
archive: clean
	tar -chzf ${ARCHIVE} ${EXCLUDE} . --transform=s%^\\.%${NAME}-${VERSION}%

dist: archive
	rpmlint project.spec
	rpmbuild --define "buildnumber ${BUILD}" --rmspec --rmsource -ta ${ARCHIVE}
	
check:

############################################################################
# BUILD                                                                    #
############################################################################

clean:
	-rm -f ${ARCHIVE}
	-find . -name "*~" -delete 
	-find . -name "*.pyc" -delete 

release:

debug:

prebuild:

build: 
	# check code has no errors
	python -m py_compile scr/*.py 


postbuild:

