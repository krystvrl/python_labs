import argparse
from lib.json_csv import *
from lib.csv_xlsx import *

def main():
    parser = argparse.ArgumentParser(description="Конвертер JSON↔CSV, CSV→XLSX")
    sub = parser.add_subparsers(dest="cmd")

    # json → csv
    json2csv_parser = sub.add_parser("json2csv")
    json2csv_parser.add_argument("--in", dest="input", required=True, help="Путь к входному JSON")
    json2csv_parser.add_argument("--out", dest="output", required=True, help="Путь к выходному CSV")

    # csv → json
    csv2json_parser = sub.add_parser("csv2json")
    csv2json_parser.add_argument("--in", dest="input", required=True, help="Путь к входному CSV")
    csv2json_parser.add_argument("--out", dest="output", required=True, help="Путь к выходному JSON")

    # csv → xlsx
    csv2xlsx_parser = sub.add_parser("csv2xlsx")
    csv2xlsx_parser.add_argument("--in", dest="input", required=True, help="Путь к входному CSV")
    csv2xlsx_parser.add_argument("--out", dest="output", required=True, help="Путь к выходному XLSX")

    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        parser.error(f"Входной файл '{args.input}' не найден")

    if args.cmd == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.cmd == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

#python -m lab06.src.cli_convert json2csv --in data/samples/people.json --out data/out/peoplejson2csv.csv 
#python -m lab06.src.cli_convert csv2json --in data/samples/cities.csv --out data/out/citiescsv2json.json
#python -m lab06.src.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/peoplecsv2xlsx.xlsx 