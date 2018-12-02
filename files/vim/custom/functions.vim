" Helper function. Returns input from user
function GetInput()
    call inputsave()
    let x = input("input: ")
    call inputrestore()
    return x
endfunction

" Inserts string into current line, at cursor position
function PutStr(str)
    let original = getline('.')
    let cursor = getcurpos()[2]
    let one_before_cursor = cursor - 1
    let two_before_cursor = cursor - 2
    let beginning = original[0:one_before_cursor]
    let ending = original[one_before_cursor:-1]
    let final = beginning . a:str . ending
    call setline('.', final)
endfunction

function Grep()
    let str = GetInput()
    let excluded = "deps,node_modules,priv,_build"
    let options = " -rin -l --exclude-dir={" . excluded . "} "
    let location = " *"
    execute "grep" . options . str . location
endfunction

nnoremap <leader>grep :call Grep()<CR>

" Fix weird bug where backspace isn't registered            
function Backspace()
    if col('.') == 1
        if line('.') != 1
            return "\<ESC>ka\<Del>"
        else
            return ""
        endif
    else
        return "\<Left>\<Del>"
    endif
endfunction

inoremap <BS> <c-r>=Backspace()<CR>

" dw becomes d2w if word preceeds a comma

function HandleDW()
    if getline(".")[col(".")-1] == ','
        :normal dw
    endif
endfunction
nnoremap dw dw:call HandleDW()<CR>

