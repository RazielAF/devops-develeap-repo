def main(logfile_path):
    try:
        with open(logfile_path) as f:
            f = f.readlines()
    except:
        return "err"

    codes = [line.split(' ')[8] for line in f]
    result = [(int(code), codes.count(code) )for code in set(codes)]
    return sorted(result)


