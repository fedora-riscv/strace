# Makefile for source rpm: strace
# $Id: Makefile,v 1.1 2004/08/31 17:57:52 cvsdist Exp $
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
