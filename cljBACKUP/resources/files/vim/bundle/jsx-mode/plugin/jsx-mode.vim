function! ToggleJSXMode()
    if !exists('b:jsx')
        echom "JSX MODE"
        let b:jsx=1
    else
        echom "NORMAL MODE"
        unlet b:jsx
    endif

    return ""
endfunction

nnoremap <C-w> :call ToggleJSXMode()<CR>

function! GetAllLines()
    let cursor = getcurpos()
    let line_ending = {"unix": "\n", "dos": "\r\n", "mac": "\r"}[&fileformat]
    let text = join(getline(1, '$'), line_ending).line_ending
    let reg = '<\(\S\+\)>.*<\/\1>'
    normal lvim '<\(\S\+\)>.*<\/\1>' '%'
    echo lopen
    
endfunction
nnoremap <expr> w exists('b:jsx') ? '/><CR>l' : 'w'
nnoremap <expr> b exists('b:jsx') ? '?><CR>h' : 'b'
