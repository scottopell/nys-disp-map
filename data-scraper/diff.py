import argparse
import json
import os
from deepdiff import DeepDiff

def diff_json(file1, file2):
    # Ensure both files exist
    if not os.path.exists(file1):
        print(f"Error: File '{file1}' does not exist.")
        return
    if not os.path.exists(file2):
        print(f"Error: File '{file2}' does not exist.")
        return

    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        json1 = json.load(f1)
        json2 = json.load(f2)

    diff = DeepDiff(json1, json2, ignore_order=True)

    # Summarize output
    print("Keys only in the first json: ", diff.get('dictionary_item_added', set()))
    print("Keys only in the second json: ", diff.get('dictionary_item_removed', set()))
    print("Values different between the two jsons: ", diff.get('values_changed', set()))
    print("Types different between the two jsons: ", diff.get('type_changes', set()))
    print("Lists different between the two jsons: ", diff.get('iterable_item_added', set()), diff.get('iterable_item_removed', set()))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare two JSON files.')
    parser.add_argument('file1', help='First JSON file for comparison.')
    parser.add_argument('file2', help='Second JSON file for comparison.')
    args = parser.parse_args()

    diff_json(args.file1, args.file2)
