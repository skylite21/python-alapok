# https://vi.stackexchange.com/questions/25076/coc-python-reports-unresolved-import-in-git-subfolder
# assumes that a directory containing .git/ is the root of your project.  To
# override this behaviour you can set the list to include the name of your
# virtual environment. In this case:
# autocmd FileType python let b:coc_root_patterns = ['.git', '.venv']

from my_module import say_hi, multiply


say_hi()
multiply(2, 2)
