from PIL import Image, ImageEnhance
import random, os
colorscale = [['r'],['r']],  [['r'],['t','i','c']],[['i','t','c'],['i','t','c']], [['i','t','c'],['f','v','F']],[['f','v','F'],['f','v','F']],[['f','v','F'], ['z','l']],[['z','l'],['z','l']],[['z','l'],['Y']],[['Y'],['Y']],[['Y'],['x','m']],[['x','m'],['x','m']],[['x','m'],['k','U']],[['k','U'],['k','U']],[['k','U'],['e','s','C','J']],[['e','s','C','J'],['e','s','C','J']],[['e','s','C','J'],['y','u','o','l','L','Z']],[['y','u','o','l','L','Z'],['y','u','o','l','L','Z']],[['y','u','o','l','L','Z'],['a','n','V']],[['a','n','V'],['a','n','V']],[['a','n','V'],['q','d','j','Q','S','X']],[['q','d','j','Q','S','X'],['q','d','j','Q','S','X']],[['q','d','j','Q','S','X'],['w','T','D','A']],[['w','T','D','A'],['w','T','D','A']],[['w','T','D','A'],['R']] ,[['R'],['R']],[['R'],['G','K','N']],[['G','K','N'],['G','K','N']],[['G','K','N'],['g','h','M']],[['g','h','M'],['g','h','M']],[['g','h','M'],['E','P']],[['E','P'],['E','P']],[['E','P'],['O','H']],[['O','H'],['O','H']],[['O','H'],['p']],[['p'],['p']],[['p'],['b']],[['b'],['b']],[['b'],['W']],[['W'],['W']],[['W'],['B']],[['B'],['B']]
display = ''
image = Image.open(os.path.join('uploadimage', os.listdir('uploadimage')[0]))
enchancer = ImageEnhance.Color(image)
enhanced = enchancer.enhance(2)
enchancedImage = image.resize((image.size[0]//(image.size[0]//50),image.size[1]//(image.size[0]//50))).convert('L')
pixels = list(enchancedImage.getdata())
count = 0
x=1
while max(pixels)//x > 40:
  x+=1
for i in range(len(pixels)): 
  display+=colorscale[round(pixels[i]//x)][0][0]
  display+=colorscale[round(pixels[i]//x)][1][0]
  count+=1
  if count == image.size[0]//(image.size[0]//50):
    display+='\n'
    count = 0
print(display)
