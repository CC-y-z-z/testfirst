def count_words(filename):
    try:
        with open(filename,encoding='utf-8') as f:
            contents=f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        pass # 静默失败，及什么都不要做
    else:
        words=contents.split()
        num_words=len(words)
        print(f"The file {filename} has about {num_words} words.")
filenames=['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)