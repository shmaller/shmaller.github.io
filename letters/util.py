'''Bulk update h1 and h2 syntax.'''

from pathlib import Path

BAD_H1 = '<h1 class="bw-header writing-h1"'
BAD_H2 = '<h2 class="bw body-header">'
GOOD_H1 = '<h1 class="bw nav-header"'
GOOD_H2 = '<h2 class="bw body-header">'
BAD_H1_LEN = len(BAD_H1)
BAD_H2_LEN = len(BAD_H2)
GOOD_H1_LEN = len(GOOD_H1)
GOOD_H2_LEN = len(GOOD_H2)

def update_headers():
    files = _get_files()
    for file in files:
        print(file)
        if str(file) == __file__:
            print('skipping self')
            continue
        with open(file) as f: 
            outfile = ''
            for line in f.readlines():
                outline = line
                bad_h1_pos = line.find(BAD_H1)
                bad_h2_pos = line.find(BAD_H2)                

                if not bad_h1_pos == -1:
                    outline = _correct(line,bad_h1_pos,'h1')
                elif not bad_h2_pos == -1:
                    outline = _correct(line,bad_h2_pos,'h2')

                outfile += outline

        with open(file, 'w') as out_f:        
            out_f.writelines(outfile)

def _correct(line,bad_pos,h1_or_h2):
    if bad_pos == -1:
        return

    print('bad header found')
    if h1_or_h2 == 'h1':
        pickup_point = bad_pos + BAD_H1_LEN
        good_header = GOOD_H1
    elif h1_or_h2 == 'h2':
        pickup_point = bad_pos + BAD_H2_LEN
        good_header = GOOD_H2

    prefix = line[0:bad_pos]
    suffix = line[pickup_point:]
    return prefix + good_header + suffix
    
def _get_files():
    cwd = Path.cwd()
    return [file for file in cwd.iterdir() if file.is_file()]

if __name__ == '__main__':
    update_headers()