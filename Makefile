# Makefile for source rpm: strace
# $Id$
NAME := strace
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common

ifdef FILES
import: $(FILES)
	md5sum $^ > sources
	(read m f; \
	 tar xOjf $$f '*/$(SPECFILE)' > $(SPECFILE); \
	 echo $$f > .cvsignore; \
	 $(upload-file)) < sources
endif
