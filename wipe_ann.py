import argparse
from psim.core.treeset import TreeSet
from psim.core.tree import EditHistory
import xml.etree.cElementTree as ET

 
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Wipes annotation from a file')
    parser.add_argument('input', nargs=1, help='.d.xml file in')
    parser.add_argument('output', nargs=1, help='.d.xml file out')
    args = parser.parse_args()

    tset=TreeSet.fromFile(args.input[0])
    for s in tset.sentences:
        s.deps={}
        s.eh=EditHistory(ET.Element("edithistory"))
    tset.fileName=args.output[0]
    tset.save()

    
