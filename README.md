# PyABT

PyABT, a Python audio batch transcoder depends on SoX

---

## Attention

PyABT doesn't work under Windows and I don't know why.  
Print out the command to be executed directly, the result is as follows:

```
Source path: C:\Users\zhaoy\Music\INSYDE - HoYoMix
Source format (extension name): flac
Target/Output path: C:\Users\zhaoy\Music\INSYDE - HoYoMix\out
Target format(extension name): ogg
sox 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\01 Sway to My Beat in Cosmos.flac' 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\out\01 Sway to My Beat in Cosmos.ogg'
sox 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\02 If I Can Stop One Heart From Breaking.flac' 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\out\02 If I Can Stop One Heart From Breaking.ogg'
sox 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\03 Hope is the Thing With Feathers.flac' 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\out\03 Hope is the Thing With Feathers.ogg'
sox 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\04 Had I Not Seen the Sun.flac' 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\out\04 Had I Not Seen the Sun.ogg'
sox 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\05 Sway to My Beat in Cosmos [Instrumental].flac' 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\out\05 Sway to My Beat in Cosmos [Instrumental].ogg'
sox 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\06 If I Can Stop One Heart From Breaking [Instrumental].flac' 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\out\06 If I Can Stop One Heart From Breaking [Instrumental].ogg'
sox 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\07 Hope is the Thing With Feathers [Instrumental].flac' 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\out\07 Hope is the Thing With Feathers [Instrumental].ogg'
sox 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\08 Had I Not Seen the Sun [Instrumental].flac' 'C:\Users\zhaoy\Music\INSYDE - HoYoMix\out\08 Had I Not Seen the Sun [Instrumental].ogg'
```

Copy it to the terminal and execute it, it can be converted correctly

But if you execute it directly with os.system(), it will report these errors:

```
Source path: C:\Users\zhaoy\Music\INSYDE - HoYoMix
Source format (extension name): flac
Target/Output path: C:\Users\zhaoy\Music\INSYDE - HoYoMix\out
Target format(extension name): ogg
sox FAIL formats: can't open input file `in': No such file or directory
sox FAIL formats: can't open input file `From': No such file or directory
sox FAIL formats: can't open input file `With': No such file or directory
sox FAIL formats: can't open input file `the': No such file or directory
sox FAIL formats: can't open input file `Cosmos': No such file or directory
sox FAIL formats: can't open input file `Breaking': No such file or directory
sox FAIL formats: can't open input file `Feathers': No such file or directory
sox FAIL formats: can't open input file `Sun': No such file or directory
```

If you have any idea about this, please contact me <a href='mailto:zhaoym233@hotmail.com'>zhaoym233@hotmail.com</a>

---

```
Usage: 

    Interactive command line:
        Just run pyabt.py, the script will ask you all the questions in need
        
    ====================--------------------
    
    pyabt.py [source path] [source format] [target path] [target format]
    
        source path: the path to the file you want to convert
        
        source format: the extension name for the source file's format
            tips: this script passes in the source format parameter
                  to determine what file extension needs to be converted.
                  
        target path: the path to output files
            tips: please create this path before running the script
            
        target format: the target format's stander extension name
            tips: SoX use the extension name to determine the format
        
    ====================--------------------

    pyabt.py [-h|--help]
        Print this help massage
```
