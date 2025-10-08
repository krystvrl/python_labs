def format_record(rec: tuple[str, str, float]) -> str:
    if type(rec[2]) is not int and type(rec[2]) is not float:
        return TypeError
    if len(rec[1])==0:
        return ValueError
    name_parts=rec[0].strip().split()
    if len(name_parts)==3:
        n1, n2, n3 = name_parts
        return f"{n1.capitalize()} {n2[0].upper()}.{n3[0].upper()}., гр. {rec[1].upper()}, GPA {rec[2]:.2f}"
    elif len(name_parts)==2:
        n1, n2 = name_parts
        return f"{n1.capitalize()} {n2[0].upper()}., гр. {rec[1].upper()}, GPA {rec[2]:.2f}"
    else:
        return ValueError
print(f"format_record\n[('Иванов Иван Иванович', 'BIVT-25', 4.6)] -> {format_record([('Иванов Иван Иванович', 'BIVT-25', 4.6)])}\n[] -('Петров Пётр', 'IKBO-12', 5.0)> {format_record([('Петров Пётр', 'IKBO-12', 5.0)])}\n[('Петров Пётр Петрович', 'IKBO-12', 5.0)] -> {format_record([('Петров Пётр Петрович', 'IKBO-12', 5.0)])}\n[('  сидорова  анна   сергеевна ', 'ABB-01', 3.999)] -> {format_record([('  сидорова  анна   сергеевна ', 'ABB-01', 3.999)])}")