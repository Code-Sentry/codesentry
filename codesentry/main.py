import argparse
from .commands import Commands

def main():
    banner()

    parser = argparse.ArgumentParser(
        description="CodeSentry CLI - A security scanning tool"
    )

    commands = Commands(parser)
    commands.start()
    commands.run()

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

    version_text = "CodeSentry CLI - Version 0.1.0"
    author_text = "Developed by Kaio Gerhardt"

    banner_width = len(banner.splitlines()[1])
    centered_version_text = version_text.center(banner_width)
    centered_author_text = author_text.center(banner_width)

    print(banner)
    print(centered_version_text)
    print(centered_author_text)
    print("")

if __name__ == "__main__":
    banner()