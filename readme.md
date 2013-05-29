SubLilyPond
===========

LilyPond syntax highlighting in Sublime Text 2 & 3.


### Description

This project aims at providing comprehensive and consistent syntax highlighting of [GNU Lilypond](http://lilypond.org) code in [Sublime Text 2 and 3](http://www.sublimetext.com).

Future versions may include a LilyPond build engine and snippets/autcompletions. Feel free to contact me for feedback, bug reports, and feature suggestions.

Music scholars seeking a complete typesetting solution may be interested in [LyTeXTools](https://www.github.com/yrammos/LyTeXTools), my LilyPond-enabled fork of [Marciano Siniscalchi’s](http://tekonomist.wordpress.com/) [LaTeXTools](http://github.com/SublimeText/LaTeXTools) package.

### Installing SubLilyPond

SubLilyPond is distributed via [Will Bond's](http://wbond.net/) superb [Package Control](http://wbond.net/sublime_packages/package_control/package_developers). Alternatively, you may clone (or copy the contents of) this repository into your Sublime Text packages folder:

    git clone http://github.com/yrammos/SubLilyPond.git

### Color schemes

SubLilyPond is a LilyPond _syntax definition_, not a color scheme. It enables Sublime Text to distinguish the various syntactical elements in the LilyPond code, yet the particular color assigned to each element is defined elsewhere, in the active _color scheme_. A wide range of schemes is freely available, for example via Package Control. Not all schemes provide the highest level of visual differentiation, so you may need to test several.

![Screenshot](https://raw.github.com/yrammos/SubLilyPond/master/SubLilyPond.png)

### Tweaking SubLilyPond

You may easily optimize SubLilyPond for use with your favorite color scheme by tweaking the scope names of the syntax definition. See [this](http://manual.macromates.com/en/language_grammars) if you really insist on doing so.

### Scheme code embedded in LilyPond

Since no Scheme syntax definition is currently available for Sublime Text 2 or 3, SubLilyPond parses embedded Scheme code using the Lisp syntax definition. Scheme is a Lisp dialect, of course, and this workaround has caused no glitches so far.

### Acknowledgement

The list of keywords used in SubLilyPond was extracted from Heikki Junes's syntax definition for vim, which comes [bundled](http://lilypond.org/doc/v2.12/Documentation/user/lilypond-program/Vim-mode) with LilyPond.

Copyright © 2013 by [Yannis Rammos](http://www.twitter.com/yannisrammos). This work is made available under the terms of the Creative Commons Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0) license, <http://creativecommons.org/licenses/by-sa/3.0/>.
