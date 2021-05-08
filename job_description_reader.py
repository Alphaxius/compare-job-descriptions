from re import search

## print a sorted list of filtered words from a file by count ##
def main():

    common = read_common()
    
    job_description_keywords = list(key(common, "jd.txt").keys())
    resume_keywords = list(key(common, "r.txt").keys())
 
    ## open the output file, this will store the formatted list for viewing ##
    rhas = open("rhas.txt","w")
    rnh = open("rnh.txt","w")
    ex = open("ex.txt","w")

    ## print to file sorted by value
    for word in job_description_keywords:
        if word in resume_keywords:
            rhas.write(word + "\n")
            resume_keywords.remove(word)
        else:
            rnh.write(word + "\n")

    for word in resume_keywords:
        ex.write(word + "\n")

    rhas.close()
    rnh.close()
    ex.close()

## ##
def read_common():
    common = open("common.txt","r")
    common_l = list()
    for word in common:
        common_l.append(word[0:-1])
    return common_l


## list words from a file in order of quantity ##
def key(common, file_name = "default.txt"):
    ## open the requested file ##
    job_description = open(file_name, "r")

    ## stores a list of words with counts of each word ##
    keywords = dict([])

    for line in job_description:
        for word in line.split():

            word = filter_word(common, word)
            if word == -1:
                continue

            ## add word to dictionary, add one to its count ##
            if word not in keywords:
                keywords[word] = 1
            else:
                keywords[word] = keywords[word]+1

    job_description.close()

    ## https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    keywords = dict(sorted(keywords.items(), key=lambda item: item[1]))

    return keywords


## a set of filters meant to be used with the keywords function ##
def filter_word(common, word):
    
    ## make word lower case ##
    word = word.lower()
    
    ## remove non letter/number chars ##
    for l in word:
        if search("\W",l) is not None:
            word = word.replace(l,'')

    ## remove common words ##
    if word in common:
        return -1

    ## remove plain numbers ##
    if search("\d+",word):
        return -1

    ## remove single letter errors ##
    if len(word) == 0:
        return -1

    ## todo / better filter ##
##            ## attempt to remove plurals ##
##            if word[-1] == 's':
##                word = word[0:-1]

    return word

if __name__ == "main":
    main()

