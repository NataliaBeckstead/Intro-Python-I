

def countVowels(str):
    vowels = ('a', 'e', 'i', 'o', 'u')
    vowelcount = 0
    for x in str:
        if x in vowels:
            vowelcount += 1
    return vowelcount


print(countVowels("there are so many vowels in this string"))
print(countVowels("aaa"))

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