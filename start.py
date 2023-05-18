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
        print("\033[1;92m║ \033[1;94m—> \033[1;92mCheck Generated Password For Duplicate? y/N")
        dup = pick()
        if dup[0] is "y" or dup[0] is "Y":
            self.isChekablePassword = True
        else:
            self.isChekablePassword = False
        for a in self.first_name, self.last_name, self.middle_name:
            if a is not "skip":
                self.name.append(a.lower())
                self.strings.append(a.lower())
                self.name.append(a.upper())
                self.strings.append(a.upper())
        for string in self.etc.split(" "):
            self.strings.append(string.lower())
            self.strings.append(string.upper())
        self.numbers.append(str(self.birth_day))
        self.numbers.append(str(self.birth_month))
        self.numbers.append(str(self.birth_year))
        self.file_name = str(self.first_name)
        self.run()
        
    def createPossibleNamePatterns(self) -> list[str]:
        possible_name_patterns = []
        for a in self.name:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
            sys.stdout.flush()
            self.total += 1
            for b in self.name:
                sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
                sys.stdout.flush()
                self.total += 1
                for c in self.name:
                    sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
                    sys.stdout.flush()
                    self.total += 1
                    if "skip" not in list[a, b, c]:
                        possible_name_patterns.append(str(a)+str(b)+str(c))
                    elif a is "skip":
                        possible_name_patterns.append(str(b)+str(c))
                    elif b is "skip":
                        possible_name_patterns.append(str(a)+str(c))
                    elif c is "skip":
                        possible_name_patterns.append(str(a)+str(b))
        for i in possible_name_patterns:
            if str(i)[0] in string.ascii_lowercase:
                a = str(i).replace(str(i)[0], str(i)[0].upper())
                possible_name_patterns.append(a)
        return possible_name_patterns
    
    def createPossibleBirthPatterns(self) -> list[str]:
        possible_birth_patterns = []
        for a in self.numbers:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
            sys.stdout.flush()
            self.total += 1
            for b in self.numbers:
                sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
                sys.stdout.flush()
                self.total += 1
                for c in self.numbers:
                    sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
                    sys.stdout.flush()
                    self.total += 1
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
                    elif len(str(a)) is 4:
                        a = a[:1]
                        possible_birth_patterns.append(str(a)+str(b)+str(c))
        return possible_birth_patterns
    def createPossibleEtc(self) -> list[str]:
        possible_etc_patterns = []
        for a in self.strings:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
            sys.stdout.flush()
            self.total += 1
            for b in self.numbers:
                sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
                sys.stdout.flush()
                self.total += 1
                possible_etc_patterns.append(str(a)+str(b))
                possible_etc_patterns.append(str(b)+str(a))
        for i in possible_etc_patterns:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
            sys.stdout.flush()
            self.total += 1
            if str(i)[0] in string.ascii_lowercase:
                a = str(i).replace(str(i)[0], str(i)[0].upper())
                possible_etc_patterns.append(a)
        to_upper = []
        for i in possible_etc_patterns:    
            to_upper.append(str(i).upper())
        possible_etc_patterns.extend(to_upper)
        return possible_etc_patterns
    
    def createPossibleNamePatternsWithBirthday(self, names, birth) -> list[str]:
        a = []
        for b in self.name:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
            sys.stdout.flush()
            self.total += 1
            for c in self.numbers:
                sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
                sys.stdout.flush()
                self.total += 1
                a.append(str(b)+str(c))
                a.append(str(c)+str(b))
            for d in birth:
                sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
                sys.stdout.flush()
                self.total += 1
                a.append(str(d)+str(b))
                a.append(str(b)+str(d))
        for b in names:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
            sys.stdout.flush()
            self.total += 1
            for c in self.numbers:
                sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
                sys.stdout.flush()
                self.total += 1
                a.append(str(b)+str(c))
                a.append(str(c)+str(b))
            for d in birth:
                sys.stdout.write(f"\033[1000D\033[1;92m{self.total} processing..")
                sys.stdout.flush()
                self.total += 1
                a.append(str(d)+str(b))
                a.append(str(b)+str(d))
        return a
        

    def run(self) -> None:
        results = []
        arrays_of_names = self.createPossibleNamePatterns()
        arrays_of_birth = self.createPossibleBirthPatterns()
        arrays_of_etc_with_birthday = self.createPossibleEtc()
        arrays_of_names_with_birthday = self.createPossibleNamePatternsWithBirthday(arrays_of_names, arrays_of_birth)
        results.extend(arrays_of_names)
        results.extend(arrays_of_birth)
        results.extend(arrays_of_etc_with_birthday)
        results.extend(arrays_of_names_with_birthday)
        #test for duplicate names
        self.total = 0
        final_results = []
        if self.isChekablePassword:
            for a in results:
                sys.stdout.write(f"\033[1000D\033[1;92m{self.total} checking for duplicates..")
                sys.stdout.flush()
                self.total += 1
                if not a in final_results:
                    final_results.append(a)
        else:
            final_results = results
        try:
            os.mkdir("results")
        except OSError:
            pass
        
        self.total = 0
        f = open(f"results/{self.first_name}.txt", "a")
        for a in final_results:
            sys.stdout.write(f"\033[1000D\033[1;92m{self.total} writing results in file...")
            sys.stdout.flush()
            self.total += 1
            f.write(str(a)+"\n")
        f.close()
        print("\r\r\r\r\r"+line)
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