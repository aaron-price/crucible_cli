" inserts variable into console.log("VARIABLE: ", VARIABLE)
function! EchoConsole()
    echom getcurpos()[2]
    let name = GetInput()
    let str = "console.log(\"" . name . ": \", " . name . ")"
    call PutStr(str)
endfunction

nnoremap <leader>log :call EchoConsole()<CR>
inoremap <leader>log p<ESC>:call EchoConsole()<CR>x$xa

" Handle className boilerplate in react
function! EchoClassName()
    let name = GetInput()
    let str = "className=\"" . name . "\" "
    call PutStr(str)
endfunction

nnoremap <leader>cn :call EchoClassName()<CR>$
inoremap <leader>cn p<ESC>:call EchoClassName()<CR>x2f"fpxa

" Generates this.myFunc = this.myFunc.bind(this)
function! BindMethod()
    let name = GetInput()
    let str = "this." . name . " = this." . name . ".bind(this)"
    call PutStr(str)
endfunction

nnoremap <leader>bind :call BindMethod()<CR>$
inoremap <leader>bind p<ESC>:call BindMethod()<CR>x$xa

