" move to beginning/end of line
nnoremap B ^
nnoremap E $

" Clear last search with space
noremap <Space> :noh<cr>

" hit qq to record, q to stop recording, and Q to apply.
nnoremap Q @q
vnoremap Q :norm @q<cr>

" faster :
nnoremap ; :

nnoremap gV `[v`] " highlight last inserted text
inoremap jk x<C-c>"_x					" jk exits insert mode, without moving the cursor like esc normally does

" ,sa = search all
inoremap <leader>sa <ESC>:%s/
nnoremap <leader>sa :%s/

" ,sl = search line
inoremap <leader>sl <ESC>:.s/
nnoremap <leader>sl :.s/

" paste inner. Pastes starting on the current column, NOT the next one
nnoremap <leader>pi hp

" Map ctrl-s to :w
command -nargs=0 -bar Update if &modified 
   \|    if empty(bufname('%'))
   \|        browse confirm write
   \|    else
   \|        confirm write
   \|    endif
   \|endif
noremap <silent> <C-S>          :update<CR>
vnoremap <silent> <C-S>         <C-C>:update<CR>
inoremap <silent> <C-S>         <C-O>:update<CR>

" Comment out JSX
nnoremap <leader>// O{/*<ESC>jo*/}

" 'I' drops the remainder of the line twice and inserts between
nnoremap <leader>O i<CR><ESC>O
inoremap <leader>O <CR><ESC>O

" convert 4 spaces to 2
nnoremap <leader>4to2 :%s;^\(\s\+\);\=repeat(' ', len(submatch(0))/2);g<cr><esc>

" convert 2 spaces to 4
nnoremap <leader>2to4 :%s/^\s*/&&<cr><esc>

" convert tab to 2
nnoremap <leader>tabto4 :%s/\t/    /g<cr><esc>
nnoremap <leader>tabto2 :%s/\t/  /g<cr><esc>
