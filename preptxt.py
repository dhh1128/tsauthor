#! /usr/bin/python

import os, sys, re

scriptural_books = 'genesis,exodus,leviticus,numbers,duetoronomy,joshua,judges,ruth,' + \
    'samuel,kings,ezra,nehemiah,ester,job,psalms,proverbs,ecclesiastes,solomon,' + \
    'isaiah,jeremiah,lamentations,ezekiel,daniel,hosea,joel,amos,obadiah,jonah,micah,' + \
    'nahum,habakkuk,zephaniah,haggai,zechariah,malachi,matthew,mark,luke,john,acts,' + \
    'romans,corinthians,galatians,ephesians,philippians,colossians,thessalonians,' + \
    'timothy,titus,philemon,hebrews,james,peter,jude,revelation,nephi,jacob,enos,' + \
    'jarom,omni,mormon,mosiah,alma,helaman,ether,moroni,moses,abraham'

other_proper_nouns_to_keep = 'lord,god,holy,spirit,bible,book'

citation_pat = re.compile()

def remove_quotes(txt, qchar):
    while True:
        i = txt.find(qchar)
        if i == -1:
            return txt
        j = txt.find(qchar, i + 1)
        if j == -1:
            j = i
        txt = txt[:i] + txt[j + 1:]
        
def remove_citations(txt):
    cit_pat = re.compile('(\(\[)?])))

def find_proper_nouns(txt):
    unhandled_count = 0
    pat = re.compile(r'\W[A-Z][A-Za-z]+')
    for hit in pat.finditer(txt):
        i = hit.start() - 1
        while i > 0 and txt[i].isspace():
            i -= 1
        if i > 0 and txt[i] != '.':
            unhandled_count += 1
            print('Found unhandled proper noun "%s" at %d.' % (hit.group(0), hit.start())

def find_ellipses(txt):
    found_count = 0
    i = 0
    while True:
        i = txt.find('...', i)
        if i > -1:
            found_count += 1
            print('Found ellipsis at %d.' % i)
            i += 3
        else:
            break
    return found_count

def normalize_common_variants(txt)
    txt = re.subst(r'(\W)&c(\W)', r'\1etc\2', txt)
    txt = re.subst(r'(\W)i\.e\.(\W)', r'\1ie\2', txt)
    txt = re.subst(r'(\W)e\.g\.(\W)', r'\1eg\2', txt)
    return txt

def normalize(fname):
    with open(fname, 'r') as f:
        txt = f.read()
    if find_ellipses(txt) > 0:
        return
    if find_proper_nouns(txt) > 0:
        return
    txt = normalize_common_variants(txt)
    txt = txt.lower()
    txt = remove_quotes(txt, '"')
    txt = remove_quotes(txt, "'")
    txt = re.subst(r'\d+', 'NUM', txt)
    
    

if __name__ == '__main__':
    normalize(sys.argv[0])