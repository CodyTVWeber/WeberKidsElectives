% Five-Note Scale Warmups in C major
\version "2.24.0"
\header {
  title = "Five-Note Scale Warmups"
  subtitle = "C Major"
}

patternOne = \relative c' { c d e f g f e d c2 }
patternTwo = \relative c' { c e g e c2 c2 }

\score {
  \new Staff <<
    \clef treble
    \key c \major
    \time 4/4
    \patternOne
    \break
    \patternTwo
  >>
  \layout { }
  \midi { }
}

