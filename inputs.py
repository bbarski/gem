import urls
import helpers

STEAMCMD='steamcmd'
DOOM3='dhewm3'
QUAKE='quakespasm'
DOOM='dsda-doom'
DUNE2='dunelegacy'
#
INST_COMMAND=['sudo','zypper','-n','in','-l']
STEAMCMDINSTLL=[*INST_COMMAND,STEAMCMD]
DHEWM3INSTLL=[*INST_COMMAND,DOOM3]
QUAKESPASMINSTLL=[*INST_COMMAND,QUAKE]
DSDADOOM=[*INST_COMMAND,DOOM]
DUNELEGACY=[*INST_COMMAND,'dunelegacy']
FHEROES2=[*INST_COMMAND,'fheroes2']
OPENTYRIAN=[*INST_COMMAND,'opentyrian']
XRICK=[*INST_COMMAND,'xrick']
OPENXCOM=[*INST_COMMAND,'openxcom']
SCUMMVM=[*INST_COMMAND,'scummvm']
REMINISCENCE=[*INST_COMMAND,'reminiscence']
#
ADD_REP_CMD=['sudo','zypper','ar']
TW_GMS_REP_ALS='games-openSUSE_Tumbleweed'
ADD_TW_GMS_REP=[*ADD_REP_CMD,urls.TW_GMS_REP,TW_GMS_REP_ALS]
TW_GMS_TLS_REP_ALS='games-tools-openSUSE_Tumbleweed'
ADD_TW_GMS_TLS_REP=[*ADD_REP_CMD,urls.TW_GMS_TLS_REP,TW_GMS_TLS_REP_ALS]
ACCPT_REP_GPGKEYS=['sudo','zypper','--gpg-auto-import-keys','ref']
#
DOWNDIR='/tmp/'
CURL_COMMAND=['curl','-o']
DOOM3DEMOURL=urls.DOOM3DEMMRR3
DOOM3DEMODOWNPATH=DOWNDIR+helpers.get_file_name_from_url(urls.DOOM3DEMMRR3)
GETDOOM3DEMO=[*CURL_COMMAND,DOOM3DEMODOWNPATH,DOOM3DEMOURL]
#
EXTRDOOM3PAKS=['sh',DOOM3DEMODOWNPATH,'--tar','xvf','-C',DOWNDIR,'demo/']
DOOM3MVFROM=DOWNDIR+'/demo/demo00.pk4'
DOOM3MVTO='/home/bart/.local/share/dhewm3/demo/'
CPDOOM3DEMODAT=['cp',DOOM3MVFROM,DOOM3MVTO]
MKDIRDHEWM3=['mkdir','-p','/home/bart/.local/share/dhewm3/demo/']












