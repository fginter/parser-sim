#Global options currently in effect
from optparse import OptionParser

options=None
args=None

setup={}

#treePaneAlert -> color-coded background
#textEdit -> sentence splitting/merging, token editing
setupPB={"treePaneAlert":False,"textEdit":False}
setupTDT={"treePaneAlert":True,"textEdit":False}

setup=setupTDT

def parseOptions():
    global options,args,setup
    parser = OptionParser(description="treeset editor")
    parser.add_option("--nocgcache", dest="usecgcache",action="store_false", default=True, help="Ignore cached CG analyses from .d.xml files and rerun CG from scratch")
    parser.add_option("--config", dest="config",action="store", default="TDT", help="Annotator config: TDT or PB")
    options, args = parser.parse_args()
    
    if options.config=="TDT":
        setup=setupTDT
    elif options.config=="PB":
        setup=setupPB

    for k,v in options.__dict__.items():
        if v!=None:
            setup[k]=v

    #Other defaults
