def progressBar(progress, maxVal, prefix = "", suffix = ""):
    ratio = float(progress/(maxVal-1))
    bar = int(round(ratio*20, 0))
    text = "[{0}] {1}%".format(("#"*bar)+"-"*(20-bar), int(ratio*100))
    print(prefix, text, suffix, end="\r")

