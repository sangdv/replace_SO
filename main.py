import os
import argparse
from photoshop import Session

def replace_smart_object(opt):
    input_psd_path = opt.psd 
    so_path = opt.so  
    out_path = opt.out 
    curdir = os.path.abspath(os.path.dirname(__file__))
    input_psd_path = os.path.join(curdir, input_psd_path)
    so_path = os.path.join(curdir, so_path)
    out_path = os.path.join(curdir, out_path)
    with Session(input_psd_path, action="open", auto_close=True) as ps:
        doc = ps.active_document
        layers = doc.artLayers

        replace_contents = ps.app.stringIDToTypeID("placedLayerReplaceContents")
        desc = ps.ActionDescriptor
        idnull = ps.app.charIDToTypeID("null")
        desc.putPath(idnull, so_path)
        ps.app.executeAction(replace_contents, desc)
        
        options = ps.PNGSaveOptions()
        doc.saveAs(out_path, options, True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--psd', type=str, default='01.psd', help='input psd path')
    parser.add_argument('--so', type=str, default='rs111.psb', help='input smart object path')
    parser.add_argument('--out', type=str, default='export.png', help='output path')
    opt = parser.parse_args()
    replace_smart_object(opt)

if __name__ == "__main__":
    main()
