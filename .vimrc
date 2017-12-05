set nocompatible

"Using vim in fish
set shell=/bin/bash

" ~~~ VUNDLE SETTINGS ~~~
" ~~~~~~~~~~~~~~~~~~~~~~~
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just
" :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; 
"             append `!` to auto-approve removal
" see :h vundle for more details or wiki for FAQ
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
" Install plugins
Plugin 'flazz/vim-colorschemes'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'scrooloose/nerdtree'
Plugin 'vim-syntastic/syntastic'
Plugin 'ctrlpvim/ctrlp.vim'
Plugin 'airblade/vim-gitgutter'
Plugin 'tpope/vim-fugitive'
Plugin 'lervag/vimtex'
Plugin 'christoomey/vim-tmux-navigator'
"Plugin 'tpope/vim-surround'
Plugin 'jiangmiao/auto-pairs'
" Plugin 'christoomey/vim-tmux-navigator'
" Extra install required. See - http://vimawesome.com/plugin/youcompleteme
" $ sudo apt-get install build-essential cmake python-dev python3-dev
" $ cd ~/.vim/bundle/YouCompleteMe
" $ ./install.py --all
Plugin 'valloric/youcompleteme'

call vundle#end()
filetype plugin indent on


" ~~~ GENERAL SETTINGS ~~~
" ~~~~~~~~~~~~~~~~~~~~~~~~
set backspace=indent,eol,start
set listchars=eol:⚬,tab:▸▸,trail:␣ ",space:␣,nbsp:☠
set list
set ruler
set wrap lbr
set colorcolumn=79
highlight colorcolumn ctermbg=darkgray
set history=1000
set undolevels=1000
set title
set number
set hidden
set autochdir
set showcmd
set showmatch
set ignorecase
set smartcase
set incsearch
set hlsearch
set splitbelow
set splitright
" split navigations
" nnoremap <C-J> <C-W><C-J>
" nnoremap <C-K> <C-W><C-K>
" nnoremap <C-L> <C-W><C-L>
" nnoremap <C-H> <C-W><C-H>
" tab spacing
set tabstop=4
set shiftwidth=4
set expandtab
syntax on
"set mouse=a    "Enable the mouse (click, scroll, select, etc)
hi clear SignColumn

"Enable ctrl+u/ctrl+d to move lines up and down
nnoremap <C-A-Down> :m .+1<CR>==
nnoremap <C-A-Up> :m .-2<CR>==
inoremap <C-A-Down> <Esc>:m .+1<CR>==gi
inoremap <C-A-Up> <Esc>:m .-2<CR>==gi
vnoremap <C-A-Down> :m '>+1<CR>gv=gv
vnoremap <C-A-Up> :m '<-2<CR>gv=gv

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
:map ,<space> :nohl<CR>
:map - dd

" ~~~ Theme ~~~
set background=dark
" set termguicolors " if you want to run vim in a terminal
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
let g:airline#extensions#tabline#enabled=1
let g:airline_theme='jellybeans'

" ~~~ Syntastic ~~~
let g:syntastic_error_symbol='✘'
let g:syntastic_warning_symbol='▲'
let g:syntastic_always_populate_loc_list = 1
" let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
let g:syntastic_aggregate_errors = 1
let g:syntastic_auto_jump = 1
let g:syntastic_stl_format = "[%E{Err: %fe #%e}%B{, }%W{Wrn: %fw #%w}]"
augroup mySyntastic
    au!
    au FileType tex let b:syntastic_mode="passive"
augroup END

function Py2()
    let g:syntastic_python_python_exec = '/usr/local/bin/python2.7'
    let g:syntastic_python_pylint_exe = '/usr/local/bin/python2.7 -m pylint'
endfunction
function Py3()
    let g:syntastic_python_python_exec = '/usr/local/bin/python3.6'
    let g:syntastic_python_pylint_exe = '/usr/local/bin/python3.6 -m pylint'
endfunction
call Py3() " Default to python2.

" ~~~ Gitgutter ~~~
let g:airline#extensions#hunks#non_zero_only=1

" ~~~ NERDTree ~~~
map <C-n> :NERDTreeToggle<CR>

" ~~~ YouCompleteMe ~~~
let g:ycm_confirm_extra_conf = 0
let g:ycm_global_ycm_extra_conf = '~/.vim/.ycm_extra_conf.py'
let g:ycm_autoclose_preview_window_after_completion = 1
