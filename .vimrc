set nocompatible
filetype off

"Using vim in fish
"set shell=/bin/bash

" ~~~ VUNDLE SETTINGS ~~~
" ~~~~~~~~~~~~~~~~~~~~~~~ (see :h vundle for more details or wiki for FAQ)
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just
" :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - remove unused plugins (use `!` for auto-approve removal)
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'

" ~~~ INSTALL PLUGINS ~~~
" ~~~~~~~~~~~~~~~~~~~~~~~
"" Tmux integration helpers
Plugin 'christoomey/vim-tmux-navigator'
Plugin 'tmux-plugins/vim-tmux-focus-events'
"" File navigation / manipulation
Plugin 'ctrlpvim/ctrlp.vim'
Plugin 'scrooloose/nerdtree'
"" For Markdown or other prose writing
Plugin 'reedes/vim-pencil'
"" Others
Plugin 'sjl/gundo.vim'
"" Look and Feel
Plugin 'flazz/vim-colorschemes'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'airblade/vim-gitgutter'
Plugin 'tiagofumo/vim-nerdtree-syntax-highlight'
Plugin 'ryanoasis/vim-devicons' "Load as the last Plugin (per instructions)
        "Test if this actually needs to be the last plugin loaded or not

"" To try
"Plugin 'tpope/vim-dispatch'
"Plugin 'gilsondev/searchtasks.vim'
"Plugin 'wesQ3/vim-windowswap'
"Plugin 'majutsushi/tagbar'

"Plugin 'LanguageTool' " Requires additional setup to get working

"Plugin 'Townk/vim-autoclose' OR Plugin 'jiangmiao/auto-pairs'

"" Disabled / Unused Plugins
"Plugin 'vim-syntastic/syntastic'
"Plugin 'mileszs/ack.vim'
"Plugin 'lervag/vimtex'
"Plugin 'valloric/youcompleteme'
  " Extra install required. See - http://vimawesome.com/plugin/youcompleteme
  " $ sudo apt-get install build-essential cmake python-dev python3-dev
  " $ cd ~/.vim/bundle/YouCompleteMe
  " $ ./install.py --all

call vundle#end()
filetype plugin indent on


" ~~~ ALLOW PROJECT SPECIFIC SETTINGS ~~~
" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
" Allows vim to locally source .vimrc files from project working directory
"set exrc
" Restricts commands in non-default .vimrc file (like shell commands, etc.)
"set secure


" ~~~ GENERAL SETTINGS ~~~
" ~~~~~~~~~~~~~~~~~~~~~~~~
:let mapleader=","
set encoding=UTF-8
set backspace=indent,eol,start
set listchars=eol:⚬,tab:▸▸,trail:␣ ",space:␣,nbsp:☠
set list
set ruler
set wrap lbr
set colorcolumn=80
highlight colorcolumn ctermbg=darkgray
set history=1000
set undolevels=1000
set title
set number
set relativenumber
set hidden
"set autochdir
set autoread
set wildmenu
set showcmd
set showmatch
set ignorecase
set smartcase
set incsearch
set hlsearch
set splitbelow
set splitright
syntax on
"set mouse=a    "Enable the mouse (click, scroll, select, etc)
hi clear SignColumn

" tab spacing rules
set tabstop=2
set shiftwidth=2
set softtabstop=2
set expandtab
set smarttab

"Enable ctrl+u/ctrl+d to move lines up and down
nnoremap <C-A-Down> :m .+1<CR>==
nnoremap <C-A-Up> :m .-2<CR>==
inoremap <C-A-Down> <Esc>:m .+1<CR>==gi
inoremap <C-A-Up> <Esc>:m .-2<CR>==gi
vnoremap <C-A-Down> :m '>+1<CR>gv=gv
vnoremap <C-A-Up> :m '<-2<CR>gv=gv

"Easier buffer navigation
nnoremap <C-A-Left> :bp<CR>
nnoremap <C-A-Right> :bn<CR>
inoremap <C-A-Left> :bp<CR>
inoremap <C-A-Right> :bn<CR>
vnoremap <C-A-Left> :bp<CR>
vnoremap <C-A-Right> :bn<CR>

"Easy splitting current buffer
nnoremap <C-A-Space> :vsplit<CR>
inoremap <C-A-Space> :vsplit<CR>
vnoremap <C-A-Space> :vsplit<CR>

"Make it so I don't have to press two keys to navigate display lines
nnoremap j gj
nnoremap k gk
vnoremap j gj
vnoremap k gk
nnoremap <Down> gj
nnoremap <Up> gk
vnoremap <Down> gj
vnoremap <Up> gk
inoremap <Down> <C-o>gj
inoremap <Up> <C-o>gk

"Other mapping
  "Remove highlighting
:map <leader><space> :nohl<CR>
  "Save the current vim session (window configuration, etc)
:map <leader>s :mksession<CR>
:map - dd

" toggle between number and relativenumber
function! ToggleNumber()
    if(&relativenumber == 1)
        set norelativenumber
        set number
    else
        set relativenumber
    endif
endfunc
:map <leader>n :call ToggleNumber()<CR>

" ~~~ Gundo ~~~
nnoremap <leader>u :GundoToggle<CR>
let g:gundo_prefer_python3=1
let g:gundo_width=80
let g:gundo_preview_height=40
let g:gundo_right=1

" ~~~ CTRL P ~~~
let g:ctrlp_match_window = 'bottom,order:ttb'
let g:ctrlp_switch_buffer = 0
let g:ctrlp_working_path_mode = 0

" ~~~ NERDTree ~~~
map <C-n> :NERDTreeToggle<CR>
:let g:NERDTreeWinSize=40
" Automatically open NERDTree if vim opened on a directory
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | endif
" Close vim if NERDTree is the only buffer with data
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
" Fix lagging from line highlighting
let g:NERDTreeHighlightCursorline=0

" ~~~ Markdown ~~~
augroup markdown
    autocmd!
    autocmd BufNewFile,BufRead *.md,*.markdown setlocal filetype=markdown
    autocmd FileType markdown nnoremap <leader>c :exec '!google-chrome % &> /dev/null'<CR>
augroup END

let g:pencil#wrapModeDefault = 'soft'
"let g:languagetool_jar  = '/opt/languagetool/languagetool-commandline.jar'

augroup pencil
  autocmd!
  autocmd FileType markdown call pencil#init()
  autocmd FileType text     call pencil#init()
augroup END

" ~~~ Theme ~~~
set background=dark
if (has("termguicolors"))
  set termguicolors " if you want to run vim in a terminal
endif
colorscheme jellybeans
if &term =~ '256color'
    " Disable Background Color Erase (BCE) so that color schemes
    " work properly when Vim is used inside tmux and GNU screen.
    " From - superuser.com/questions/457911/\
    "    in-vim-background-color-changes-on-scrolling
    set t_ut=
endif

" ~~~ Airline ~~~
" For fonts: https://github.com/abertsch/Menlo-for-Powerline
set laststatus=2
let g:airline_powerline_fonts=1
let g:airline_detect_paste=1
let g:airline#extensions#tabline#enabled=1 "show tabs at the top for buffers
let g:airline_theme='jellybeans'

"" ~~~ Airline Gitgutter Section ~~~
"Only show the differences on the powerline if there any, otherwise omit it
let g:airline#extensions#hunks#non_zero_only=1

" ~~~ Syntastic ~~~
"let g:syntastic_error_symbol='✘'
"let g:syntastic_warning_symbol='▲'
"let g:syntastic_always_populate_loc_list = 1
" let g:syntastic_auto_loc_list = 1
"let g:syntastic_check_on_open = 0
"let g:syntastic_check_on_wq = 0
"let g:syntastic_aggregate_errors = 1
"let g:syntastic_auto_jump = 0
"let g:syntastic_stl_format = "[%E{Err: %fe #%e}%B{, }%W{Wrn: %fw #%w}]"
"augroup mySyntastic
"    au!
"    au FileType tex let b:syntastic_mode="passive"
"augroup END
"
"function Py2()
"    let g:syntastic_python_python_exec = '/usr/local/bin/python2.7'
"    let g:syntastic_python_pylint_exe = '/usr/local/bin/python2.7 -m pylint'
"endfunction
"function Py3()
"    let g:syntastic_python_python_exec = '/usr/local/bin/python3.6'
"    let g:syntastic_python_pylint_exe = '/usr/local/bin/python3.6 -m pylint'
"endfunction
"call Py3() " Default to python2.

"" ~~~ YouCompleteMe ~~~
"let g:ycm_confirm_extra_conf = 0
"let g:ycm_global_ycm_extra_conf = '~/.vim/.ycm_extra_conf.py'
"let g:ycm_autoclose_preview_window_after_completion = 1
