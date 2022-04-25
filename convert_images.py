from os import listdir, system, mkdir
from os.path import isfile, join, exists

sourceDir = "source"
targetDir = "target"
targetSize = 400000


files = [f for f in listdir(sourceDir) if isfile(join(sourceDir, f))]

for f in files:
    sourceFile = join(sourceDir, f)
    targetFile = join(targetDir, f.split('.')[0] + ".webp")

    if not exists(targetDir):
        mkdir(targetDir)

    command = "cwebp -size {targetSize} {sourceFile} -o {targetFile}"\
        .format(targetSize=targetSize,
                sourceFile=sourceFile,
                targetFile=targetFile)

    print(command)

    system(command)

