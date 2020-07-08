vowelcount = 0

def countVowels(str):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in str:
        if x in vowels:
            global vowelcount
            vowelcount += 1


countVowels("there are so many vowels in this string")
countVowels("aaa")
print(vowelcount)

"""
JavaScript Code

function countVowels(str)
{
  var vowels = 'aeiou';
  var vowelCount = 0;
  for(var x = 0; x < str.length ; x++)
  {
    if (vowels.includes(str[x])) {
        vowelsCount++;
    }
  }
  return vowelCount;
}

"""