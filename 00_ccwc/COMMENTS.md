
Build your own Unix wc tool. This coding challenge ended up being a lot more complicated than I expected. This is how I tackled it and what I learned.

Assuming you are already familiar with `wc` tool. If not, please refer to [the coding challenge - Write Your Own wc Tool](https://codingchallenges.fyi/challenges/challenge-wc/)  page to get an idea of the task.

## Let's break it down
The challenge itself only described the end result. What the program should do, but not how.
I broke it down into the following steps:

#### 1. Parse arguments from the command line. 
At the beginning, I used `sys.args`, but soon found it insufficient for the task, thus choosed to use `argparser` to properly handle cli arguments.

#### 2. If a filename is passed, process it with the filename.
To do so, first, you need to open the file. Proper error handling is needed.
Second, count the file based on the flag passed.

#### 3. If no filename is passed, use system standard input to proceed.
To read from system standard input, you could either use `sys.stdin` or `input()`. I ended up using `sys.stdin` which returns a `file` object that is similiar to the result of `open()` method. 
Python documentation states these two as the `same`, it was not the case in my code. The result of `sys.stdin` evokes error when it tries to call `stream.seek()`. `seek()` is not avaliable for `sys.stdin`'s  file object.
It would be ideal to parse the file from standard input into the same kind, and use the same process function. I did not manage to get it work, and had to write a seperate process function to handle this situation.

#### 4. Implement count bytes, characters, words, and lines function.
I ran into great difficulty in making the character count work. 

#### 5. Don't forget to add tests.
To test the code, you need to run cli commands in Python. `subprocess` module is used. Great care needs to be taken to make sure the processes are closed afterwards.


## How does parsearg handle file input from the commandline?

`file` argument can be configured in multiple ways. 
- `nargs='?'`
 `parser.add_argument('file',nargs='?',type=argparse.FileType('r'))`
> One of the more common uses of nargs='?' is to allow optional input and output files:
When `file` argument is not provided, the value is `None`.
- `nargs='*'`

However, if `nargs` is set to `*`, in case of absent, `file` is `[]`. This is because,
> '*'. All command-line arguments present are gathered into a list.

## How to open and read files in Python?
Python uses `open()` API to open a file, it expects `str`, `bytes` or `os.PathLike` object. It returns a *file handle* object, as shown below:
`<_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>`

If it fails to open the file, it throws a `FileNotFoundError` as shown below:
`FileNotFoundError: [Errno 2] No such file or directory: 'tet.txt'`

Use a `try` and `except` block to handle errors.

Once a file is opened, it is treated as a stream which consists a sequence of lines, just like in Python, string can be thought of as a sequence of characters. To break files into lines, Python uses `\n` to represent the end of the line, and this counts as 1 character.

The stream has access to methods such as `.read()`, `.readline()`, `.seek()`, etc.

## Count bytes

The most straightforward way would be to open the file as bytes stream with the `rb` flag. Then you could simply call `len(stream.read())` to get the bytes.

However, to avoid duplicated code, I perfer to only open the file at one place. The file is opened as text stream by using the `r` flag. To count bytes, you can use `.seek()` method to move the cursor from the start to the end of the file, and return the count by calling `.tell()`.

After completing the count, the cursor needs to be reset to the beginning of the file.
 
## Count lines

To count lines, you could use a for loop to read through the lines and count them.
```
count=0
for line in stream:
    count+=1
```
Or if you know the file size is reasonable, can use the `len(stream)` method as stream is already a list of lines.

## Count words
Words are seperated by empty space. To count word, you could simply split each line with `.split()` method into a list of words. Python list comprehension comes handy.

`sum([len(s.split()) for s in stream])`

### Count characters
The `read()` method reads the entire content into a single string, including new line characters. Simple return the `len(stream.read())` works if there isn't problem with multiple locales. 

```
python ccwc.py -m test.txt
[332297]
```
```
wc -m test.txt          
  339486 test.txt
```
The problem lies in `locale`. This is still work in progress.

## No flag, count all

If no flag is passed, the program treats it as the default option and returns lines, words and bytes count.

At the beginning, my program falsely returned `0` for `lines_count` and `words_count`.

Later I discovered that, `.seek()` put the `stream` in a certain position and remains there. After each operation, he stream needs to be reset to the beginning: position `0`.

## Tests

I used Python's native `unitest` library. 

The crux is to run piping commands. For example, this command did not work in test:

`wc_arg=['cat','test.txt','|','wc','-c']`

Passing this to `subprocess` results in `file not found` error threw by `cat`.

Potentially, this can be achieved by running multiple processes and pass the previous process's output as the input of the next process.

I am confused about the different ways to run process in Python, namely:

`subprocess.run()` vs `subprocess.Popen()` vs `subprocess.communicate()`.

Python gave me warnings about having processes running.

## Unresolved questions
1. Character count and configure locale in Python
2. Ran piping command in with subprocess in Python
3. Further re-factor to reduce duplication.


## Resources

Amazing free, online, interactive Python course [Python for Everybody](https://runestone.academy/ns/books/published/py4e-int/index.html)

