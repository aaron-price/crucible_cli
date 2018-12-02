"""" NERDTree
" you can add these colors to your .vimrc to help customizing
let s:brown = "905532"
let s:aqua =  "3AFFDB"
let s:blue = "689FB6"
let s:darkBlue = "44788E"
let s:purple = "834F79"
let s:lightPurple = "834F79"
let s:red = "AE403F"
let s:beige = "F5C06F"
let s:yellow = "F09F17"
let s:orange = "D4843E"
let s:darkOrange = "F16529"
let s:pink = "CB6F6F"
let s:salmon = "EE6E73"
let s:green = "8FAA54"
let s:lightGreen = "31B53E"
let s:white = "FFFFFF"
let s:rspec_red = 'FE405F'
let s:git_orange = 'F54D27'
let g:WebDevIconsUnicodeDecorateFileNodesExtensionSymbols = {}
let g:WebDevIconsUnicodeDecorateFileNodesExtensionSymbols['ex'] = ''
let g:WebDevIconsUnicodeDecorateFileNodesExtensionSymbols['exs'] = ''

let g:NERDTreeExtensionHighlightColor = {} " this line is needed to avoid error
let g:NERDTreeExtensionHighlightColor['ex'] = s:pink " sets the color of ex files to blue
let g:NERDTreeExtensionHighlightColor['exs'] = s:pink " sets the color of exs files to blue

let g:NERDTreeExactMatchHighlightColor = {} " this line is needed to avoid error
let g:NERDTreeExactMatchHighlightColor['.gitignore'] = s:git_orange " sets the color for .gitignore files

let g:NERDTreePatternMatchHighlightColor = {} " this line is needed to avoid error
let g:NERDTreePatternMatchHighlightColor['.*_spec\.rb$'] = s:rspec_red " sets the color for files ending with _spec.rb

" NERDTree setting defaults to work around http://github.com/scrooloose/nerdtree/issues/489
let g:NERDTreeDirArrows = 1
let g:NERDTreeDirArrowExpandable = '▸'
let g:NERDTreeDirArrowCollapsible = '▾'
let g:NERDTreeGlyphReadOnly = "RO"
let g:NERDTreeWinSize=35
let g:NERDTreeFileExtensionHighlightFullName = 1
let g:NERDTreeExactMatchHighlightFullName = 1
let g:NERDTreePatternMatchHighlightFullName = 1

" Fix lag
let g:NERDTreeSyntaxDisableDefaultExtensions = 1
let g:NERDTreeDisableExactMatchHighlight = 1
let g:NERDTreeDisablePatternMatchHighlight = 1
let g:NERDTreeSyntaxEnabledExtensions = ['vim', 'js', 'ex', 'exs', 'html', 'css', 're', 'json', 'scss', 'md', 'sh']
let g:NERDTreeHighlightCursorline = 0

autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
noremap <Leader>f :NERDTreeToggle<Enter>
noremap <silent> <Leader>v :NERDTreeFind<CR>

let NERDTreeAutoDeleteBuffer = 1
let NERDTreeMinimalUI = 1
let NERDTreeDirArrows = 1
let NERDTreeShowHidden=1

" Close vim if NERDTree is the last thing open
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" Navigate splits with ctrl + direction
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

"""" Gundo
nnoremap <F5> :GundoToggle<CR>
nnoremap <leader>u :GundoToggle<CR> 

"""" CtrlP
set runtimepath^=~/.vim/bundle/ctrlp/plugin/ctrlp.vim

"""" DRAG VISUALS
runtime /bundle/dragvisuals/dragvisuals.vim
vmap  <expr>  <LEFT>   DVB_Drag('left')
vmap  <expr>  <RIGHT>  DVB_Drag('right')
vmap  <expr>  <DOWN>   DVB_Drag('down')
vmap  <expr>  <UP>     DVB_Drag('up')
vmap  <expr>  D        DVB_Duplicate()
let g:DVB_TrimWS = 1 " Remove trailing whitespace

"""" Emmet
nnoremap <leader>fin <c-y>,
let g:user_emmet_settings = {
    \'javascript.jsx' : {
    \     'extends': 'jsx',
    \     'quote_char': "'",
    \   }
    \}

"""" Vim-JSX-Utils
"nnoremap <leader>xret :call JSXEncloseReturn()<CR> " JSX RETURN
"nnoremap <leader>xpre :call JSXEachAttributeInLine()<CR> " JSX prettify
"nnoremap <leader>xc :call JSXChangeTagPrompt()<CR> " JSX Change
"nnoremap <leader>x* :call JSXSelectTag()<CR>

