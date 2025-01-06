### Vim Cheat Sheet

#### Basic Commands
- **Open a file**: `vim filename`
- **Exit Vim**: `:q`
- **Exit without saving**: `:q!`
- **Save changes**: `:w`
- **Save and exit**: `:wq` or `ZZ`
- **Undo**: `u`
- **Redo**: `Ctrl + r`

#### Navigation
- **Move cursor**: 
  - `h` - left
  - `j` - down
  - `k` - up
  - `l` - right
- **Word navigation**:
  - `w` - next word
  - `b` - previous word
  - `e` - end of word
- **Line navigation**:
  - `0` - beginning of line
  - `$` - end of line
  - `G` - go to the end of the file
  - `gg` - go to the beginning of the file
  - `:n` - go to line number n

#### Editing
- **Insert mode**: 
  - `i` - insert before the cursor
  - `I` - insert at the beginning of the line
  - `a` - append after the cursor
  - `A` - append at the end of the line
  - `o` - open a new line below
  - `O` - open a new line above
- **Delete**:
  - `x` - delete character under the cursor
  - `dw` - delete word
  - `dd` - delete line
  - `d$` - delete to the end of the line
- **Copy and Paste**:
  - `yy` - copy (yank) line
  - `y` + motion (e.g., `yw`, `y$`) - copy text
  - `p` - paste after the cursor
  - `P` - paste before the cursor

#### Searching
- **Search forward**: `/search_term`
- **Search backward**: `?search_term`
- **Next match**: `n`
- **Previous match**: `N`

#### Visual Mode
- **Enter visual mode**: `v` (character-wise), `V` (line-wise), `Ctrl + v` (block-wise)
- **Select text**: Move the cursor to select
- **Copy selected text**: `y`
- **Delete selected text**: `d`

#### Miscellaneous
- **Show line numbers**: `:set number`
- **Toggle syntax highlighting**: `:syntax on` / `:syntax off`
- **Open command line**: `:`
- **Repeat last command**: `.`

### Tips
- Use `Ctrl + f` to scroll down a page and `Ctrl + b` to scroll up a page.
- Use `:help` for detailed help on any command.

