# Summary

A small algorithm that I came up with. It takes an ```email``` and a ```secret```. These are then used to generate a
totp, which is appended to the provided email which is then encrypted in base64.

This algorithm was used to complete the third part of a __CHALLENGE__.

__Note:__ 

- I am not allowed to name the challenge this was used in ;-; .
- I did get it right and got accepted!

## Steps

1. Enter an email
2. Enter some secret
3. Secret gets appended to the email 
4. The resulting string gets encoded __base32__
5. The encoding then is used to generate a __TOTP__ (using SHA512)
6. The generated TOTP is then append to an email ```email:{totp}```
7. This is then encoded in base64


