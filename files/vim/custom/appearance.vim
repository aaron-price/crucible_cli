colorscheme desert

set tabstop=8 softtabstop=0 expandtab shiftwidth=4 smarttab

" Hybrid line numbers
set number relativenumber
augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
  autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
augroup END

set showcmd             " show command in bottom bar

filetype indent on      " load filetype-specific indent files
set wildmenu            " visual autocomplete for command menu
set lazyredraw          " redraw only when we need to.
set showmatch           " highlight matching [{()}]
set incsearch           " search as characters are entered
set hlsearch            " highlight matches
nnoremap <leader><space> :nohlsearch<CR>	" turn off search highlight

" Show tab and trailing spaces better
" set listchars=tab:>~,nbsp:_,trail:.
set listchars=tab:>~
set list

" Make column 80 and 100 stand out
highlight CautionColumn ctermbg=11 ctermfg=1
highlight DangerColumn ctermbg=9 ctermfg=15
call matchadd('CautionColumn', '\%80v', 100)
call matchadd('DangerColumn', '\%100v', 100)

" syntax highlighting for diff files
augroup PatchDiffHighlight
    autocmd!
    autocmd BufEnter *.patch,*.ref,*.diff  syntax enable
augroup END
