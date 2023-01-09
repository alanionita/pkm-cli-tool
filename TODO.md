# App Features

- [ ] clean up all the redundant code in `_examples` and in `commands` 
- [ ] create daily notes 
	- AS a USER I can:
		- [x] create a daily note
		- [x] only create one daily note per day
		- [x] create a note with frontmatter
		- [x] add better error handling 
			- only render 'Note exists' for the one scenario
			- capture and log other errors to the console 
		- [ ] add traits to the frontmatter specific to daily notes
- [ ] open notes
	- AS a user I can my editor of choice: vscodium and vim
	- AS a user I can open a note in my editor of choice
		THEN when that note is opened the updated at timestamp is modified to match the last action timestamp
- [ ] create notes under a namespace
	- AS a user I can create a note namespace
		- projects
		- areas
		- resources
		- archive
	- AS a user I can create a note under a name space
		THEN namespaces are suggested to me
			AND the namespaces can be nested `resources.pythong...`
		THEN I can select my relevant namespace

# TODOs

- [x] install miniconda
- [x] try out click - cli library
	- [x] make a conda environment that contains the click dependencies 
	- [x] try out the 'Getting Started' example here - https://click.palletsprojects.com/en/8.1.x/
	- [x] complete the `Complex Guide` tutorial - https://click.palletsprojects.com/en/8.1.x/complex/#complex-guide
		- guide was good but a bit too much technical waffle to make it interesting 
		- the examples seemed to miss bits of code too 
	- [x] finish this dev.to tutorial
		- https://dev.to/drcloudycoder/develop-python-cli-with-subcommands-using-click-4892

Future:
- [ ] try out other Python cli libraries 
	- from this article https://lewoudar.medium.com/click-a-beautiful-python-library-to-write-cli-applications-9c8154847066 
	- also try pyCLI https://pythonhosted.org/pyCLI/
	- and try http://docopt.org/