s = input("Enter a string :-\n")

countVowel=0

for i in range(0,len(s)) :
    if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u') :
        countVowel+=1

print("Count of Vowel in",s,"is :-",countVowel)