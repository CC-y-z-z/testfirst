favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name,language in favorite_languages.items():#遍历键值对
    print(f"{name.title()}'s favorite language is {language.title()}.")
for name in favorite_languages.keys():#遍历键
    print(name.title())
friends=['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language=favorite_languages[name].title()
        print(f"\t{name.title()},I see you love {language}!")
for name in sorted(favorite_languages.keys()):#按字母顺序排序
    print(f"{name.title()}, thank you for taking the poll.")
print("The following languages have been mentioned:")
# for language in favorite_languages.values():#遍历值（未考虑重复
#     print(language.title())
for language in set(favorite_languages.values()):
    print(language.title())