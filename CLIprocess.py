from fileprocess import generateFile, replaceFile


def generateCLI(password, compresslevel, compressPath: str, compressFile: str, size: str = '15g'):
    generStr = f"7z a -v{size} -p{password} -mx{compresslevel} -mhe=on \"{compressPath}.7z\" \"{compressFile}\"\n"
    return generStr


def processRunModeCLIArgs(CLIArgs: list):
    processedArgs = []
    r_index = -1
    n_index = -1
    lock = -1
    for i in CLIArgs:
        processedArgs.append(i)
    try:
        processedArgs.index("-r")
    except ValueError:
        lock += 1
    else:
        r_index = processedArgs.index("-r")

    try:
        processedArgs.index("-n")
    except ValueError:
        lock += 1
    else:
        n_index = processedArgs.index("-n")

    if lock == True:
        processedArgs.append("-r")
        return processedArgs, "-r"

    if r_index > -1 and n_index > -1:
        method = processedArgs.pop(r_index if r_index > n_index else n_index)
        return processedArgs, "-n" if method == "-r" else "-r"
    else:
        method = processedArgs[processedArgs.index(
            "-r" if r_index > n_index else "-n")]
        return processedArgs, method


def swtichRunMode(runCLI, method):
    if method == "-r":
        replaceFile(runCLI)
    else:
        generateFile(runCLI)


def processCLIArgs(args: list[str]):
    validCLI: list[str] = ["-p", "-v", "-h"]
    arg = str
    try:
        for arg in args:
            for i in range(0, args):
                if arg.find(validCLI[i]) == -1:
                    raise Exception("Not Found Arg")
                else:
                    None

    except Exception:
        print("参数传入错误")
