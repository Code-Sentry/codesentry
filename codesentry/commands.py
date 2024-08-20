from .ScanFactory import ScanFactory

class Commands:

    def __init__(self, parser):
        self.parser = parser

    def start(self):
        self.addArguments()

    def addArguments(self):
        # adicionar aqui os demais argumentos
        self.parser.add_argument(
        '--scan', 
        choices=['sql-injection', 'xss', 'static-analysis'], 
        help="Specify the type of scan to run"
        )
    
    def getArgs(self):
        return self.parser.parse_args()
    
    def run(self):
        args = self.getArgs()
        if args.scan:
            try:
                scan = ScanFactory.get_scan(args.scan)
                print(f"Running: {scan.description()}")
                scan.run()
            except ValueError as e:
                print(e)
        else:
            parser.print_help()