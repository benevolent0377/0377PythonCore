# PyCaliCore

#### This is a repository to host all of my core files used in all my python programs.


To use these files in your own project, or to install these files in one of my projects, download install.py and run it.

It requires that you have a directory called source, but you can always move the files around.

---

## Using the Updaters

In the update directory, there are some updaters, one for project specific libraries, and one for the core files.

Grab whichever you need, place them in the folders source/update inside the root directory of the project, and import them from the parent directory by typing:

      from source.update import Ucore, Ulib

And call their updaters by typing (where they are imported):

      Ucore.get()
      Ulib.get("projectname")

The Ulib.get() function will ONLY download libraries from MY projects, and you have to specify, without spaces, the name of the repository in order for it to work.

For example, if I wanted to update the libraries for Wanderer, my file would look like this:

      from source.update import Ulib as lib

      lib.get("wanderer")

---

That's it.

Create an issue if there are any bugs and don't forget to import the modules in requirements.txt.

There will be a Pypi package exported soon once the updaters have been finished and the core files are reletively complete.
