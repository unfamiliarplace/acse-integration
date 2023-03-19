import os
import csv

DIR_OUT = './output'

##all_rows = []

def clean_row(cells: list[str]) -> list[str]:
    return [cells[4], cells[9], cells[11], cells[19], cells[21]]

def clean_csv(fname: str) -> None:

    new_fname = fname.split('.csv')[0] + '_51459.csv'
    
    with open(fname, newline='') as f_old:
        reader = csv.reader(f_old, delimiter=',')
        
        with open(f'{DIR_OUT}/{new_fname}', 'w', newline='') as f_new:
            writer = csv.writer(f_new)

            headers = clean_row(next(reader))
            headers[0] = 'Date'
            headers[1] = 'Max Temp (C)'
            headers[2] = 'Min Temp (C)'
            writer.writerow(headers)

            #if not all_rows:
                #all_rows.append(headers)
            
            for row in reader:
                row = clean_row(row)
                writer.writerow(row)
                # all_rows.append(row)
    
_, _, filenames = list(os.walk('.'))[0]
for fname in filenames:
    if fname.endswith('2022-12.csv'):
        clean_csv(fname)


##all_rows.sort(key=lambda r: r[0])
##
##with open(f'{DIR_OUT}/2022_51459.csv', 'w', newline='') as f_all:
##    writer = csv.writer(f_all)
##    for row in all_rows:
##        writer.writerow(row)
