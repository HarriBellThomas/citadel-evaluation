import os, sys

folders = ["vanilla", "citadel"]
script_dir = (os.path.dirname(os.path.realpath(__file__)))

apps = [
    ("io", [
        ("-b", ["{}".format(2**i) for i in range(5, 24)]),
        ("-t", ["16777216"]),
        ("-", ["r", "w"]),
        ("?", [{
            "vanilla": "{}/samples/16MiB.txt".format(script_dir),
            "citadel": "/opt/tainted/16MiB.txt", # Hack.
        }])
    ]),
    ("ipc", [
        ("-i", ["pipe", "local", "tcp"]),
        ("-b", ["{}".format(2**i) for i in range(5, 24)]),
        ("-t", ["16777216"]),
        ("", ["1thread", "2thread", "2proc"]),
    ])
]
iterations = 1

def result_to_log(folder, opt_s, res):
    _id = opt_s.replace(" ", "") \
               .replace("{}/samples/".format(script_dir), "-") \
               .replace(".txt", "")
    _val = res.replace("\\n", "").replace(" KBytes/sec", "")

    with open("{}/results.log".format(script_dir), "a+") as f:
        f.write("{}-{},{}".format(folder, _id, _val))

for folder in folders:
    for app in apps:
        name = app[0]
        option_strings = []
        hdr = "{}.{}".format(folder, name)
        sys.stdout.write("{} -- {} / {}".format(hdr, 0, "?"))
        sys.stdout.flush()

        def optval_to_s(app, option, val):
            if option == "":
                return val
            elif option == "-":
                return "-{}".format(val)
            elif option == "?":
                return val[app]
            else:
                return "{} {}".format(option, val)

        def append_options(app, option, values):
            global option_strings
            if len(option_strings) == 0:
                option_strings = [optval_to_s(app, option, v) for v in values]
            else:
                new_option_strings = []
                for v in values:
                    new_option_strings.extend(
                        ["{} {}".format(_os, optval_to_s(app, option, v)) for _os in option_strings]
                    )
                option_strings = new_option_strings
                # for x in option_strings:
                #     print(x)

        # For each parameter, loop through options.
        for param in app[1]:
            append_options(folder, *param)

        # Do number of iterations.
        option_strings = option_strings * iterations

        sys.stdout.write("\r{} -- {} / {}".format(hdr, 0, len(option_strings)))
        sys.stdout.flush()

        #
        i = 1
        for _os in option_strings:
            cmd = ("{0}/{1}/{2}/{2} {3}".format(script_dir, folder, name, _os))
            output = os.popen(cmd).read()
            result_to_log(folder, _os, output)
            sys.stdout.write("\r{} -- {} / {}".format(hdr, i, len(option_strings)))
            sys.stdout.flush()
            i += 1
        sys.stdout.write("\n")
