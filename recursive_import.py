'''
Recursively import all python files in a directory
and clean the result.
'''
c.recursiveImport(
    dir_ = '~/',
    kind = '@clean', #'@nosent','@auto','@file',
    one_file = False,
    safe_at_file = False, # True,
    theTypes = ['.py', '.html'],
)


'''
Recursively import all python files in a directory and clean the results.

Parameters::
dir_         The root directory or file to import.
kind         One of ('@clean','@edit','@file','@nosent').
one_file     True: import only the file given by dir_.
safe_at_file True: produce @@file nodes instead of
             @file nodes.
theTypes     A list of file extensions to import.
             None is equivalent to ['.py']
    
This method cleans imported files as follows:

- Replace backslashes with forward slashes in headlines.
- Remove empty nodes.
- Add @path directives that reduce the needed path specifiers in descendant nodes.
- Add @file to nodes or replace @file with @@file.
'''