from .ScanFactory import ScanFactory
import pkg_resources

class Commands:

    def __init__(self, parser):
        self.parser = parser

    def start(self):
        self.addArguments()

    def addArguments(self):
        # adicionar aqui os demais argumentos
        self.parser.add_argument(
        '--scan', 
        choices=['sql-injection', 'xss', 'static-analysis', 'full'], 
        help="Specify the type of scan to run"
        )
        self.parser.add_argument(
            '--version', '-v',
            action='version',
            version=self.get_version(),
            help="Show the version of the tool and exit"
        )
        self.parser.add_argument(
            '--directory', '-d',
            type=str,
            default='.',
            help="Directory to scan for vulnerabilities"
        )
    
    def getArgs(self):
        return self.parser.parse_args()
    
    def run(self):
        args = self.getArgs()
        if args.scan:
            try:
                scan = ScanFactory.get_scan(args.scan)
                print(f"Running: {scan.description()}")
                scan.run(args.directory)
            except ValueError as e:
                print(e)
        else:
            parser.print_help()

    def get_version(self):
        return pkg_resources.get_distribution('codesentry').version