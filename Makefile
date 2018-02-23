
ARCHIVE = sugar
all: clean
	zip -r $(ARCHIVE) * --exclude Makefile

clean:
	# problems under MacOS xargs...
	#find . -name \*.pyc -o -iname \*.pyo | xargs -r rm
	find . \( -name \*.pyc -o -iname \*.pyo \) -delete
	rm -f $(ARCHIVE).zip
