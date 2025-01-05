# Bash Cheat Sheet

## Basic Syntax

### Shebang
```bash
#!/bin/bash
```
- Indicates that the script should be run using the Bash shell.

### Comments
- **Single Line:** 
  ```bash
  # This is a comment
  ```
- **Multi-line:**
  ```bash
  : <<'END'
  This is a
  multi-line comment
  END
  ```

## Variables

### Creating and Using Variables
```bash
name="John"          # Assign value
echo $name          # Access value
```

### Special Variables
- `$0`: Name of the script
- `$1`, `$2`, ...: Command line arguments
- `$#`: Number of arguments
- `$?`: Exit status of the last command
- `$$`: Process ID of the current script

## Command Execution

### Running Commands
```bash
ls                   # List files in the current directory
pwd                  # Print working directory
```

### Command Substitution
```bash
current_dir=$(pwd)   # Assign output of pwd to variable
```

### Redirecting Output
```bash
command > file.txt   # Redirect output to a file (overwrite)
command >> file.txt  # Redirect output to a file (append)
```

### Piping
```bash
command1 | command2  # Use output of command1 as input to command2
```

## Input/Output

### Reading User Input
```bash
read -p "Enter your name: " user_name
echo "Hello, $user_name!"
```

### Redirecting Input
```bash
command < input.txt   # Read input from a file
```

## Control Structures

### Conditional Statements
```bash
if [ condition ]; then
    # code to execute if condition is true
fi

if [ condition ]; then
    # code if true
else
    # code if false
fi
```

### Case Statement
```bash
case variable in
    pattern1)
        # code
        ;;
    pattern2)
        # code
        ;;
    *)
        # default code
        ;;
esac
```

### Loops
#### For Loop
```bash
for item in list; do
    echo $item
done
```

#### While Loop
```bash
while [ condition ]; do
    # code
done
```

#### Until Loop
```bash
until [ condition ]; do
    # code
done
```

## Functions

### Defining and Calling Functions
```bash
my_function() {
    echo "Hello from my function!"
}

my_function  # Call the function
```

## Arithmetic Operations
```bash
result=$((5 + 3))  # Addition
echo $result       # Output: 8
```

## String Manipulation

### Concatenation
```bash
greeting="Hello"
name="World"
message="$greeting, $name!"  # "Hello, World!"
echo $message
```

### String Length
```bash
length=${#message}  # Get length of the string
echo $length
```

## Useful Commands

- `clear`: Clear the terminal screen.
- `man command`: Show the manual for a command.
- `history`: Show command history.
- `exit`: Exit the current shell or script.

