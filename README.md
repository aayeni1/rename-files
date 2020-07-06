# rename-files
Basic scripting challenge to rename all files to lower case

Implement a public function `RenameFilesLower`.

This function should do the following:
  - Given a directory path, every non-directory file should be renamed to the
    lower case version and return the full paths in a list. Including files that
    are in subdirectoties, but directories should not be renamed.

If a file already exists append a number on the end (starting with a 1 index),
if there is already a number increment it. The file extension should be
preserved (if it exists).

Example: [file, FILE, File] -> [file, file1, file2]

The function signature is:
  `def RenameFilesLower(path: str) -> List[str]:`
