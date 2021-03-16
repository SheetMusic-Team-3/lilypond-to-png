import os


# Hilary's path: "/Users/hilnels/Desktop/lilyPondFiles"
def lilypond_to_png(path):

    os.system("export PATH=~/bin:$PATH")
    os.chdir(path)

    for filename in os.listdir(path):
        print(filename)
        if filename.endswith(".ly"):
            os.system("lilypond --png " + filename)
            continue
        else:
            continue

