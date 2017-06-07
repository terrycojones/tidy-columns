## tidy-columns

Align columns of data read from standard input and write the formatted
result to standard output.

Note that all data is read into RAM, so this may not work on very large inputs.

### Usage

```sh
tidy-columns.py [--defaultAlignment R|L] [--alignment alignment] [--addCommas] [--separator X] < input > output
```

where `alignment` is a string of `L` and `R` characters, and `X` is any string.

### Examples

Suppose we have this input data in a file called `/tmp/data`:

```
01-1-bursa 1288703
02-1-cecal-tonsil 1199476
03-1-spleen 1095290
04-1-thymus 1950795
05-1-cloaca-swab 1196991
06-1-oropharynx-swab 934725
07-2-bursa 1469444
08-2-cecal-tonsil 2172147
09-2-spleen 2188220
10-2-thymus -939127
11-2-cloaca-swab 1554
12-2-oropharynx-swab 12653204
```

we can format it nicely via:

```sh
$ tidy-columns.py < /tmp/data
01-1-bursa           1288703
02-1-cecal-tonsil    1199476
03-1-spleen          1095290
04-1-thymus          1950795
05-1-cloaca-swab     1196991
06-1-oropharynx-swab 934725
07-2-bursa           1469444
08-2-cecal-tonsil    2172147
09-2-spleen          2188220
10-2-thymus          -939127
11-2-cloaca-swab     1554
12-2-oropharynx-swab 12653204
```

To align the second column to the right:

```sh
$ tidy-columns.py --alignment LR < /tmp/data
01-1-bursa            1288703
02-1-cecal-tonsil     1199476
03-1-spleen           1095290
04-1-thymus           1950795
05-1-cloaca-swab      1196991
06-1-oropharynx-swab   934725
07-2-bursa            1469444
08-2-cecal-tonsil     2172147
09-2-spleen           2188220
10-2-thymus           -939127
11-2-cloaca-swab         1554
12-2-oropharynx-swab 12653204
```

To change the default alignment to right:

```sh
$ tidy-columns.py --defaultAlignment R < /tmp/data
          01-1-bursa  1288703
   02-1-cecal-tonsil  1199476
         03-1-spleen  1095290
         04-1-thymus  1950795
    05-1-cloaca-swab  1196991
06-1-oropharynx-swab   934725
          07-2-bursa  1469444
   08-2-cecal-tonsil  2172147
         09-2-spleen  2188220
         10-2-thymus  -939127
    11-2-cloaca-swab     1554
12-2-oropharynx-swab 12653204
```

Or right then left alignment:

```sh
$ tidy-columns.py --alignment RL < /tmp/data
          01-1-bursa 1288703
   02-1-cecal-tonsil 1199476
         03-1-spleen 1095290
         04-1-thymus 1950795
    05-1-cloaca-swab 1196991
06-1-oropharynx-swab 934725
          07-2-bursa 1469444
   08-2-cecal-tonsil 2172147
         09-2-spleen 2188220
         10-2-thymus -939127
    11-2-cloaca-swab 1554
12-2-oropharynx-swab 12653204
```

Add commas to (integer) numbers:

```sh
$ tidy-columns.py --alignment LR --addCommas < /tmp/data
01-1-bursa            1,288,703
02-1-cecal-tonsil     1,199,476
03-1-spleen           1,095,290
04-1-thymus           1,950,795
05-1-cloaca-swab      1,196,991
06-1-oropharynx-swab    934,725
07-2-bursa            1,469,444
08-2-cecal-tonsil     2,172,147
09-2-spleen           2,188,220
10-2-thymus            -939,127
11-2-cloaca-swab          1,554
12-2-oropharynx-swab 12,653,204
```

Change the field separator to `' | '`:

```sh
$ tidy-columns.py --alignment LR --addCommas --separator ' | ' < /tmp/data
01-1-bursa           |  1,288,703
02-1-cecal-tonsil    |  1,199,476
03-1-spleen          |  1,095,290
04-1-thymus          |  1,950,795
05-1-cloaca-swab     |  1,196,991
06-1-oropharynx-swab |    934,725
07-2-bursa           |  1,469,444
08-2-cecal-tonsil    |  2,172,147
09-2-spleen          |  2,188,220
10-2-thymus          |   -939,127
11-2-cloaca-swab     |      1,554
12-2-oropharynx-swab | 12,653,204
```
