# Makefile for source rpm: strace
# $Id$
NAME := strace
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
