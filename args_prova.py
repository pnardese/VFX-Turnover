import argparse
import sys
import os

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Import EDL, create JSON and export various stuff for AVID')   # Define parser

    parser.add_argument('-e', '--edl', metavar =(''), help='Import an EDL and export a JSON, requires an EDL')  # Define arguments
    parser.add_argument('-m', '--markers', metavar =(''), help='Export markers for AVID, requires a JSON')  # Define arguments
    parser.add_argument('-s', '--subcaps', metavar =(''), help='Export subcaps file for AVID, requires a JSON') # Define arguments
    parser.add_argument('-p', '--pulls', metavar =(''), help='Export ALE file for creating pulls in AVID bin, requires a JSON') # Define arguments
    parser.add_argument('-x', '--edl_pulls', metavar =(''), help='Export EDL for cutting in pulls in AVID, requires a JSON')    # Define arguments
    parser.add_argument('-d', '--dummy_edl', metavar =(''), help='Export Dummy EDL of VFX in AVID, requires a JSON')        # Define arguments
    parser.add_argument('-g', '--google', metavar =(''), help='Export TAB file to import into a Spreadsheet, requires a JSON')  # Define arguments
    parser.add_argument('-f', '--final', nargs=2, metavar=('JSON file', 'BIN file'), help='Export EDL for cutting in final vfx in AVID, requires a JSON and an AVID bin (TAB)') # Define arguments
      
    args = parser.parse_args() # Call function to parse arguments

    if len(sys.argv) == 1:  # Check if no arguments are given
        parser.print_help(sys.stderr)  # Print help message
        sys.exit(0) # Exit program
    
    print(vars(args)) # Print arguments

    if args.edl:
        print("EDL import and JSON export") # Print message
    elif args.markers:
        print("Markers export for AVID") # Print message
    elif args.subcaps:
        print("Subcaps export for AVID")
    elif args.pulls:
        print("Export ALE for pulls export from AVID")
    elif args.edl_pulls:
        print("EDL for cutting in pulls in AVID")
    elif args.dummy_edl:
        print("Dummy EDL of VFX in AVID")   
    elif args.google:
        print("TAB file export for Google Spreadsheet")
    elif args.final:
        print("EDL for cutting in final vfx in AVID")   
