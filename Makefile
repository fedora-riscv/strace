# Makefile for source rpm: strace
# $Id: Makefile,v 1.2 2004/10/20 03:07:40 roland Exp $
NAME := strace
SPECFILE = $(firstword $(wildcard *.spec))

define find-makefile-common
for d in common ../common ../../common ; do if [ -f $$d/Makefile.common ] ; then if [ -f $$d/CVS/Root -a -w $$/Makefile.common ] ; then cd $$d ; cvs -Q update ; fi ; echo "$$d/Makefile.common" ; break ; fi ; done
endef

MAKEFILE_COMMON := $(shell $(find-makefile-common))

ifeq ($(MAKEFILE_COMMON),)
# attempt a checkout
define checkout-makefile-common
test -f CVS/Root && { cvs -Q -d $$(cat CVS/Root) checkout common && echo "common/Makefile.common" ; } || { echo "ERROR: I can't figure out how to checkout the 'common' module." ; exit -1 ; } >&2
endef

MAKEFILE_COMMON := $(shell $(checkout-makefile-common))
endif

include $(MAKEFILE_COMMON)

ifdef FILES
import: $(FILES)
	md5sum $^ > sources
	(read m f; \
	 tar xOjf $$f '*/$(SPECFILE)' > $(SPECFILE); \
	 echo $$f > .cvsignore; \
	 $(upload-file)) < sources
endif
