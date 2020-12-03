# ifollowextractor
[Manual operation] Instagram follower/following extractor

## Extract the followers / followings from a Instagram page
**NOTE:** This is a script to extract data *from* a HTML page. So, first, you have to download the page ;)

I know... it's a bit manually process. But, it works ;)

## Dependecis
- Beautiful Soup

## How to use
1. Access someone instagram page via browser (chomre, edge, firefox etc)
2. Access the followers/following popup then scroll down until there's no more info to load
3. Save this page to some folder in your computer
    - I like to open dev tools, copy the entire HTML then save it to any folder
4. Run the script with 2 arguments:
    - first: html file (relative/absolute input file path)
    - second: output file (relative/absolute path)

**Example**
```
$ py ifollowextractor.py input.html outputList.txt
```

## Output format
A list of ordered follow's user name.