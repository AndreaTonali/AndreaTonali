## TASK SUMMARY

### Word Frequency Finder

Knowing how often a word appears in a sentence or block of text is helpful for creating word clouds and other types of word analysis. And it’s more useful when running it against lots of text.

Create a program that reads in a file and counts the frequency of words in the file. Then construct a histogram displaying the words and the frequency, and display the histogram to the screen.

### Example Output

Given the text file words.txt with this content badger badger 

```
badger badger mushroom mushroom snake badger badger badger
```

the program would produce the following output:

```
badger:   *******
mushroom: **
snake:    *
```
## USAGE
#### DEVELOPMENT (1hr - 2hrs)

The application runs within a docker container and reads the file `./words.txt`. 

1) Parses the file to a `List[List[str]]`.
2) Calculates the frequency of the occurences of a specific word within the List. 

The result is then output into a dictionary where the key defines the actual word and the value defines the number of occurences `{"badger": 5, "mushroom": 2, "snake": 1}`. The dictionary is then displayed in the command line like below.

```bash
badger: *****
mushroom: **
snake: *
```

Within the docker container, automated tests on the `parser()` and `frequency()` functions are excuted before the build is completed, together with `flake8` and `mypy`.  

### HOW TO RUN

*Note*: Assuming Linux/MacOS environment plus Docker.

Run `./init.sh`, make sure the file is executable, example below:

```bash
chmod 755 init.sh
```

## Assumptions

- Structure/Format of the file is constant.
- Only one file at the time.
- File size is approximately constant.

## Further Considerations

This could be designed as Python daemon.
 
 - How to handle multiprocessing or threading (e.g. `pyspark`, `threading`)

### Reference:

- [PySpark](https://spark.apache.org/docs/latest/api/python/)
- [Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)
- [Threading](https://docs.python.org/3.8/library/threading.html)
