# auto-locus
Auto locus is a small programm that automatically determines the locus of a given funciton.

## Installation (Windows)

1. Download the latest release from [release tab](https://github.com/Gobidev/auto-locus/releases).
2. Unzip the file.
3. Run _Auto_Locus.exe_

## Installation (Mac/Linux)

1. Make sure you have Python 3.5 or higher installed.
2. Install [sympy](https://pypi.org/project/sympy/).
3. [Clone the repository](https://github.com/Gobidev/auto-locus/archive/master.zip).
4. Run _Auto_Locus.py_

## Installation (Android)

1. Download [Pydroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) from the Google Play Store.
2. Open the app, expand the menu and navigate to Pip.
3. Type **sympy** and click install.
4. [Clone the repository](https://github.com/Gobidev/auto-locus/archive/master.zip), unzip it and move it to your phone.
5. Open _Auto_Locus.py_ in Pydroid 3.
6. Run the program.

## How to Use

![alt text](https://github.com/Gobidev/auto-locus/blob/master/screenshots/gui.png?raw=true)

- Insert a function f(x) with the parameter a:
<pre>
    Translations:
    Squareroot = sqrt()
    x^2 = x^2
    a*x = ax
    3a = 3*a
    
    Examples:
    1. x^2+ax+2
    2. x^2-6*x+11+ax-3*a
    
    Make sure to add a '*' after coefficients!
    Exponential functions can not be processed.
</pre>
- Select if you want the locus for the bend points or the turning points
- Click either on _Calculate Locus_ or on _Calculate Common Points_.

### Examples
![alt text](https://github.com/Gobidev/auto-locus/blob/master/screenshots/gui_bend_points.png?raw=true)
![alt text](https://github.com/Gobidev/auto-locus/blob/master/screenshots/gui_common_points.png?raw=true)