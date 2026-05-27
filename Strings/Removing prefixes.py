##how does the browser auto remove the prefix while displaying the site url 
##eg: https://acb.com" displays as "abc.com"
abc_url ='https://abc.com'
display_url = abc_url.removeprefix('https://')
print(display_url)