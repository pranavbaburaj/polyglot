# Polyglot

<hr>

## `Polyglot`

The `polyglot.core.Polyglot` is the main class of polyglot the polyglot module.

```python
from polyglot.core import Polyglot
```

Initialize a polyglot instance

```python
polyglot = Polyglot("path/to/directory", ignore=["language.yml"])
```

Polyglot takes in to parameters, the path to the directory and the ingore file

- directory_name(**required**) - `string` The path of the directory
- ignore - The ignore filename
  <br>
  The ignore file should have a `.polyglot` file extension and has a syntax similar to a `.gitignore` file.
    -  `.<extension>` for file extensions
    -  `<folder>/` for folders
    -  `<filename>` for files
```rb
# for a specific file extension
.json

# for a specific folder
dist/

# for a specific file
dub.sdl
LICENSE

# for specific folders in the directory
~.tox
```  


  and use the file with the polyglot object
  ```python
  poly = Polyglot(".", "example.polyglot")
  ```

Getting information from the polyglot object

```python
polyglot.show(language_detection_file="language.yml", display=True)
```

The `show` method takes in two parameters, the language detection file as well as the disply option

- language_detection_file(**optional**) - `string` The yaml file containing information about all the languages. By default, the `language_detection_file` is set to `None`. and the file is downloaded from the internet.
- display(**optional**) - `bool` Whether to output the table on the console or not. The show method returns a dict containing information about the files.

## `Arguments`

The `polyglot.arguments.Arguments` helps you parse a set of arguments and execute functions accordingly.

```python
from polyglot.arugments import Arguments
```

passing in arguments

```python
args = Arguments(arguments=[], return_value=False)
args.parse()
```

- arguments(**optional**) - `list` The set of arguments. By default, the arguments in set to `sys.argv[1:]`.
- return_value(**optional**) - `bool` Whether to return anything or not
