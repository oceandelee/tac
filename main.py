"""Module principal"""

import os, sys, subprocess
from rapport.s1_keywordse import searchKeywords
from rapport.s3_freq import freq

wordsToSearch = ['inonde', 'inondé' , 'inondée' , 'inondées' , 'inondés' , 'inondation' , 'inondations' , 
'chaux' , 'noyé', 'noyée' , 'noyés' , 'noyées' , 'noyade' , 'noyades' , 'rive' , 'digue' , 'cave' , 'caves' , 
'voûte' , 'vouté' , 'voûtée' , 'voûtement' , 'canal' , 'canaux' , 'Senne' , 'Maelbeek' , 'marécage' , 'marécages' , 'irrigation' , 
'naviguer' , 'naviguable' , 'écluse' , 'secours' , 'pompiers' , 'barque' , 'boue' , 'amont' , 'aval' , 'écoulements' , 
'barques' , 'flotte' , 'bouée' , 'fluvial' , 'écoulement' , 'écouler' , 'cave inondée' , 'caves inondées' , 'décrue' , 'décrues' ,
'écoule' , 'orage' , 'bassin d orage' , 'tempête' , 'pluie' , 'pluies' , 'calamité' , 'catastrophe' , 'piscine' , 'débordement' , 
'déborde' , 'débordé' , 'déborde' , 'dégât des eaux' , 'dégâts des eaux' , 'crue' , 'crues' , 'rivière' , 'avaloir' , 'égout' , 'égouts', 'risque naturel' , 
'climat' , 'météo' , 'déluge' , 'déluges' , 'collecteur' , 'collecteurs' , 'sinistre' , 'précipitation' , 'précipitations' , 'étang' ,
'bassin' , 'bassins' , 'canalisation' , 'déversoir' , 'déversoirs'] 
gitPath = ""
workingDir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":

    #pour appeler le bash de git
    for p in os.environ["PATH"].split(";"):
        pos = p.find("Git")
        if(pos>-1):
            tmpPath = p.split("Git")[0] + "Git\\git-bash.exe"
            if(os.path.exists(tmpPath)):
                gitPath = tmpPath
    
    
    
    if not os.path.exists(workingDir + f"\\rapport\\data\\pdf"):
        
        #module1/s4_scrape.py 
        os.system("py "+ workingDir + "\\rapport\\s4_scrape.py download")
    else:
        os.system("py "+ workingDir + "\\rapport\\s4_scrape.py check")
        

    if not os.path.exists(workingDir + f"\\rapport\\data\\txt"):
        #module1/s1_convert.sh
         p = subprocess.Popen(gitPath + " ./s1_convert.sh " + y, 
                        bufsize=-1, 
                        executable=None, 
                        stdin=None, 
                        stdout=None, 
                        stderr=None, 
                        preexec_fn=None, 
                        close_fds=True, 
                        shell=False, 
                        cwd=workingDir + f"\\rapport", 
                        )

    #module3/s1_keywordse.py
    if not os.path.exists(workingDir + f"\\rapport\\data\\filesFound"):
        resultSearch = searchKeywords("Bxl_", wordsToSearch, "fr", 500)
        os.system("mkdir "+workingDir + f"\\rapport\\data\\filesFound")
        for r in resultSearch:
            os.system("copy "+workingDir+f"\\rapport\\data\\txt\\"+r+" "+workingDir+f"\\rapport\\data\\filesFound\\"+r)

    #module3/s2_wordcloude.sh 
    if(len(gitPath)>0):
        yearsList = []
        for f in os.listdir(workingDir + "\\rapport\\data\\filesFound"):
            yearsList.append(f.split("_")[1])
        yearsSet = set(yearsList)
        for y in yearsSet:
            p = subprocess.Popen(gitPath + " ./s2_wordcloude.sh " + y, 
                        bufsize=-1, 
                        executable=None, 
                        stdin=None, 
                        stdout=None, 
                        stderr=None, 
                        preexec_fn=None, 
                        close_fds=True, 
                        shell=False, 
                        cwd=workingDir + f"\\rapport", 
                        ) 
            p.wait()
    
    #module2/s3_freq.py 
    freq(wordsToSearch)

