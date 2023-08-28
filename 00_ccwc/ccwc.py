import sys
import os

def main():
    if(len(sys.argv)<2 or len(sys.argv)>3):
        print("Invalid input.")

    else:
        count=0
        
        # if no option is provided(arg len=2)
        if(len(sys.argv)==2):
            print('default flag-no flag')

        # if option is provided correctly, arg len=3
        else:
            file_path=sys.argv[2]
            if sys.argv[1] in ['-l','-c','-m','-w']:
                if sys.argv[1]=='-c':
                    count=byte_count(file_path)
                print(f' ',count,file_path)
            else:
                print('invalid flag')
    
    
        

def byte_count(file_path):
    return os.path.getsize(file_path)

def line_count(string):
    return len(string.readlines())

def word_count(string):
    return len(string.read().split())

def character_count(byte):
    return len(byte)








if __name__=="__main__":
    main()