import argparse
from .scans import run_sql_injection_scan, run_xss_scan, run_static_analysis

def main():
    banner()
    # parser = argparse.ArgumentParser(
    #     description="CodeSentry CLI - A security scanning tool"
    # )

    # parser.add_argument(
    #     '--scan', 
    #     choices=['sql-injection', 'xss', 'static-analysis'], 
    #     help="Specify the type of scan to run"
    # )

    # args = parser.parse_args()

    # if args.scan == 'sql-injection':
    #     run_sql_injection_scan()
    # elif args.scan == 'xss':
    #     run_xss_scan()
    # elif args.scan == 'static-analysis':
    #     run_static_analysis()
    # else:
    #     parser.print_help()

def banner():
    banner = r"""                                                                                       
                                                                                                       
  ,----..                                  .--.--.                            ___                      
 /   /   \                ,---,           /  /    '.                        ,--.'|_                    
|   :     :  ,---.      ,---.'|          |  :  /`. /                ,---,   |  | :,'   __  ,-.         
.   |  ;. / '   ,'\     |   | :          ;  |  |--`             ,-+-. /  |  :  : ' : ,' ,'/ /|         
.   ; /--` /   /   |    |   | |   ,---.  |  :  ;_       ,---.  ,--.'|'   |.;__,'  /  '  | |' |   .--,  
;   | ;   .   ; ,. :  ,--.__| |  /     \  \  \    `.   /     \|   |  ,"' ||  |   |   |  |   ,' /_ ./|  
|   : |   '   | |: : /   ,'   | /    /  |  `----.   \ /    /  |   | /  | |:__,'| :   '  :  /, ' , ' :  
.   | '___'   | .; :.   '  /  |.    ' / |  __ \  \  |.    ' / |   | |  | |  '  : |__ |  | '/___/ \: |  
'   ; : .'|   :    |'   ; |:  |'   ;   /| /  /`--'  /'   ;   /|   | |  |/   |  | '.'|;  : | .  \  ' |  
'   | '/  :\   \  / |   | '/  ''   |  / |'--'.     / '   |  / |   | |--'    ;  :    ;|  , ;  \  ;   :  
|   :    /  `----'  |   :    :||   :    |  `--'---'  |   :    |   |/        |  ,   /  ---'    \  \  ;  
 \   \ .'            \   \  /   \   \  /              \   \  /'---'          ---`-'            :  \  \ 
  `---`               `----'     `----'                `----'                                   \  ' ; 
                                                                                                 `--`  
                                                     
    """

    # Centralizar o texto "CodeSentry CLI - Version 0.1.0"
    version_text = "CodeSentry CLI - Version 0.1.0"
    author_text = "Developed by Kaio Gerhardt"

    # Calcular os espaços necessários para centralizar o texto
    banner_width = len(banner.splitlines()[1])  # Comprimento de uma linha do banner
    centered_version_text = version_text.center(banner_width)
    centered_author_text = author_text.center(banner_width)

    print(banner)
    print(centered_version_text)
    print(centered_author_text)
    print("")

if __name__ == "__main__":
    banner()