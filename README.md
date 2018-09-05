# Tracery Kernel

By [Allison Parrish](http://www.decontextualize.com/)

This is a very bare-bones custom Jupyter kernel for evaluating Tracery
grammars. (I made it because I wanted to write a few Tracery tutorials using my
usual workflow of sketching in Jupyter Notebook and then annotating the
sketches.) The kernel uses [my Python
port](https://github.com/aparrish/pytracery) of Kate Compton's wonderful
[Tracery](http://tracery.io/) language.

Features:

* Write and evaluate Tracery grammars right in a Jupyter Notebook!
* No confusing magic or boilerplate code to get in the way of people reading
  your notebook. (So you can use this to write Tracery tutorials for
  non-programmers. Or that's the idea, anyway.)
* Syntax highlighting and error messages!

## Installation

To install this kernel:

    pip install https://github.com/aparrish/tracery_kernel/archive/master.zip
    python -m tracery_kernel.install

Maybe someday I'll put it on PyPI, but this is just a quick hack and I'm not
even sure if I'll go on using it, let alone anyone else.

## Usage

After installation, the *New* menu in the notebook should show an option for
Tracery. Put a Tracery grammar in a code cell and execute! [An example notebook
in this repository](example-notebook.ipynb) shows how it works.

Note that every code cell is independent; rules in one cell don't affect rules
in another.

## License

Copyright (c) 2018 Allison Parish

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

