# SubLilyPond: LilyPond syntax highlighting in Sublime Text 2
by [Yannis Rammos](www.twitter.com/yannisrammos)

## Description

This project aims at providing comprehensive and consistent syntax highlighting of [GNU Lilypond](http://lilypond.org) code in [Sublime Text 2](http://www.sublimetext.com).

Future versions may include a LilyPond build engine and snippets/autcompletions. Feel free to contact me for feedback, bug reports, and feature suggestions.

Music scholars seeking a complete typesetting solution may be interested in my [LyTeXTools](www.github.com/yrammos/lytextools) package, which forks and adds `lilypond-book` support to [Marciano Siniscalchi’s](http://tekonomist.wordpress.com/) [LaTeXTools](http://github.com/SublimeText/LaTeXTools) package.

## Installing SubLilyPond

By far the most straightforward installation method is via [Will Bond's](http://wbond.net/) superb [Package Control](http://wbond.net/sublime_packages/package_control/package_developers). Alternatively, you may clone (or copy the contents of) this repository into your Sublime Text `./Packages` folder:

    git clone http://github.com/yrammos/SubLilyPond.git

## Color schemes

SubLilyPond is a LilyPond _syntax definition_, not a color scheme. It enables Sublime Text to distinguish the various syntactical elements in the LilyPond code, yet the particular color assigned to each element is defined elsewhere, in the active _color scheme_. A wide range of schemes is freely available, for example via Package Control. Not all schemes provide the highest level of visual differentiation, so you may need to try out several. Out of the box, SubLilyPond is fine-tuned for use with the popular [Tomorrow Night](https://github.com/chriskempson/tomorrow-theme/tree/master/textmate) scheme, also available via Package Control.

![Screenshot](https://raw.github.com/yrammos/SubLilyPond/master/SubLilyPond.png)

## Optimizing SubLilyPond for your favorite color scheme

You may easily optimize SubLilyPond for use with your favorite color scheme by tweaking the scope names of the syntax definition. See [this](http://manual.macromates.com/en/language_grammars) if you really insist on doing this.

## Scheme code embedded in LilyPond

Since no Scheme syntax definition is currently available for Sublime Text 2, SubLilyPond parses embedded Scheme code as if it were Lisp. This seems to work without glitches so far.

## Acknowledgement

The list of keywords used in SubLilyPond was extracted from [Heikki Junes's](mailto:hjunes@cc.hut.fi) syntax file for vim, which is [bundled](http://lilypond.org/doc/v2.12/Documentation/user/lilypond-program/Vim-mode) with LilyPond.