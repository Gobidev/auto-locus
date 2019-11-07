from cx_Freeze import setup, Executable

setup(
    name="Auto Locus",
    version="1.0",
    description="Auto locus is a small programm that automatically determines the locus of a given funciton.",
    executables=[Executable(script="Auto_Locus.py", base="Win32GUI")]
)
