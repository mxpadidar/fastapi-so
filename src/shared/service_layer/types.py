from typing import Callable

type MimeTypeDetectorFunc = Callable[[bytes], str]

type FilenameGeneratorFunc = Callable[[str], str]
