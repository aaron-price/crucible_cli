" inserts variable into IO.inspect(VARIABLE, label: "VARIABLE")
function! EchoIO()
    let name = GetInput()
    let str = "IO.inspect(" . name . ", label: \"" . name . "\")"
    call PutStr(str)
endfunction

" Handle logging boilerplate in elixir and js
nnoremap <leader>io :call EchoIO()<CR>$
inoremap <leader>io p<ESC>:call EchoIO()<CR>x$xa
