import sys
import argparse
from os import SEEK_END

# It parses args from the command line
def parse_args():

    parser=argparse.ArgumentParser(description='A copy of wc. Count words, bytes, lines and characters in a file.')
    
    parser.add_argument('-c',action='store_true',help='count the bytes')
    parser.add_argument('-l',action='store_true',help='count the lines')
    parser.add_argument('-w',action='store_true',help='count the words')
    parser.add_argument('-m',action='store_true',help='count the characters')
    parser.add_argument('file',nargs='?')

    return parser.parse_args()
    

def main():
    # It takes args from command line, process it and call run
    args=parse_args()

    print(run(args))



# If no files, parse from standard input 
# If files, parse with ccwc tool
# Handle erros while open files 
def run(args):

    count=[]
    
    # if file is not present, treat it as standard input
    if not args.file:
        file=""
        
        user_input=sys.stdin

        count=process_user_input(user_input,args)
            
    else:
        file=args.file
        try:
            with open(file,"r", encoding="utf-8") as stream:
                count= process_file(stream, args)
            
        except FileNotFoundError:
            print(f"Error: {file} not found.")
    
    return format_output(count,file)

def process_user_input(user_input, args):
    result=[]
    lines=0
    words=0
    bytes=0
    characters=0

    for line in user_input:
        lines+=1
        words+=len(line.split())
        bytes+=len(line.encode())
        characters+=len(line)

    if args.l:
        result.append(lines)
    if args.w:
        result.append(words)
    if args.c:
        result.append(bytes)
    if args.m:
        result.append(characters)
    if not any([args.l,args.w,args.c,args.m]):
        result.append(lines)
        result.append(words)
        result.append(bytes)

    return result
    

def process_file(stream, args):
    result=[]
        
    if args.c:
        # Count bytes
        result.append(bytes_count(stream))
    
    if args.l:
        # Count lines
        result.append(lines_count(stream))

    if args.w:
        # Count words
        result.append(words_count(stream))

    if args.m:
        # Count characters
        result.append(characters_count(stream))

    if not any([args.c,args.l,args.w,args.m]):
        result.append(lines_count(stream))
        result.append(words_count(stream))
        result.append(bytes_count(stream))

    return result


def bytes_count(stream):
    stream.seek(0,SEEK_END)
    count=stream.tell()
    stream.seek(0)
    return count

def lines_count(stream):
    count=len(stream.readlines())
    stream.seek(0)
    return count

def words_count(stream):
    return sum([len(s.split()) for s in stream])

def characters_count(stream):
    # TODO not returning the correct count. Fix later.
    return len(stream.read())

# Format it
def format_output(count,file_path):
    output=[str(c) for c in count]
    output.append(file_path)
    return " ".join(output)




if __name__=="__main__":
    main()