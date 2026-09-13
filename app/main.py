import sys
import shlex
import subprocess
from app.packages import locate_exec

def main():
    '''
    main function: entry point of the shell program
    '''

    # implement REPL
    while True:
        sys.stdout.write('$ ') # print a prompt

        try:
            user_cmd = input() # captures user input from shell
            args = shlex.split(user_cmd) # seprates the input into arguments
        except EOFError:
            sys.exit() # handles CTRL + D

        match args[0]:
            case 'exit': # handles exit builtin
                sys.exit()

            case 'echo': # handles echo builtin
                subprocess.run(args)

            case 'type': # handles type builtin
                if args[1] in ['exit', 'echo', 'type']:
                    print(f'{args[1]} is a shell builtin')
                elif locate_exec.locate_exec(args[1]):
                    print(f'{args[1]} is {locate_exec.locate_exec(args[1])}')
                else:
                    print(f'{args[1]}: not found')

            case _: # handles executables
                if locate_exec.locate_exec(args[0]): # run executables
                    result = subprocess.run(
                        args=args,
                        capture_output=True,
                        text=True
                    )
                    print(f'{result.stdout}', end='')
                else:
                    print(f'{args[0]}: command not found') # handles invalid commands

if __name__ == '__main__':
    main()