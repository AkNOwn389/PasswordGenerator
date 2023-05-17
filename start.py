import sys, os, time, random, string
if sys.platform == "linux" or sys.platform == "linux2":
    clr="clear"
elif sys.platform == "win32" or sys.platform == "cygwin" or sys.platform == "msys":
    clr="cls"
line=("\033[1;92m╔═"+57*"\033[1;92m═")
line2=("\033[1;92m║"+58*"\033[1;92m═")
logo=""" \033[1;92m█████╗ ██╗  ██╗███╗   ██╗ ██████╗ ██╗    ██╗███╗   ██╗
██╔══██╗██║ ██╔╝████╗  ██║██╔═══██╗██║    ██║████╗  ██║
███████║█████╔╝ ██╔██╗ ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
██╔══██║██╔═██╗ ██║╚██╗██║██║   ██║██║███╗██║██║╚██╗██║
██║  ██║██║  ██╗██║ ╚████║╚██████╔╝╚███╔███╔╝██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝"""

class GenerateUserPassword:
    def __init__(self) -> None:
        self.start()
        
    def start(self) -> None:
        self.total = 0
        self.numbers = []
        self.strings = []
        self.name = []
        os.system(clr)
        print(logo)
        print(line)
        print("\033[1;92m║ \033[1;94m—> \033[1;92mFirst Name")
        self.first_name = pick()
        print("\033[1;92m║ \033[1;94m—> \033[1;92mLast Name")
        self.last_name = pick()
        print("\033[1;92m║ \033[1;94m—> \033[1;92mMiddle Name")
        self.middle_name = pick()
        print("\033[1;92m║ \033[1;94m—> \033[1;92mBirth Year ex:2000")
        self.birth_year = pick()
        print("\033[1;92m║ \033[1;94m—> \033[1;92mBirth Month ex:12")
        self.birth_month = pick()
        print("\033[1;92m║ \033[1;94m—> \033[1;92mBirth Day ex:16")
        self.birth_day = pick()
        print("\033[1;92m║ \033[1;94m—> \033[1;92mInput More Details About User\n\033[1;92m║ \033[1;92mWith Space ex: dog/food/place etc.")
        self.etc = pick()
        for a in self.first_name, self.last_name, self.middle_name:
            if a is not "skip":
                self.name.append(a)
                self.strings.append(a)
        for string in self.etc.split(" "):
            self.strings.append(string)
        self.numbers.append(int(self.birth_day))
        self.numbers.append(int(self.birth_month))
        self.numbers.append(int(self.birth_year))
        self.file_name = str(self.first_name)
        self.run()
        
    def run(self) -> None:
        results = []
        possible_name_patterns = []
        for a in self.name:
            for b in self.name:
                for c in self.name:
                    if "skip" not in list[a, b, c]:
                        possible_name_patterns.append(str(a)+str(b)+str(c))
                    elif a is "skip":
                        possible_name_patterns.append(str(b)+str(c))
                    elif b is "skip":
                        possible_name_patterns.append(str(a)+str(c))
                    elif c is "skip":
                        possible_name_patterns.append(str(a)+str(b))
                        
        possible_birth_patterns = []
        for a in self.numbers:
            for b in self.numbers:
                for c in self.numbers:
                    possible_birth_patterns.append(str(a)+str(b)+str(c))
                    if len(str(a)) is 1 and str(a) is not "0":
                        a = "0" + str(a)
                        possible_birth_patterns.append(str(a)+str(b)+str(c))
                    elif len(str(b)) is 1 and str(b) is not "0":
                        b = "0" + str(b)
                        possible_birth_patterns.append(str(a)+str(b)+str(c))
                    elif len(str(c)) is 1 and str(c) is not "0":
                        c = "0" + str(c)
                        possible_birth_patterns.append(str(a)+str(b)+str(c))
                        
        possible_etc = []
        for a in self.strings:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
            sys.stdout.flush()
            self.total += 1
            for b in possible_name_patterns:
                sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
                sys.stdout.flush()
                self.total += 1
                for c in possible_birth_patterns:
                    sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
                    sys.stdout.flush()
                    self.total += 1
                    possible_etc.append(str(a)+str(b)+str(c))
        possible_name_patterns_with_birth = []
        for a in possible_name_patterns:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
            sys.stdout.flush()
            self.total += 1
            for b in possible_birth_patterns:
                sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
                sys.stdout.flush()
                self.total += 1
                possible_name_patterns_with_birth.append(str(a)+str(b))
                possible_name_patterns_with_birth.append(str(b)+str(a))
        possible_etc_patterns_with_birth = []
        for a in possible_etc:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
            sys.stdout.flush()
            self.total += 1
            for b in possible_birth_patterns:
                sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
                sys.stdout.flush()
                self.total += 1
                possible_etc_patterns_with_birth.append(str(a)+str(b))
                possible_etc_patterns_with_birth.append(str(b)+str(a))
            for c in self.strings:
                sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
                sys.stdout.flush()
                self.total += 1
                possible_etc_patterns_with_birth.append(str(c)+str(a))
                possible_etc_patterns_with_birth.append(str(a)+str(c))
        for a in possible_birth_patterns:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
            sys.stdout.flush()
            self.total += 1
            results.append(a)
        for a in possible_etc:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
            sys.stdout.flush()
            self.total += 1
            results.append(a)
        for a in possible_name_patterns:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
            sys.stdout.flush()
            self.total += 1
            results.append(a)
        for a in possible_name_patterns_with_birth:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
            sys.stdout.flush()
            self.total += 1
            results.append(a)   
        for a in possible_etc_patterns_with_birth:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
            sys.stdout.flush()
            self.total += 1
            results.append(a)
        results_second = []
        for a in results:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
            sys.stdout.flush()
            self.total += 1
            results_second.append(str(a).upper())
            if str(a)[0] in string.ascii_lowercase:
                b = str(a).replace(str(a)[0], str(a)[0].upper())
                results_second.append(b)
            results_second.append(a)
                
        #test for duplicate names
        final_results = []
        for a in results_second:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} checking for duplicates..")
            sys.stdout.flush()
            self.total += 1
            if not a in final_results:
                final_results.append(a)
        try:
            os.mkdir("results")
        except OSError:
            pass
        f = open(f"results/{self.first_name}.txt", "a")
        for a in final_results:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} writing results in file...")
            sys.stdout.flush()
            self.total += 1
            f.write(str(a)+"\n")
        f.close()
        print(line)
        print(f"\033[1;92m║ \033[1;94m—> \033[1;93m Result stored in result/{self.first_name}.txt")
        input("\033[1;92mExit")
        home()
            
def home_pick() -> None:
    p = pick()
    if p == "1":
        GenerateUserPassword()
    else:
        print("\033[1;92m\033[1;91minvalid input")
        home_pick()
def pick():
    a = input("\033[1;92m╚═════\033[1;91m>>>\033[1;97m")
    return a
def home():
    os.system(clr)
    print(logo)
    print(line)
    print("\033[1;92m║ \033[1;91m1. \033[1;94m—> \033[1;92mGenerate User Password")
    print("\033[1;92m║ \033[1;91m0. \033[1;94m—> \033[1;93mExit")
    home_pick()
if __name__ == "__main__":
    home()