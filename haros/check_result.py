import os
import sys
import json
import re

def main(argv=sys.argv[1:]):
    try:
        # $HOME/haros/data/data/ament_virtualenv/compliance/source/
        home_dir = os.environ.get("HOME")
        haros_data_dir = os.path.join(home_dir, 'haros', 'data')
        haros_reports_dir = os.path.join(haros_data_dir, 'data', 'ament_virtualenv', 'compliance', 'source')
        found_any_violation = False
        for root, dirs, files in os.walk(haros_reports_dir, topdown=True):
            for file in files:
                if not '.json' in file:
                   continue
                with open(os.path.join(root, file)) as json_file:
                    report = json.load(json_file)
                if len(report) == 0:
                    continue
                # else: violations found
                found_any_violation = True
                for violation in report:
                    print(violation)
        if found_any_violation:
            return -1
        # else
        return 0
    except:
        print('[ERROR] Failed to parse HAROS output')
        return -1

sys.exit(main())
