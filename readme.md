SubLilyPond v.2
===============

LilyPond syntax highlighting in Sublime Text 2 & 3.

**ANNOUNCEMENT:** Using [Atom](http://atom.io) or [TextMate](http://macromates.com) instead? SubLilyPond ports to these editors are now available ([AtLilyPond](https://www.github.com/yrammos/AtLilyPond), [tmLilyPond](https://www.github.com/yrammos/tmLilyPond)).

### Description

This project aims at providing comprehensive and consistent syntax highlighting of [GNU LilyPond](http://lilypond.org) code in [Sublime Text 2 and 3](http://www.sublimetext.com).

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

### New in version 2.1.1

- Hides partial syntax definitions such as "LilyPond figured bass" from the status bar menu, as they are intended for internal use. (Feature available only in Sublime Text 3.)

### New in version 2.1
- Support for the Toggle Comment and Toggle Block Comment editor commands
- Support for new LilyPond 2.18 keywords
- Bug fixes and minor improvements

### New in version 2

This significant update provides:

- Support for previously unsupported LilyPond modes:
	- chord mode
	- figured bass
	- markup modes
	- lyrics modes
	- drum modes
- Note mode improvements, with proper highlighting of:
	- time signatures
	- tempo ranges
	- scaling durations
	- circled fingerings
	- ligatures
	- abbreviated tremolo notation

### Reporting bugs

Please include the following with your bug reports: screenshot, LilyPond snippet manifesting the issue, short issue description, and the name of your color scheme.

### Acknowledgement

The list of keywords in the first release of SubLilyPond was an extended version of Heikki Junes's syntax definition for vim, which comes [bundled](http://lilypond.org/doc/v2.12/Documentation/user/lilypond-program/Vim-mode) with LilyPond.

Copyright © 2013 by [Yannis Rammos](http://www.twitter.com/yannisrammos). This work is made available under the terms of the Creative Commons Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0) license, <http://creativecommons.org/licenses/by-sa/3.0/>.
